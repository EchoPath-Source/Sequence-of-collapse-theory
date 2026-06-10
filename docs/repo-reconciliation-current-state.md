# Repository Reconciliation: Current State

**Reconciliation date:** 2026-06-10  
**Repository:** `EchoPath-Source/Sequence-of-collapse-theory`  
**Scope:** recursive structure, overlap, duplicate paths, import status, and missing artifacts after the latest Markdown, root-cleanup, and manual import passes.

This reconciliation is a repository-structure document. It does **not** expand SoCT/PNT claims, does **not** claim confirmation, and treats empirical outputs as source material, candidate results, reproducibility artifacts, preregistrations, simulations, or speculative/theory notes as labeled below.

## Inputs compared

This pass compared the actual file tree against these status and audit files:

- `docs/repo-audit-current-state.md`
- `docs/import-pass-2026-06-08-markdown.md`
- `docs/distribution-readiness-audit.md`
- `STATUS.md`
- `PREDICTIONS.md`
- `README.md`

## Recursive inventory summary

The repo is no longer an empty scaffold. It contains roadmap documents, theory notes, paper hubs, SPARC candidate data/results, Pantheon+ scaffolding, PNT/P5 toy-model notes, quantum preregistration excerpts, simulations, references, and OSF mapping files.

Requested directory file-count summary from this pass:

| Directory | File count | Current role |
|---|---:|---|
| `docs` | 51 | Audits, maps, imported source notes, theory/context notes, intake records, and this reconciliation document. |
| `observations/sparc` | 16 | Canonical SPARC reproducibility workspace; contains source notes, duplicated derived data, candidate result notes, and run sheets. |
| `data` | 8 | Canonical repo-level data staging; SPARC derived CSVs and Pantheon+ provenance/schema notes. |
| `notebooks` | 6 | Notebook plans plus current SPARC script and Pantheon notebook scaffold. |
| `figures` | 7 | Figure outputs/provenance for SPARC and Pantheon candidate artifacts. |
| `papers` | 45 | Canonical P1-P7 hubs plus support/source folders and imported paper drafts. |
| `simulations` | 30 | Toy/simulation records and code for memory-field, parent-child, MZI, PNT, recursive-universe, and QRRg tracks. |
| `experiments` | 12 | Experimental/preregistration plans for SPARC, Pantheon, OSF, and quantum tracks. |
| `references` | 3 | Bibliography and literature-positioning notes. |
| `visualizations` | 1 | Standalone visualization copy for the PNT Hubble void toy model. |
| `osf` | 6 | OSF project map and imported OSF/preregistration source summaries. |

## Canonical folder map

| Track / artifact class | Canonical path | Supporting or legacy paths | Status label | Recommendation |
|---|---|---|---|---|
| Repo state/audit | `docs/repo-reconciliation-current-state.md`, `docs/repo-audit-current-state.md`, `docs/distribution-readiness-audit.md`, `STATUS.md` | `docs/root-upload-cleanup-2026-06-08.md`, `docs/repo-cleanup-status-2026-06-09.md` | Source / governance | **Keep**; use this file as the newest reconciliation layer and avoid rewriting older audit history except for explicit errata. |
| P1 SPARC manuscript | `papers/p1-age-dependent-rotation-curves-sparc/` | `papers/p1-memory-field-gravity-sparc/`, `papers/cosmology/sparc/`, `papers/sparc-age-dm/` | Candidate result / manuscript source | **Keep canonical P1 path**; migrate future paper text and result manifests into canonical P1; deprecate old paper-only paths by cross-linking rather than deleting. |
| P1 SPARC reproducibility workspace | `observations/sparc/` | `data/sparc/`, `docs/observations/data/`, `figures/sparc/`, `notebooks/sparc/`, `simulations/sparc/` | Reproducibility artifact / candidate result | **Keep** `observations/sparc/` as the runnable package; keep `data/sparc/` as repo-level data mirror until provenance is fully settled; mark `docs/observations/data/` as imported source data requiring review. |
| P2 high-redshift / time-dependent gravity | `papers/p2-high-redshift-time-dependent-gravity/` | `docs/empirical-exploration-thread-summary-v0-1.md`, `simulations/cosmology/` | Theory / exploratory | **Keep**; needs manuscript source import before claiming readiness. |
| P3 concept-to-equation | `papers/p3-soc-concept-to-equation/`, `papers/math/` | `docs/theory/`, `docs/theory-notes/`, `papers/cosmology/cih/` | Speculative/theory | **Keep** canonical P3 and math scaffold; migrate reusable derivations from `docs/theory/` into paper-specific source files only with claim boundaries. |
| P4 SOC-MZI / observer decoherence | `papers/p4-soc-mzi-awareness-modulated-decoherence/` | `papers/p4-observer-dependent-decoherence-cgds/`, `experiments/quantum/`, `experiments/osf/`, `docs/experiments/` | Preregistration / speculative experiment | **Keep** canonical P4; keep CGDS and experiment folders as protocol support; needs protocol index tying duplicate names together. |
| P5 Hubble tension / PNT | `papers/p5-hubble-tension-memory-gradient/` | `papers/pnt-dark-energy-hubble-window/`, `papers/cosmology/pnt/`, `simulations/pnt_hubble_void/`, `visualizations/`, `figures/pantheon/`, `data/pantheon/` | Simulation / candidate result scaffold | **Keep** P5 as paper hub; keep PNT working folder as source package; prefer `simulations/pnt_hubble_void/` for executable/visual code and link `visualizations/` as duplicate/deploy copy. |
| P6 black holes / memory compression | `papers/p6-black-holes-memory-compression-nodes/` | `papers/p3-causal-inversion-directional-memory/`, `docs/theory/`, `docs/concepts/` | Speculative/theory | **Keep** P6 canonical; preserve older P3-labeled CIH folder as source/support for P6 until migration is complete. |
| P7 unified framework | `papers/p7-unified-framework/` | `papers/p5-soct-synthesis/`, `papers/soct-comprehensive-report/`, `docs/frameworks/` | Speculative/theory source | **Keep** P7 canonical; preserve broad imports as source artifacts with explicit speculative labels. |
| OSF / preregistration | `osf/`, `experiments/osf/` | `docs/experiments/`, paper-specific prereg folders | Preregistration / source | **Keep**; avoid duplicating full preregistration text without source/provenance notes. |

## Duplicate and overlap table

| Area | Duplicate / overlapping paths | Relationship observed | Recommendation |
|---|---|---|---|
| SPARC derived data | `data/sparc/sparc_age_fdm_data.csv` and `observations/sparc/data/sparc_age_fdm_data.csv` | Byte-identical duplicate. | **Keep** for now; canonical runnable copy should be `observations/sparc/data/`; `data/sparc/` can remain a repo-level mirror until data provenance is finalized. |
| SPARC inner/outer split data | `data/sparc/sparc_wise_inner_outer_fdm_split.csv` and `observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv` | Byte-identical duplicate. | **Keep** for now; same mirror rule as above. |
| Imported SPARC source data | `docs/observations/data/sparc_wise_fdm_with_Q_and_radii.csv` | Related but not byte-identical to the derived SPARC copies. | **Needs review**; treat as imported source/candidate data until columns/provenance are mapped into the canonical SPARC package. |
| SPARC P1 result CSVs | `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv`, `SPARC_age_fdm_partial_correlations.csv`, `SPARC_age_fdm_binned_bootstrap.csv`, plus `bootstrap_results.csv` and duplicate `bootstrap_results_import_test.csv` | Current paper-local candidate result artifacts; two bootstrap CSVs are byte-identical. | **Keep** paper-local result CSVs; **deprecate** `bootstrap_results_import_test.csv` after confirming no external reference depends on that filename. |
| SPARC figures | `figures/sparc/sparc_fdm_vs_age_full_analysis.png`, `figures/sparc/sparc_mass_controlled_analysis.png`, `figures/sparc/sparc_age_fdm_main_result.png`, `figures/sparc/sparc_age_fdm_mass_bins.png`, `papers/sparc-age-dm/paper_grade_analysis.png` | Figure outputs split between canonical figure folder and older paper folder. | **Migrate/index** future figure references through `figures/sparc/figure-provenance.md`; preserve `papers/sparc-age-dm/` as an older publication-summary package until references are updated. |
| SPARC code name mismatch | Present: `notebooks/sparc/sparc_age_dm_analysis.py`; missing expected name: `sparc_age_fdm_analysis.py` | Analysis script exists under a different name than the earlier missing list. | **Needs review**; either add a wrapper/alias or update manifests to use the actual path after confirming equivalence. |
| PNT/P5 working material | `papers/pnt-dark-energy-hubble-window/`, `papers/p5-hubble-tension-memory-gradient/`, `papers/cosmology/pnt/`, `simulations/pnt_hubble_void/`, `visualizations/pnt_hubble_void.jsx` | Paper hub, source/support package, master note, simulation folder, and duplicate visualization copy. | **Keep** all; canonical paper hub is P5, source/support is `papers/pnt-dark-energy-hubble-window/`, executable visualization belongs in `simulations/pnt_hubble_void/`; `visualizations/` should be treated as a deploy/copy location. |
| P3/P6 CIH/Kerr/Engramon | `docs/theory/causal-inversion-hypothesis.md`, `docs/theory/from-kerr-to-cosmos-axis-of-evil-prediction.md`, `docs/theory/engramon-scale-notes.md`, `papers/p6-black-holes-memory-compression-nodes/source/`, `papers/p3-causal-inversion-directional-memory/`, `papers/cosmology/cih/` | Theory source duplicated between docs and P6 source imports; older P3 label overlaps P6. | **Keep** P6 source imports as paper-local source; preserve `docs/theory/` as concept library; mark older P3 CIH folder as support/legacy until migrated. |
| P4/CGDS/SOC-MZI | `experiments/quantum/`, `papers/p4-observer-dependent-decoherence-cgds/`, `papers/p4-soc-mzi-awareness-modulated-decoherence/`, `docs/experiments/`, `experiments/osf/` | Protocol/preregistration material split by experiment type, paper hub, and OSF import location. | **Keep** canonical P4 paper folder; add a future protocol index linking CGDS, MZI, OSF, and docs excerpts; no deletion recommended. |
| Pantheon+ scaffolding | Root `Pantheon_cov_subset-6.txt`, `data/pantheon/`, `experiments/pantheon-h0-environment/`, `experiments/cosmology/pantheon-environment-h0-test.md`, `notebooks/pantheon/`, `figures/pantheon/environment_H0_analysis.png` | A root covariance subset-like file exists, but full covariance, SN table, and environment-label table are still absent. | **Migrate/review** root `Pantheon_cov_subset-6.txt` into `data/pantheon/` only after provenance and naming are confirmed; keep full Pantheon+ inputs external/documented until redistribution rights and source URLs are recorded. |
| Broad framework imports | `docs/frameworks/sequence-of-collapse-unified-physics-framework.md`, `papers/soct-comprehensive-report/SOC_Unified_Physics_Framework_2.docx`, `papers/p7-unified-framework/` | Source framework material overlaps P7. | **Keep** as source/speculative material; avoid asserting empirical confirmation from these files. |

## Current artifact status table

| Artifact | Current path(s) | Label | Current status |
|---|---|---|---|
| Reconciliation document | `docs/repo-reconciliation-current-state.md` | Source / governance | Present; newest current-state map. |
| Repo audit | `docs/repo-audit-current-state.md` | Source / governance | Present, but predates latest P1 CSV and figure imports. |
| Import pass log | `docs/import-pass-2026-06-08-markdown.md` | Source / governance | Updated to include latest P1 CSV/README imports. |
| P1 SPARC data | `observations/sparc/data/`, `data/sparc/` | Reproducibility artifact / candidate result | Present in duplicate canonical/mirror locations; provenance still needs a complete run notebook. |
| P1 SPARC imported result CSVs | `papers/p1-age-dependent-rotation-curves-sparc/results/` | Candidate result | Present: correlations, partial correlations, binned bootstrap, bootstrap copies, and results README. |
| P1 SPARC script | `notebooks/sparc/sparc_age_dm_analysis.py` | Reproducibility artifact | Present under `age_dm` name; expected `age_fdm` filename remains absent. |
| P1 SPARC notebook | `observations/sparc/sparc_age_dark_matter_analysis.ipynb` | Reproducibility artifact | Missing. |
| P1 SPARC figures | `figures/sparc/`, `papers/sparc-age-dm/` | Candidate result | Several figures present; requested `SPARC_age_vs_fdm_scatter.png` remains missing. |
| PNT/P5 toy model notes | `papers/pnt-dark-energy-hubble-window/`, `papers/cosmology/pnt/` | Simulation / theory | Present as source notes and toy-model results; executable calculation scripts still incomplete. |
| PNT visualization | `simulations/pnt_hubble_void/pnt_hubble_void.jsx`, `visualizations/pnt_hubble_void.jsx` | Simulation / visualization | Present in duplicate/copy locations. |
| Pantheon+ environment-H0 scaffold | `data/pantheon/`, `experiments/cosmology/`, `experiments/pantheon-h0-environment/`, `notebooks/pantheon/`, `figures/pantheon/` | Candidate result scaffold | Scaffold and one figure present; full covariance, SN table, and labels absent/external. |
| P3/P6 CIH/Kerr/Engramon | `papers/p6-black-holes-memory-compression-nodes/source/`, `docs/theory/`, `papers/p3-causal-inversion-directional-memory/` | Speculative/theory | Present as source notes; needs paper-facing derivation/claim-boundary synthesis. |
| P4 SOC-MZI / CGDS | `papers/p4-soc-mzi-awareness-modulated-decoherence/`, `papers/p4-observer-dependent-decoherence-cgds/`, `experiments/quantum/` | Preregistration / speculative experiment | Preregistration excerpt and protocol notes present; full preregistration-grade package still incomplete. |
| SOC-MZI visibility decay simulation script | Expected `SOC MZI Visibility Decay Simulation.py` | Simulation | Missing by exact filename; `simulations/mzi-visibility-decay/model-summary.md` exists as a summary only. |
| OSF mapping | `osf/OSF_PROJECT_MAP.md`, `experiments/osf/` | Source / preregistration | Present. |
| Broad theory reports | `docs/frameworks/`, `papers/soct-comprehensive-report/`, `papers/p7-unified-framework/` | Speculative/theory source | Present; must remain separated from empirical claims. |

## Remaining missing-file checklist

From the earlier missing list and this reconciliation pass:

| Requested / expected item | Current status | Recommendation |
|---|---|---|
| `sparc_age_fdm_analysis.py` | **Missing by exact filename**; `notebooks/sparc/sparc_age_dm_analysis.py` exists. | Review equivalence; if equivalent, add an alias/wrapper or update manifests to canonical actual path. |
| `mass_proxy_comparison.csv` | **Missing**. | Import only with provenance and column documentation. |
| `paper_grade_analysis.png` | **Present** at `papers/sparc-age-dm/paper_grade_analysis.png`. | Link from `figures/sparc/figure-provenance.md` or migrate a canonical copy later. |
| `sparc_fdm_vs_age_full_analysis.png` | **Present** at `figures/sparc/sparc_fdm_vs_age_full_analysis.png`. | Keep under `figures/sparc/`. |
| `sparc_mass_controlled_analysis.png` | **Present** at `figures/sparc/sparc_mass_controlled_analysis.png`. | Keep under `figures/sparc/`. |
| `SPARC_age_fdm_regression_models.csv` | **Missing**. | Import with provenance or regenerate from a reproducible script. |
| `SPARC_age_vs_fdm_scatter.png` | **Missing**. | Regenerate from the final P1 notebook/script if needed. |
| `repo_bundle_sparc_pnt_void.zip` | **Missing as ZIP**; README imported at `docs/imported-thread-artifacts/repo_bundle_sparc_pnt_void_README.md`. | Do not commit ZIP unless needed; prefer extracted, documented contents. |
| `SOC MZI Visibility Decay Simulation.py` | **Missing by exact filename**. | Import or regenerate under `simulations/mzi-visibility-decay/` with README and assumptions. |
| `environment_H0_analysis.png` | **Present** at `figures/pantheon/environment_H0_analysis.png`. | Keep as candidate figure; document data/provenance before using in claims. |
| Pantheon+ covariance matrix | **Absent/external**; root `Pantheon_cov_subset-6.txt` exists but is not the full covariance. | Add source notes and checksum/provenance; avoid redistributing restricted full data unless permitted. |
| Pantheon+ SN table | **Missing**. | Add external source instructions or permitted local copy. |
| Pantheon+ environment-label table | **Missing**; schema exists at `data/pantheon/environment-labels-schema.md`. | Create or import labels with methodology and provenance. |

## Keep / migrate / deprecate / needs-review recommendations

### Keep

- Keep `observations/sparc/` as the canonical SPARC reproducibility package.
- Keep `papers/p1-age-dependent-rotation-curves-sparc/` as the canonical P1 manuscript/result hub.
- Keep `papers/p5-hubble-tension-memory-gradient/` as the canonical P5 paper hub, with `papers/pnt-dark-energy-hubble-window/` as support/source.
- Keep `papers/p4-soc-mzi-awareness-modulated-decoherence/` as canonical P4 and `papers/p4-observer-dependent-decoherence-cgds/` as support.
- Keep `papers/p6-black-holes-memory-compression-nodes/` as canonical P6 and preserve CIH/Kerr/Engramon source imports.
- Keep all theory/metaphysical material clearly labeled as speculative/theory or interpretive context.

### Migrate / index

- Add future SPARC result manifests to `observations/sparc/results/` and point paper-local result CSVs back to those manifests.
- Move or index any future SPARC figures through `figures/sparc/figure-provenance.md`.
- If `Pantheon_cov_subset-6.txt` is validated, move it to `data/pantheon/` with a provenance note and leave no active root data artifact.
- Prefer `simulations/pnt_hubble_void/` for executable/visualization source and treat `visualizations/` as a deployment or presentation copy.
- Add a future P4 protocol index that links paper, experiments, OSF, and docs excerpts.

### Deprecate later, not now

- `papers/p1-memory-field-gravity-sparc/` after its outline/source material is folded into canonical P1 or explicitly cross-linked.
- `papers/p5-soct-synthesis/` after P7 imports are complete.
- `bootstrap_results_import_test.csv` after confirming `bootstrap_results.csv` is the canonical identical copy.
- Older duplicate paper/figure folders only after inbound links are checked.

### Needs review

- Whether `notebooks/sparc/sparc_age_dm_analysis.py` is equivalent to the missing `sparc_age_fdm_analysis.py`.
- Provenance and intended destination of root `Pantheon_cov_subset-6.txt`.
- Column-level relationship between `docs/observations/data/sparc_wise_fdm_with_Q_and_radii.csv` and the canonical SPARC data files.
- Whether full Pantheon+ data can be redistributed or must remain external with instructions.
- Whether P4 simulation source exists under a different name or still needs import/regeneration.

## Next PR plan

1. Add lightweight index/deprecation notes in the highest-risk duplicate areas:
   - `observations/sparc/README.md` or a SPARC manifest that distinguishes canonical runnable files from mirrors.
   - `papers/p1-age-dependent-rotation-curves-sparc/results/README.md` to identify candidate result status and duplicated bootstrap file.
   - `simulations/pnt_hubble_void/README.md` to identify the canonical JSX source versus `visualizations/` copy.
2. Resolve exact-name SPARC script mismatch by either adding `sparc_age_fdm_analysis.py` as a wrapper or formally renaming references to `notebooks/sparc/sparc_age_dm_analysis.py`.
3. Move validated root Pantheon subset data to `data/pantheon/` with provenance, or document why it remains uncommitted/unmoved.
4. Add a SPARC notebook or script that regenerates current candidate tables and figures from committed inputs.
5. Add missing P1 controls/regression outputs only through a reproducible generation path.
6. Keep all output labels conservative: source, candidate result, reproducibility artifact, preregistration, simulation, or speculative/theory.
