# Pantheon+ Environment Labels README

**Artifact:** `data/pantheon/environment_labels.csv`
**Status:** present / derived cross-match artifact imported on 2026-06-30
**Rows:** 1701
**SHA-256:** `ff3006e8cbf7316db29b3760f39d02e911b99a86e814e1a698014a8242695a9d`

## Purpose

`environment_labels.csv` is the row-aligned environment-label companion table for preliminary Pantheon+ environment-dependent H0 pipeline testing. The labels are derived SDSS void + Tempel/Bisous filament cross-match labels, not official Pantheon+ metadata.

## Imported artifacts

```text
data/pantheon/environment_labels.csv
data/pantheon/environment_labels_preview.csv
data/pantheon/environment_labels_summary.md
data/pantheon/environment_labels.sha256.json
```

`environment_labels_preview.csv` is a small preview of the derived table. `environment_labels_summary.md` documents the local generation and validation pass. `environment_labels.sha256.json` records the canonical checksum metadata for `data/pantheon/environment_labels.csv`.

## Required staged inputs for regeneration

Raw inputs remain external/ignored and are not committed:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov
data/pantheon/external/void_catalog_2014.06.18_just_sdss/
data/pantheon/external/J_MNRAS_438_3465/
```

## Preferred script

```text
notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py
```

The older void-only fallback remains available:

```text
notebooks/pantheon/generate_environment_labels_from_void_catalog.py
```

## Run command

```text
python notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py --pantheon data/pantheon/raw/Pantheon+SH0ES.dat --void-catalog-dir data/pantheon/external/void_catalog_2014.06.18_just_sdss --filament-catalog-dir data/pantheon/external/J_MNRAS_438_3465 --output data/pantheon/environment_labels.csv
```

## Imported label counts

| Label | Count |
|---|---:|
| `field_or_wall` | 827 |
| `sdss_nonvoid` | 741 |
| `outside_catalog_coverage` | 75 |
| `void` | 34 |
| `near_void_edge` | 21 |
| `filament` | 2 |
| `near_filament` | 1 |

## Imported coverage counts

| Coverage flag | Count |
|---|---:|
| `derived_crossmatch` | 1626 |
| `outside_catalog_coverage` | 75 |

## Row-order rule

The output preserves Pantheon+ row order through sequential `row_index` values 0 through 1700, so labels can be joined to the covariance-aligned SN table without reordering.

## Claim boundary

These are derived SDSS void + Tempel/Bisous filament cross-match labels for preliminary Pantheon+ environment-H0 pipeline testing. They are not official Pantheon+ metadata and do not establish an H0/environment detection without the full covariance-aware fit and independent reproducibility audit.

## Downstream covariance-aware H0 diagnostic

The imported `environment_labels.csv` table is consumed by `notebooks/pantheon/run_pantheon_environment_h0_analysis.py`. The runner treats `environment_label` as the canonical label column and normalizes it to an analysis column named `environment` after loading. It joins by row order using `row_index`, then verifies `CID`, `RA`, `DEC`, `zHD`, and `zCMB` against `data/pantheon/raw/Pantheon+SH0ES.dat` before any fit.

The diagnostic predeclares strict, edge-inclusive, structure-contrast, and catalog-covered grouping modes. Because the imported labels contain only 2 exact `filament` rows and 1 `near_filament` row, the strict and edge-inclusive void-vs-filament modes are expected to be underpowered unless a future label-generation policy changes. The runner marks any grouping with fewer than 5 rows on either side after the locked redshift cut as `SKIPPED_UNDERPOWERED`.
