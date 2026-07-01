# Import/Reconciliation Pass — 2026-06-11 — Pantheon+ Filament Catalog Pipeline

**Purpose:** record the addition of the Tempel et al. / Bisous SDSS filament catalog route for the Pantheon+ environment-label workstream.

## External catalog

The user provided the VizieR archive for:

```text
J/MNRAS/438/3465
Tempel et al. 2014 — Cosmic web filaments in the SDSS
```

The archive contains:

```text
ReadMe
table1.dat.gz
table2.dat.gz
table3.dat.gz
```

Only methodology and scripts are committed. Raw catalog archives and extracted tables should be staged externally unless storage and redistribution policy is cleared.

## Added / updated files

| Repo path | Track | Status |
|---|---|---|
| `notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py` | P5 / Pantheon+ | Preferred combined void+filament label generator. |
| `data/pantheon/environment-labels-methodology.md` | P5 / Pantheon+ | Updated to describe void+filament derived labels and priority rules. |
| `data/pantheon/environment_labels_README.md` | P5 / Pantheon+ | Updated with preferred command and required staged inputs. |
| `data/pantheon/README.md` | P5 / Pantheon+ | Updated to document combined label route. |

## Preferred staged inputs

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/external/void_catalog_2014.06.18_just_sdss/
data/pantheon/external/J_MNRAS_438_3465/
```

## Output

```text
data/pantheon/environment_labels.csv
```

## Label set

```text
void
near_void_edge
filament
near_filament
field_or_wall
sdss_nonvoid
outside_catalog_coverage
```


## 2026-06-14 operational validation update

The combined void+filament generator remains present at `notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py`, and syntax/help smoke checks passed. The full generation command was not run to completion because the required local Pantheon+ table and external catalog archives/extractions were not available in the container. Consequently, `data/pantheon/environment_labels.csv` was **not generated and not committed** in this pass.

Before generating labels, stage the raw public inputs only in ignored local paths and keep raw Pantheon+/catalog archives out of git unless redistribution policy is explicitly cleared.

## 2026-06-19 operational validation update

A follow-up generation pass was attempted. The required ignored raw/staged inputs were still absent, and the expected uploaded/source filenames were not discoverable in the workspace, so the pass remains blocked by missing local inputs. The combined script passed syntax validation and failed safely at runtime with an explicit missing Pantheon+ table input error. No derived `environment_labels.csv`, preview CSV, or checksum was generated or committed.

Future completion requires staging the Pantheon+SH0ES table/covariance plus extracted SDSS void and Tempel/Bisous filament catalogs in the documented ignored paths, confirming the filament archive contains `ReadMe`, `table1.dat.gz`, `table2.dat.gz`, and `table3.dat.gz`, and then rerunning the generator plus row-order validation.


## 2026-06-30 generated artifact import update

The generated derived artifacts manually uploaded to the repository root were moved into canonical `data/pantheon/` paths:

```text
data/pantheon/environment_labels.csv
data/pantheon/environment_labels_preview.csv
data/pantheon/environment_labels_summary.md
data/pantheon/environment_labels.sha256.json
```

The canonical CSV has 1701 rows with sequential `row_index` values 0 through 1700, preserving Pantheon+ row order for covariance-safe joining. Label counts are `field_or_wall` 827, `sdss_nonvoid` 741, `outside_catalog_coverage` 75, `void` 34, `near_void_edge` 21, `filament` 2, and `near_filament` 1. Coverage counts are `derived_crossmatch` 1626 and `outside_catalog_coverage` 75. The canonical CSV SHA-256 is `ff3006e8cbf7316db29b3760f39d02e911b99a86e814e1a698014a8242695a9d`.

The raw Pantheon+ source files, raw covariance files, void catalog archives, and extracted external catalogs remain external/ignored and were not committed. The root-only local generator was removed rather than retained as a parallel script; the canonical generator remains `notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py`.

No Pantheon H0/environment result is claimed from this import.

## Claim boundary

These are derived SDSS void + Tempel/Bisous filament cross-match labels for preliminary Pantheon+ environment-H0 pipeline testing. They are not official Pantheon+ metadata and do not establish an H0/environment detection without the full covariance-aware fit and independent reproducibility audit.

## Follow-up covariance-aware H0 runner — 2026-06-30

A downstream runner was added at `notebooks/pantheon/run_pantheon_environment_h0_analysis.py` to consume the imported SDSS void + Tempel/Bisous filament labels in a covariance-aware Pantheon+ environment-H0 diagnostic. The runner expects the canonical ignored raw table `data/pantheon/raw/Pantheon+SH0ES.dat`, accepts the canonical ignored covariance `data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov` plus documented fallback covariance candidates, and validates row-order safety through `row_index` plus `CID`, `RA`, `DEC`, `zHD`, and `zCMB` checks.

The local execution in this pass was blocked by missing raw Pantheon+ table and covariance inputs. It exited cleanly and wrote `observations/pantheon-environment-h0/results/pantheon_environment_h0_run_summary.md`. No Pantheon H0/environment result is claimed from this run.

The runner includes conservative predeclared grouping modes and skips any contrast with fewer than 5 rows on either side after the locked `0.01 <= zHD <= 0.15` redshift cut. Given the imported label counts of 2 exact `filament` rows and 1 `near_filament` row, strict and edge-inclusive void-vs-filament contrasts are expected to be marked underpowered when raw inputs are staged.
