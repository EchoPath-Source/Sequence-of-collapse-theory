# SPARC Age-DM Correlation — Publication Summary v1

**Status:** Empirical-result summary / requires code and data verification before public claim escalation  
**Source:** `SPARC_Age_DM_Publication_Summary.md`  
**Date in source:** February 17, 2026  
**Claim level:** Reported internal verification result; not yet peer reviewed.

---

## Executive Summary

The source report states that a statistically significant positive correlation was found between mean stellar age and inferred outer dark matter fraction in SPARC galaxies.

Reported primary result:

```text
Pearson r = +0.201
p = 0.0077
sigma ≈ 2.67
n = 175
```

Reported interpretation:

> Older galaxies show systematically higher apparent outer dark matter fractions, in the direction predicted by the Sequence of Collapse Theory memory-field model.

Research boundary:

> This should be treated as a promising internal result until the exact age-proxy construction, derived CSV, analysis code, and robustness checks are committed and independently reproduced.

---

## Data and Methods Summary

Reported sample:

```text
Source: SPARC galaxy rotation curve database
N = 175 galaxies
Age indicator = combined proxy from literature values + photometric indicators
DM measurement = outer DM fraction = 1 - (V_bary / V_obs)^2 at last measured radius
```

Reported statistical methods:

1. Pearson correlation.
2. Spearman correlation.
3. Partial correlations controlling for structural parameters.
4. Mass-binned analysis.
5. Bootstrap confidence intervals.
6. Multivariate regression.

---

## Primary Correlation

Reported:

```text
Pearson r = +0.201, p = 0.0077, n = 175
Spearman rho = +0.211, p = 0.0050
```

Interpretation:

> Positive age-f_DM correlation in the predicted direction.

---

## Partial Correlations

Reported partial correlations:

| Control Variables | Partial r | p-value |
|---|---:|---:|
| Vmax only | +0.289 | 1.0e-4 |
| Rmax only | +0.223 | 3.0e-3 |
| SB0 only | +0.156 | 0.040 |
| Vmax + Rmax | +0.265 | 4.1e-4 |

Interpretation in source:

> The signal strengthens when controlling for Vmax/Rmax, arguing against simple mass confounding.

Caution:

> The result weakens under the fullest structural model including SB0, so the mediation/confounding structure must be handled carefully in the paper.

---

## Mass-Binned Analysis

Reported terciles by Vmax:

| Mass Bin | n | r | p-value |
|---|---:|---:|---:|
| Low | 59 | +0.115 | 0.384 |
| Mid | 58 | +0.456 | 3.2e-4 |
| High | 58 | +0.277 | 0.036 |

Reported bootstrap 95% CI for mid-mass:

```text
[+0.134, +0.662]
```

Interpretation:

> Strongest reported signal occurs in the intermediate-mass bin.

---

## Multivariate Regression

Reported age coefficients:

| Model | beta_age | SE | p-value |
|---|---:|---:|---:|
| f_DM ~ age | +0.024 | 0.009 | 0.0077 |
| f_DM ~ age + logVmax + logRmax | +0.041 | 0.012 | 0.0004 |
| f_DM ~ age + logVmax + logRmax + logSB0 | +0.018 | 0.013 | 0.162 |

Interpretation:

> Age remains positive, but significance depends on structural controls. This may reflect mediation through structure, but it may also reflect confounding. The final paper must explicitly distinguish mediation from confounding.

---

## Repo-Safe Interpretation

Recommended language:

> We report an internally reproduced, statistically significant positive association between mean stellar age and inferred outer dark matter fraction in the SPARC sample. The sign and approximate magnitude are consistent with the SoCT memory-field prediction. However, because the analysis depends on an age proxy and derived f_DM estimates, all claims remain provisional until the derived dataset, scripts, and sensitivity tests are committed and independently reproduced.

Avoid:

> This confirms SoCT.

Use instead:

> This is the first empirical candidate signal consistent with the preregistered memory-accumulation prediction.

---

## Immediate Required Artifacts

Before public release or manuscript submission, add:

```text
data/sparc/sparc_age_fdm_data.csv
scripts or notebooks/sparc_age_fdm_analysis.py / .ipynb
figures/sparc/age_dm_full_sample.png
figures/sparc/age_dm_mass_bins.png
papers/cosmology/sparc/sparc-age-dm-paper-draft.md
```

---

## Follow-Up Tests From Source

1. Independent age indicator: D4000, H-alpha EW, color/SED estimate.
2. Out-of-sample validation: 70/30 split.
3. Environment dependence: isolated vs group galaxies.
4. Temporal history proxy: time-integrated star formation history.
5. Radial decomposition: inner vs outer f_DM preference.

---

## Relationship to Existing Repo Files

Related:

```text
experiments/cosmology/sparc-memory-field-preregistration-v0-1.md
experiments/cosmology/sparc-analysis-plan.md
papers/cosmology/sparc/sparc-age-dm-paper-draft.md
```

---

## Verification Checklist

- [ ] Commit derived CSV.
- [ ] Commit exact age proxy source and construction method.
- [ ] Commit f_DM calculation script.
- [ ] Regenerate primary figure from code.
- [ ] Verify p-values from raw arrays.
- [ ] Run sensitivity to outliers.
- [ ] Run Q-only or quality-filtered subset.
- [ ] Add environment/group membership control.
- [ ] Compare against Lambda-CDM assembly-bias interpretation.
- [ ] Update manuscript placeholders.
