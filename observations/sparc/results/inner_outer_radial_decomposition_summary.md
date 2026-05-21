# SPARC Inner/Outer Radial Decomposition Summary

**Status:** Candidate empirical result / radial-discriminator analysis  
**Source artifacts:** `sparc_wise_inner_outer_fdm_split.csv`, `sparc_inner_outer_correlation_summary.csv`  
**Claim level:** Candidate signal with radial-discriminator support, pending notebook reproduction.

---

## Purpose

This analysis tests whether a formation-history / stellar-population proxy correlates more strongly with apparent dark residuals in the outer rotation curve than in the inner disk.

This matters because SoCT predicts that memory-field or accumulated-history effects should be cleaner in outer, lower-baryon-dominance regions. If the signal were only an inner baryonic modeling artifact, it should not preferentially strengthen in the outer halo.

---

## Derived Quantity

For each radius:

```text
f_DM(r) = 1 - [V_gas^2 + V_disk^2 + V_bulge^2] / V_obs^2
```

Two radial splits were tested:

1. **Half-radius split:** inner vs outer using half of the measured rotation-curve extent.
2. **Effective-radius split:** inner vs outer relative to effective radius, more physically meaningful for disk structure.

Formation proxy:

```text
g - W1
```

Caution:

> `g-W1` is a formation-history / stellar-population proxy, not a direct cosmic age measurement.

---

## Main Result

The cleanest subset is:

```text
Disk-dominated + Q=1 high-quality curves
N = 56
```

This subset removes lower-quality curves and bulge-contaminated systems.

### Half-Radius Split

| Metric | N | Spearman rho vs g-W1 | p-value |
|---|---:|---:|---:|
| Inner fDM | 56 | -0.553 | 9.79e-6 |
| Outer fDM | 56 | -0.657 | 3.71e-8 |

Result:

> The outer correlation is stronger than the inner correlation.

### Effective-Radius Split

| Metric | N | Spearman rho vs g-W1 | p-value |
|---|---:|---:|---:|
| Inner fDM | 56 | -0.409 | 0.00177 |
| Outer fDM | 56 | -0.637 | 1.31e-7 |

Result:

> The outer correlation is again stronger, and this split is likely more physically meaningful.

---

## Full Correlation Summary

The full summary CSV is stored at:

```text
observations/sparc/results/inner_outer_correlation_summary.csv
```

The derived split dataset should be stored at:

```text
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
```

---

## Interpretation

Conservative headline:

> In the clean disk-dominated, high-quality SPARC subset, the correlation between WISE color and apparent dark residual is stronger in the outer rotation curve than in the inner region, especially when using an effective-radius split.

SoCT-facing implication:

> This suggests the residual is not merely an inner baryonic modeling artifact and may encode formation-history-dependent structure.

Conventional alternatives remain viable:

- Lambda-CDM assembly bias;
- halo concentration;
- feedback history;
- stellar mass coupling;
- color/age proxy bias;
- environment and gas fraction.

---

## Why This Strengthens Paper 1

The earlier SPARC age-DM result reported a full-sample age/outer-DM candidate correlation.

This radial decomposition adds a more specific discriminator:

```text
formation-history proxy association is stronger in outer residuals than inner residuals
```

That is a stronger pattern than a single global correlation and should be highlighted in the Paper 1 manuscript as a candidate radial-discriminator result.

---

## Required Before Public Claim Escalation

- Commit the full derived split CSV.
- Commit the notebook or script that regenerates the split.
- Verify sample filters: all, Q=1, disk, disk+Q=1.
- Verify bulge-fraction threshold for disk classification.
- Test robustness to alternate split definitions.
- Compare against mass, surface brightness, gas fraction, and environment.
- Add outlier and leverage diagnostics.

---

## Paper-Safe Language

Use:

> The radial decomposition provides candidate evidence that the formation-history proxy is more strongly associated with outer apparent dark residuals than inner residuals in the clean disk + Q=1 subset.

Avoid:

> The radial decomposition proves SoCT or falsifies Lambda-CDM.
