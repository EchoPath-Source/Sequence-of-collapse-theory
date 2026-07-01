# Pantheon+ Data Notes

**Status:** PRELIMINARY scaffold / public source inputs documented; generated derived environment-label artifacts imported on 2026-06-30

This directory documents the Pantheon+ environment-dependent H0 test inputs. It does **not** contain a completed Pantheon H0 result.

## Required files for the notebook

The notebook `notebooks/pantheon/pantheon_environment_h0_test.ipynb` refuses to run the primary fit unless all of the following are available:

| Required artifact | Expected path | Status | Label | Notes |
|---|---|---|---|---|
| Pantheon+SH0ES supernova table | `data/pantheon/raw/Pantheon+SH0ES.dat` if committed locally | DOCUMENTED / EXTERNAL | PUBLIC SOURCE INPUT | Source file is `Pantheon+SH0ES.dat` from the PantheonPlusSH0ES/DataRelease `Pantheon+_Data/4_DISTANCES_AND_COVAR/` release. |
| Environment labels | `data/pantheon/environment_labels.csv` | PRESENT | DERIVED CROSS-MATCH ARTIFACT | Imported generated SDSS void + Tempel/Bisous filament cross-match labels for 1701 Pantheon+ rows. |
| Pantheon+SH0ES STAT+SYS covariance | `data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov` if committed locally | DOCUMENTED / EXTERNAL | PUBLIC SOURCE INPUT | Source file is `Pantheon+SH0ES_STAT+SYS.cov` from the same public release; commit raw covariance only after storage/redistribution policy is settled. |

Supported covariance candidate paths:

```text
data/pantheon/pantheon_covariance.txt
data/pantheon/Pantheon_cov_subset.txt
data/pantheon/Pantheon_SH0ES_cov.txt.gz
data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov
```

## Public Pantheon+SH0ES source inputs

The public PantheonPlusSH0ES/DataRelease directory `Pantheon+_Data/4_DISTANCES_AND_COVAR/` documents:

- `Pantheon+SH0ES.dat` as the nominal SN and Cepheid-host distance data vector;
- `Pantheon+SH0ES_STAT+SYS.cov` as the all-systematics covariance matrix;
- covariance format as a leading matrix size (`N=1701`) followed by `N x N` flattened covariance entries.

If raw source inputs are committed later, use:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov
```

and record byte sizes plus SHA-256 checksums in this README.

## Environment labels from SDSS void + filament catalogs

The preferred reproducible environment-label route is now documented as a derived SDSS void+filament cross-match:

```text
notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py
notebooks/pantheon/generate_environment_labels_from_void_catalog.py
data/pantheon/environment-labels-methodology.md
data/pantheon/environment_labels_README.md
```

Expected external catalog locations after extraction:

```text
data/pantheon/external/void_catalog_2014.06.18_just_sdss/
data/pantheon/external/J_MNRAS_438_3465/
```

The generated combined labels are conservative catalog cross-match labels:

```text
void
near_void_edge
filament
near_filament
field_or_wall
sdss_nonvoid
outside_catalog_coverage
```

These are derived labels, not official Pantheon+ classifications. They remain preliminary until the full environment-H0 fit is reproduced and audited.

## Full Pantheon+/SH0ES covariance

A root upload named `Pantheon_SH0ES_cov.txt.gz` was inspected on 2026-06-08:

- compressed size: `10,334,474` bytes;
- readable as gzip text;
- first value: `1701`;
- remaining numeric value count: `2,893,401`, equal to `1701 * 1701` covariance entries.

Because this appears to be a full public-data covariance artifact and redistribution terms were not verified during cleanup, it is classified as **EXTERNAL/DOCUMENTED** rather than committed as canonical data. If redistribution is cleared and the project wants it in-repo, use Git LFS or a documented data-release workflow before adding `data/pantheon/Pantheon_SH0ES_cov.txt.gz` or `data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov`.


## 2026-06-14 generation attempt

A local validation pass confirmed that the combined generator script is present on the current branch and that syntax/help smoke checks pass. The required user-provided raw/staged files were not present anywhere discoverable in the container, so `data/pantheon/environment_labels.csv` was **not generated or committed** in this pass. The raw input directories were created locally as ignored staging locations only:

```text
data/pantheon/raw/
data/pantheon/external/
```

The following inputs must be staged locally before rerunning the documented generation command:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov
data/pantheon/external/void_catalog_2014.06.18_just_sdss/
data/pantheon/external/J_MNRAS_438_3465/table2.dat.gz
```

## 2026-06-19 generation attempt

A follow-up local pass again found that the required raw Pantheon+ table/covariance and extracted external SDSS void + Tempel/Bisous filament catalogs were absent. The expected uploaded/source filenames were also not discoverable under `/workspace`, so the raw inputs could not be staged automatically. Syntax validation passed, and the documented generator exited with an input error before creating any partial output. Consequently, `data/pantheon/environment_labels.csv` remains **not generated and not committed** in this pass. See `data/pantheon/environment_labels_summary.md` for the command record and claim boundary.


## 2026-06-30 generated derived-artifact import

The generated derived environment-label artifacts are now present under `data/pantheon/`:

```text
data/pantheon/environment_labels.csv
data/pantheon/environment_labels_preview.csv
data/pantheon/environment_labels_summary.md
data/pantheon/environment_labels.sha256.json
```

`data/pantheon/environment_labels.csv` is a derived SDSS void + Tempel/Bisous filament cross-match artifact with 1701 row-aligned Pantheon+ entries. `data/pantheon/environment_labels_preview.csv` is a small preview, `data/pantheon/environment_labels_summary.md` records generation and validation, and `data/pantheon/environment_labels.sha256.json` records the canonical CSV checksum. Raw Pantheon+ tables, raw covariance files, void catalog archives, and extracted external catalog tables remain external/ignored and were not committed.

The imported label counts are: `field_or_wall` 827, `sdss_nonvoid` 741, `outside_catalog_coverage` 75, `void` 34, `near_void_edge` 21, `filament` 2, and `near_filament` 1. Coverage counts are `derived_crossmatch` 1626 and `outside_catalog_coverage` 75. Row order is preserved through sequential `row_index` values 0 through 1700 for covariance-safe joining.

## Claim boundary

These are derived SDSS void + Tempel/Bisous filament cross-match labels for preliminary Pantheon+ environment-H0 pipeline testing. They are not official Pantheon+ metadata and do not establish an H0/environment detection without the full covariance-aware fit and independent reproducibility audit.

## 2026-06-30 covariance-aware environment-H0 runner

A paired runnable script now advances the imported label artifact toward the covariance-aware Pantheon+ environment-H0 diagnostic:

```bash
python notebooks/pantheon/run_pantheon_environment_h0_analysis.py
```

The runner uses `data/pantheon/raw/Pantheon+SH0ES.dat` as the canonical whitespace-delimited Pantheon+ table, `data/pantheon/environment_labels.csv` as the row-aligned derived label table, and the first available covariance candidate from:

```text
data/pantheon/Pantheon_SH0ES_cov.txt.gz
data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov
data/pantheon/pantheon_covariance.txt
data/pantheon/Pantheon_cov_subset.txt
```

It supports Pantheon-style covariance files with a leading matrix size followed by `N*N` flattened entries, validates a `(1701, 1701)` covariance against the Pantheon row count, preserves covariance row order through `row_index`, and verifies `CID`, `RA`, `DEC`, `zHD`, and `zCMB` row-by-row before fitting.

In this container pass, the raw Pantheon+ table and covariance were missing, so the runner wrote a blocked summary at `observations/pantheon-environment-h0/results/pantheon_environment_h0_run_summary.md` and did not emit fit CSV outputs. Raw Pantheon+ tables and covariance files remain external/ignored and should not be committed unless project policy changes.
