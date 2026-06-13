# Pantheon+ Environment Labels README

**Artifact:** `data/pantheon/environment_labels.csv`  
**Status:** missing until generated / derived cross-match artifact

## Purpose

`environment_labels.csv` is the row-aligned environment-label companion table for the Pantheon+ environment-dependent H0 pipeline.

It is generated from:

```text
data/pantheon/raw/Pantheon+SH0ES.dat
data/pantheon/external/void_catalog_2014.06.18_just_sdss/
```

using:

```text
notebooks/pantheon/generate_environment_labels_from_void_catalog.py
```

## Generate

After placing the raw public inputs outside normal git tracking, run:

```bash
python notebooks/pantheon/generate_environment_labels_from_void_catalog.py \
  --pantheon data/pantheon/raw/Pantheon+SH0ES.dat \
  --void-catalog-dir data/pantheon/external/void_catalog_2014.06.18_just_sdss \
  --output data/pantheon/environment_labels.csv
```

## Expected labels

```text
void
near_void_edge
sdss_nonvoid
outside_catalog_coverage
```

These labels are derived from a public SDSS void catalog. They should not be presented as official Pantheon+ classifications or as true filament labels.

## Future upgrade

When a public SDSS filament/cosmic-web catalog is added, `sdss_nonvoid` may be subdivided into filament/wall/field/node labels with a separate methodology note and versioned output.
