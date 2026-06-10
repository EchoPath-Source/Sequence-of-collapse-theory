# SPARC Reproducibility Manifest

**Status:** PRELIMINARY / reproducibility support  
**Claim level:** Candidate empirical result, pending full independent review.  
**Track:** P1 — Age-Dependent Galactic Rotation Curves / SPARC

---

## Purpose

This manifest records the current runnable and machine-readable artifacts for the SPARC age / outer-fDM track.

The goal is to distinguish:

- canonical inputs,
- runnable scripts,
- generated outputs,
- paper-local candidate result tables,
- remaining missing controls.

---

## Canonical runnable script

The canonical implementation currently lives at:

```text
notebooks/sparc/sparc_age_dm_analysis.py
```

A compatibility wrapper has been added at the filename expected by older manifests:

```text
notebooks/sparc/sparc_age_fdm_analysis.py
```

Both should execute the same analysis path.

Run from repository root:

```bash
python notebooks/sparc/sparc_age_fdm_analysis.py
```

or:

```bash
python notebooks/sparc/sparc_age_dm_analysis.py
```

---

## Canonical input tables

Primary age/fDM input:

```text
data/sparc/sparc_age_fdm_data.csv
```

Inner/outer radial split data:

```text
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
```

Repo-level mirror:

```text
data/sparc/sparc_wise_inner_outer_fdm_split.csv
```

---

## Generated output targets from the current script

The current script writes:

```text
observations/sparc/results/sparc_age_fdm_summary.csv
observations/sparc/results/sparc_mass_bin_summary.csv
observations/sparc/results/sparc_bootstrap_summary.csv
observations/sparc/results/sparc_memory_fit_parameters.csv
figures/sparc/sparc_age_fdm_scatter.png
figures/sparc/sparc_memory_fit.png
figures/sparc/sparc_mass_bins.png
```

These should be regenerated and compared against existing paper-local tables before any claim escalation.

---

## Existing derived/result artifacts

Already present in the repo:

```text
observations/sparc/results/outer_mass_discrepancy_analysis.md
observations/sparc/results/inner_outer_radial_decomposition_summary.md
observations/sparc/results/inner_outer_correlation_summary.csv
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_partial_correlations.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_binned_bootstrap.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_regression_models.csv
papers/p1-age-dependent-rotation-curves-sparc/results/mass_proxy_comparison.csv
```

---

## Current missing / incomplete items

Still needed for a stronger P1 reproducibility package:

```text
observations/sparc/sparc_age_dark_matter_analysis.ipynb
figures/sparc/figure-provenance.md updates for all new figures
SPARC_age_vs_fdm_scatter.png or confirmed replacement path
complete provenance note for age_source / proxy-age construction
outlier and leverage diagnostics
environment / cosmic-web cross-match controls
```

---

## Claim boundary

Use:

> The SPARC package now contains candidate result tables, derived data, and runnable analysis support for the age/fDM and inner/outer radial-decomposition tracks.

Avoid:

> The SPARC package proves SoCT or rules out dark matter.
