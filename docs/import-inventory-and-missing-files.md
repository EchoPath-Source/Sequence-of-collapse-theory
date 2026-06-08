# Import Inventory and Missing Files

**Purpose:** track what can be added directly from available project material and what still needs to be provided for a full distribution-ready update.

---

## Available source documents in current working set

These files are available to be converted into repo material, summarized, or referenced in paper/protocol hubs.

### Core theory / manuscript sources

| File | Repo use | Suggested destination |
|---|---|---|
| `SOC_Unified_Physics_Framework.docx` | Core theory, memory field, Hamiltonian, open-problem framing | `papers/math/`, `docs/`, `papers/p5-soct-synthesis/` |
| `The_Book_of_Collapse_Online_Edition.docx` | Public-facing 12-article map and conceptual lineage | `docs/`, `papers/p5-soct-synthesis/` |
| `🜂 The Book of Awakening (Full Version).pdf` | Philosophical/contextual source; not empirical evidence | `docs/philosophical/` or referenced only |
| `The_Book_of_Awakening_Astrael_Living_Edition.pdf` | Astrael/NBLE living-edition context; metaphysical layer | `docs/philosophical/` only if included |
| `Echo_Genesis_Master_Architecture_IP_Record.docx` | Architecture lineage; proprietary/public boundary caution | `docs/source-corpus.md`, selective public excerpts |

### P1 / SPARC / gravity-memory sources

| File | Repo use | Suggested destination |
|---|---|---|
| `Gravity as Accumulated Collapse History.PDF` | P1 paper source | `papers/p1-memory-field-gravity-sparc/` |
| `SPARC. I. Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves_.pdf` | Dataset/reference source | `references/`, `data/sparc/source-notes.md` |
| `SOC_Simulation_Documentation.docx` | SoCT-PM simulation notes | `simulations/memory-kernel/`, `papers/p1-memory-field-gravity-sparc/` |
| `Echo Labs Technical Simulation Report v1.PDF` | simulation report, broader technical validation context | `simulations/`, `references/` |
| `Echo_Labs_Scientific_Field_Report_SOC_v1.2.pdf` | field report / synthesis context | `docs/`, `papers/p5-soct-synthesis/` |

### P2 / PNT dark energy sources

| File | Repo use | Suggested destination |
|---|---|---|
| `PNT_Working_Paper.docx` | P2 working paper content | `papers/pnt-dark-energy-hubble-window/` |
| `SoCT_Comprehensive_Report_PNT_Annotated.PDF` | PNT annotated synthesis | `papers/pnt-dark-energy-hubble-window/`, `papers/p5-soct-synthesis/` |
| `engramon_scale.docx` | Engramon/Planck-memory scale | `docs/planck-memory-substrate.md`, `papers/math/` |

### P3 / causal inversion / directional memory sources

| File | Repo use | Suggested destination |
|---|---|---|
| `causal_inversion.docx` | Causal Inversion Hypothesis source | `papers/p3-causal-inversion-directional-memory/` |
| `kerr_to_cosmos.docx` | Kerr-to-Cosmos source | `papers/p3-causal-inversion-directional-memory/` |
| `engramon_scale.docx` | substrate scale supporting P3/PNT | `papers/math/`, `papers/p3-causal-inversion-directional-memory/` |

### P4 / observer-dependent decoherence / OSF sources

| File | Repo use | Suggested destination |
|---|---|---|
| `OSF_Preregistration_Excerpt_v1.1_clean.docx` | P4 preregistration excerpt | `osf/`, `papers/p4-observer-dependent-decoherence-cgds/` |
| `OSF_Preregistration_Excerpt_v1.1_clean-1.docx` | duplicate/variant prereg excerpt | compare before import |
| `OSF_Prereg_SoCT_PM_v061_and_SPARC_Plan.pdf` | P1/SoCT-PM/SPARC prereg plan | `osf/`, `papers/p1-memory-field-gravity-sparc/` |
| `OSF_Prereg_Combined_v061.pdf` | combined prereg source | `osf/`, `experiments/` |
| `OSF_Home_Page_Book_of_Sacred_Science.md` | OSF landing page text | `osf/` |

---

## Can add directly now

The following can be added immediately as Markdown summaries or working outlines without needing more files:

1. Distribution-readiness audit.
2. Import inventory and missing-file list.
3. P1 SPARC paper outline.
4. SPARC reproducibility runsheet.
5. P3 CIH/Kerr-to-Cosmos paper outline.
6. P4 CGDS/SOC-MZI protocol outline.
7. Distribution checklist.
8. Conservative claim-language guide.
9. Source-corpus update pointing to newly available files.

---

## Needs extraction before direct import

The following available files need careful extraction/conversion before being committed as full Markdown papers:

1. `PNT_Working_Paper.docx`
2. `SOC_Simulation_Documentation.docx`
3. `causal_inversion.docx`
4. `kerr_to_cosmos.docx`
5. `engramon_scale.docx`
6. `Gravity as Accumulated Collapse History.PDF`
7. OSF preregistration PDFs/docx files

Reason:

- preserve formatting;
- avoid duplicate/contradictory versions;
- separate empirical claims from philosophical context;
- avoid importing private/proprietary material unnecessarily.

---

## Still needed from user for full distribution-ready implementation

### Critical

```text
observations/sparc/sparc_age_dark_matter_analysis.ipynb
observations/sparc/scripts/regenerate_inner_outer_summary.py
observations/sparc/results/bootstrap_results.csv
observations/sparc/results/summary.json
figures/SPARC_age_vs_fdm_full_sample.png
figures/inner_outer_radial_decomposition.png
```

### High priority

```text
notebooks/pantheon_environment_h0_fit.ipynb
data/pantheon/environment_labels.csv
data/pantheon/void_filament_catalog_cross_match.csv
simulations/pnt-dark-energy/pnt_ede_toy_model.py
notebooks/pnt_dark_energy_toy_model.ipynb
```

### Medium priority

```text
CMB directional-memory toy outputs
parent-child transfer parameter logs
multi-seed parent-child simulation outputs
null-model definitions for parent-child transfer
formal bibliography / BibTeX file
paper figures and diagrams
```

---

## Recommended user upload order

1. SPARC notebook or script used to generate the inner/outer decomposition.
2. Full SPARC derived CSVs and any bootstrap/control tables.
3. PNT toy-model code or notebook.
4. Pantheon+ environment-label output and any covariance notes.
5. Figures/charts/screenshots tied to validation.
6. Any latest manuscript drafts that supersede the uploaded docx/PDF versions.

---

## Import rule going forward

Every imported file should receive one of these labels:

- `empirical-data`
- `reproducible-code`
- `candidate-result`
- `working-paper`
- `protocol`
- `philosophical-context`
- `reference`
- `internal-architecture`

This prevents the repo from mixing evidence, theory, metaphysics, and product architecture without clear boundaries.
