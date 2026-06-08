# Root Upload Cleanup — 2026-06-08

**Status:** ESTABLISHED file-organization record; scientific claims remain PRELIMINARY/SPECULATIVE as labeled below.

This table was prepared before removing root-level uploads. Files were removed from root only after they were moved, extracted, documented as external, or identified as byte-identical duplicates.

| Original root path | Detected type | Destination path | Action taken | Reason |
|---|---|---|---|---|
| `Pantheon_SH0ES_cov.txt.gz` | gzip text full covariance candidate | documented in `data/pantheon/README.md`; not committed as data | Removed from root after validation and documentation | Full public-data covariance; redistribution not verified, so classified EXTERNAL/DOCUMENTED. |
| `Pantheon_cov_subset.txt` | covariance subset | `data/pantheon/Pantheon_cov_subset.txt` | No action | File was not present in repo root during inspection. |
| `environment_H0_analysis-1.png` | generated Pantheon/PNT environment-H0 figure | `figures/pantheon/environment_H0_analysis.png` | Moved | Keeps figure out of root; filename canonicalized. |
| `environment_H0_analysis-2.png` | generated figure duplicate | `figures/pantheon/environment_H0_analysis.png` | Removed duplicate | Byte-identical to `environment_H0_analysis-1.png`. |
| `paper_grade_analysis.png` | generated SPARC/report figure | `papers/sparc-age-dm/paper_grade_analysis.png` | Moved | Publication/report artifact for SPARC age-DM track. |
| `paper_grade_analysis-1.png` | generated figure duplicate | `papers/sparc-age-dm/paper_grade_analysis.png` | Removed duplicate | Byte-identical to `paper_grade_analysis.png`. |
| `sparc_age_fdm_main_result-2.png` | generated SPARC figure | `figures/sparc/sparc_age_fdm_main_result.png` | Moved | Canonical SPARC figure location. |
| `sparc_age_fdm_mass_bins-2.png` | generated SPARC figure | `figures/sparc/sparc_age_fdm_mass_bins.png` | Moved | Canonical SPARC figure location. |
| `sparc_fdm_vs_age_full_analysis-1.png` | generated SPARC figure | `figures/sparc/sparc_fdm_vs_age_full_analysis.png` | Moved | Canonical SPARC figure location. |
| `sparc_fdm_vs_age_full_analysis-2.png` | generated figure duplicate | `figures/sparc/sparc_fdm_vs_age_full_analysis.png` | Removed duplicate | Byte-identical to `sparc_fdm_vs_age_full_analysis-1.png`. |
| `sparc_mass_controlled_analysis-1.png` | generated SPARC figure | `figures/sparc/sparc_mass_controlled_analysis.png` | Moved | Canonical SPARC figure location. |
| `sparc_mass_controlled_analysis-2.png` | generated figure duplicate | `figures/sparc/sparc_mass_controlled_analysis.png` | Removed duplicate | Byte-identical to `sparc_mass_controlled_analysis-1.png`. |
| `sparc_mass_controlled_analysis-3.png` | generated figure duplicate | `figures/sparc/sparc_mass_controlled_analysis.png` | Removed duplicate | Byte-identical to `sparc_mass_controlled_analysis-1.png`. |
| `sparc_wise_inner_outer_fdm_split.csv` | SPARC derived data table | `data/sparc/sparc_wise_inner_outer_fdm_split.csv` and `observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv` | Imported then removed from root | Same table was also inside `repo_bundle_sparc_pnt_void.zip`; canonical data locations now contain it. |
| `repo_bundle_sparc_pnt_void.zip` | ZIP bundle of SPARC/PNT artifacts | extracted to documented canonical paths; README copied to `docs/imported-thread-artifacts/repo_bundle_sparc_pnt_void_README.md` | Extracted then removed from root | Bundle contents were imported; root ZIP was redundant. |
| `SOC_Unified_Physics_Framework(2).docx` | broad internal SoCT theory/report DOCX | `papers/soct-comprehensive-report/SOC_Unified_Physics_Framework_2.docx` | Moved | Broad SPECULATIVE theory/report artifact should not remain in repo root. |

## Pantheon covariance validation

`Pantheon_SH0ES_cov.txt.gz` validation result before root cleanup:

| Check | Result |
|---|---|
| Compressed file size | `10,334,474` bytes |
| gzip text readable | yes |
| first value | `1701` |
| values after first | `2,893,401` |
| consistency check | `2,893,401 = 1701 * 1701` |
| handling decision | EXTERNAL/DOCUMENTED; not committed as canonical data |

## Remaining missing files

- `data/pantheon/pantheon_plus.csv` — MISSING.
- `data/pantheon/environment_labels.csv` — MISSING.
- `data/pantheon/Pantheon_cov_subset.txt` — MISSING unless generated/imported later.
- `data/pantheon/Pantheon_SH0ES_cov.txt.gz` — EXTERNAL/DOCUMENTED, intentionally not committed in this cleanup pass.
