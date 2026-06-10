# SPARC Scripts

**Evidence label:** `real-data-analysis` when scripts reproduce committed SPARC outputs.

This folder is reserved for scripts and notebooks that regenerate the SPARC analysis artifacts.

## Current status
The repo contains SPARC result summaries and derived data, but the runnable reproduction script/notebook is still the main missing artifact.

## Required reproduction targets
A script or notebook added here should regenerate:

```text
observations/sparc/results/outer_mass_discrepancy_analysis.md
observations/sparc/results/inner_outer_radial_decomposition_summary.md
observations/sparc/results/inner_outer_correlation_summary.csv
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
```

## Required metadata
Each script should state:

1. input files used,
2. external data source and version,
3. filtering rules,
4. derived variable definitions,
5. exact command to run,
6. expected output paths.

## Priority
Highest-priority missing artifact for the SPARC track:

```text
observations/sparc/scripts/reproduce_inner_outer_radial_decomposition.py
```
