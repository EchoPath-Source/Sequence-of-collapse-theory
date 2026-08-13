# DESI Environment Query Plan

## Purpose

This document defines how DESI DR1 can support the P5 Hubble-tension / memory-gradient track without overstating what DESI can prove.

DESI is useful for constructing a large-scale structure and galaxy-environment scaffold. In SoCT/PNT terms, this can become an operational proxy for collapse-history density:

```text
void regions     -> low collapse history / low memory-density proxy
filaments/walls  -> higher collapse history / higher memory-density proxy
clusters/halos   -> high collapse history / high accumulated-structure proxy
```

This does not prove SoCT, PNT, dark-sector memory, or gravity-as-memory. It provides a data-driven environment layer that can later be used for Pantheon+ crossmatching and galaxy-evolution tests.

## Repository role

Canonical paper track:

```text
papers/p5-hubble-tension-memory-gradient/
```

Related status docs:

```text
data/PANTHEON_IMPORT_STATUS.md
docs/reproducibility_checklist.md
docs/dark-sector-taxonomy.md
```

## DESI role in the SoCT/PNT program

DESI can support three research paths:

1. Build a galaxy-density / cosmic-web proxy.
2. Generate void / low-density / filament-like / cluster-like environment labels.
3. Crossmatch those environment labels to Pantheon+ supernovae for the preregistered H0 environment test.

Primary SoCT/PNT prediction already tracked elsewhere:

```text
H0_void > H0_filament
```

DESI does not directly measure supernova H0. It can help construct the environment-label map needed before Pantheon+ can test that prediction.

## Useful DESI DR1 resources

The most relevant DESI DR1 tables are expected to include:

- `desi_dr1.zpix`
- `desi_dr1.photometry`
- `desi_dr1.stellar_mass_emline`
- `desi_dr1.emfit`
- `desi_dr1.agngal`

Use `zpix` as the primary spectroscopic catalog for reliable redshifts and HEALPix-based sky structure. Use value-added catalogs such as `stellar_mass_emline` or `emfit` for galaxy-evolution proxies where available.

Before running production queries, verify table and column names against the current NOIRLab Data Lab DESI DR1 schema.

## DESI subset script role

The `desi_get_dr_subset` script is useful for small local downloads around a selected sky position:

```bash
desi_get_dr_subset --dr dr1 --ra 56.0 --dec -9.0 --radius 0.1 --base-dir ./tiny_dr1 --no-tiles
```

Use this for:

- inspecting spectra around a targeted RA/Dec;
- validating a small sky patch;
- checking whether a selected region has useful target density;
- creating a tutorial-scale local sample.

Do not use the subset script as the primary large-scale statistical pipeline. Large-scale SoCT/PNT tests should use Data Lab SQL queries or catalog-level workflows.

## Starter query 1 — reliable galaxy redshift sample

Purpose: build the base galaxy sample for density/environment mapping.

```sql
SELECT
  targetid,
  target_ra,
  target_dec,
  z,
  zwarn,
  spectype,
  healpix
FROM desi_dr1.zpix
WHERE zcat_primary = true
  AND zwarn = 0
  AND spectype = 'GALAXY'
  AND z BETWEEN 0.01 AND 0.5
LIMIT 100000;
```

## Starter query 2 — stellar mass / emission-line join

Purpose: add galaxy maturity, star-formation, or spectral-evolution proxies.

```sql
SELECT
  z.targetid,
  z.target_ra,
  z.target_dec,
  z.z,
  z.spectype,
  s.*
FROM desi_dr1.zpix AS z
JOIN desi_dr1.stellar_mass_emline AS s
  ON z.targetid = s.targetid
WHERE z.zcat_primary = true
  AND z.zwarn = 0
  AND z.spectype = 'GALAXY'
  AND z.z BETWEEN 0.01 AND 0.5
LIMIT 100000;
```

## Starter query 3 — low-redshift emission-line sample

Purpose: examine star-forming versus quiescent behavior across density environments.

```sql
SELECT
  z.targetid,
  z.target_ra,
  z.target_dec,
  z.z,
  e.*
FROM desi_dr1.zpix AS z
JOIN desi_dr1.emfit AS e
  ON z.targetid = e.targetid
WHERE z.zcat_primary = true
  AND z.zwarn = 0
  AND z.spectype = 'GALAXY'
  AND z.z BETWEEN 0.01 AND 0.45
LIMIT 100000;
```

## Starter query 4 — sky patch preview

Purpose: preview a field before running the DESI subset downloader.

```sql
SELECT
  targetid,
  target_ra,
  target_dec,
  z,
  zwarn,
  spectype,
  healpix
FROM desi_dr1.zpix
WHERE zcat_primary = true
  AND zwarn = 0
  AND target_ra BETWEEN 55.5 AND 56.5
  AND target_dec BETWEEN -9.5 AND -8.5
LIMIT 5000;
```

## First analysis pipeline

Recommended first notebook flow:

```text
DESI reliable galaxy sample
  -> redshift shell selection
  -> local density estimator
  -> environment binning
  -> stellar mass / emission-line joins
  -> redshift-controlled property comparisons
  -> environment-label export
  -> Pantheon+ crossmatch-ready catalog
```

Candidate environment bins:

- void-like / low-density
- sheet-like / intermediate-density
- filament-like / high-density
- cluster/halo-like / highest-density

## Candidate outputs

```text
data/desi/desi_dr1_environment_labels.csv
data/desi/desi_dr1_density_shell_summary.csv
figures/desi/desi_density_environment_map.png
notebooks/desi/desi_environment_density_map.ipynb
```

## SoCT/PNT interpretation

If the memory-gradient interpretation is useful, then high-density cosmic-web structures should behave like higher-collapse-history regions, while voids should behave like lower-collapse-history regions.

Safe language:

> DESI can help operationalize a collapse-history proxy by mapping galaxy density, environment, redshift, stellar mass, and spectral state. That proxy can then be used to test whether SoCT/PNT predictions about voids, filaments, and memory-gradient behavior hold up statistically.

Avoid:

- DESI proves SoCT.
- DESI proves dark matter is memory.
- DESI proves voids contain no dark matter.
- DESI proves `H0_void > H0_filament` without Pantheon+ crossmatching.
- DESI validates PNT.

## Relationship to Pantheon+

The DESI environment map should eventually support the Pantheon+ track:

```text
Pantheon+ SN coordinates
  -> crossmatch to DESI density/environment labels
  -> split SN sample by void/filament-like environment
  -> fit H0 by environment
  -> test Delta H0 = H0_void - H0_filament
```

This requires the Pantheon+ SN table, covariance matrix, environment-label methodology, and row-order validation tracked in:

```text
data/PANTHEON_IMPORT_STATUS.md
```

## Reproducibility/data-staging docs

Before any large query, environment-label generation, or Pantheon+ crossmatch, use:

```text
data/desi/README.md
notebooks/desi/DESI_ENVIRONMENT_NOTEBOOK_PLAN.md
```

These documents define the DESI data/provenance contract and lock the intended notebook sequence before implementation.

## Claim boundary

This is a research-query and environment-label plan. It does not create empirical confirmation. It defines how DESI may help generate testable environment labels for later SoCT/PNT analysis.
