# Repository Audit: Current SoCT Empirical/Theory State

**Audit date:** 2026-06-08  
**Scope:** full recursive scan of the current repository, with detailed grouping for `docs/`, `observations/sparc/`, `data/`, `notebooks/`, `figures/sparc/`, `papers/`, `simulations/`, `experiments/`, `references/`, and `visualizations/`.  
**Claim rule:** this audit does not create or strengthen scientific claims. It separates files that already exist from files that are missing, and labels artifacts as **ESTABLISHED**, **PRELIMINARY**, **SYNTHETIC**, **SPECULATIVE**, or **MISSING**.

## Status-label definitions

- **ESTABLISHED**: the repository contains a concrete file artifact with enough local context to verify that the artifact exists. This label does **not** mean the scientific claim is established externally.
- **PRELIMINARY**: the repository contains a draft, plan, scaffold, result note, schema, or partial derived dataset, but not a complete reproducible analysis package.
- **SYNTHETIC**: the repository contains toy-model, simulation, generated, or non-observational artifacts.
- **SPECULATIVE**: the repository contains conceptual/theory material without a complete empirical validation path in-repo.
- **MISSING**: the artifact or folder named in the intended structure was not found in the repository scan.

## Executive summary

The repo is documentation-rich and already includes several SoCT/SPARC/PNT/CIH scaffolds, drafts, notes, and some derived SPARC CSV artifacts. The strongest local empirical asset is the SPARC age/f_DM derived table, present in both `data/sparc/` and `observations/sparc/data/`. However, the repo does **not** yet contain runnable SPARC notebooks/scripts that regenerate the reported statistics, and it does **not** contain actual Pantheon+ SN table, full covariance matrix, or environment-label table. The Pantheon+ lane is currently an analysis-plan/schema scaffold rather than a reproducible pipeline.

The intended new structure is only partially present. Current paper folders follow older/canonical roadmap names such as `papers/p1-*`, `papers/p3-*`, and `papers/pnt-dark-energy-hubble-window/`; several intended folders such as `papers/sparc-gravitational-memory/`, `papers/soct-comprehensive-report/`, and `observations/pantheon-environment-h0/` are missing.

## Current repo inventory

### `docs/`

- `docs/book-of-collapse-article-map.md`
- `docs/canonical-parameter-ledger.md`
- `docs/concepts/engramon-scale.md`
- `docs/dark-sector-taxonomy.md`
- `docs/dimensional-projection-ansatz.md`
- `docs/empirical-exploration-thread-summary-v0-1.md`
- `docs/equations-and-testable-hypotheses.md`
- `docs/experiments/osf-consciousness-gated-double-slit-prereg-excerpt-v1.1.md`
- `docs/final-import-manifest-2026-05-05.md`
- `docs/frameworks/sequence-of-collapse-unified-physics-framework.md`
- `docs/import-batch-2026-04-07.md`
- `docs/import_log_2026-05-05.md`
- `docs/intake/wave-01-file-map.md`
- `docs/intake/wave-02-file-map.md`
- `docs/intake/wave-03-file-map.md`
- `docs/metaphysics/full-vision-overview.md`
- `docs/metaphysics/metaphysical-declarations.md`
- `docs/next-calculation-priority-roadmap.md`
- `docs/next_wave_import_candidates.md`
- `docs/observations/data/README.md`
- `docs/observations/data/sparc_wise_fdm_with_Q_and_radii.csv`
- `docs/observations/sparc-wise-color-residual-analysis-summary.md`
- `docs/origin-echo-recursion.md`
- `docs/philosophical-foundations-consciousness-continuity.md`
- `docs/planck-memory-substrate.md`
- `docs/publication-roadmap-march-2026.md`
- `docs/publications/source-lineage-index.md`
- `docs/repo-map.md`
- `docs/simulations/parent-child-directional-transfer-research-record.md`
- `docs/source-corpus.md`
- `docs/theory/causal-inversion-hypothesis.md`
- `docs/theory/engramon-scale-notes.md`
- `docs/theory/from-kerr-to-cosmos-axis-of-evil-prediction.md`
- `docs/theory/gravity-as-accumulated-collapse-history.md`
- `docs/theory-notes/README.md`
- `docs/theory-notes/dimensional-bridge-principle.md`
- `docs/theory-notes/origin-curvature-synthesis.md`
- `docs/theory-notes/origin-point-postulate.md`
- `docs/theory-notes/planck-cell-unfolding-hypothesis.md`
- `docs/theory-notes/quark-projection-hypothesis.md`
- `docs/theory-notes/threshold-unfolding-principle.md`
- `docs/theory-overview.md`
- `docs/validation/soct-validation-roadmap-feb-2026.md`

### `observations/sparc/`

- `observations/sparc/README.md`
- `observations/sparc/analyses/current-status-note.md`
- `observations/sparc/analysis-plan.md`
- `observations/sparc/data/README.md`
- `observations/sparc/data/source-links.md`
- `observations/sparc/data/sparc_age_fdm_data.csv`
- `observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv`
- `observations/sparc/preregistration.md`
- `observations/sparc/requirements.txt`
- `observations/sparc/results/inner_outer_correlation_summary.csv`
- `observations/sparc/results/inner_outer_radial_decomposition_summary.md`
- `observations/sparc/results/outer_mass_discrepancy_analysis.md`

### `data/`

- `data/README.md`
- `data/pantheon/README.md`
- `data/pantheon/covariance-notes.md`
- `data/pantheon/environment-labels-schema.md`
- `data/sparc/README.md`
- `data/sparc/derived-data-schema.md`
- `data/sparc/sparc_age_fdm_data.csv`

### `notebooks/`

- `notebooks/README.md`
- `notebooks/pantheon_environment_h0_fit_plan.md`
- `notebooks/sparc_age_dm_analysis_plan.md`
- `notebooks/sparc_memory_fit_plan.md`

### `figures/sparc/`

- `figures/sparc/figure-provenance.md`

### `papers/`

- `papers/README.md`
- `papers/cosmology/cih/cih-package-index.md`
- `papers/cosmology/pnt/planck-nucleation-theory-master-note.md`
- `papers/cosmology/sparc/sparc-age-dm-paper-draft.md`
- `papers/cosmology/sparc/sparc-age-dm-publication-summary-v1.md`
- `papers/math/soc-localization-memory-hamiltonian.md`
- `papers/notes/references.bib`
- `papers/notes/sparc-wise-color-dependent-residual-note.md`
- `papers/notes/sparc-wise-color-dependent-residual-note.tex`
- `papers/p1-age-dependent-rotation-curves-sparc/README.md`
- `papers/p1-memory-field-gravity-sparc/README.md`
- `papers/p1-memory-field-gravity-sparc/outline-v0-1.md`
- `papers/p2-high-redshift-time-dependent-gravity/README.md`
- `papers/p3-causal-inversion-directional-memory/README.md`
- `papers/p3-causal-inversion-directional-memory/outline-v0-1.md`
- `papers/p3-soc-concept-to-equation/README.md`
- `papers/p4-observer-dependent-decoherence-cgds/README.md`
- `papers/p4-observer-dependent-decoherence-cgds/outline-v0-1.md`
- `papers/p4-soc-mzi-awareness-modulated-decoherence/README.md`
- `papers/p5-hubble-tension-memory-gradient/README.md`
- `papers/p5-soct-synthesis/README.md`
- `papers/p5-soct-synthesis/outline-v0-1.md`
- `papers/p6-black-holes-memory-compression-nodes/README.md`
- `papers/p7-unified-framework/README.md`
- `papers/pnt-dark-energy-hubble-window/toy-model-results-v0-1.md`
- `papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md`
- `papers/pnt-dark-energy-hubble-window/void-filament-hubble-subsection-v0-1.md`
- `papers/pnt-dark-energy-hubble-window/working-draft-v0-1.md`

### `simulations/`

- `simulations/README.md`
- `simulations/coherence/soc-scientific-field-report-v1.2.md`
- `simulations/cosmology/gravity-imprint-dm-analog-update-2026-01-30.md`
- `simulations/cosmology/pm-void-filament-hsplit-notes.md`
- `simulations/imported-assets/tables/monte-carlo-results-summary-50-seeds.csv`
- `simulations/memory-field-pm/README.md`
- `simulations/memory-field-pm/code/soct_pm_v061_final.py`
- `simulations/memory-field-pm/validation/v061_acceptance_summary.md`
- `simulations/memory-kernel/effective-g-memory-model.md`
- `simulations/mzi-visibility-decay/model-summary.md`
- `simulations/parent-child-transfer/README.md`
- `simulations/parent-child-transfer/kernel-robustness-summary.md`
- `simulations/parent-child-transfer/null-models.md`
- `simulations/parent-child-transfer/parameter-log.md`
- `simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md`
- `simulations/pnt_hubble_void/README.md`
- `simulations/pnt_hubble_void/pnt_hubble_void.jsx`
- `simulations/qrrg/qrrg-internal-simulation-report-summary-v1-1.md`
- `simulations/qrrg/qrrg-robustness-declaration-summary-v1-0.md`
- `simulations/qrrg/qrrg-robustness-declaration-v1-0.md`
- `simulations/qrrg/qrrg-spec-summary-v1-1.md`
- `simulations/recursive-universe/README.md`
- `simulations/recursive-universe/exploratory-analysis-v0-1.md`
- `simulations/recursive-universe/figure-provenance.md`
- `simulations/recursive-universe/testable-framework-v2-summary.md`
- `simulations/sparc/README.md`
- `simulations/sparc/notes.md`

### `experiments/`

- `experiments/README.md`
- `experiments/cosmology/pantheon-environment-h0-test.md`
- `experiments/cosmology/sparc-analysis-plan.md`
- `experiments/cosmology/sparc-memory-field-preregistration-v0-1.md`
- `experiments/osf/OSF_PREREGISTRATION_SOCT.md`
- `experiments/osf/README.md`
- `experiments/osf/V061_ACCEPTANCE_CERTIFICATE.md`
- `experiments/osf/osf-project-links.md`
- `experiments/osf/preregistration-package-index.md`
- `experiments/pantheon-h0-environment/README.md`
- `experiments/quantum/SOC-CGDS-01_Consciousness_Gated_Double_Slit.md`
- `experiments/quantum/mach-zehnder-consciousness-test.md`

### `references/`

- `references/bibliography-and-validation-notes.md`
- `references/consensus-pnt-soct-literature-positioning.md`
- `references/supplementary-figure-pack-index-v1-2.md`

### `visualizations/`

- `visualizations/pnt_hubble_void.jsx`

### Other scanned top-level artifacts outside the requested inventory groups

- Root docs/files: `README.md`, `STATUS.md`, `PREDICTIONS.md`, `SOC_Unified_Physics_Framework(2).docx`, `repo_bundle_sparc_pnt_void.zip`, `sparc_wise_inner_outer_fdm_split.csv`.
- Other folders found: `imports/`, `osf/`, and `exploratory/`.

## Recent research artifact presence check

| Artifact requested | Status | Existing file evidence | Notes |
|---|---|---|---|
| SPARC age-f_DM dataset and analysis | **PRELIMINARY** | `data/sparc/sparc_age_fdm_data.csv`; `observations/sparc/data/sparc_age_fdm_data.csv`; `observations/sparc/analysis-plan.md`; `observations/sparc/results/outer_mass_discrepancy_analysis.md`; `papers/cosmology/sparc/sparc-age-dm-paper-draft.md` | Derived CSV exists with 176 lines including header. Analysis notes exist, but no runnable notebook/script regenerating the reported statistics was found. |
| SPARC nonlinear memory fit: `f_DM = f0 + A(1-exp(-age/tau))` | **PRELIMINARY** | `notebooks/sparc_memory_fit_plan.md`; `data/sparc/derived-data-schema.md` | A plan/schema exists. No executed notebook, script, parameter-output table, or figure file for this fit was found. |
| Mass-bin SPARC plots | **MISSING** | `data/sparc/derived-data-schema.md` mentions mass-bin results; `figures/sparc/figure-provenance.md` exists | No actual plotted image/PDF/SVG files were found in `figures/sparc/`. |
| Effective-G memory model: `G_eff = G0(1 + alpha M)` | **SPECULATIVE** | `simulations/memory-kernel/effective-g-memory-model.md`; `docs/empirical-exploration-thread-summary-v0-1.md` | The model is documented as a framework/scaffold. This is not a validated empirical result in-repo. |
| Pantheon+ covariance-aware environment-H0 pipeline | **PRELIMINARY** | `notebooks/pantheon_environment_h0_fit_plan.md`; `experiments/cosmology/pantheon-environment-h0-test.md`; `experiments/pantheon-h0-environment/README.md` | Plans exist. No runnable covariance-aware pipeline script/notebook was found. |
| Pantheon+ covariance file | **MISSING** | `data/pantheon/covariance-notes.md` | Notes/schema only; no matrix file found. |
| Pantheon+ SN table | **MISSING** | `data/pantheon/README.md` | Notes/schema only; no SN table found. |
| Environment labels: void/filament/unclassified | **MISSING** | `data/pantheon/environment-labels-schema.md` | Schema exists, but no label table was found. |
| PNT working paper | **PRELIMINARY** | `papers/pnt-dark-energy-hubble-window/working-draft-v0-1.md`; `papers/cosmology/pnt/planck-nucleation-theory-master-note.md` | Working draft exists under the current folder, not under a separate `papers/pnt-working-paper/` folder. |
| SoCT comprehensive PNT/CIH report | **PRELIMINARY** | `docs/frameworks/sequence-of-collapse-unified-physics-framework.md`; `docs/theory-overview.md`; `papers/p5-soct-synthesis/outline-v0-1.md` | Broad synthesis material exists, but the intended `papers/soct-comprehensive-report/` folder/file is missing. |
| CIH parent-universe directional memory simulation notes | **SYNTHETIC** | `docs/simulations/parent-child-directional-transfer-research-record.md`; `simulations/parent-child-transfer/README.md`; `simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md`; `simulations/parent-child-transfer/kernel-robustness-summary.md` | Simulation notes and summaries exist. Treat as synthetic/toy-model material until scripts/notebooks and reproducibility logs are complete. |
| OSF preregistration PDFs and references | **PRELIMINARY** | `experiments/osf/preregistration-package-index.md`; `experiments/osf/osf-project-links.md`; `experiments/osf/OSF_PREREGISTRATION_SOCT.md`; `osf/OSF_PROJECT_MAP.md` | Markdown prereg/reference material exists. The index names PDFs as source/import targets, but those PDF files were not found in the scanned repo tree. |

## Intended structure comparison

### Intended `papers/` structure

| Intended path | Current status | Closest existing path(s) |
|---|---|---|
| `papers/sparc-gravitational-memory/` | **MISSING** | `papers/p1-age-dependent-rotation-curves-sparc/`; `papers/p1-memory-field-gravity-sparc/`; `papers/cosmology/sparc/` |
| `papers/pnt-dark-energy-hubble-window/` | **ESTABLISHED** | Present with working draft, mechanism note, subsection, and toy-model note. |
| `papers/cih-parent-universe-directional-memory/` | **MISSING** | `papers/p3-causal-inversion-directional-memory/`; `papers/cosmology/cih/`; `simulations/parent-child-transfer/`; `docs/simulations/parent-child-directional-transfer-research-record.md` |
| `papers/soc-mzi-observer-decoherence/` | **MISSING** | `papers/p4-soc-mzi-awareness-modulated-decoherence/`; `papers/p4-observer-dependent-decoherence-cgds/`; `experiments/quantum/` |
| `papers/gravity-as-accumulated-collapse-history/` | **MISSING** | `docs/theory/gravity-as-accumulated-collapse-history.md` |
| `papers/soct-comprehensive-report/` | **MISSING** | `docs/frameworks/sequence-of-collapse-unified-physics-framework.md`; `docs/theory-overview.md`; `papers/p5-soct-synthesis/` |

### Intended observations/data/notebook structure

| Intended path | Current status | Notes |
|---|---|---|
| `observations/sparc/` | **ESTABLISHED** | Present with data, requirements, preregistration, plan, and result notes. |
| `observations/pantheon-environment-h0/` | **MISSING** | A related folder exists at `experiments/pantheon-h0-environment/`, but not under `observations/`. |
| `data/sparc/` | **ESTABLISHED** | Present with README, schema, and `sparc_age_fdm_data.csv`. |
| `data/pantheon/` | **PRELIMINARY** | Present with README, covariance notes, and environment-label schema only. |
| `notebooks/sparc/` | **MISSING** | SPARC notebook plans exist as Markdown files directly under `notebooks/`; no subfolder or runnable notebook found. |
| `notebooks/pantheon/` | **MISSING** | Pantheon plan exists as Markdown directly under `notebooks/`; no subfolder or runnable notebook found. |

## Missing critical reproducibility files

| Critical item | Status | Recommendation |
|---|---|---|
| `sparc_age_fdm_data.csv` | **ESTABLISHED** | Present in both `data/sparc/` and `observations/sparc/data/`. Decide which location is canonical and keep the other as a mirrored/cited copy or remove duplication in a later cleanup PR. |
| Pantheon+ SN table | **MISSING** | Add a documented local path only if license permits; otherwise add download instructions, checksum, and schema. |
| Pantheon covariance matrix | **MISSING** | Do not invent. Add official download instructions/checksum first; commit file only if redistribution is allowed and size is acceptable. |
| SN environment-label table | **MISSING** | Create a derived table with columns documented in `data/pantheon/environment-labels-schema.md`, including provenance, label method, and unclassified/null cases. |
| Scripts/notebooks that generated SPARC plots/results | **MISSING** | Add runnable scripts or notebooks under `notebooks/sparc/` or `observations/sparc/scripts/` that regenerate CSV summaries and figures from committed/externally documented inputs. |
| Scripts/notebooks that generated Pantheon+ environment-H0 results | **MISSING** | Add covariance-aware pipeline under `notebooks/pantheon/` or `observations/pantheon-environment-h0/`, using no diagonal-only shortcut unless explicitly marked exploratory. |
| Mass-bin SPARC plot image files | **MISSING** | Regenerate and commit figure files plus provenance only after code and source data path are documented. |

## What is already present

- **SPARC empirical scaffold:** derived SPARC age/f_DM table, WISE inner/outer split, analysis plans, current-status note, preregistration, requirements, and result summaries.
- **SPARC publication scaffolds:** paper drafts and paper-summary files under `papers/cosmology/sparc/` plus P1 roadmap folders.
- **PNT dark-energy/Hubble-window package:** working draft and void/filament H0 mechanism notes under `papers/pnt-dark-energy-hubble-window/`, plus visualization and toy-model assets.
- **Effective-G/memory-kernel theory:** model notes under `simulations/memory-kernel/` and related documentation under `docs/`.
- **CIH/parent-child synthetic notes:** directional-transfer research record and parent-child simulation summaries.
- **OSF-facing Markdown material:** preregistration package index, OSF links, and several Markdown preregistration/protocol files.
- **Broad SoCT theory framework:** theory overview, framework document, validation roadmap, publication roadmap, parameter ledger, and source-lineage materials.

## What is missing

- Actual Pantheon+ SN table and full covariance matrix.
- Actual void/filament/unclassified SN environment-label table.
- Runnable covariance-aware Pantheon+ environment-H0 notebook/script.
- Runnable SPARC notebook/script that regenerates the age/f_DM correlations, nonlinear memory fit, mass-bin statistics, and plot files.
- Mass-bin SPARC plot files under `figures/sparc/`.
- Intended paper folders for `sparc-gravitational-memory`, `cih-parent-universe-directional-memory`, `soc-mzi-observer-decoherence`, `gravity-as-accumulated-collapse-history`, and `soct-comprehensive-report`.
- OSF preregistration PDF files referenced by the OSF package index.
- Clear one-source-of-truth decision for duplicated SPARC derived CSVs.

## Files that should not be added publicly without license/provenance review

- Raw SPARC rotation-curve/source tables if upstream redistribution terms do not allow mirroring.
- Pantheon+ full SN table and covariance matrix unless the public license and file-size constraints are verified.
- Any third-party catalog crossmatches used for environment labels if their license prohibits redistribution.
- Proprietary, unpublished, or personally supplied age-estimate tables unless explicit permission is recorded.
- OSF PDFs or external preregistration snapshots if they include copyrighted third-party content, non-public metadata, signatures, or private collaborator information.
- Large binary archives such as bundled data zips unless each included file has provenance, license, and checksum documentation.

## What should be added next

1. **Canonicalize SPARC data location.** Choose `data/sparc/sparc_age_fdm_data.csv` as the canonical derived data file, or explicitly document why a duplicate copy lives under `observations/sparc/data/`.
2. **Add SPARC reproducibility code.** Create a script/notebook that reads the canonical SPARC CSV, recomputes age/f_DM correlations, mass-bin statistics, and nonlinear memory-fit parameters, and writes result tables/figures.
3. **Add SPARC figure outputs.** Commit generated mass-bin plots and nonlinear-fit plots only after the code can regenerate them.
4. **Create `observations/pantheon-environment-h0/`.** Move or link the Pantheon+ environment-H0 plan into an observations package with README, data policy, scripts/notebooks, and outputs.
5. **Add Pantheon+ data provenance.** Record official source URLs, version dates, checksums, and local filenames for the SN table and covariance matrix. Commit raw files only if allowed.
6. **Build SN environment-label table.** Create a derived label table with void/filament/unclassified values, method provenance, matching radius/crossmatch rules, and an unclassified/null policy.
7. **Implement covariance-aware Pantheon+ pipeline.** Require full-covariance likelihood or clearly label any diagonal-only work as exploratory.
8. **Create intended paper folders or map aliases.** Either add the intended folders with concise README files or update the intended-structure plan to the current P1/P3/P4/P5 naming scheme.
9. **Audit OSF artifacts.** Verify which OSF PDFs are public, redistributable, and current; then either commit allowed PDFs or keep external links/checksums only.

## Recommended PR plan in priority order

1. **PR 1 — Repository audit and structure map.** Add this audit report and link it from the README. No scientific claims changed.
2. **PR 2 — SPARC reproducibility foundation.** Canonicalize the SPARC CSV location, add a small validation script, and write checks that verify row count, required columns, and f_DM range.
3. **PR 3 — SPARC analysis regeneration.** Add runnable notebook/script for correlations, nonlinear memory fit, mass bins, and figure generation. Mark outputs **PRELIMINARY** until independently reviewed.
4. **PR 4 — SPARC figure package.** Add generated mass-bin and nonlinear-fit plots with `figures/sparc/figure-provenance.md` updated to include command, input file, date, and checksum.
5. **PR 5 — Pantheon+ data policy and observation package.** Add `observations/pantheon-environment-h0/`, source/provenance instructions, and placeholder schemas without committing restricted data.
6. **PR 6 — Pantheon+ covariance-aware pipeline.** Add reproducible full-covariance H0 environment code after legal data paths and environment labels are ready.
7. **PR 7 — Paper-folder alignment.** Create missing intended folders or formally map intended names to current roadmap names.
8. **PR 8 — OSF artifact verification.** Verify public status and licenses of OSF PDFs/references; commit only redistributable artifacts or add citation/download instructions.
9. **PR 9 — Comprehensive report assembly.** Create `papers/soct-comprehensive-report/` only after the empirical lanes have reproducible support and clear claim labels.

## Bottom-line claim boundaries

- **ESTABLISHED as repo artifacts:** many documents, schemas, notes, draft folders, a SPARC derived CSV, simulation notes, and OSF Markdown links exist locally.
- **PRELIMINARY as empirical work:** SPARC age/f_DM and PNT/Pantheon environment-H0 materials are not yet complete reproducibility packages.
- **SYNTHETIC:** parent-child/CIH directional-memory simulations and some PNT void/filament simulations are toy/simulation artifacts unless rerunnable code and logs are imported.
- **SPECULATIVE:** broader SoCT/PNT/CIH theory claims remain conceptual unless tied to validated analysis outputs.
- **MISSING:** Pantheon+ data/covariance/environment labels, runnable notebooks/scripts, several intended paper folders, and SPARC mass-bin figure outputs.
