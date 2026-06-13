# Import/Reconciliation Pass — 2026-06-11 — Pantheon+ Void-Catalog Environment Labels

**Purpose:** record the addition of a documented derived-label route for the Pantheon+ environment-H0 workstream.

## Added files

| Repo path | Track | Status |
|---|---|---|
| `notebooks/pantheon/generate_environment_labels_from_void_catalog.py` | P5 / Pantheon+ | Script scaffold for generating row-aligned environment labels from an extracted SDSS void catalog. |
| `data/pantheon/environment-labels-methodology.md` | P5 / Pantheon+ | Methodology and claim-boundary note for void-catalog cross-match labels. |
| `data/pantheon/environment_labels_README.md` | P5 / Pantheon+ | Operational README for generating `environment_labels.csv`. |
| `data/pantheon/README.md` | P5 / Pantheon+ | Updated to document the new void-catalog label route. |

## External inputs

The script expects public data inputs to be staged outside normal git tracking:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/external/void_catalog_2014.06.18_just_sdss/
```

The uploaded void-catalog archives are treated as external source inputs. The repository now documents how to use them but does not commit the raw archive or extracted catalog.

## Claim boundary

The generated labels are conservative void-catalog labels:

```text
void
near_void_edge
sdss_nonvoid
outside_catalog_coverage
```

These are not official Pantheon+ labels and are not true filament/wall/node classifications. A later public filament/cosmic-web catalog should be added before using filament-specific language.

## Remaining item

`data/pantheon/environment_labels.csv` remains missing until the script is run against staged raw inputs and the output is reviewed.
