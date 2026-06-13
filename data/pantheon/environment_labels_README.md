# Pantheon+ Environment Labels README

**Artifact:** `data/pantheon/environment_labels.csv`  
**Status:** missing until generated / derived cross-match artifact

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
