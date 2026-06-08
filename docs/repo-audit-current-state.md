# Repository Audit: Current SoCT Empirical/Theory State

**Audit date:** 2026-06-08  
**Scope:** current repository state plus intake Waves 01-03 received in chat.  
**Purpose:** distinguish files already committed to the repository from files that were received/uploaded but still need conversion, extraction, or import.

This audit does **not** create or strengthen scientific claims. It separates artifacts by local evidence state and keeps claim boundaries explicit.

## Status-label definitions

- **PRESENT**: the repository contains the file/folder now.
- **RECEIVED / NOT IMPORTED**: the artifact was uploaded in chat and mapped in an intake file, but is not yet committed to its final repository destination.
- **PARTIAL**: some supporting material exists, but a complete reproducible package or manuscript source is not present.
- **MISSING**: the artifact is known from the roadmap/audit, but no uploaded or committed file has been found.
- **ESTABLISHED**: a concrete file artifact exists locally; this does **not** mean the scientific claim is externally established.
- **PRELIMINARY**: a draft, plan, result note, schema, or partial derived dataset exists, but not a full reproducible analysis package.
- **SYNTHETIC**: toy-model, simulation, generated, or non-observational artifact.
- **SPECULATIVE**: conceptual/theory material without a complete empirical validation path in-repo.

## Executive summary

The repository is structurally aligned around the March 2026 seven-paper publication roadmap and now contains canonical paper folders for P1-P7, earlier support scaffolds, and intake trackers for three waves of uploaded files.

The strongest current repository direction is clear: move from scaffold to import/conversion. Several important artifacts are **received but not imported**. These include SPARC CSVs/scripts/figures, PNT and CIH/Kerr/Engramon DOCX source papers, OSF preregistration files, and a ZIP bundle containing SPARC radial-decomposition and PNT/H0 mechanism assets.

The main remaining gap is no longer conceptual structure. It is reproducibility and manuscript readiness:

1. Convert received DOCX/PDF material to Markdown source.
2. Import received CSV/script/Markdown files into canonical locations.
3. Extract ZIP bundle contents and place them in the mapped data/results folders.
4. Add missing reproducibility pieces: notebooks, final regression tables, figure-generation scripts, Pantheon+ real-data outputs, and full P4 protocol/AI observer arm.
5. Keep claim labels conservative until artifacts are reproducible from in-repo data and code.

## Current repo structure already present

### Roadmap, indexes, and intake logs

| Artifact | Status | Notes |
|---|---|---|
| `docs/publication-roadmap-march-2026.md` | PRESENT | Canonical P1-P7 roadmap summary. |
| `papers/README.md` | PRESENT | Paper index and mapping of support folders. |
| `README.md` | PRESENT | Root README references P1-P7 structure and audit links. |
| `docs/intake/wave-01-file-map.md` | PRESENT | Intake tracker for first upload wave. |
| `docs/intake/wave-02-file-map.md` | PRESENT | Intake tracker for second upload wave. |
| `docs/intake/wave-03-file-map.md` | PRESENT | Intake tracker for CIH/Kerr/Engramon/comprehensive report wave. |
| `docs/repo-audit-current-state.md` | PRESENT | This current audit. |

### Canonical paper folders

| Paper | Canonical folder | Status |
|---|---|---|
| P1 | `papers/p1-age-dependent-rotation-curves-sparc/` | PRESENT scaffold; source/results partly received but not imported. |
| P2 | `papers/p2-high-redshift-time-dependent-gravity/` | PRESENT scaffold; source text missing. |
| P3 | `papers/p3-soc-concept-to-equation/` | PRESENT scaffold; source text missing. |
| P4 | `papers/p4-soc-mzi-awareness-modulated-decoherence/` | PRESENT scaffold; prereg excerpt/simulation received but not imported. |
| P5 | `papers/p5-hubble-tension-memory-gradient/` | PRESENT scaffold; PNT/H0 artifacts received but not fully imported. |
| P6 | `papers/p6-black-holes-memory-compression-nodes/` | PRESENT scaffold; strong CIH/Kerr/Engramon source files received but not imported. |
| P7 | `papers/p7-unified-framework/` | PRESENT scaffold; comprehensive report received but not imported. |

### Support folders preserved from earlier scaffold

| Folder | Status | Current role |
|---|---|---|
| `papers/p1-memory-field-gravity-sparc/` | PRESENT | Supports canonical P1. |
| `papers/pnt-dark-energy-hubble-window/` | PRESENT | Supports canonical P5. |
| `papers/p3-causal-inversion-directional-memory/` | PRESENT | Supports canonical P6; older provisional P3 label. |
| `papers/p4-observer-dependent-decoherence-cgds/` | PRESENT | Supports canonical P4. |
| `papers/p5-soct-synthesis/` | PRESENT | Superseded by canonical P7; preserved as earlier synthesis scaffold. |
| `papers/math/` | PRESENT | Supports canonical P3 and P7. |

## Recent-artifact presence table

### P1 — SPARC age / f_DM and gravity-memory

| Artifact | Status | Intended repo location | Notes |
|---|---|---|---|
| `sparc_age_fdm_data.csv` | RECEIVED / NOT IMPORTED | `data/sparc/sparc_age_fdm_data.csv` | Source dataset. |
| `sparc_age_fdm_analysis.py` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py` | Reproducible analysis script. |
| `SPARC_age_fdm_correlations.csv` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv` | Correlation results. |
| `SPARC_age_fdm_partial_correlations.csv` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_partial_correlations.csv` | Partial correlations. |
| `SPARC_age_fdm_binned_bootstrap.csv` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_binned_bootstrap.csv` | Bootstrap result table. |
| `mass_proxy_comparison.csv` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/results/mass_proxy_comparison.csv` | Mass-proxy robustness table. |
| `paper_grade_analysis.png` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/figures/paper_grade_analysis.png` | Figure; binary import pending. |
| `sparc_fdm_vs_age_full_analysis.png` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/figures/sparc_fdm_vs_age_full_analysis.png` | Figure; binary import pending. |
| `sparc_mass_controlled_analysis.png` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/figures/sparc_mass_controlled_analysis.png` | Figure; binary import pending. |
| `Gravity as Accumulated Collapse History.md` | RECEIVED / NOT IMPORTED | `papers/p1-age-dependent-rotation-curves-sparc/source/gravity-as-accumulated-collapse-history.md` | Public-facing source article. |
| `OSF_Prereg_Combined_v061 (1).pdf` | RECEIVED / NOT IMPORTED | `osf/prereg/OSF_Prereg_Combined_v061.pdf`; extracted Markdown at `osf/prereg/soct-pm-v061-sparc-plan.md` | Binary import / Markdown extraction pending. |
| `repo_bundle_sparc_pnt_void.zip` SPARC contents | RECEIVED / NOT IMPORTED | `data/sparc/` and `papers/p1-age-dependent-rotation-curves-sparc/results/` | ZIP extraction/import pending. |
| `SPARC_age_fdm_regression_models.csv` | MISSING | `papers/p1-age-dependent-rotation-curves-sparc/results/` | Mentioned as generated but not uploaded/found. |
| `SPARC_age_vs_fdm_scatter.png` | MISSING | `papers/p1-age-dependent-rotation-curves-sparc/figures/` | Mentioned as generated but not uploaded/found. |
| B-V color / stellar mass controls | MISSING | `data/sparc/` | Needed for stronger mass/color controls. |

### P2 — High-redshift time-dependent gravity

| Artifact | Status | Intended repo location | Notes |
|---|---|---|---|
| Medium export/full text for P2 | MISSING | `papers/p2-high-redshift-time-dependent-gravity/source/` | Needed before manuscript conversion. |
| Formal bibliography | MISSING | `papers/p2-high-redshift-time-dependent-gravity/references.md` | Needed for arXiv/journal version. |

### P3 — SOC: From Concept to Equation

| Artifact | Status | Intended repo location | Notes |
|---|---|---|---|
| Medium export/full text for P3 | MISSING | `papers/p3-soc-concept-to-equation/source/` | Needed before manuscript conversion. |
| Lindblad/equation appendix | MISSING / PARTIAL | `papers/p3-soc-concept-to-equation/appendices/` | Some math support exists, but canonical article is not imported. |

### P4 — SOC-MZI awareness-modulated decoherence

| Artifact | Status | Intended repo location | Notes |
|---|---|---|---|
| `SOC MZI Visibility Decay Simulation.py` | RECEIVED / NOT IMPORTED | `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py` | Simulation script import pending. |
| `OSF_Preregistration_Excerpt_v1.1_clean (1).docx` | RECEIVED / NOT IMPORTED | `papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/OSF_Preregistration_Excerpt_v1.1_clean.md` | Convert DOCX to Markdown. |
| Full SOC-MZI protocol | MISSING / PARTIAL | `papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/` | Excerpt exists; full protocol may still be needed. |
| AI observer control arm | MISSING / PARTIAL | `papers/p4-soc-mzi-awareness-modulated-decoherence/preregistration/` | Mentioned in roadmap; details not yet imported. |

### P5 — Hubble tension / memory gradient / PNT

| Artifact | Status | Intended repo location | Notes |
|---|---|---|---|
| `PNT_Working_Paper.docx` | RECEIVED / NOT IMPORTED | `papers/pnt-dark-energy-hubble-window/pnt-working-paper-v0-1.md` | Convert DOCX to Markdown. |
| `void-filament-h0-mechanism.md` | RECEIVED / NOT IMPORTED | `papers/p5-hubble-tension-memory-gradient/mechanism/void-filament-h0-mechanism.md` | Import directly. |
| `environment_H0_analysis.png` | RECEIVED / NOT IMPORTED | `papers/p5-hubble-tension-memory-gradient/figures/environment_H0_analysis.png` | Figure; binary import pending. |
| `pnt_hubble_void.jsx` from ZIP | RECEIVED / NOT IMPORTED | `papers/p5-hubble-tension-memory-gradient/visualizations/pnt_hubble_void.jsx` | ZIP extraction/import pending. |
| Pantheon+ covariance-aware pipeline/data | MISSING / PARTIAL | `data/pantheon/`, `notebooks/` | Plans/schema exist; real outputs not confirmed. |
| Environment labels | MISSING / PARTIAL | `data/pantheon/` | Schema exists; generated labels not confirmed. |
| Canonical P5 manuscript | MISSING | `papers/p5-hubble-tension-memory-gradient/working-draft.md` | Not yet assembled. |

### P6 — Black holes / CIH / Kerr / Engramon

| Artifact | Status | Intended repo location | Notes |
|---|---|---|---|
| `causal_inversion.docx` | RECEIVED / NOT IMPORTED | `papers/p6-black-holes-memory-compression-nodes/source/causal-inversion-hypothesis.md` | Convert DOCX to Markdown. |
| `kerr_to_cosmos.docx` | RECEIVED / NOT IMPORTED | `papers/p6-black-holes-memory-compression-nodes/source/kerr-to-cosmos.md` | Convert DOCX to Markdown. |
| `engramon_scale.docx` | RECEIVED / NOT IMPORTED | `papers/p6-black-holes-memory-compression-nodes/source/engramon-scale.md` | Convert DOCX to Markdown. |
| `SoCT_Comprehensive_Report_PNT_Annotated.docx` | RECEIVED / NOT IMPORTED | `papers/p7-unified-framework/source/soct-comprehensive-report-pnt-annotated.md` plus P6 extracts | Convert DOCX to Markdown. |
| P6 `open-issues.md` | MISSING | `papers/p6-black-holes-memory-compression-nodes/open-issues.md` | Needed to track M_parent discrepancy, axis derivation, A=f_Omega derivation, and N≈42 tension. |
| Simulation files v1.0-v4.1 | MISSING | `simulations/parent-child-transfer/` | Report references files, but code not uploaded/found. |
| SPARC directional script | MISSING | `simulations/parent-child-transfer/sparc_directional.py` or `papers/p6.../analysis/` | Referenced as pending. |

### P7 — Unified framework

| Artifact | Status | Intended repo location | Notes |
|---|---|---|---|
| `SoCT_Comprehensive_Report_PNT_Annotated.docx` | RECEIVED / NOT IMPORTED | `papers/p7-unified-framework/source/soct-comprehensive-report-pnt-annotated.md` | Strong P7 source document; conversion pending. |
| Unified framework manuscript | MISSING / PARTIAL | `papers/p7-unified-framework/working-draft.md` | Earlier synthesis scaffold exists but canonical P7 draft not assembled. |
| Equation index | MISSING / PARTIAL | `papers/p7-unified-framework/equation-index.md` | Needed for synthesis. |
| Claim-boundary matrix | MISSING | `papers/p7-unified-framework/claim-boundaries.md` | Needed before external release. |

## Intended-structure comparison

The repo now uses the March 2026 seven-paper roadmap as canonical. Earlier folder names remain as support packages and should not be deleted until their contents are migrated or cross-linked.

| Canonical track | Current canonical folder | Support / older folder |
|---|---|---|
| P1 SPARC / age-dependent rotation curves | `papers/p1-age-dependent-rotation-curves-sparc/` | `papers/p1-memory-field-gravity-sparc/` |
| P2 high-redshift time-dependent gravity | `papers/p2-high-redshift-time-dependent-gravity/` | none yet |
| P3 concept-to-equation | `papers/p3-soc-concept-to-equation/` | `papers/math/` |
| P4 SOC-MZI | `papers/p4-soc-mzi-awareness-modulated-decoherence/` | `papers/p4-observer-dependent-decoherence-cgds/` |
| P5 Hubble tension / memory gradient | `papers/p5-hubble-tension-memory-gradient/` | `papers/pnt-dark-energy-hubble-window/` |
| P6 black holes / CIH / Kerr / Engramon | `papers/p6-black-holes-memory-compression-nodes/` | `papers/p3-causal-inversion-directional-memory/` |
| P7 unified framework | `papers/p7-unified-framework/` | `papers/p5-soct-synthesis/` |

## Public-data and copyright cautions

- Do not commit copyrighted full paper PDFs unless license permits redistribution.
- For public datasets such as SPARC or Pantheon+, prefer scripts, schemas, derived tables, and source links over redistributing raw datasets unless the dataset license permits it.
- For uploaded DOCX/PDF manuscripts authored by Antoine/Echo Labs, convert to Markdown source and preserve original binaries only if repo policy permits binary manuscript assets.
- For figures/screenshots generated internally, commit PNGs only if they are original generated outputs.
- Keep claim labels explicit: `internal`, `exploratory`, `preregistered`, `reproducible`, `submission-facing`.

## Claim-boundary rules

1. A result is **reproducible** only when source data, code, and output table/figure are in the repo or linked to stable external storage.
2. A result is **received** only when it has been uploaded in chat or provided in a source file but not yet imported.
3. A result is **publication-ready** only when it has methods, data provenance, reproducible outputs, caveats, and references.
4. Avoid stating that SoCT is confirmed. Use language such as `consistent with`, `initial signal`, `toy-model result`, `requires independent validation`, or `pending reproducible import`.
5. Distinguish real-data analysis, toy simulation, theoretical derivation, source-corpus narrative, and speculative interpretation.

## Recommended PR plan in priority order

### PR 1 — Intake import baseline

Import low-risk received text/CSV/code artifacts:

- P1 CSVs and analysis script.
- P1 `Gravity as Accumulated Collapse History.md` source article.
- P5 `void-filament-h0-mechanism.md`.
- P4 SOC-MZI simulation script.
- ZIP text/CSV contents from `repo_bundle_sparc_pnt_void.zip`.

### PR 2 — Convert DOCX source papers to Markdown

Convert and import:

- `PNT_Working_Paper.docx`.
- `OSF_Preregistration_Excerpt_v1.1_clean (1).docx`.
- `causal_inversion.docx`.
- `kerr_to_cosmos.docx`.
- `engramon_scale.docx`.
- `SoCT_Comprehensive_Report_PNT_Annotated.docx`.

### PR 3 — Figure and binary artifact import

Import generated PNG figures and any permitted original PDFs/DOCX source artifacts. Avoid third-party copyrighted PDFs unless license is clear.

### PR 4 — P6 open issues and simulation registry

Add:

- `papers/p6-black-holes-memory-compression-nodes/open-issues.md`.
- `simulations/parent-child-transfer/README.md`.
- placeholders for missing simulation source files.

### PR 5 — Manuscript assembly

Begin draft assembly in this order:

1. P1 SPARC paper.
2. P5 PNT/Hubble mechanism paper.
3. P6 CIH/Kerr/Engramon paper package.
4. P4 prereg/protocol paper.
5. P7 synthesis after P1-P6 stabilize.

## Current bottom line

The repo is structurally ready. The principal remaining work is moving artifacts from **received in chat** into **repo-imported, converted, reproducible, and manuscript-ready** form.
