# Import Bundle — 2026-06-09 — SPARC Script + MZI Simulation

**Purpose:** track user-provided files imported during the bundle pass.

## Imported files

| Uploaded file | Imported path | Track | Import status |
|---|---|---|---|
| `sparc_age_fdm_analysis.py` | `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py` | P1 / SPARC | Imported as reproducibility script. |
| `SOC MZI Visibility Decay Simulation.py` | `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py` | P4 / SOC-MZI | Initially imported as received; superseded on 2026-06-10 by the complete runnable script from `simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py`. |

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

The SOC-MZI simulation file was initially imported as received and appeared incomplete/truncated at the end of the `simulate_main_effect()` print loop. On 2026-06-10, the canonical paper copy was replaced with the complete runnable script already present under `simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py`.

## Still needed after this bundle

### P1 / SPARC

- `SPARC_age_vs_fdm_scatter.png`
- complete verification that `sparc_age_fdm_analysis.py` runs against the committed dataset from the correct working directory

### P4 / SOC-MZI

- generated P4 simulation outputs/figures, if needed
- statistical analysis plan / negative-result handling

### P5 / Pantheon+

- environment-label table
- any additional environment-H0 tabular output files needed to reproduce the figure
