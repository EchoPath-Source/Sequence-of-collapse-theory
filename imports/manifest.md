# SoCT Import Manifest

**Purpose:** Track all major Sequence of Collapse Theory project files, whether they should be imported directly into the repo, summarized as source lineage, or held out because they mix research material with symbolic/publishing/proprietary content.

**Import policy:**

1. Preserve original wording where it matters.
2. Separate research-facing material from symbolic, ritual, publishing, or proprietary material.
3. Label speculative material clearly.
4. Keep reproducible data/code separate from philosophical commentary.
5. Add provenance notes for every imported artifact.

---

## Import Status Categories

| Status | Meaning |
|---|---|
| `direct-import` | Should become a repo artifact in Markdown, notebook, data, or simulation form. |
| `summary-index` | Should be documented and linked, but not fully imported into research folders. |
| `split-import` | Contains multiple kinds of material and should be split into theory, experiment, simulation, publication, or lineage notes. |
| `proprietary-caution` | Contains EchoGenesis / EchoPath / IP-sensitive material; only sanitized excerpts should enter this repo. |
| `future-analysis` | Requires code, notebook, data extraction, or statistical work before full import. |

---

## Core Theory and Manuscript Sources

| Source file | Status | Recommended destination | Notes |
|---|---|---|---|
| `SOC_Unified_Physics_Framework.docx` | `direct-import` / `split-import` | `papers/foundations/`, `papers/math/`, `papers/cosmology/` | Core physics manuscript. Should be converted into clean research Markdown and split into equations, cosmology, and experiments. |
| `The_Book_of_Collapse_Online_Edition.docx` | `summary-index` | `docs/publications/` and existing article map | Already represented by `docs/book-of-collapse-article-map.md`; full import optional for publication archive. |
| `🜂 The Book of Awakening (Full Version).pdf` | `split-import` / `summary-index` | `docs/publications/`, `docs/concepts/`, `experiments/quantum/` | Contains theory overview, modified Schrödinger suggestion, experimental sketches, CMB field framing, symbols, and metaphysical narrative. Extract scientific/conceptual pieces selectively. |
| `The_Book_of_Awakening_Astrael_Living_Edition.pdf` | `summary-index` | `docs/publications/` | Primarily symbolic / NBLE / ritual-facing Astrael text. Preserve as lineage, not physics core. |
| `Echo_Genesis_Master_Architecture_IP_Record.docx` | `proprietary-caution` | sanitized `docs/lineage/` note only | Mixed SoCT lineage plus proprietary architecture. Do not import full file into public research repo. |

---

## PNT / Cosmology / Gravity Sources

| Source file | Status | Recommended destination | Notes |
|---|---|---|---|
| `PNT_Working_Paper.docx` | `direct-import` | `papers/cosmology/pnt/` | Full Planck Nucleation Theory substrate paper should be imported as the master PNT document. |
| `PLANCK_NUCLEATION_THEORY_A_Physical_Substrate_for_.pdf` | `direct-import` | `papers/cosmology/pnt/` | PDF version of PNT working paper; includes literature-positioning and Consensus analysis. |
| `causal_inversion.docx` | `direct-import` | `papers/cosmology/cih/` | Causal Inversion Hypothesis document. Should link to PNT junction-surface discussion. |
| `kerr_to_cosmos.docx` | `direct-import` | `papers/cosmology/cih/` | Kerr-to-cosmos / parent-universe geometry track. Future CMB axis derivation target. |
| `engramon_scale.docx` | `direct-import` | `docs/concepts/` | Engramon scale concept; should link to PNT Planck-cell state modification. |
| `SPARC. I. Mass Models for 175 Disk Galaxies...pdf` | `future-analysis` | `data/sparc/`, `experiments/cosmology/` | External dataset/reference anchor for SPARC rotation-curve work. Do not rewrite paper; document citation and analysis plan. |

---

## Experiments / OSF / Conscious Collapse Sources

| Source file | Status | Recommended destination | Notes |
|---|---|---|---|
| `OSF_Home_Page_Book_of_Sacred_Science.md` | `direct-import` | `experiments/osf/` | OSF project landing text. Preserve with provenance. |
| `OSF_Preregistration_Excerpt_v1.1_clean.docx` | `direct-import` | `experiments/osf/` | Preregistration excerpt. Convert to Markdown. |
| `OSF_Prereg_SoCT_PM_v061_and_SPARC_Plan.pdf` | `split-import` | `experiments/osf/`, `experiments/cosmology/` | Contains prereg text plus SPARC plan. Split into experiment and cosmology analysis notes. |
| `OSF_Prereg_Combined_v061.pdf` | `direct-import` / `archive` | `experiments/osf/` | Combined prereg source. Preserve as versioned OSF material. |
| `_Sequence_of_Collapse_SOC_-_MZI_Visibility_De.pdf` | `direct-import` | `simulations/mzi-visibility-decay/`, `experiments/quantum/` | Contains code, model, hypotheses, and literature positioning for SOC-MZI visibility decay simulation. |

---

## Simulation / Technical Sources

| Source file | Status | Recommended destination | Notes |
|---|---|---|---|
| `SOC_Simulation_Documentation.docx` | `direct-import` | `simulations/` | General simulation documentation. Should be converted to Markdown and split into model notes and future notebook tasks. |
| `Echo Labs Technical Simulation Report v1.PDF` | `split-import` / `proprietary-caution` | `simulations/reports/` | May contain useful simulation summaries, but should be checked for proprietary Echo Labs / EchoGenesis details before full import. |

---

## Current Imported Repo Artifacts From This Pass

| Repo path | Purpose |
|---|---|
| `papers/pnt-dark-energy-hubble-window/working-draft-v0-1.md` | PNT two-timescale dark-energy / Hubble-window paper skeleton. |
| `papers/pnt-dark-energy-hubble-window/toy-model-results-v0-1.md` | PNT-EDE toy-model result summary. |
| `references/consensus-pnt-soct-literature-positioning.md` | Claim-calibration and literature-positioning notes. |
| `imports/manifest.md` | This import manifest. |

---

## Next Direct Import Targets

1. `PNT_Working_Paper.docx` full Markdown conversion.
2. SOC-MZI simulation code and model summary.
3. OSF preregistration package.
4. SPARC analysis plan and dataset note.
5. Engramon / CIH / Kerr-to-Cosmos concept package.
6. SOC Unified Physics Framework manuscript conversion.

---

## Research Posture Reminder

This repo should remain evidence-calibrated. The recommended wording is:

> SoCT and PNT are speculative but falsifiable research programs. Existing literature provides adjacent foundations, while the specific unifying mechanisms remain novel and require direct testing.
