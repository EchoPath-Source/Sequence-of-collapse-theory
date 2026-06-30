#!/usr/bin/env python3
"""
Reproduce the SPARC inner/outer radial-decomposition correlation table.

Status: PRELIMINARY / reproducibility support
Claim level: Candidate empirical result, pending independent review.

Purpose
-------
This script regenerates the committed radial-decomposition correlation table:

    observations/sparc/results/inner_outer_correlation_summary.csv

from the canonical derived radial-split dataset:

    observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv

It writes:

    observations/sparc/results/inner_outer_correlation_summary_regenerated.csv
    observations/sparc/results/inner_outer_reproduction_check.md

Run from repository root:

    python observations/sparc/scripts/reproduce_inner_outer_radial_decomposition.py

Scientific boundary
-------------------
This script checks reproducibility of a derived candidate-result table. It does not
prove SoCT, disprove dark matter, or establish a new physical theory. The result
remains preliminary until input provenance, conventional controls, outlier/leverage
analysis, and independent replication are complete.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd

try:
    from scipy.stats import pearsonr, spearmanr
except Exception:  # pragma: no cover - fallback keeps script importable without scipy
    pearsonr = None
    spearmanr = None


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT = REPO_ROOT / "observations" / "sparc" / "data" / "sparc_wise_inner_outer_fdm_split.csv"
DEFAULT_EXPECTED = REPO_ROOT / "observations" / "sparc" / "results" / "inner_outer_correlation_summary.csv"
DEFAULT_REGENERATED = REPO_ROOT / "observations" / "sparc" / "results" / "inner_outer_correlation_summary_regenerated.csv"
DEFAULT_REPORT = REPO_ROOT / "observations" / "sparc" / "results" / "inner_outer_reproduction_check.md"

X_COLUMN = "gW1"
SUBSET_ORDER = ["All", "Q=1", "Disk", "Disk+Q=1"]
METRIC_ORDER = [
    "fDM_inner_half_mean",
    "fDM_outer_half_mean",
    "fDM_outer_minus_inner_half",
    "fDM_inner_Reff_mean",
    "fDM_outer_Reff_mean",
    "fDM_outer_minus_inner_Reff",
]
OUTPUT_COLUMNS = ["subset", "metric", "N", "Pearson_r", "Pearson_p", "Spearman_rho", "Spearman_p"]


@dataclass(frozen=True)
class ComparisonResult:
    matched: bool
    max_abs_diff: float
    compared_numeric_cells: int
    missing_rows: int
    extra_rows: int
    tolerance: float


def require_columns(df: pd.DataFrame, columns: list[str], source: Path) -> None:
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"{source} is missing required columns: {missing}")


def subset_masks(df: pd.DataFrame) -> dict[str, pd.Series]:
    """Return the subset definitions used in the committed correlation table.

    All: all rows with finite values for the requested metric and gW1.
    Q=1: high-quality rotation curves.
    Disk: canonical disk-dominated criterion, bulge_frac_outer < 0.2.
    Disk+Q=1: bulge_frac_outer < 0.2 and Q == 1.
    """

    q_is_one = pd.to_numeric(df["Q"], errors="coerce") == 1
    disk = pd.to_numeric(df["bulge_frac_outer"], errors="coerce").fillna(np.inf) < 0.2
    return {
        "All": pd.Series(True, index=df.index),
        "Q=1": q_is_one,
        "Disk": disk,
        "Disk+Q=1": disk & q_is_one,
    }


def _pearson(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    if len(x) < 3:
        return math.nan, math.nan
    if pearsonr is None:
        return float(np.corrcoef(x, y)[0, 1]), math.nan
    result = pearsonr(x, y)
    return float(result.statistic), float(result.pvalue)


def _spearman(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    if len(x) < 3:
        return math.nan, math.nan
    if spearmanr is None:
        ranks_x = pd.Series(x).rank(method="average").to_numpy(dtype=float)
        ranks_y = pd.Series(y).rank(method="average").to_numpy(dtype=float)
        return float(np.corrcoef(ranks_x, ranks_y)[0, 1]), math.nan
    result = spearmanr(x, y)
    return float(result.statistic), float(result.pvalue)


def correlation_row(df: pd.DataFrame, subset: str, metric: str, mask: pd.Series) -> dict[str, object]:
    work = df.loc[mask, [X_COLUMN, metric]].copy()
    work[X_COLUMN] = pd.to_numeric(work[X_COLUMN], errors="coerce")
    work[metric] = pd.to_numeric(work[metric], errors="coerce")
    work = work.replace([np.inf, -np.inf], np.nan).dropna()

    x = work[X_COLUMN].to_numpy(dtype=float)
    y = work[metric].to_numpy(dtype=float)
    pearson_r, pearson_p = _pearson(x, y)
    spearman_rho, spearman_p = _spearman(x, y)

    return {
        "subset": subset,
        "metric": metric,
        "N": int(len(work)),
        "Pearson_r": pearson_r,
        "Pearson_p": pearson_p,
        "Spearman_rho": spearman_rho,
        "Spearman_p": spearman_p,
    }


def regenerate(input_path: Path = DEFAULT_INPUT) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    require_columns(df, [X_COLUMN, "Q", "bulge_frac_outer", *METRIC_ORDER], input_path)

    masks = subset_masks(df)
    rows: list[dict[str, object]] = []
    for subset in SUBSET_ORDER:
        for metric in METRIC_ORDER:
            rows.append(correlation_row(df, subset, metric, masks[subset]))

    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS)


def load_expected(path: Path) -> pd.DataFrame:
    expected = pd.read_csv(path)
    require_columns(expected, OUTPUT_COLUMNS, path)
    return expected[OUTPUT_COLUMNS].copy()


def compare_tables(regenerated: pd.DataFrame, expected: pd.DataFrame, tolerance: float) -> ComparisonResult:
    key_cols = ["subset", "metric"]
    numeric_cols = ["N", "Pearson_r", "Pearson_p", "Spearman_rho", "Spearman_p"]

    merged = regenerated.merge(expected, on=key_cols, how="outer", suffixes=("_regenerated", "_expected"), indicator=True)
    missing_rows = int((merged["_merge"] == "right_only").sum())
    extra_rows = int((merged["_merge"] == "left_only").sum())

    both = merged[merged["_merge"] == "both"].copy()
    max_abs_diff = 0.0
    compared = 0
    for col in numeric_cols:
        left = pd.to_numeric(both[f"{col}_regenerated"], errors="coerce")
        right = pd.to_numeric(both[f"{col}_expected"], errors="coerce")
        diff = (left - right).abs()
        finite = diff[np.isfinite(diff)]
        if not finite.empty:
            max_abs_diff = max(max_abs_diff, float(finite.max()))
            compared += int(finite.shape[0])

        # Treat matching NaNs as matching; nonmatching NaNs will be caught below.
        left_nan = left.isna()
        right_nan = right.isna()
        nonmatching_nan = int((left_nan ^ right_nan).sum())
        if nonmatching_nan:
            max_abs_diff = math.inf

    matched = missing_rows == 0 and extra_rows == 0 and max_abs_diff <= tolerance
    return ComparisonResult(
        matched=matched,
        max_abs_diff=max_abs_diff,
        compared_numeric_cells=compared,
        missing_rows=missing_rows,
        extra_rows=extra_rows,
        tolerance=tolerance,
    )


def write_report(
    path: Path,
    input_path: Path,
    expected_path: Path,
    regenerated_path: Path,
    result: ComparisonResult,
) -> None:
    status = "PASS" if result.matched else "REVIEW_REQUIRED"
    max_diff = "inf" if math.isinf(result.max_abs_diff) else f"{result.max_abs_diff:.17g}"

    content = f"""# SPARC Inner/Outer Radial-Decomposition Reproduction Check

**Status:** {status}  
**Claim level:** candidate empirical result / reproducibility support  
**Input dataset:** `{input_path.relative_to(REPO_ROOT)}`  
**Expected table:** `{expected_path.relative_to(REPO_ROOT)}`  
**Regenerated table:** `{regenerated_path.relative_to(REPO_ROOT)}`

## What this checks

This reproduction script recalculates Pearson and Spearman correlations between `gW1` and each inner/outer apparent dark-fraction metric across four subsets:

```text
All
Q=1
Disk
Disk+Q=1
```

It then compares the regenerated table against the committed reference table.

## Comparison result

| Field | Value |
|---|---:|
| matched | `{result.matched}` |
| tolerance | `{result.tolerance}` |
| max_abs_diff | `{max_diff}` |
| compared_numeric_cells | `{result.compared_numeric_cells}` |
| missing_rows | `{result.missing_rows}` |
| extra_rows | `{result.extra_rows}` |

## Interpretation

Use:

> The radial-decomposition correlation table can be regenerated from the committed derived radial-split dataset, subject to the comparison status above.

Avoid:

> This reproduction check proves SoCT, proves gravity is memory, or rules out conventional halo/assembly explanations.

## Remaining scientific controls

Even if this check passes, publication-grade use still requires:

1. source/provenance notes for the radial-split dataset;
2. controls for stellar mass, gas fraction, morphology, surface brightness, curve quality, and environment;
3. bootstrap, jackknife, and outlier/leverage diagnostics;
4. independent replication or adversarial review.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Reproduce SPARC inner/outer radial-decomposition correlations.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--expected", type=Path, default=DEFAULT_EXPECTED)
    parser.add_argument("--output", type=Path, default=DEFAULT_REGENERATED)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--tolerance", type=float, default=1e-12)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    regenerated = regenerate(args.input)
    expected = load_expected(args.expected)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    regenerated.to_csv(args.output, index=False)

    result = compare_tables(regenerated, expected, args.tolerance)
    write_report(args.report, args.input, args.expected, args.output, result)

    print("SPARC inner/outer radial-decomposition reproduction check complete")
    print(f"Input: {args.input}")
    print(f"Expected: {args.expected}")
    print(f"Regenerated: {args.output}")
    print(f"Report: {args.report}")
    print(f"Matched: {result.matched}")
    print(f"Max abs diff: {result.max_abs_diff}")

    if not result.matched:
        raise SystemExit("Reproduction check did not match expected table within tolerance")


if __name__ == "__main__":
    main()
