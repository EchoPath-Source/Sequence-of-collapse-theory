# SPARC Results Outputs

**Status:** PRELIMINARY / reproducibility outputs  
**Paper track:** P1 — Age-Dependent Rotation Curves (SPARC)

This folder is the canonical destination for generated SPARC result tables.

The current reproducibility script is:

```text
notebooks/sparc/sparc_age_dm_analysis.py
```

Run from repository root:

```bash
python notebooks/sparc/sparc_age_dm_analysis.py
```

## Expected generated tables

### `sparc_age_fdm_summary.csv`

Primary correlation summary table. Expected rows include:

- sample size
- Pearson correlation between `age_best` and `fdm_outer_mean`
- Spearman correlation between `age_best` and `fdm_outer_mean`
- mass-proxy correlations
- partial Spearman correlation controlling for mass proxy

### `sparc_mass_bin_summary.csv`

Mass-proxy tertile analysis. This table supports checking whether the age--fDM signal is concentrated in low-, mid-, or high-mass proxy bins.

### `sparc_bootstrap_summary.csv`

Bootstrap stability summary from repeated resampling using the script's fixed random seed.

### `sparc_memory_fit_parameters.csv`

Parameters for the exploratory nonlinear memory fit:

```math
f_{DM}(t) = f_0 + A_{mem}(1 - e^{-t/\tau})
```

These fit parameters are exploratory and should not be treated as physical constants without independent validation.

## Claim boundary

These outputs support a preliminary empirical-correlation claim only. They do not establish a gravitational mechanism, do not prove SoCT, and do not rule out age-proxy, structure, environment, or selection effects.

Publication-grade use requires:

1. Independent rerun of the script.
2. Verification of input data provenance.
3. Review of age-proxy construction.
4. External audit of mass controls and selection cuts.
5. Clear distinction between reported correlation and theoretical interpretation.
