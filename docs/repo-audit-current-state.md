# Repository Audit: Current SoCT Empirical/Theory State

**Audit date:** 2026-06-08  
**Scope:** current repository state after the root-upload cleanup/import pass.  
**Purpose:** distinguish files now present in canonical repo locations from files that remain missing, external, preliminary, synthetic, or speculative.

This audit does **not** create or strengthen scientific claims. In particular, it does **not** claim a Pantheon H0 detection.

## Status-label definitions

- **PRESENT**: the repository contains the file/folder now.
- **PARTIAL**: some supporting material exists, but a complete reproducible package or manuscript source is not present.
- **MISSING**: the artifact is known from the roadmap/audit, but no committed file has been found.
- **EXTERNAL/DOCUMENTED**: the artifact was inspected or is required, but is intentionally not committed because provenance, license, size, or redistribution status requires external handling.
- **ESTABLISHED**: a concrete local artifact exists; this does **not** mean the scientific claim is externally established.
- **PRELIMINARY**: a draft, plan, result note, schema, figure, or derived dataset exists, but not a full reproducible analysis package.
- **SYNTHETIC**: toy-model, simulation, generated, or non-observational artifact.
- **SPECULATIVE**: conceptual/theory material without a complete empirical validation path in-repo.

## 2026-06-08 cleanup summary

Root-level uploads were inspected, moved into canonical folders, extracted from the uploaded ZIP bundle, documented as external, or removed only after duplication/move confirmation. The detailed deletion/import table is preserved in `docs/root-upload-cleanup-2026-06-08.md`.

| Cleanup item | Status | Label | Notes |
|---|---|---|---|
| Root upload cleanup | completed | ESTABLISHED | Root now contains only intentional top-level files/config plus `.git` metadata. |
| SPARC derived data import | PRESENT | PRELIMINARY | `data/sparc/sparc_age_fdm_data.csv` and `data/sparc/sparc_wise_inner_outer_fdm_split.csv` are present. |
| SPARC runnable analysis script | PRESENT | PRELIMINARY | `notebooks/sparc/sparc_age_dm_analysis.py` compiles. |
| SPARC figures/results | PRESENT | PRELIMINARY | Generated figures are under `figures/sparc/`; derived result tables/notes are under `observations/sparc/results/`. |
| Pantheon covariance subset | MISSING | MISSING | `Pantheon_cov_subset.txt` was not present in root during cleanup, so `data/pantheon/Pantheon_cov_subset.txt` was not created. |
| Full Pantheon covariance | EXTERNAL/DOCUMENTED | EXTERNAL/DOCUMENTED | Root `Pantheon_SH0ES_cov.txt.gz` was readable and internally consistent with N=1701, but not committed because redistribution terms were not verified. |
| Pantheon SN table | MISSING | MISSING | `data/pantheon/pantheon_plus.csv` is required before running the fit. |
| Environment labels | MISSING | MISSING | `data/pantheon/environment_labels.csv` is required before running the fit. |
| Pantheon notebook scaffold | PRESENT | PRELIMINARY | Notebook searches the canonical covariance paths and supports gzip covariance text. |
| SOC unified physics DOCX | PRESENT | SPECULATIVE | Moved to `papers/soct-comprehensive-report/` as an internal broad-theory source artifact. |

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
| `docs/root-upload-cleanup-2026-06-08.md` | PRESENT | File-by-file root cleanup, move, duplicate-removal, and external-data handling record. |

### Canonical paper folders

| Paper | Canonical folder | Status | Label |
|---|---|---|---|
| P1 | `papers/p1-age-dependent-rotation-curves-sparc/` | PRESENT scaffold/support | PRELIMINARY |
| P2 | `papers/p2-high-redshift-time-dependent-gravity/` | PRESENT scaffold; source text still partial | PRELIMINARY |
| P3 | `papers/p3-soc-concept-to-equation/` | PRESENT scaffold; source text still partial | SPECULATIVE |
| P4 | `papers/p4-soc-mzi-awareness-modulated-decoherence/` | PRESENT scaffold; prereg/simulation package still partial | PRELIMINARY |
| P5 | `papers/p5-hubble-tension-memory-gradient/` | PRESENT scaffold; PNT support artifact exists | SYNTHETIC / PRELIMINARY |
| P6 | `papers/p6-black-holes-memory-compression-nodes/` | PRESENT scaffold; source package still partial | SPECULATIVE |
| P7 | `papers/p7-unified-framework/` | PRESENT scaffold; broad report import is separate | SPECULATIVE |

### Support folders preserved from earlier scaffold

| Folder | Status | Current role |
|---|---|---|
| `papers/p1-memory-field-gravity-sparc/` | PRESENT | Supports canonical P1. |
| `papers/pnt-dark-energy-hubble-window/` | PRESENT | Supports canonical P5; contains the imported void-filament H0 mechanism toy-model note. |
| `papers/p3-causal-inversion-directional-memory/` | PRESENT | Supports canonical P6; older provisional P3 label. |
| `papers/p4-observer-dependent-decoherence-cgds/` | PRESENT | Supports canonical P4. |
| `papers/p5-soct-synthesis/` | PRESENT | Superseded by canonical P7; preserved as earlier synthesis scaffold. |
| `papers/soct-comprehensive-report/` | PRESENT | Holds broad imported SoCT framework/report binary; SPECULATIVE until converted and claim-bounded. |
| `papers/math/` | PRESENT | Supports canonical P3 and P7. |

## Recent-artifact presence table

### P1 — SPARC age / fDM and gravity-memory

| Artifact | Status | Repo location | Label | Notes |
|---|---|---|---|---|
| SPARC derived dataset | PRESENT | `data/sparc/sparc_age_fdm_data.csv` | PRELIMINARY | Canonical age/fDM derived table exists. |
| SPARC WISE inner/outer derived dataset | PRESENT | `data/sparc/sparc_wise_inner_outer_fdm_split.csv`; mirrored in `observations/sparc/data/` | PRELIMINARY | Imported from root/ZIP upload. |
| SPARC runnable analysis script | PRESENT | `notebooks/sparc/sparc_age_dm_analysis.py` | PRELIMINARY | Compiles under `py_compile`. |
| SPARC figures | PRESENT | `figures/sparc/` | PRELIMINARY | Root PNG uploads moved here with duplicate copies removed. |
| SPARC radial decomposition results | PRESENT | `observations/sparc/results/` | PRELIMINARY | ZIP result tables/notes imported; these are derived artifacts, not independent validation. |
| SPARC publication/report figure | PRESENT | `papers/sparc-age-dm/paper_grade_analysis.png` | PRELIMINARY | Moved from root as manuscript/report artifact. |

### P5 / Pantheon / environment-dependent H0

| Artifact | Status | Repo location | Label | Notes |
|---|---|---|---|---|
| Pantheon notebook scaffold | PRESENT | `notebooks/pantheon/pantheon_environment_h0_test.ipynb` | PRELIMINARY | Refuses to run full result unless SN table, environment labels, and covariance exist. |
| Pantheon covariance subset | MISSING | `data/pantheon/Pantheon_cov_subset.txt` | MISSING | Requested file was not present in root during cleanup. |
| Full Pantheon covariance | EXTERNAL/DOCUMENTED | documented in `data/pantheon/README.md` | EXTERNAL/DOCUMENTED | Validated gzip: N=1701 and N*N entries; not committed pending redistribution/LFS decision. |
| Pantheon SN table | MISSING | `data/pantheon/pantheon_plus.csv` | MISSING | Required before any fit. |
| Environment labels | MISSING | `data/pantheon/environment_labels.csv` | MISSING | Required before any fit. |
| Environment-H0 figure upload | PRESENT | `figures/pantheon/environment_H0_analysis.png` | PRELIMINARY | Imported figure only; not evidence of a Pantheon H0 detection. |
| PNT void-filament H0 mechanism note | PRESENT | `papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md` | SYNTHETIC / PRELIMINARY | Toy-model mechanism artifact imported from ZIP; not a full cosmological fit. |
| PNT visualization | PRESENT | `visualizations/pnt_hubble_void.jsx` | SYNTHETIC | Visualization artifact imported from ZIP. |

### P6/P7 — broad theory and comprehensive reports

| Artifact | Status | Repo location | Label | Notes |
|---|---|---|---|---|
| `SOC_Unified_Physics_Framework(2).docx` | PRESENT | `papers/soct-comprehensive-report/SOC_Unified_Physics_Framework_2.docx` | SPECULATIVE | Moved out of root; binary preserved as internal broad-theory source artifact. |
| Converted Markdown comprehensive report | MISSING | `papers/soct-comprehensive-report/` or `papers/p7-unified-framework/` | MISSING | Conversion and claim-boundary review still needed. |
| P6 open issues | MISSING | `papers/p6-black-holes-memory-compression-nodes/open-issues.md` | MISSING | Needed to track unresolved model issues. |

## Public-data and copyright cautions

- Do not commit copyrighted full paper PDFs unless license permits redistribution.
- For public datasets such as SPARC or Pantheon+, prefer scripts, schemas, derived tables, and source links over redistributing raw datasets unless the dataset license permits it.
- The full Pantheon covariance upload is documented as **EXTERNAL/DOCUMENTED** and ignored by default until redistribution and storage policy are resolved.
- For uploaded DOCX/PDF manuscripts authored by Antoine/Echo Labs, convert to Markdown source and preserve original binaries only if repo policy permits binary manuscript assets.
- For figures/screenshots generated internally, commit PNGs only if they are original generated outputs.

## Claim-boundary rules

1. A result is **reproducible** only when source data, code, and output table/figure are in the repo or linked to stable external storage.
2. A result is **publication-ready** only when it has methods, data provenance, reproducible outputs, caveats, and references.
3. Avoid stating that SoCT is confirmed. Use language such as `consistent with`, `initial signal`, `toy-model result`, `requires independent validation`, or `pending reproducible import`.
4. Distinguish real-data analysis, toy simulation, theoretical derivation, source-corpus narrative, and speculative interpretation.
5. No Pantheon environment-H0 result is established until `data/pantheon/pantheon_plus.csv`, `data/pantheon/environment_labels.csv`, and a usable covariance file are present and the notebook is run.

## Current bottom line

The root upload cleanup is complete. SPARC derived data, figures, result notes, and runnable script support are present in canonical locations. The Pantheon track remains a safe scaffold: the covariance upload was validated but documented externally, while the required Pantheon SN table and environment labels are still missing.
