# Intake Wave 02 — File Map and Repo Placement

Status: received in chat and mapped. This wave adds figure artifacts, duplicated/updated PNT and Gravity source files, a repo bundle ZIP, an OSF preregistration PDF, a mass-proxy comparison table, and a clean SOC-MZI preregistration excerpt.

## Received files

| File | Type | Track | Recommended repo destination | Import action | Notes |
|---|---|---|---|---|---|
| `paper_grade_analysis.png` | Figure PNG | P1 | `papers/p1-age-dependent-rotation-curves-sparc/figures/paper_grade_analysis.png` | Import as binary figure when binary upload path is available | Paper-grade robustness panel. Visual verdict: mixed evidence; mass-proxy and med-high bootstrap pass, multivariate independence fails. |
| `sparc_fdm_vs_age_full_analysis.png` | Figure PNG | P1 | `papers/p1-age-dependent-rotation-curves-sparc/figures/sparc_fdm_vs_age_full_analysis.png` | Import as binary figure | Four-panel SPARC age vs outer f_DM analysis. Overall trend shown as r≈0.211, p≈0.005. |
| `environment_H0_analysis.png` | Figure PNG | P5 | `papers/p5-hubble-tension-memory-gradient/figures/environment_H0_analysis.png` | Import as binary figure | Environment-dependent H0 figure: voids, field, filaments; visual annotation shows void-filament significance around 3.39 sigma. |
| `sparc_mass_controlled_analysis.png` | Figure PNG | P1 | `papers/p1-age-dependent-rotation-curves-sparc/figures/sparc_mass_controlled_analysis.png` | Import as binary figure | Mass-controlled SPARC analysis. Shows raw age-f_DM trend and partial age-f_DM after mass control. |
| `Gravity as Accumulated Collapse History.md` | Markdown source article | P1 / P7 support | `papers/p1-age-dependent-rotation-curves-sparc/source/gravity-as-accumulated-collapse-history.md` | Import text directly | Duplicate/update of Wave 01. Public-facing explanatory source for memory-field gravity and SPARC signal. |
| `PNT_Working_Paper.docx` | DOCX working paper | P5 / P6 / P7 support | `papers/pnt-dark-energy-hubble-window/pnt-working-paper-v0-1.md` after conversion | Convert DOCX to Markdown; preserve original source externally or as binary release asset | Duplicate/update of Wave 01. PNT substrate paper for memory field, dark energy, black-hole nucleation, and void-filament differential. |
| `repo_bundle_sparc_pnt_void.zip` | ZIP bundle | P1 / P5 | Multiple destinations listed below | Extract and import text/CSV/JS artifacts | Contains SPARC radial decomposition results, PNT H0 visualization, and void-filament mechanism note. |
| `OSF_Prereg_Combined_v061 (1).pdf` | PDF methods/prereg artifact | P1 / P5 / simulations | `osf/prereg/OSF_Prereg_Combined_v061.pdf` and extracted summary at `osf/prereg/soct-pm-v061-sparc-plan.md` | Preserve PDF externally or binary upload; convert key text to Markdown | SoCT-PM v0.6.1 code freeze + SPARC Age-f_DM analysis plan. |
| `mass_proxy_comparison.csv` | CSV result table | P1 | `papers/p1-age-dependent-rotation-curves-sparc/results/mass_proxy_comparison.csv` | Import directly | Three mass proxies all positive/significant: kinematic, photometric, combined. |
| `OSF_Preregistration_Excerpt_v1.1_clean (1).docx` | DOCX prereg excerpt | P4 | `papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/OSF_Preregistration_Excerpt_v1.1_clean.md` after conversion | Convert DOCX to Markdown | Clean P4 preregistration excerpt: conscious-access variable, triple blinding, deletion protocol, three confirmatory tests, SESOI, risk mitigation. |

## ZIP bundle contents

`repo_bundle_sparc_pnt_void.zip` contains:

| Bundle path | Recommended repo destination | Track | Notes |
|---|---|---|---|
| `README_BUNDLE.md` | `docs/intake/repo_bundle_sparc_pnt_void_README.md` | Intake | Bundle metadata. |
| `visualizations/pnt_hubble_void.jsx` | `papers/p5-hubble-tension-memory-gradient/visualizations/pnt_hubble_void.jsx` | P5 | Visualization for PNT Hubble void mechanism. |
| `papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md` | `papers/p5-hubble-tension-memory-gradient/mechanism/void-filament-h0-mechanism.md` and/or support package | P5 | Same mechanism note as standalone upload. |
| `observations/sparc/results/inner_outer_correlation_summary.csv` | `papers/p1-age-dependent-rotation-curves-sparc/results/inner_outer_correlation_summary.csv` | P1 | Radial decomposition / inner-outer correlation result. |
| `observations/sparc/results/outer_mass_discrepancy_analysis.md` | `papers/p1-age-dependent-rotation-curves-sparc/results/outer_mass_discrepancy_analysis.md` | P1 | Outer mass-discrepancy analysis note. |
| `observations/sparc/results/inner_outer_radial_decomposition_summary.md` | `papers/p1-age-dependent-rotation-curves-sparc/results/inner_outer_radial_decomposition_summary.md` | P1 | Inner/outer radial decomposition summary. |
| `observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv` | `data/sparc/sparc_wise_inner_outer_fdm_split.csv` | P1 / data | SPARC WISE inner/outer f_DM split dataset. |

## Current have / need by paper after Wave 02

### P1 — Age-Dependent Galactic Rotation Curves / SPARC

Have:

- Source dataset: `sparc_age_fdm_data.csv`.
- Reproducible analysis script: `sparc_age_fdm_analysis.py`.
- Correlation, partial-correlation, bootstrap, and mass-proxy comparison tables.
- SPARC figures: full analysis, mass-controlled analysis, paper-grade robustness panel.
- Gravity-as-memory source article.
- OSF combined prereg/methods PDF covering SoCT-PM v0.6.1 + SPARC Age-f_DM plan.
- ZIP bundle with inner/outer radial decomposition materials.

Still need:

- `SPARC_age_fdm_regression_models.csv` if generated.
- `SPARC_age_vs_fdm_scatter.png` if generated.
- Preferred stellar mass / B-V color control table.
- Formal P1 manuscript draft.

### P2 — High-Redshift Time-Dependent Gravity

Have:

- No canonical P2 source text yet in Waves 01–02.

Still need:

- Medium article export or full text from Feb 9 2026.
- Formal references / bibliography.

### P3 — SOC: From Concept to Equation

Have:

- No canonical P3 source text yet in Waves 01–02.

Still need:

- Medium article export or full text from Oct 23 2025.
- Equation derivations / Lindblad appendix.

### P4 — SOC-MZI-01 Awareness-Modulated Decoherence

Have:

- SOC-MZI visibility decay simulation script.
- OSF preregistration excerpt v1.1 with conscious-access variable, blinding, deletion, three confirmatory tests, SESOI, and risk mitigation.

Still need:

- Full SOC-MZI-01 preregistration protocol if excerpt is not complete.
- AI observer control arm details.
- Appendices and device-specific analysis plan.

### P5 — Hubble Tension as Memory Field Gradient

Have:

- PNT working paper.
- Void-filament H0 mechanism note.
- Environment-H0 analysis figure.
- PNT Hubble void JSX visualization from bundle.
- Existing PNT dark-energy support package in repo.

Still need:

- Pantheon+ environment labels / real-data tables if available.
- Covariance-aware H0 fitting outputs if generated.
- Canonical P5 manuscript draft.

### P6 — Black Holes as Memory Compression Nodes

Have:

- PNT working paper contains black-hole nucleation and child-universe mechanism.
- Existing causal-inversion / directional-memory support folder in repo.

Still need:

- Dedicated black-hole memory compression paper or outline.
- Kerr-to-Cosmos draft.
- Causal inversion full source if not already imported.
- CMB correlation preregistration plan.

### P7 — Unified Framework

Have:

- PNT contributes substrate language.
- Gravity-as-memory contributes conceptual P1/P7 language.
- Existing math scaffold and earlier synthesis scaffold.

Still need:

- Current unified framework working paper.
- Equation index / claim-boundary matrix if available.

## Import priority after Wave 02

1. Import P1 CSVs, mass-proxy comparison, analysis code, and radial-decomposition bundle outputs.
2. Import P5 mechanism note and PNT Hubble visualization source.
3. Convert PNT working paper to Markdown and place in PNT support package.
4. Convert P4 preregistration excerpt to Markdown and place in P4 preregistration folder.
5. Track images as figure assets; import binary PNGs when binary upload workflow is available.
6. Wait for P2/P3 Medium exports and full P4 protocol in later waves.
