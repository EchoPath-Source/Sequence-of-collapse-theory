# SPARC Derived Data

**Status:** scaffold pending source files / links  
**Purpose:** document the provenance and reproducibility path for every SPARC-derived table used in the age / missing-mass analysis.

## Rules

Do not add derived or cleaned tables without documenting:

1. source URL or citation,
2. access date,
3. license or usage constraints,
4. variables imported,
5. cleaning steps,
6. whether the table is raw, cleaned, merged, or derived.

## Required primary derived files

The two highest-priority derived datasets are:

```text
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
observations/sparc/data/sparc_age_fdm_data.csv
```

These files are not currently generated in-repo. They should be committed only after the derivation path is documented and the source provenance is clear.

## Expected file roles

### `sparc_wise_inner_outer_fdm_split.csv`

Primary radial-decomposition table. This should contain one row per usable galaxy with WISE-derived age or stellar-population proxy fields, inner and outer dark-matter-fraction estimates, and any quality-control flags used in the radial split.

Recommended minimum columns:

```text
galaxy_id
age_proxy_gyr
mass_proxy
surface_brightness_proxy
r_inner_definition
r_outer_definition
fdm_inner
fdm_outer
fdm_outer_error
quality_flag
source_notes
```

### `sparc_age_fdm_data.csv`

Primary age-versus-outer-dark-fraction table used for the core correlation and memory-fit analyses.

Recommended minimum columns:

```text
galaxy_id
age_proxy_gyr
fdm_outer
fdm_outer_error
mass_proxy
rmax
vmax
surface_brightness_proxy
environment_label
interaction_flag
quality_flag
source_notes
```

## Regenerated outputs

The analysis notebook or script should regenerate:

```text
observations/sparc/results/inner_outer_correlation_summary.csv
observations/sparc/results/correlation_table.csv
observations/sparc/results/bootstrap_results.csv
observations/sparc/figures/
```

## Integrity rule

Do not treat visually extracted values, screenshots, or LLM-assisted estimates as production data. They may be described in internal notes only and must be replaced by reproducible tables before manuscript-level claims are made.
