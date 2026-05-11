# SPARC Preregistration Mirror

**Status:** Mirror / pointer file  
**Primary prereg artifact:** `experiments/cosmology/sparc-memory-field-preregistration-v0-1.md`

---

## Purpose

This file points the executable SPARC reproducibility package to the preregistration governing the analysis.

The full preregistration draft is maintained at:

```text
experiments/cosmology/sparc-memory-field-preregistration-v0-1.md
```

---

## Locked Primary Hypothesis

Older galaxies should show stronger apparent dark-matter-like signatures than younger galaxies, operationalized as a positive relationship between stellar age and outer inferred dark matter fraction.

Working direction:

```text
corr(age_gyr, f_dm_outer) > 0
```

---

## Primary Analysis Target

```text
Pearson r(age_gyr, f_dm_outer)
Spearman rho(age_gyr, f_dm_outer)
```

---

## Secondary Targets

- partial correlations controlling for Vmax, Rmax, SB0, mass and structure proxies;
- mass-binned correlations;
- bootstrap confidence intervals;
- out-of-sample validation;
- robustness to age proxy and quality cuts.

---

## Rule

If this folder's executable analysis deviates from the preregistration draft, the deviation must be labeled explicitly as exploratory.
