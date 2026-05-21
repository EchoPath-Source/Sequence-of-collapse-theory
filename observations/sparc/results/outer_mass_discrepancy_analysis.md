# SPARC Outer Mass Discrepancy Analysis — SoCT Framework

**Status:** Candidate empirical result / derived SPARC artifact  
**Source thread artifact:** `soct_outer_dm_analysis.txt`  
**Dataset:** SPARC / Rotmod LTG sample, N = 175 galaxies  
**Proxy:** `fdm_outer` = apparent dark matter fraction, mean of last 3 rotation-curve radii  
**Claim level:** Candidate pattern consistent with SoCT; not proof.

---

## Executive Summary

The outer mass discrepancy analysis reports that outer SPARC rotation-curve regions are strongly skewed toward high inferred dark matter fraction, while the correlation between outer dark fraction and central disk surface brightness is weak and not statistically significant.

This supports a conservative SoCT-facing interpretation:

> Central baryonic brightness alone does not explain outer mass discrepancy in this derived SPARC sample. The result motivates testing environmental and formation-history variables, especially filament/void classification and inner/outer radial decomposition.

---

## Distribution Characteristics

Reported values:

```text
Mean fdm_outer:     0.700 ± 0.189
Median fdm_outer:   0.754
Range:              [0.043, 0.927]
Q1:                 0.658
Q2:                 0.754
Q3:                 0.828
Skewness:          -1.709
Kurtosis:           2.800
```

---

## Bimodality / Population Split

Reported categories:

```text
DM-dominated, fdm > 0.7:        111 galaxies, 63.4%
Baryon-dominated, fdm < 0.3:     10 galaxies, 5.7%
Intermediate, 0.3 <= fdm <= 0.7: 54 galaxies, 30.9%
```

Interpretation:

- Strong skew toward dark-matter-dominated outer regions.
- Small but important population of baryon-dominated outer systems.
- Possible two-channel behavior, but this remains exploratory until tested against environment, morphology, and feedback histories.

---

## Correlation With Baryonic Properties

Reported correlations:

```text
fdm_outer vs SB0_disk: r = -0.093, p = 0.223, not significant
fdm_outer vs Vmax:     r = +0.034, p = 0.657, not significant
fdm_outer vs Rmax:     r = +0.168, p = 0.026, weak/significant
```

Interpretation:

- Weak negative correlation with central brightness.
- Essentially no correlation with Vmax.
- Weak positive relationship with Rmax.
- High scatter dominates, suggesting central disk properties alone do not predict the outer residual.

---

## Brightness-Stratified Means

Reported outer dark fraction by central disk surface-brightness quartile:

```text
SB0 Quartile 1, faintest:   0.723, n = 44
SB0 Quartile 2:             0.721, n = 44
SB0 Quartile 3:             0.687, n = 43
SB0 Quartile 4, brightest:  0.667, n = 44
Delta Q1-Q4:               +0.056
```

Interpretation:

> Faintest galaxies have slightly higher outer dark fractions, but the effect is weak.

---

## Extreme Cases

Top 10 highest `fdm_outer`:

```text
Mean fdm:      0.904
Mean SB0_disk: 354.7 Lsun/pc^2
Mean Vmax:     86.5 km/s
```

Bottom 10 lowest `fdm_outer`:

```text
Mean fdm:      0.145
Mean SB0_disk: 214.7 Lsun/pc^2
Mean Vmax:     63.7 km/s
```

Source interpretation:

- Low-DM galaxies are brighter centrally and have somewhat lower Vmax.
- Central baryonic content can suppress apparent outer dark fraction in extreme cases.
- This is a minority population, roughly 5.7% of the sample.

---

## SoCT Interpretation

### Prediction 1 — Outer regions are less sensitive to central baryonic physics

Status: supported as a candidate pattern.

Evidence:

```text
fdm_outer vs SB0_disk: r ≈ -0.09, not significant
```

### Prediction 2 — Environment-dependent memory accumulation matters

Status: not yet tested.

Required:

- cosmic web classification;
- large-scale density field;
- filament/void labels;
- local galaxy density within 1-5 Mpc.

### Prediction 3 — Two-channel behavior may create bimodal outcomes

Status: suggestive only.

Evidence:

```text
63.4% DM-dominated outer regions
5.7% baryon-dominated outer regions
```

### Prediction 4 — Central feedback can suppress apparent DM in rare cases

Status: supported in extreme subset, but not dominant.

### Prediction 5 — Outer/inner ratio should correlate with memory or formation proxy

Status: now partially tested in the radial-decomposition follow-up.

Related file:

```text
observations/sparc/results/inner_outer_radial_decomposition_summary.md
```

---

## Critical Next Tests

1. Cross-match with cosmic web catalogs such as NEXUS+ or V-Web.
2. Correlate `fdm_outer` with filament/void classification.
3. Measure local galaxy density within 1-5 Mpc.
4. Cross-match with HI deficiency / group-environment proxies.
5. Run a toy model comparing bound fraction vs regional memory proxy.
6. Reproduce all results from committed derived CSV and notebook.

---

## Research Boundary

Use:

> The outer SPARC mass-discrepancy distribution shows weak dependence on central disk surface brightness and strong skew toward high outer inferred dark fraction, motivating environmental and radial-decomposition tests.

Avoid:

> This proves SoCT or rules out dark matter.
