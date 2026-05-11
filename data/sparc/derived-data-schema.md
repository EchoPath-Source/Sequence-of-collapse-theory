# SPARC Derived Data Schema

**Status:** Data schema scaffold  
**Related files:**

```text
experiments/cosmology/sparc-memory-field-preregistration-v0-1.md
experiments/cosmology/sparc-analysis-plan.md
papers/cosmology/sparc/sparc-age-dm-publication-summary-v1.md
papers/cosmology/sparc/sparc-age-dm-paper-draft.md
```

---

## Purpose

This file defines the required schema for the derived SPARC table needed to reproduce the reported age-dark-matter correlation and all downstream figures/statistics.

The next committed data artifact should be:

```text
data/sparc/sparc_age_fdm_data.csv
```

or, if the raw/derived data should not be committed yet:

```text
data/sparc/sparc_age_fdm_data.schema-only.md
```

---

## Required Columns

| Column | Type | Required | Description |
|---|---|---:|---|
| `galaxy_id` | string | yes | SPARC galaxy identifier. |
| `sparc_name` | string | yes | Original SPARC name if different from `galaxy_id`. |
| `quality_flag` | int | yes | SPARC quality flag used for filtering. |
| `inclination_deg` | float | yes | Disk inclination in degrees. |
| `distance_mpc` | float | yes | Galaxy distance in Mpc. |
| `morphology` | string | recommended | Hubble type / morphology label. |
| `log_mstar` | float | yes | Log stellar mass estimate. |
| `log_mgas` | float | recommended | Log gas mass estimate. |
| `gas_fraction` | float | recommended | Gas-to-stellar mass ratio or equivalent. |
| `vmax_kms` | float | yes | Maximum observed rotation velocity. |
| `rmax_kpc` | float | yes | Radius associated with outermost reliable point or maximum radius. |
| `sb0` | float | yes | Central surface brightness or structural proxy used in controls. |
| `age_gyr` | float | yes | Mean stellar age proxy in Gyr. |
| `age_source` | string | yes | Source/method for age estimate. |
| `age_unc_gyr` | float | recommended | Age uncertainty if available. |
| `v_obs_outer_kms` | float | yes | Observed velocity at outer measurement radius. |
| `v_bary_outer_kms` | float | yes | Baryonic velocity contribution at same radius. |
| `r_outer_kpc` | float | yes | Radius of outer measurement. |
| `r_half_kpc` | float | recommended | Half-light or effective radius. |
| `f_dm_outer` | float | yes | Outer inferred dark matter fraction. |
| `mass_bin` | categorical | yes | Low / Mid / High mass bin used in tercile analysis. |
| `environment` | string | optional | Isolated / group / cluster / unknown. |
| `notes` | string | optional | Flags, caveats, manual notes. |

---

## Derived Quantities

### Outer Dark Matter Fraction

Primary working definition:

```text
f_dm_outer = 1 - (v_bary_outer_kms / v_obs_outer_kms)^2
```

Boundary handling:

- Values below 0 should be flagged and retained/excluded according to prereg rules.
- Values above 1 should be flagged.
- Any clipping must be reported and justified.

### Flatness Ratio

For preregistration-aligned analysis:

```text
F = v_out / v_in
```

Where:

```text
v_in  = median velocity at r < 0.5 R_eff
v_out = median velocity at 2.0 < r/R_eff < 3.0
```

If `R_eff` is unavailable, the analysis must document the proxy used.

### Mass Bins

Current reported mass bins used terciles by `Vmax`:

```text
Low mass:  n = 59
Mid mass:  n = 58
High mass: n = 58
```

The exact bin thresholds must be committed in the analysis notebook.

---

## Required Validation Checks

Before publication claims:

1. Confirm `n = 175` after all filters or document differences.
2. Verify `age_gyr` construction and source for every galaxy.
3. Verify `f_dm_outer` recomputes from velocity columns.
4. Verify mass-bin membership from `vmax_kms` thresholds.
5. Reproduce:

```text
Pearson r = +0.201, p = 0.0077
Spearman rho = +0.211, p = 0.0050
```

6. Reproduce mass-bin results:

```text
Low:  r = +0.115, p = 0.384
Mid:  r = +0.456, p = 3.2e-4
High: r = +0.277, p = 0.036
```

7. Reproduce partial correlations:

```text
Vmax only       partial r = +0.289
Rmax only       partial r = +0.223
SB0 only        partial r = +0.156
Vmax + Rmax     partial r = +0.265
```

8. Reproduce multivariate regression coefficients.
9. Run outlier and high-leverage diagnostics.
10. Run quality-flag and inclination robustness checks.

---

## Recommended File Plan

```text
data/sparc/
  derived-data-schema.md
  sparc_age_fdm_data.csv
  sparc_age_fdm_data_dictionary.md
  raw-source-notes.md

notebooks/
  sparc_age_dm_analysis.ipynb

figures/sparc/
  age_dm_full_sample.png
  age_dm_mass_bins.png
```

---

## Provenance Requirement

Every derived column must include a documented source.

Minimum provenance fields:

```text
source_file
source_catalog
calculation_method
script_version
analysis_date
```

---

## Research Boundary

The current SPARC result should remain described as an internally reported candidate signal until this schema is populated and the analysis is reproduced from committed data/code.
