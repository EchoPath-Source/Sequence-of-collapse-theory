# P1 Result Tables

This folder stores machine-readable result tables for the canonical P1 SPARC / age-dependent rotation-curve package.

## Imported bundle: 2026-06-09

The following user-provided result CSVs were imported:

| File | Status | Notes |
|---|---|---|
| `SPARC_age_fdm_correlations.csv` | imported | Pearson and Spearman correlation between `age_best` and `fdm_outer_mean`; N=175. |
| `SPARC_age_fdm_partial_correlations.csv` | imported | Partial-correlation checks controlling for `logVmax`, `logRmax`, and `logSB0`; N=175. |
| `SPARC_age_fdm_binned_bootstrap.csv` | imported | Mass-bin bootstrap results for lowV, midV, and highV bins. |

## Claim boundary

These tables are result artifacts, not a complete reproducibility package by themselves. They should be paired with:

- the source/derived SPARC dataset;
- the analysis script or notebook used to generate the tables;
- figure outputs;
- data provenance notes;
- controls/confounds documentation.

Use:

> These result tables report candidate SPARC age/fDM correlations and controls pending full reproduction from committed code.

Avoid:

> These tables prove SoCT or prove that dark matter is collapse memory.
