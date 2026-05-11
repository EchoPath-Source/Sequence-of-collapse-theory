# SPARC Observations Analysis Plan

**Status:** Mirror / implementation checklist  
**Primary detailed plan:** `notebooks/sparc_age_dm_analysis_plan.md`  
**Derived data schema:** `data/sparc/derived-data-schema.md`

---

## Purpose

This file summarizes the executable analysis steps for the `observations/sparc/` package.

---

## Required Input

```text
observations/sparc/data/sparc_age_fdm_data.csv
```

The required schema is defined at:

```text
data/sparc/derived-data-schema.md
```

---

## Analysis Sequence

1. Load derived SPARC table.
2. Validate required columns and sample size.
3. Recompute `f_dm_outer` from velocity columns.
4. Confirm mass-bin assignments.
5. Run primary Pearson and Spearman correlations.
6. Generate full-sample figure.
7. Run mass-binned correlations.
8. Generate mass-bin figure.
9. Run partial correlations.
10. Run multivariate regressions.
11. Run bootstrap confidence intervals.
12. Run 70/30 train-test validation.
13. Run robustness checks.
14. Export tables and summary JSON.
15. Save figure outputs with provenance.

---

## Target Outputs

```text
observations/sparc/results/summary.json
observations/sparc/results/correlation_table.csv
observations/sparc/results/partial_correlations.csv
observations/sparc/results/mass_bin_results.csv
observations/sparc/results/regression_models.csv
observations/sparc/results/bootstrap_results.csv
observations/sparc/figures/age_dm_full_sample.png
observations/sparc/figures/age_dm_mass_bins.png
```

---

## Non-Tuning Rule

The notebook should regenerate the preregistered statistics, not search for better filters after inspecting the result.

Any non-preregistered filter, model, binning, or proxy should be marked:

```text
EXPLORATORY
```

---

## Next Implementation Step

Create:

```text
observations/sparc/sparc_age_dark_matter_analysis.ipynb
```

or a script equivalent:

```text
observations/sparc/sparc_age_dark_matter_analysis.py
```
