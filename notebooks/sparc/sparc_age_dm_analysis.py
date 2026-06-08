# %%
"""
SPARC age--outer-fDM reproducibility analysis

Status: PRELIMINARY / reproducibility support
Claim level: Evidence-bearing only when run against the committed CSV and reviewed.
Input files:
  - data/sparc/sparc_age_fdm_data.csv
Output files:
  - observations/sparc/results/sparc_age_fdm_summary.csv
  - observations/sparc/results/sparc_mass_bin_summary.csv
  - observations/sparc/results/sparc_bootstrap_summary.csv
  - observations/sparc/results/sparc_memory_fit_parameters.csv
  - figures/sparc/sparc_age_fdm_scatter.png
  - figures/sparc/sparc_memory_fit.png
  - figures/sparc/sparc_mass_bins.png
Random seed: 42
Dependencies: pandas, numpy, matplotlib; scipy optional but recommended.
Known limitations:
  - This script uses the derived SPARC table committed to this repository.
  - Age values mix literature ages and proxy ages; inspect `age_source` before claims.
  - The nonlinear memory fit is exploratory unless preregistered and independently audited.

Run from repository root:

    python notebooks/sparc/sparc_age_dm_analysis.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    from scipy.optimize import curve_fit
    from scipy.stats import pearsonr, spearmanr, rankdata
except Exception:  # pragma: no cover - keeps script importable without scipy
    curve_fit = None
    pearsonr = None
    spearmanr = None
    rankdata = None


REPO_ROOT = Path(__file__).resolve().parents[2]
INPUT_CSV = REPO_ROOT / "data" / "sparc" / "sparc_age_fdm_data.csv"
RESULT_DIR = REPO_ROOT / "observations" / "sparc" / "results"
FIGURE_DIR = REPO_ROOT / "figures" / "sparc"
SEED = 42


@dataclass(frozen=True)
class MemoryFit:
    f0: float
    amplitude: float
    tau_gyr: float
    rmse: float
    method: str


def ensure_dirs() -> None:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def load_data(path: Path = INPUT_CSV) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing input CSV: {path}")

    df = pd.read_csv(path)
    required = {
        "galaxy",
        "fdm_outer_mean",
        "age_best",
        "SB0_disk_Lpc2",
        "Rmax_kpc",
    }
    missing = sorted(required.difference(df.columns))
    if missing:
        raise ValueError(f"Input CSV missing required columns: {missing}")

    df = df.copy()
    df["mass_proxy"] = np.log10(df["SB0_disk_Lpc2"] * df["Rmax_kpc"] ** 2)
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=["age_best", "fdm_outer_mean", "mass_proxy"])
    return df


def _corr(x: Iterable[float], y: Iterable[float], method: str) -> tuple[float, float]:
    x_arr = np.asarray(list(x), dtype=float)
    y_arr = np.asarray(list(y), dtype=float)
    mask = np.isfinite(x_arr) & np.isfinite(y_arr)
    x_arr = x_arr[mask]
    y_arr = y_arr[mask]
    if len(x_arr) < 3:
        return np.nan, np.nan

    if method == "pearson":
        if pearsonr is not None:
            res = pearsonr(x_arr, y_arr)
            return float(res.statistic), float(res.pvalue)
        return float(np.corrcoef(x_arr, y_arr)[0, 1]), np.nan

    if method == "spearman":
        if spearmanr is not None:
            res = spearmanr(x_arr, y_arr)
            return float(res.statistic), float(res.pvalue)
        if rankdata is None:
            ranks_x = pd.Series(x_arr).rank().to_numpy()
            ranks_y = pd.Series(y_arr).rank().to_numpy()
        else:
            ranks_x = rankdata(x_arr)
            ranks_y = rankdata(y_arr)
        return float(np.corrcoef(ranks_x, ranks_y)[0, 1]), np.nan

    raise ValueError(f"Unknown correlation method: {method}")


def partial_spearman(x: pd.Series, y: pd.Series, control: pd.Series) -> tuple[float, float]:
    """Rank-residualized partial Spearman correlation."""
    tmp = pd.DataFrame({"x": x, "y": y, "control": control}).dropna()
    if len(tmp) < 5:
        return np.nan, np.nan

    if rankdata is not None:
        rx = rankdata(tmp["x"].to_numpy(dtype=float))
        ry = rankdata(tmp["y"].to_numpy(dtype=float))
        rc = rankdata(tmp["control"].to_numpy(dtype=float))
    else:
        rx = tmp["x"].rank().to_numpy(dtype=float)
        ry = tmp["y"].rank().to_numpy(dtype=float)
        rc = tmp["control"].rank().to_numpy(dtype=float)

    design = np.column_stack([np.ones_like(rc), rc])
    bx = np.linalg.lstsq(design, rx, rcond=None)[0]
    by = np.linalg.lstsq(design, ry, rcond=None)[0]
    x_resid = rx - design @ bx
    y_resid = ry - design @ by
    return _corr(x_resid, y_resid, "pearson")


def memory_model(age_gyr: np.ndarray, f0: float, amplitude: float, tau_gyr: float) -> np.ndarray:
    return f0 + amplitude * (1.0 - np.exp(-age_gyr / tau_gyr))


def fit_memory_model(age: pd.Series, fdm: pd.Series) -> MemoryFit:
    x = age.to_numpy(dtype=float)
    y = fdm.to_numpy(dtype=float)
    mask = np.isfinite(x) & np.isfinite(y) & (x > 0)
    x = x[mask]
    y = y[mask]

    if curve_fit is not None:
        # Bounds keep the fit physically interpretable for this first-pass model.
        bounds = ([0.0, 0.0, 0.1], [1.0, 1.0, 30.0])
        p0 = [float(np.nanpercentile(y, 10)), 0.2, 8.0]
        try:
            popt, _ = curve_fit(memory_model, x, y, p0=p0, bounds=bounds, maxfev=20000)
            pred = memory_model(x, *popt)
            rmse = float(np.sqrt(np.mean((y - pred) ** 2)))
            return MemoryFit(float(popt[0]), float(popt[1]), float(popt[2]), rmse, "scipy_curve_fit")
        except Exception:
            pass

    # Deterministic fallback grid search when scipy is unavailable or fit fails.
    best: MemoryFit | None = None
    for f0 in np.linspace(0.0, 0.9, 91):
        for amplitude in np.linspace(0.0, 0.8, 81):
            for tau in np.linspace(0.5, 30.0, 118):
                pred = memory_model(x, f0, amplitude, tau)
                rmse = float(np.sqrt(np.mean((y - pred) ** 2)))
                candidate = MemoryFit(float(f0), float(amplitude), float(tau), rmse, "grid_search")
                if best is None or candidate.rmse < best.rmse:
                    best = candidate
    assert best is not None
    return best


def bootstrap_correlations(df: pd.DataFrame, n_boot: int = 1000, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    n = len(df)
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        sample = df.iloc[idx]
        pearson_r, pearson_p = _corr(sample["age_best"], sample["fdm_outer_mean"], "pearson")
        spearman_r, spearman_p = _corr(sample["age_best"], sample["fdm_outer_mean"], "spearman")
        rows.append(
            {
                "bootstrap_index": i,
                "pearson_r": pearson_r,
                "pearson_p": pearson_p,
                "spearman_r": spearman_r,
                "spearman_p": spearman_p,
            }
        )
    return pd.DataFrame(rows)


def summarize_mass_bins(df: pd.DataFrame, bins: int = 3) -> pd.DataFrame:
    labels = [f"bin_{i + 1}" for i in range(bins)]
    work = df.copy()
    work["mass_bin"] = pd.qcut(work["mass_proxy"], q=bins, labels=labels, duplicates="drop")
    rows = []
    for mass_bin, group in work.groupby("mass_bin", observed=True):
        pearson_r, pearson_p = _corr(group["age_best"], group["fdm_outer_mean"], "pearson")
        spearman_r, spearman_p = _corr(group["age_best"], group["fdm_outer_mean"], "spearman")
        rows.append(
            {
                "mass_bin": str(mass_bin),
                "n": int(len(group)),
                "mass_proxy_min": float(group["mass_proxy"].min()),
                "mass_proxy_max": float(group["mass_proxy"].max()),
                "age_min": float(group["age_best"].min()),
                "age_max": float(group["age_best"].max()),
                "pearson_r": pearson_r,
                "pearson_p": pearson_p,
                "spearman_r": spearman_r,
                "spearman_p": spearman_p,
            }
        )
    return pd.DataFrame(rows)


def write_summary_tables(df: pd.DataFrame, fit: MemoryFit) -> None:
    pearson_age, pearson_age_p = _corr(df["age_best"], df["fdm_outer_mean"], "pearson")
    spearman_age, spearman_age_p = _corr(df["age_best"], df["fdm_outer_mean"], "spearman")
    pearson_mass, pearson_mass_p = _corr(df["mass_proxy"], df["fdm_outer_mean"], "pearson")
    spearman_mass, spearman_mass_p = _corr(df["mass_proxy"], df["fdm_outer_mean"], "spearman")
    partial_r, partial_p = partial_spearman(df["age_best"], df["fdm_outer_mean"], df["mass_proxy"])

    summary = pd.DataFrame(
        [
            {"metric": "N", "value": len(df), "p_value": np.nan},
            {"metric": "Pearson(age_best, fdm_outer_mean)", "value": pearson_age, "p_value": pearson_age_p},
            {"metric": "Spearman(age_best, fdm_outer_mean)", "value": spearman_age, "p_value": spearman_age_p},
            {"metric": "Pearson(mass_proxy, fdm_outer_mean)", "value": pearson_mass, "p_value": pearson_mass_p},
            {"metric": "Spearman(mass_proxy, fdm_outer_mean)", "value": spearman_mass, "p_value": spearman_mass_p},
            {"metric": "Partial Spearman(age, fdm | mass_proxy)", "value": partial_r, "p_value": partial_p},
        ]
    )
    summary.to_csv(RESULT_DIR / "sparc_age_fdm_summary.csv", index=False)

    pd.DataFrame([fit.__dict__]).to_csv(RESULT_DIR / "sparc_memory_fit_parameters.csv", index=False)

    mass_bins = summarize_mass_bins(df)
    mass_bins.to_csv(RESULT_DIR / "sparc_mass_bin_summary.csv", index=False)

    boot = bootstrap_correlations(df)
    boot_summary = pd.DataFrame(
        [
            {
                "n_bootstrap": len(boot),
                "pearson_r_mean": float(boot["pearson_r"].mean()),
                "pearson_r_p025": float(boot["pearson_r"].quantile(0.025)),
                "pearson_r_p975": float(boot["pearson_r"].quantile(0.975)),
                "spearman_r_mean": float(boot["spearman_r"].mean()),
                "spearman_r_p025": float(boot["spearman_r"].quantile(0.025)),
                "spearman_r_p975": float(boot["spearman_r"].quantile(0.975)),
                "fraction_pearson_positive": float((boot["pearson_r"] > 0).mean()),
                "fraction_spearman_positive": float((boot["spearman_r"] > 0).mean()),
            }
        ]
    )
    boot_summary.to_csv(RESULT_DIR / "sparc_bootstrap_summary.csv", index=False)


def make_figures(df: pd.DataFrame, fit: MemoryFit) -> None:
    # Scatter + linear trend
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(df["age_best"], df["fdm_outer_mean"], alpha=0.75)
    coeff = np.polyfit(df["age_best"], df["fdm_outer_mean"], deg=1)
    x_grid = np.linspace(df["age_best"].min(), df["age_best"].max(), 200)
    ax.plot(x_grid, np.polyval(coeff, x_grid), linewidth=2)
    ax.set_xlabel("Age best estimate (Gyr)")
    ax.set_ylabel("Outer f_DM")
    ax.set_title("SPARC age vs outer dark-matter fraction")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sparc_age_fdm_scatter.png", dpi=200)
    plt.close(fig)

    # Nonlinear memory fit
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(df["age_best"], df["fdm_outer_mean"], alpha=0.75)
    ax.plot(x_grid, memory_model(x_grid, fit.f0, fit.amplitude, fit.tau_gyr), linewidth=2)
    ax.set_xlabel("Age best estimate (Gyr)")
    ax.set_ylabel("Outer f_DM")
    ax.set_title(
        "Memory model fit: f_DM = f0 + A(1 - exp(-age/tau))\n"
        f"f0={fit.f0:.3f}, A={fit.amplitude:.3f}, tau={fit.tau_gyr:.2f} Gyr"
    )
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sparc_memory_fit.png", dpi=200)
    plt.close(fig)

    # Mass bins
    work = df.copy()
    work["mass_bin"] = pd.qcut(work["mass_proxy"], q=3, labels=["low", "mid", "high"], duplicates="drop")
    fig, ax = plt.subplots(figsize=(7, 5))
    for mass_bin, group in work.groupby("mass_bin", observed=True):
        ax.scatter(group["age_best"], group["fdm_outer_mean"], alpha=0.75, label=str(mass_bin))
        if len(group) >= 3:
            coeff = np.polyfit(group["age_best"], group["fdm_outer_mean"], deg=1)
            local_grid = np.linspace(group["age_best"].min(), group["age_best"].max(), 100)
            ax.plot(local_grid, np.polyval(coeff, local_grid), linewidth=1.5)
    ax.set_xlabel("Age best estimate (Gyr)")
    ax.set_ylabel("Outer f_DM")
    ax.set_title("SPARC age--f_DM trend by mass-proxy tertile")
    ax.legend(title="Mass proxy")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sparc_mass_bins.png", dpi=200)
    plt.close(fig)


def main() -> None:
    ensure_dirs()
    df = load_data()
    fit = fit_memory_model(df["age_best"], df["fdm_outer_mean"])
    write_summary_tables(df, fit)
    make_figures(df, fit)

    print("SPARC age--fDM analysis complete")
    print(f"Input rows used: {len(df)}")
    print(f"Memory fit: f0={fit.f0:.4f}, A={fit.amplitude:.4f}, tau={fit.tau_gyr:.4f} Gyr, rmse={fit.rmse:.4f}")
    print(f"Results written to: {RESULT_DIR.relative_to(REPO_ROOT)}")
    print(f"Figures written to: {FIGURE_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
