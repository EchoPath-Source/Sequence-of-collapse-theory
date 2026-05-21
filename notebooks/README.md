# Notebooks

**Status:** Reproducibility landing zone

This folder is reserved for runnable analyses and simulation notebooks supporting SoCT/PNT empirical claims.

---

## Purpose

Every notebook should make a repo claim reproducible.

Preferred standard:

```text
clone repo
install requirements
run notebook
regenerate tables/figures
compare against documented result
```

---

## Notebook Categories

| Category | Example | Claim level |
|---|---|---|
| `observational-analysis` | SPARC age/fDM, Pantheon+ H0 | Evidence-bearing if reproducible |
| `toy-model` | PNT EDE sourced-decay model | Feasibility/conceptual only |
| `simulation` | MZI visibility decay, recursive-universe transfer | Exploratory unless validated |
| `derivation-check` | Kerr ring quantization, f0 cross-constraint | Calculation support |

---

## Required Notebook Header

Every notebook should state:

```text
Title:
Status:
Claim level:
Input files:
Output files:
Random seed:
Dependencies:
Known limitations:
```

---

## Current Priority Notebooks

1. `sparc_age_dm_analysis.ipynb`
   - Reproduce age/fDM correlation.
   - Regenerate full-sample and mass-bin figures.

2. `sparc_inner_outer_radial_decomposition.ipynb`
   - Regenerate `sparc_wise_inner_outer_fdm_split.csv`.
   - Regenerate `inner_outer_correlation_summary.csv`.

3. `pantheon_environment_h0_test.ipynb`
   - Load Pantheon+ covariance.
   - Fit H0 for void and filament subsets.
   - Run robustness checks.

4. `pnt_void_filament_h0_mechanism.ipynb`
   - Reproduce the environment-dependent toy H0 model.
   - Export plots/tables corresponding to the JSX dashboard.

5. `pnt_ede_sourced_decay.ipynb`
   - Reproduce prompt-exhaust / EDE-window toy calculations.

6. `kerr_ring_quantization_check.ipynb`
   - Recompute `M_parent`, `l_E`, `E_E`, and neutrino coincidence check from a single convention.

7. `memory_field_h0_correction.ipynb`
   - Estimate the direct memory-field contribution to local-vs-CMB H0.

8. `tau_ex_plasma_thermalization.ipynb`
   - Estimate whether early-universe plasma microphysics supports required prompt-exhaust timescales.

---

## Output Rules

Notebooks should write small machine-readable summaries to:

```text
data/<track>/results/
observations/<track>/results/
```

Recommended output formats:

```text
summary.json
correlation_table.csv
fit_results.csv
bootstrap_results.csv
figures/*.png
```

---

## Claim Boundary

A notebook result should not be upgraded to manuscript evidence until:

1. inputs are documented;
2. dependencies are pinned;
3. figures regenerate from code;
4. result is stable under basic rerun;
5. limitations and conventional alternatives are stated.
