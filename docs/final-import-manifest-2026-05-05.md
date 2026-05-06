# Final Import Manifest — 2026-05-05

This document records the current recommended structure for preserving Sequence of Collapse Theory materials inside the repository.

## Purpose
The goal of this manifest is to keep the repository organized by **evidence status** and **research function** so that:
- theory writing does not get confused with validated results
- exploratory simulations do not get promoted to publication claims by accident
- preregistration materials remain easy to find
- later paper drafting can reuse clean, labeled source files

---

# Evidence Taxonomy

Every future addition should be labeled with one of the following tags in the file header or README context.

## 1. `validated-simulation`
Use for simulation artifacts that passed internal validation checks and are safe to cite as the current working implementation.

Examples:
- v0.6.1 acceptance materials
- production-ready PM code snapshots
- simulation outputs tied to validated code versions

## 2. `real-data-analysis`
Use for observational analyses based on real external datasets with reproducible provenance.

Examples:
- controlled SPARC tables and scripts
- verified Pantheon+/void analyses
- real-data figure exports with data source notes

## 3. `exploratory-simulation`
Use for toy models, sandbox simulations, or speculative extensions that are useful for thinking but not yet publication-grade evidence.

Examples:
- recursive-universe sandbox
- parent/child-universe transfer toy models
- illustrative CMB-like transfer tests

## 4. `theory-draft`
Use for conceptual essays, article drafts, and manuscript skeletons.

Examples:
- Gravity as Accumulated Collapse History article draft
- theory-facing Substack or essay drafts
- structured paper outlines

## 5. `technical-summary`
Use for internal repo preservation notes summarizing larger artifacts.

Examples:
- Q-RRG spec summary notes
- simulation report summaries
- import batch notes

## 6. `reference-index`
Use for figure indices, candidate import lists, and bibliography-oriented notes.

Examples:
- supplementary figure pack index
- next-wave import candidate lists
- source corpus maps

---

# Recommended Repository Placement

## A. Core theory and paper-facing writing

### Folder
`papers/` and `docs/theory/`

### Recommended contents
- foundational SoCT papers
- article drafts explaining gravity as memory or collapse history
- clean manuscript versions separated from internal notes

### Current recommended file targets
- `docs/theory/gravity-as-accumulated-collapse-history.md`
- `papers/foundations/sequence-of-collapse-overview.md`

### Evidence labels
- `theory-draft`

---

## B. OSF and preregistration materials

### Folder
`experiments/osf/`

### Recommended contents
- preregistration markdown drafts
- upload-ready PDF copies
- correction addenda
- version log of submitted files

### Current recommended file targets
- `experiments/osf/OSF_PREREGISTRATION_SOCT.md`
- `experiments/osf/V061_ACCEPTANCE_CERTIFICATE.md`
- `experiments/osf/OSF_CORRECTION_ADDENDUM_V061.md`

### Evidence labels
- `validated-simulation` for acceptance / correction notes
- `theory-draft` for prereg drafts until externally frozen

---

## C. Memory-field PM simulation line

### Folder
`simulations/memory-field-pm/`

### Recommended subfolders
```text
simulations/memory-field-pm/
├─ README.md
├─ code/
├─ outputs/
├─ figures/
└─ validation/
```

### Recommended contents
- v0.6 archival code
- v0.6-corrected archival code
- v0.6.1 final code
- snapshot CSVs
- figure packs from the validated run
- validation notes and acceptance summary

### Current recommended file targets
- `simulations/memory-field-pm/code/soct_pm_v06_comoving.py`
- `simulations/memory-field-pm/code/soct_pm_v06_corrected.py`
- `simulations/memory-field-pm/code/soct_pm_v061_final.py`
- `simulations/memory-field-pm/outputs/soct_pm_v06_snapshots.csv`
- `simulations/memory-field-pm/figures/comoving-expansion_environment-H_dwarf-survival.png`
- `simulations/memory-field-pm/validation/v061_acceptance_summary.md`

### Evidence labels
- `validated-simulation` for v0.6.1 line
- older code snapshots kept as historical provenance

---

## D. SPARC observational track

### Folder
`observations/sparc/`

### Recommended subfolders
```text
observations/sparc/
├─ README.md
├─ analyses/
├─ scripts/
├─ figures/
└─ tables/
```

### Recommended contents
- the controlled age–DM analysis summary
- cleaned tables with galaxy names and proxies
- scripts used to produce results
- figure exports with provenance notes
- explicit null or inconclusive notes if controls weaken the signal

### Current recommended file targets
- `observations/sparc/analyses/soct_outer_dm_analysis.txt`
- `observations/sparc/analyses/age-dm-analysis-summary.md`
- `observations/sparc/scripts/README.md`
- `observations/sparc/tables/README.md`

### Evidence labels
- `real-data-analysis`
- never mix synthetic demos into this folder

---

## E. Exploratory recursive-universe / parent-child transfer work

### Folder
`exploratory/recursive-universe/`

### Recommended subfolders
```text
exploratory/recursive-universe/
├─ README.md
├─ code/
├─ figures/
└─ notes/
```

### Recommended contents
- recursive-universe analysis doc
- refined recursive-universe code
- 3D power spectra figures
- transfer-function figures
- child-CMB toy maps
- non-Gaussianity and falsifiability plots

### Current recommended file targets
- `exploratory/recursive-universe/notes/RECURSIVE_UNIVERSE_ANALYSIS.md`
- `exploratory/recursive-universe/code/recursive_universe_v2_testable.py`
- `exploratory/recursive-universe/figures/recursive_universe_summary.png`
- `exploratory/recursive-universe/figures/falsifiability_analysis.png`
- `exploratory/recursive-universe/figures/child_cmb_analysis.png`

### Evidence labels
- `exploratory-simulation`

### Critical rule
Nothing in this folder should be cited as established SoCT evidence unless independently upgraded by later work.

---

## F. Q-RRG / technical bridge layer

### Folder
`simulations/qrrg/`

### Recommended contents
- spec summaries
- internal simulation summaries
- robustness declaration summaries
- later notebooks or pseudocode that clarify implementation terms

### Current recommended file targets
- `simulations/qrrg/qrrg-spec-summary-v1-1.md`
- `simulations/qrrg/qrrg-internal-simulation-report-summary-v1-1.md`
- `simulations/qrrg/qrrg-robustness-declaration-summary-v1-0.md`

### Evidence labels
- `technical-summary`

---

## G. Figure and source indexing

### Folder
`references/` and `docs/`

### Recommended contents
- supplementary figure pack index
- source corpus maps
- import logs
- import candidate lists

### Current recommended file targets
- `references/supplementary-figure-pack-index-v1-2.md`
- `docs/import_log_2026-05-05.md`
- `docs/next_wave_import_candidates.md`
- `docs/import-batch-2026-04-07.md`

### Evidence labels
- `reference-index`
- `technical-summary`

---

# Current Active Reference Standard

As of this manifest, the **active validated simulation line** for the memory-field PM work should be treated as:

- **v0.6.1 final** = current reference implementation

The following are useful but should be treated as archived provenance:
- v0.6 initial
- v0.6-corrected

---

# Import Priorities From Here

## Priority 1
OSF-facing materials:
- prereg markdown
- upload-ready PDF
- correction addendum
- acceptance certificate

## Priority 2
Validated memory-field PM materials:
- v0.6.1 code
- CSV outputs
- figure pack
- validation note

## Priority 3
SPARC real-data materials:
- controlled summary
- real scripts
- tables and figures with provenance

## Priority 4
Exploratory recursive-universe materials:
- code
- notes
- figures
- hard warning labels

## Priority 5
Public-facing theory drafts:
- gravity-as-memory article draft
- cleaned foundational paper drafts

---

# One-Line Rule for Future Uploads

Before importing any new file, ask:

**Is this validated evidence, real-data analysis, exploratory simulation, theory draft, technical summary, or reference index?**

If that label is not clear, the file should not be imported into a publication-facing folder yet.
