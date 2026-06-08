# SPARC Data Notes

**Status:** PRELIMINARY derived-data import present

This folder holds SPARC-related source notes, schemas, derived tables, and small result summaries used in the SoCT collapse-memory empirical program.

## Current Role

SPARC is the recommended P1 empirical anchor for testing whether collapse-history proxies correlate with apparent missing-mass behavior in disk-galaxy rotation curves.

Primary working observable:

```math
f_DM = 1 - (V_bar / V_obs)^2
```

Primary working prediction:

```text
older stellar populations should show higher outer f_DM, especially in low-baryon-acceleration / outer-disk regions
```

## Expected Files

```text
data/sparc/
├─ README.md
├─ source-notes.md                  # source URLs, citation requirements, version notes
├─ derived-data-schema.md           # expected columns for derived analysis table
├─ sparc_age_fdm_data.csv           # PRELIMINARY derived age/fDM table
├─ sparc_wise_inner_outer_fdm_split.csv # PRELIMINARY inner/outer decomposition table
└─ results/
   ├─ correlation-summary.md
   └─ nonlinear-memory-fit-summary.md
```

## Minimum Derived Table Columns

Recommended schema for a derived analysis CSV:

```text
galaxy_id
age_proxy
age_proxy_source
f_dm_outer
f_dm_inner
v_obs_outer
v_bar_outer
mass_proxy
surface_brightness_proxy
r_max
v_max
environment_label
quality_flag
notes
```

## Required Provenance

Before adding derived CSVs, include:

- SPARC source/version used.
- Rotmod file source and access date.
- Stellar mass-to-light assumptions.
- Age proxy source and mapping method.
- Radius cut used for inner/outer decomposition.
- Quality cuts and excluded objects.

## Current Claim Boundary

Derived SPARC tables and a runnable analysis script are now present, but the repo should not treat the result as publication-grade until provenance, regeneration instructions, controls, and figure reproducibility are fully audited.
