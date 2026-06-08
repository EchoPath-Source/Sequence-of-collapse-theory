# Intake Wave 01 — File Map and Repo Placement

Status: received in chat and mapped. Some files are ready to import directly; DOCX files should be converted or preserved as source before manuscript integration.

## Received files

| File | Type | Track | Recommended repo destination | Import action | Notes |
|---|---|---|---|---|---|
| `PNT_Working_Paper.docx` | DOCX working paper | P5 support / PNT support package | `papers/pnt-dark-energy-hubble-window/source/PNT_Working_Paper.docx` and converted text at `papers/pnt-dark-energy-hubble-window/pnt-working-paper-v0-1.md` | Convert DOCX to Markdown; preserve original externally or via release asset if binary upload is desired | Provides PNT substrate for SoCT memory field, dark energy, void-filament prediction, open issues, and priority calculations. |
| `SOC MZI Visibility Decay Simulation.py` | Python simulation | P4 canonical SOC-MZI | `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py` | Import as code; update style later if needed | Simulates awareness-modulated visibility decay with lambda_eff = lambda_env + lambda_c * A(t). |
| `Gravity as Accumulated Collapse History.md` | Markdown article / working draft | P1 canonical + P1 support | `papers/p1-age-dependent-rotation-curves-sparc/source/gravity-as-accumulated-collapse-history.md` and/or `papers/p1-memory-field-gravity-sparc/source/` | Import as source article; later split into manuscript sections | Contains public-facing explanation, Shephard-Mirrowen Hamiltonian, SPARC signal summary, void prediction, and experimental tests. |
| `void-filament-h0-mechanism.md` | Markdown mechanism note | P5 canonical | `papers/p5-hubble-tension-memory-gradient/mechanism/void-filament-h0-mechanism.md` | Import directly | Toy model: representative local underdensity around delta ~= -0.35 gives H0 ~= 69.3 km/s/Mpc, about 34% of nominal local-CMB Hubble tension. |
| `sparc_age_fdm_analysis.py` | Python analysis script | P1 canonical | `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py` | Import as reproducible analysis script | Reproduces correlations, partial correlations, regression models, binned bootstrap, and scatter plot from source CSV. |
| `sparc_age_fdm_data.csv` | CSV source dataset | P1 canonical / data | `data/sparc/sparc_age_fdm_data.csv` | Import as dataset | 175 rows, 9 columns: galaxy, fdm_outer_mean, age_literature, age_combined_proxy, age_best, age_source, SB0_disk_Lpc2, Vmax_kms, Rmax_kpc. |
| `SPARC_age_fdm_correlations.csv` | CSV result table | P1 canonical / results | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv` | Import as result table | Pearson r ~= 0.200943, p ~= 0.007666; Spearman r ~= 0.211441, p ~= 0.004971; n=175. |
| `SPARC_age_fdm_partial_correlations.csv` | CSV result table | P1 canonical / results | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_partial_correlations.csv` | Import as result table | Partial correlations by controls; Vmax/Rmax/SB0 controls included. |
| `SPARC_age_fdm_binned_bootstrap.csv` | CSV result table | P1 canonical / results | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_binned_bootstrap.csv` | Import as result table | Binned by logVmax into lowV/midV/highV; midV and highV bins show positive old-minus-young mean with CI above zero. |
| `SPARC_age_fdm_README.txt` | TXT bundle README | P1 canonical / results | `papers/p1-age-dependent-rotation-curves-sparc/results/README.md` | Convert to Markdown and import | Notes missing requested B-V color and stellar mass; rerun instructions included. |

## Current have / need by paper

### P1 — Age-Dependent Galactic Rotation Curves / SPARC

Have:

- SPARC source dataset.
- Reproducible Python analysis script.
- Correlation result table.
- Partial-correlation result table.
- Binned bootstrap result table.
- Verification README.
- Gravity-as-memory public-facing source article.

Need:

- Regression models CSV if generated but not included in this wave.
- Scatter plot PNG if generated but not included in this wave.
- Any mass/color controls table with B-V color or stellar mass.
- Formal paper draft or current manuscript.

### P2 — High-Redshift Time-Dependent Gravity

Have:

- No canonical P2 article file in this wave.

Need:

- Medium article export or full text from Feb 9 2026.
- Bibliography / references.
- Any supporting high-redshift galaxy notes.

### P3 — SOC: From Concept to Equation

Have:

- No canonical P3 article file in this wave.

Need:

- Medium article export or full text from Oct 23 2025.
- Equation derivations.
- Any Lindblad / lambda_c derivation notes.

### P4 — SOC-MZI-01 Awareness-Modulated Decoherence

Have:

- SOC MZI visibility decay simulation script.

Need:

- Full SOC-MZI-01 preregistration protocol.
- Appendices.
- AI observer control arm details.
- OSF preregistration export if available.

### P5 — Hubble Tension as Memory Field Gradient

Have:

- PNT working paper.
- Void-filament H0 mechanism note.
- Existing PNT dark-energy support package in repo.

Need:

- Canonical P5 paper outline or draft, if separate from PNT support.
- Pantheon+ environment labels or output tables.
- Covariance-aware H0 fitting outputs if generated.

### P6 — Black Holes as Memory Compression Nodes

Have:

- PNT working paper includes black-hole nucleation and child-universe mechanism.

Need:

- Dedicated black-hole memory compression paper/outline if available.
- Kerr-to-Cosmos draft.
- Causal inversion source files.
- CMB correlation preregistration notes.

### P7 — Unified Framework

Have:

- PNT working paper contributes substrate material.
- Gravity-as-memory article contributes P1/P7 conceptual language.

Need:

- Current unified framework document.
- Equation index / claim-boundary matrix if available.

## Import priority

1. Import P1 CSVs and analysis code into canonical P1/data paths.
2. Import P5 mechanism note and P4 simulation script.
3. Convert `PNT_Working_Paper.docx` to Markdown and place in PNT support package.
4. Import Gravity as Accumulated Collapse History as P1 source material.
5. Wait for P2/P3 Medium exports and P4 full prereg protocol in later waves.
