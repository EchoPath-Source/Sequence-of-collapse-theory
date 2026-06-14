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

## Claim boundary

These labels are derived cross-match labels, not official Pantheon+ metadata. They should be used to unlock preliminary Pantheon+ environment-H0 pipeline testing only after row-order preservation and catalog coverage are verified.
