# SPARC Tables

**Evidence label:** `real-data-analysis` when tables are derived from documented SPARC inputs.

This folder is reserved for clean, machine-readable SPARC tables and derived metrics.

## Current status
The repo already contains at least one derived split dataset under:

```text
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
```

This tables folder should be used for additional cleaned or publication-facing tables.

## Table requirements
Every table should include or link to:

1. column definitions,
2. source data provenance,
3. filtering rules,
4. derived metric formulas,
5. script or notebook that generated it.

## Recommended future tables

```text
sparc_outer_fdm_summary_table.csv
sparc_age_proxy_crossmatch_table.csv
sparc_environment_crossmatch_table.csv
sparc_inner_outer_radial_split_table.csv
```

## Rule
Do not add AI-generated or synthetic rows to this folder. Tables here should be reproducible from named data sources.
