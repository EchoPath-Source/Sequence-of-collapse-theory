# SPARC Data Notes

**Status:** Scaffold / pending data import

This folder is reserved for SPARC-related source notes, schemas, derived tables, and small result summaries used in the SoCT collapse-memory empirical program.

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
├─ derived-table-schema.md          # expected columns for derived analysis table
├─ age_fdm_summary.csv              # small derived table, if licensing/provenance allows
├─ radial_decomposition_summary.csv # inner/outer decomposition outputs
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

Thread-level summaries indicate a modest positive age-f_DM trend, but the repo should not treat this as publication-grade until a reproducible notebook and derived table are committed.
