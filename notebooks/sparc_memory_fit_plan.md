# SPARC Memory-Fit Notebook Plan

**Status:** scaffold / pending runnable notebook  
**Target notebook:** `observations/sparc/sparc_age_dark_matter_analysis.ipynb` or `notebooks/sparc_memory_fit.ipynb`  
**Claim level:** exploratory until input tables and regenerated outputs are committed

## Purpose

This note defines the reproducibility contract for fitting the SoCT memory-accumulation model to the SPARC age / outer-dark-fraction dataset.

The central phenomenological model is:

```math
f_{DM}(t) = f_0 + A_{mem}(1 - e^{-t/\tau})
```

where:

- `f_0` is the age-independent baseline apparent dark fraction;
- `A_mem` is the memory-amplitude term;
- `tau` is the accumulation timescale;
- `t` is the selected stellar-population age proxy.

## Required Inputs

```text
observations/sparc/data/sparc_age_fdm_data.csv
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
```

Minimum required columns are documented in:

```text
observations/sparc/data/README.md
```

## Primary Outputs

The notebook should regenerate:

```text
observations/sparc/results/correlation_table.csv
observations/sparc/results/bootstrap_results.csv
observations/sparc/results/memory_fit_parameters.csv
observations/sparc/figures/age_fdm_scatter.png
observations/sparc/figures/memory_fit_curve.png
```

## Primary Analysis Steps

1. Load `sparc_age_fdm_data.csv`.
2. Validate required columns and missing values.
3. Recompute outer dark fraction where the required velocity columns are available:

```math
f_{DM} = 1 - (V_{bar}/V_{obs})^2
```

4. Run baseline Pearson and Spearman age-vs-outer-`f_DM` correlations.
5. Run controlled regressions with mass proxy and structural covariates.
6. Fit the exponential memory model.
7. Bootstrap `f_0`, `A_mem`, and `tau` confidence intervals.
8. Export tables and figures.

## Controlled Model

Minimum controlled form:

```math
f_{DM,i} = f_0 + A_{mem}(1 - e^{-age_i/\tau}) + \beta_M M_i + \epsilon_i
```

Expanded exploratory controls may include:

```text
mass_proxy
surface_brightness_proxy
rmax
vmax
environment_label
interaction_flag
```

## Interpretation Boundary

A visually estimated timescale from a figure is not a production result. The notebook must fit `tau` directly from the committed dataset and report uncertainty before this model can support a manuscript-level claim.

A positive `A_mem` and a stable `tau` in the approximate few-Gyr range would be treated as a coherence signal, not proof of modified gravity.
