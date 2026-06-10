# Import Bundle — 2026-06-09 — SPARC Script + MZI Simulation

**Purpose:** track user-provided files imported during the bundle pass.

## Imported files

| Uploaded file | Imported path | Track | Import status |
|---|---|---|---|
| `sparc_age_fdm_analysis.py` | `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py` | P1 / SPARC | Imported as reproducibility script. |
| `SOC MZI Visibility Decay Simulation.py` | `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py` | P4 / SOC-MZI | Imported exactly as received; source appears truncated/incomplete and should be replaced with complete script if available. |

## P1 status update

This closes one of the main missing reproducibility artifacts from the audit:

- `sparc_age_fdm_analysis.py`

The script generates:

- `SPARC_age_fdm_correlations.csv`
- `SPARC_age_fdm_partial_correlations.csv`
- `SPARC_age_fdm_regression_models.csv`
- `SPARC_age_fdm_binned_bootstrap.csv`
- `SPARC_age_vs_fdm_scatter.png`

## P4 status update

The SOC-MZI simulation file was imported as received, but the uploaded file appears incomplete/truncated at the end of the `simulate_main_effect()` print loop. It should be replaced by a complete version before marking the P4 simulation as runnable.

## Still needed after this bundle

### P1 / SPARC

- `mass_proxy_comparison.csv`
- `paper_grade_analysis.png`
- `sparc_fdm_vs_age_full_analysis.png`
- `sparc_mass_controlled_analysis.png`
- `SPARC_age_fdm_regression_models.csv`
- `SPARC_age_vs_fdm_scatter.png`
- complete verification that `sparc_age_fdm_analysis.py` runs against the committed dataset from the correct working directory

### P4 / SOC-MZI

- complete, non-truncated SOC-MZI visibility simulation script, if available
- generated P4 simulation outputs/figures, if available
- statistical analysis plan / negative-result handling

### P5 / Pantheon+

- Pantheon+ covariance matrix
- Pantheon+ SN table
- environment-label table
- environment-H0 figure/output files
