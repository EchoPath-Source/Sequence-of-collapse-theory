#!/usr/bin/env python3
"""Run covariance-aware Pantheon+ environment-H0 diagnostic.

This is a pipeline/reproducibility run, not a final cosmology analysis. Raw
Pantheon+ source inputs remain external/ignored by repository policy.
"""
from __future__ import annotations

from pathlib import Path
import gzip
import math
import sys
import numpy as np
import pandas as pd

PRIMARY_Z_MIN = 0.01
PRIMARY_Z_MAX = 0.15
CLAIM_BOUNDARY = (
    "This is a preliminary covariance-aware pipeline execution using derived "
    "SDSS void + Tempel/Bisous filament cross-match labels. It does not "
    "establish a Pantheon H0/environment detection. Results are candidate "
    "diagnostics only until the raw input provenance, covariance handling, "
    "grouping choices, and independent reproducibility audit are complete."
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data" / "pantheon"
RAW_SN_TABLE = DATA_DIR / "raw" / "Pantheon+SH0ES.dat"
ENV_TABLE = DATA_DIR / "environment_labels.csv"
COVARIANCE_CANDIDATES = [
    DATA_DIR / "Pantheon_SH0ES_cov.txt.gz",
    DATA_DIR / "raw" / "Pantheon+SH0ES_STAT+SYS.cov",
    DATA_DIR / "pantheon_covariance.txt",
    DATA_DIR / "Pantheon_cov_subset.txt",
]
RESULT_DIR = REPO_ROOT / "observations" / "pantheon-environment-h0" / "results"

GROUPINGS = [
    ("strict_void_vs_filament", "void_group", ["void"], "filament_group", ["filament"]),
    ("edge_inclusive_void_vs_filament", "void_group", ["void", "near_void_edge"], "filament_group", ["filament", "near_filament"]),
    (
        "structure_contrast",
        "void_group",
        ["void", "near_void_edge"],
        "structure_group",
        ["filament", "near_filament", "field_or_wall", "sdss_nonvoid"],
    ),
    (
        "catalog_covered_contrast",
        "void_like",
        ["void", "near_void_edge"],
        "nonvoid_covered",
        ["filament", "near_filament", "field_or_wall", "sdss_nonvoid"],
    ),
]


def write_summary(status: str, lines: list[str]) -> None:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    text = ["# Pantheon+ environment-H0 covariance-aware run summary", "", f"**Status:** {status}", ""]
    text.extend(lines)
    text.extend(["", "## Claim boundary", "", CLAIM_BOUNDARY, ""])
    (RESULT_DIR / "pantheon_environment_h0_run_summary.md").write_text("\n".join(text), encoding="utf-8")


def find_covariance() -> Path | None:
    return next((p for p in COVARIANCE_CANDIDATES if p.exists()), None)


def load_covariance(path: Path) -> np.ndarray:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        values = np.fromiter((float(tok) for line in fh for tok in line.split()), dtype=float)
    if values.size < 2:
        raise ValueError(f"Covariance file {path} is empty or malformed")
    n = int(values[0])
    entries = values[1:]
    if n * n != entries.size:
        raise ValueError(f"Covariance file {path} declares N={n} but contains {entries.size} entries")
    return entries.reshape((n, n))


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame, np.ndarray, Path] | None:
    missing = []
    if not RAW_SN_TABLE.exists():
        missing.append(str(RAW_SN_TABLE.relative_to(REPO_ROOT)))
    if not ENV_TABLE.exists():
        missing.append(str(ENV_TABLE.relative_to(REPO_ROOT)))
    cov_path = find_covariance()
    if cov_path is None:
        missing.append("one covariance candidate: " + ", ".join(str(p.relative_to(REPO_ROOT)) for p in COVARIANCE_CANDIDATES))
    if missing:
        write_summary("BLOCKED_MISSING_INPUTS", ["## Missing inputs", "", *[f"- `{m}`" for m in missing]])
        print("BLOCKED_MISSING_INPUTS")
        for m in missing:
            print(f"missing: {m}")
        return None
    sn = pd.read_csv(RAW_SN_TABLE, delim_whitespace=True, comment="#")
    env = pd.read_csv(ENV_TABLE)
    cov = load_covariance(cov_path)
    return sn, env, cov, cov_path


def normalize_and_join(sn: pd.DataFrame, env: pd.DataFrame, cov: np.ndarray) -> pd.DataFrame:
    required_sn = ["CID", "RA", "DEC", "zHD", "zCMB", "MU_SH0ES"]
    missing_sn = [c for c in required_sn if c not in sn.columns]
    if missing_sn:
        raise ValueError(f"Pantheon table missing columns: {missing_sn}")
    if "environment_label" in env.columns and "environment" not in env.columns:
        env = env.rename(columns={"environment_label": "environment"})
    required_env = ["row_index", "CID", "RA", "DEC", "zHD", "zCMB", "environment"]
    missing_env = [c for c in required_env if c not in env.columns]
    if missing_env:
        raise ValueError(f"Environment table missing columns: {missing_env}")
    if len(sn) != 1701 or len(env) != 1701:
        raise ValueError(f"Expected 1701 rows; Pantheon={len(sn)}, environment={len(env)}")
    if cov.shape != (len(sn), len(sn)):
        raise ValueError(f"Covariance shape {cov.shape} does not match row count {len(sn)}")
    if not np.array_equal(env["row_index"].to_numpy(dtype=int), np.arange(len(env))):
        raise ValueError("Environment row_index is not sequential 0..N-1")
    for col in ["CID", "RA", "DEC", "zHD", "zCMB"]:
        a, b = sn[col], env[col]
        if col == "CID":
            ok = a.astype(str).to_numpy().tolist() == b.astype(str).to_numpy().tolist()
        else:
            ok = np.allclose(pd.to_numeric(a), pd.to_numeric(b), rtol=0, atol=1e-10, equal_nan=True)
        if not ok:
            raise ValueError(f"Row-order safety failed for column {col}")
    out = sn.copy()
    out["row_index"] = np.arange(len(out))
    out["SN_ID"] = out["CID"]
    out["z"] = pd.to_numeric(out["zHD"])
    out["mu"] = pd.to_numeric(out["MU_SH0ES"])
    out["environment"] = env["environment"].astype(str).str.lower().str.strip().to_numpy()
    return out


def mu_lcdm_flat_h0_70(z: np.ndarray, omega_m: float = 0.3) -> np.ndarray:
    c_km_s = 299792.458
    grid = np.linspace(0.0, float(np.max(z)), 4096)
    ez = np.sqrt(omega_m * (1 + grid) ** 3 + (1 - omega_m))
    integral = np.concatenate([[0.0], np.cumsum((1 / ez[1:] + 1 / ez[:-1]) * np.diff(grid) / 2)])
    dc = (c_km_s / 70.0) * np.interp(z, grid, integral)
    dl = (1 + z) * dc
    return 5 * np.log10(dl) + 25


def fit_h0(frame: pd.DataFrame, cov: np.ndarray, group_name: str) -> dict[str, float | str | int]:
    idx = frame["row_index"].to_numpy(dtype=int)
    csub = cov[np.ix_(idx, idx)]
    cinv = np.linalg.pinv(csub, hermitian=True)
    r = frame["mu"].to_numpy(float) - mu_lcdm_flat_h0_70(frame["z"].to_numpy(float))
    one = np.ones_like(r)
    denom = float(one.T @ cinv @ one)
    alpha = float(one.T @ cinv @ r / denom)
    sigma_alpha = math.sqrt(1.0 / denom)
    h0 = 70.0 * 10 ** (-alpha / 5.0)
    sigma_h0 = h0 * math.log(10) / 5.0 * sigma_alpha
    resid = r - alpha
    return {"fit_label": group_name, "n": len(frame), "h0": h0, "sigma_h0": sigma_h0, "chi2_min": float(resid.T @ cinv @ resid)}


def main() -> int:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    loaded = load_inputs()
    if loaded is None:
        return 0
    sn, env, cov, cov_path = loaded
    joined = normalize_and_join(sn, env, cov)
    cut = joined[(joined["z"] >= PRIMARY_Z_MIN) & (joined["z"] <= PRIMARY_Z_MAX)].copy()
    print(f"Pantheon row count = {len(sn)}")
    print(f"Environment label row count = {len(env)}")
    print(f"Covariance shape = {cov.shape}")
    print("Row-order safety passes")
    print("Group counts after redshift cut:")
    print(cut["environment"].value_counts(dropna=False).to_string())

    counts_rows, fit_rows, contrast_rows = [], [], []
    for mode, left_name, left_labels, right_name, right_labels in GROUPINGS:
        left = cut[cut["environment"].isin(left_labels)]
        right = cut[cut["environment"].isin(right_labels)]
        status = "OK" if len(left) >= 5 and len(right) >= 5 else "SKIPPED_UNDERPOWERED"
        print(f"{mode}: {left_name} n={len(left)}; {right_name} n={len(right)}; {status}")
        counts_rows += [
            {"grouping_mode": mode, "fit_label": left_name, "labels": ";".join(left_labels), "n_after_redshift_cut": len(left), "status": status},
            {"grouping_mode": mode, "fit_label": right_name, "labels": ";".join(right_labels), "n_after_redshift_cut": len(right), "status": status},
        ]
        if status != "OK":
            contrast_rows.append({"grouping_mode": mode, "left_fit_label": left_name, "right_fit_label": right_name, "status": status})
            continue
        lf, rf = fit_h0(left, cov, left_name), fit_h0(right, cov, right_name)
        lf["grouping_mode"] = rf["grouping_mode"] = mode
        fit_rows += [lf, rf]
        contrast_rows.append({"grouping_mode": mode, "left_fit_label": left_name, "right_fit_label": right_name, "delta_h0_left_minus_right": lf["h0"] - rf["h0"], "status": "OK"})

    pd.DataFrame(counts_rows).to_csv(RESULT_DIR / "pantheon_environment_h0_group_counts.csv", index=False)
    pd.DataFrame(fit_rows).to_csv(RESULT_DIR / "pantheon_environment_h0_fit_by_group.csv", index=False)
    pd.DataFrame(contrast_rows).to_csv(RESULT_DIR / "pantheon_environment_h0_contrast_results.csv", index=False)
    write_summary("COMPLETED_DIAGNOSTIC_RUN", [
        f"- Raw Pantheon+ table: `{RAW_SN_TABLE.relative_to(REPO_ROOT)}`",
        f"- Covariance path: `{cov_path.relative_to(REPO_ROOT)}`",
        f"- Pantheon row count: {len(sn)}",
        f"- Environment label row count: {len(env)}",
        f"- Covariance shape: {cov.shape}",
        "- Row-order validation: PASS for CID, RA, DEC, zHD, and zCMB",
        f"- Redshift window: {PRIMARY_Z_MIN} <= zHD <= {PRIMARY_Z_MAX}",
        "- Strict void-vs-filament and edge-inclusive void-vs-filament modes are skipped when either side has fewer than 5 rows.",
    ])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        write_summary("FAILED_VALIDATION", ["## Failure", "", f"- {type(exc).__name__}: {exc}"])
        print(f"FAILED_VALIDATION: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)
