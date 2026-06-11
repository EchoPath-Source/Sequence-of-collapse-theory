#!/usr/bin/env python3
"""
SPARC age–f_DM analysis (reproducible)

INPUT:
  data/sparc/sparc_age_fdm_data.csv
    Required columns (as provided): galaxy, fdm_outer_mean, age_best, SB0_disk_Lpc2, Vmax_kms, Rmax_kpc

OUTPUTS:
  papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv
  papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_partial_correlations.csv   (partial r via residual method)
  papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_regression_models.csv      (OLS; age coefficient across models)
  papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_binned_bootstrap.csv       (qcut bins in log10(Vmax); bootstrap CI for old-young Δf_DM)
  papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_vs_fdm_scatter.png

NOTES:
- This script uses only the columns available in the provided dataset.
- If you later add stellar mass / B–V color, extend the merge and add them as controls.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
PAPER_DIR = SCRIPT_DIR.parent
REPO_ROOT = PAPER_DIR.parent.parent

IN_PATH = REPO_ROOT / "data" / "sparc" / "sparc_age_fdm_data.csv"
OUT_DIR = PAPER_DIR / "results"


def partial_corr_resid(x, y, Z):
    """Partial correlation r(x,y|Z) using residuals from OLS on Z."""
    Zm = np.column_stack([np.ones(len(x)), Z])
    bx, *_ = np.linalg.lstsq(Zm, x, rcond=None)
    by, *_ = np.linalg.lstsq(Zm, y, rcond=None)
    rx = x - Zm @ bx
    ry = y - Zm @ by
    return stats.pearsonr(rx, ry)


def ols_age_coeff(df, Xcols):
    """Return age_best coefficient stats for model fdm_outer_mean ~ Xcols."""
    sub = df.dropna(subset=["fdm_outer_mean", "age_best"] + Xcols).copy()
    yv = sub["fdm_outer_mean"].values
    X = np.column_stack([np.ones(len(sub))] + [sub[c].values for c in ["age_best"] + Xcols])
    beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
    yhat = X @ beta
    resid = yv - yhat
    dof = len(sub) - X.shape[1]
    s2 = (resid @ resid) / dof
    XtX_inv = np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(s2 * XtX_inv))
    t = beta / se
    p = 2 * (1 - stats.t.cdf(np.abs(t), dof))
    # age_best is index 1
    return len(sub), beta[1], se[1], t[1], p[1]


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(IN_PATH)
    for col in ["fdm_outer_mean", "age_best", "Vmax_kms", "Rmax_kpc", "SB0_disk_Lpc2"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["galaxy", "fdm_outer_mean", "age_best"]).copy()
    df["logVmax"] = np.log10(df["Vmax_kms"])
    df["logRmax"] = np.log10(df["Rmax_kpc"])
    df["logSB0"] = np.log10(df["SB0_disk_Lpc2"])

    x = df["age_best"].values
    y = df["fdm_outer_mean"].values

    pear_r, pear_p = stats.pearsonr(x, y)
    spear_r, spear_p = stats.spearmanr(x, y)

    corr = pd.DataFrame([
        {"test": "pearson(age_best, fdm_outer_mean)", "n": len(df), "r": pear_r, "p_value": pear_p},
        {"test": "spearman(age_best, fdm_outer_mean)", "n": len(df), "r": spear_r, "p_value": spear_p},
    ])
    corr.to_csv(OUT_DIR / "SPARC_age_fdm_correlations.csv", index=False)

    partial_rows = []
    for name, cols in [
        ("Vmax_only", ["logVmax"]),
        ("Rmax_only", ["logRmax"]),
        ("SB0_only", ["logSB0"]),
        ("Vmax_Rmax", ["logVmax", "logRmax"]),
        ("Vmax_Rmax_SB0", ["logVmax", "logRmax", "logSB0"]),
    ]:
        sub = df.dropna(subset=cols).copy()
        r, p = partial_corr_resid(sub["age_best"].values, sub["fdm_outer_mean"].values, sub[cols].values)
        partial_rows.append({"test": name, "n": len(sub), "partial_r": r, "p_value": p, "controls": "+".join(cols)})
    pd.DataFrame(partial_rows).to_csv(OUT_DIR / "SPARC_age_fdm_partial_correlations.csv", index=False)

    reg_rows = []
    for Xcols in [[], ["logVmax"], ["logRmax"], ["logVmax", "logRmax"], ["logVmax", "logRmax", "logSB0"]]:
        n, beta_age, se_age, t_age, p_age = ols_age_coeff(df, Xcols)
        reg_rows.append({
            "model": "fdm ~ age_best" + ("" if not Xcols else " + " + " + ".join(Xcols)),
            "n": n,
            "beta_age": beta_age,
            "se_age": se_age,
            "t_age": t_age,
            "p_age": p_age,
        })
    pd.DataFrame(reg_rows).to_csv(OUT_DIR / "SPARC_age_fdm_regression_models.csv", index=False)

    # Binned bootstrap by logVmax
    subb = df.dropna(subset=["logVmax"]).copy()
    subb["mass_bin"] = pd.qcut(subb["logVmax"], q=3, labels=["lowV", "midV", "highV"])
    rng = np.random.default_rng(0)
    rows = []
    for b, g in subb.groupby("mass_bin"):
        if len(g) < 10:
            continue
        r, p = stats.pearsonr(g["age_best"], g["fdm_outer_mean"])
        med = g["age_best"].median()
        dy = g[g["age_best"] >= med]["fdm_outer_mean"].mean() - g[g["age_best"] < med]["fdm_outer_mean"].mean()
        boots = []
        gg = g.reset_index(drop=True)
        for _ in range(5000):
            samp = gg.sample(n=len(gg), replace=True, random_state=int(rng.integers(0, 2**31 - 1)))
            med2 = samp["age_best"].median()
            boots.append(samp[samp["age_best"] >= med2]["fdm_outer_mean"].mean() - samp[samp["age_best"] < med2]["fdm_outer_mean"].mean())
        lo, hi = np.percentile(boots, [2.5, 97.5])
        rows.append({"mass_bin": str(b), "n": len(g), "pearson_r": r, "p_value": p, "old_minus_young_mean": dy, "boot_ci_low": lo, "boot_ci_high": hi})
    pd.DataFrame(rows).to_csv(OUT_DIR / "SPARC_age_fdm_binned_bootstrap.csv", index=False)

    # Plot
    plt.figure(figsize=(7, 5))
    plt.scatter(df["age_best"], df["fdm_outer_mean"])
    m, b = np.polyfit(df["age_best"], df["fdm_outer_mean"], 1)
    xs = np.linspace(df["age_best"].min(), df["age_best"].max(), 200)
    plt.plot(xs, m * xs + b)
    plt.xlabel("Age proxy (age_best)")
    plt.ylabel("Outer f_DM (fdm_outer_mean)")
    plt.title("SPARC: outer f_DM vs age proxy")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "SPARC_age_vs_fdm_scatter.png", dpi=200)


if __name__ == "__main__":
    main()
