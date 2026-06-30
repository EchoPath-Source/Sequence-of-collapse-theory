# Pantheon+ Environment Labels README

**Artifact:** `data/pantheon/environment_labels.csv`  
**Status:** not generated in the 2026-06-19 validation pass because required local raw/staged inputs and expected uploaded/source files were absent / derived cross-match artifact

## Purpose

`environment_labels.csv` is the row-aligned environment-label companion table for the Pantheon+ environment-dependent H0 pipeline.

## Required staged inputs

```text
data/pantheon/raw/Pantheon+SH0ES.dat
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


## 2026-06-14 validation status

The combined generator script was present and passed syntax and `--help` smoke checks. The environment label CSV was not generated because the expected local source files/archives were absent from the container:

```text
Pantheon+SH0ES.dat.txt
Pantheon+SH0ES_STAT+SYS.cov(1).txt
void_catalog_2014.06.18_just_sdss.tar.gz
J_MNRAS_438_3465.tar.gz.tar
```

After staging those files in ignored paths, rerun the command below and then validate row count, sequential `row_index`, required columns, nonempty `environment_label`, label/coverage counts, and row-order safety against Pantheon+ `CID`, `RA`, `DEC`, `zHD`, and `zCMB`.

## 2026-06-19 validation status

The combined generator still passes syntax validation, but generation remains blocked in this workspace. The required ignored local staged inputs were absent, and the expected uploaded/source files could not be found, so no full CSV, preview CSV, or checksum was produced. The documented generator command was run and failed safely with an input error for the missing Pantheon+ table.

## Run command

```text
python notebooks/pantheon/generate_environment_labels_from_void_filament_catalogs.py --pantheon data/pantheon/raw/Pantheon+SH0ES.dat --void-catalog-dir data/pantheon/external/void_catalog_2014.06.18_just_sdss --filament-catalog-dir data/pantheon/external/J_MNRAS_438_3465 --output data/pantheon/environment_labels.csv
```

## Expected labels

```text
void
near_void_edge
filament
near_filament
field_or_wall
sdss_nonvoid
outside_catalog_coverage
```

These labels are derived from public SDSS void and Tempel/Bisous filament catalogs. They should not be presented as official Pantheon+ classifications.

## Source catalogs

- Void catalog: public SDSS void catalog staged at `data/pantheon/external/void_catalog_2014.06.18_just_sdss/`.
- Filament catalog: Tempel et al. SDSS/Bisous catalog `J/MNRAS/438/3465`, staged at `data/pantheon/external/J_MNRAS_438_3465/` with `table2.dat(.gz)` available.

## Row-order rule

The output must preserve Pantheon+ row order through `row_index`, so labels can be joined to the covariance-aligned SN table without reordering.
