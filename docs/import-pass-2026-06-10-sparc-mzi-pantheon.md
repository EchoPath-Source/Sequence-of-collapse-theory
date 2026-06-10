# Import/Reconciliation Pass — 2026-06-10 — SPARC, SOC-MZI, and Pantheon+

**Purpose:** record the follow-up reconciliation for artifacts that were previously listed as missing after the June 8/9 import passes.

## Confirmed present or newly reconciled

| Artifact | Repo path | Track | Status |
|---|---|---|---|
| `sparc_age_fdm_analysis.py` | `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py` | P1 / SPARC | Imported reproducibility script. |
| `sparc_age_fdm_analysis.py` wrapper | `notebooks/sparc/sparc_age_fdm_analysis.py` | P1 / SPARC | Compatibility wrapper present for the expected notebook-path filename. |
| `SPARC_age_fdm_regression_models.csv` | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_regression_models.csv` | P1 / SPARC | Imported candidate regression-result CSV. |
| `mass_proxy_comparison.csv` | `papers/p1-age-dependent-rotation-curves-sparc/results/mass_proxy_comparison.csv` | P1 / SPARC | Verified in-place as the imported mass-proxy robustness CSV; keep exact table values as committed. |
| `SOC MZI Visibility Decay Simulation.py` | `simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py` | P4 / SOC-MZI | Complete runnable simulation script present at the exact uploaded filename. |
| SOC-MZI canonical paper simulation copy | `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py` | P4 / SOC-MZI | Replaced with the complete runnable script from `simulations/mzi-visibility-decay/`. |
| `Pantheon+SH0ES.dat` | documented in `data/pantheon/README.md`; expected raw path `data/pantheon/raw/Pantheon+SH0ES.dat` if committed later | P5 / Pantheon+ | Public source documented; local uploaded file was not present in this workspace at reconciliation time. |
| `Pantheon+SH0ES_STAT+SYS.cov` | documented in `data/pantheon/README.md`; expected raw path `data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov` if committed later | P5 / Pantheon+ | Public source documented; local uploaded file was not present in this workspace at reconciliation time. |

## Pantheon+ boundary after this pass

The real Pantheon+ missing derived artifact is the environment-label table:

```text
data/pantheon/environment_labels.csv
```

The public Pantheon+SH0ES SN table and STAT+SYS covariance are documented as source inputs, not as derived missing artifacts. If redistribution is cleared and the files are supplied inside the workspace, place them under `data/pantheon/raw/` and add size/checksum lines here.

## Claim boundary

All SPARC CSVs remain candidate result artifacts pending full reproducible regeneration. The SOC-MZI script is a simulation/preregistration support artifact, not empirical evidence. Pantheon+ environment-H0 analysis remains blocked until environment labels are created/imported and validated.
