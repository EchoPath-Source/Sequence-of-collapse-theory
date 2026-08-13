# DESI DR1 Schema Verification

## Purpose

Record the pre-query schema verification required by the DESI reproducibility contract before any smoke query, environment estimator, environment-label generation, Pantheon+ crossmatch, or H0 analysis.

Verification date:

```text
2026-08-13
```

Authoritative sources checked:

```text
NSF NOIRLab Astro Data Lab — DESI data-release documentation
https://datalab.noirlab.edu/data/desi

NSF NOIRLab Astro Data Lab Help Desk — DESI zpix coordinate query example
https://datalab.noirlab.edu/help/index.php?qa=2138&qa_1=desi-cone-search-has-a-minimum-search-radius-bug
```

This is a schema/documentation verification note, not an analysis result.

## Release verification

Verified planning target:

```text
DESI DR1
```

The NOIRLab Astro Data Lab documentation identifies DESI DR1 as the first public DESI data release and recommends the per-HEALPix `zpix` catalog for most spectroscopic analyses.

## Verified catalog resources

The following resources named in the P5 query plan are present in the current DESI DR1 documentation:

| Resource | Status | Documentation role |
|---|---|---|
| `desi_dr1.zpix` | VERIFIED PRESENT | Primary per-HEALPix redshift/spectroscopic catalog; recommended for most analyses. |
| `desi_dr1.photometry` | VERIFIED PRESENT | Legacy Surveys DR9 photometric quantities for DESI TARGETIDs. |
| `desi_dr1.stellar_mass_emline` | VERIFIED PRESENT | Stellar-mass and emission-line VAC for galaxies with reliable redshift measurements. |
| `desi_dr1.emfit` | VERIFIED PRESENT | Emission-line flux/width VAC for low-redshift sources, documented for `z <= 0.45`. |
| `desi_dr1.agngal` | VERIFIED PRESENT | Galaxy/quasar spectral and infrared classification diagnostics VAC. |

## Verified quality-selection semantics

The current NOIRLab DESI DR1 documentation defines useful spectra using:

```text
ZCAT_PRIMARY == True
OBJTYPE == 'TGT'
ZWARN == 0
```

For the Main Survey, the documentation additionally excludes:

```text
PROGRAM == 'other'
```

The P5 base-galaxy restriction:

```text
SPECTYPE == 'GALAXY'
```

is also directly supported by the DESI DR1 documentation.

For the first smoke query, the repository therefore stages the stricter documented selection rather than silently retaining the earlier minimal starter cuts.

## Coordinate-column resolution

The earlier P5 starter queries used planning names:

```text
target_ra
target_dec
```

Current NOIRLab DESI material provides a direct `desi_dr1.zpix` query example using:

```text
mean_fiber_ra
mean_fiber_dec
```

These are therefore the coordinate fields selected for smoke-query v0.1.

Important semantic boundary:

> `mean_fiber_ra` and `mean_fiber_dec` are mean fiber-position coordinates associated with the coadded zpix spectrum. They should not be renamed or described as target coordinates without a separate verified mapping.

The full environment-label export schema may later expose normalized fields such as `target_ra` / `target_dec`, but only after the coordinate source and transformation are explicitly documented.

## HEALPix and required-field status

Current NOIRLab DESI documentation verifies the per-HEALPix role of `zpix`. Current NOIRLab query/help material supports use of the following fields in the staged smoke query:

```text
targetid
mean_fiber_ra
mean_fiber_dec
z
zwarn
zcat_primary
objtype
survey
program
spectype
healpix
```

The exact database data types, nullability/sentinel behavior, and row-level values still require confirmation by executing the smoke query or inspecting live TAP metadata.

## Staged smoke query

Canonical tiny query:

```text
data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql
```

Query version:

```text
desi-dr1-smoke-v0.1
```

The query is limited to 25 rows in a one-degree sky patch and applies:

```text
zcat_primary = true
objtype = 'TGT'
zwarn = 0
spectype = 'GALAXY'
survey = 'main'
program <> 'other'
0.01 <= z <= 0.5
55.5 <= mean_fiber_ra <= 56.5
-9.5 <= mean_fiber_dec <= -8.5
```

This is deliberately a schema/access smoke test, not an environment sample.

## Execution status

The smoke query is **READY / NOT YET RUN**.

This environment was able to verify the current NOIRLab documentation and query semantics but does not expose an authenticated/anonymous Data Lab query execution channel through the available tools. A local installation attempt of the Data Lab Python client was also blocked by network/package-resolution restrictions.

Accordingly, no query rows are claimed here.

When execution access is available, the first run should record:

- execution timestamp;
- Data Lab service/profile;
- returned row count;
- returned column names;
- null/sentinel observations;
- coordinate ranges;
- redshift range;
- whether all quality predicates are satisfied;
- SHA-256 of any intentionally retained tiny CSV snapshot.

## Value-added catalog join verification still required

VAC table names are verified present, but join cardinality has **NOT YET BEEN VERIFIED**.

Before production joins, test whether `targetid` is one-to-one, one-to-zero/one, or one-to-many for:

```text
desi_dr1.stellar_mass_emline
desi_dr1.emfit
desi_dr1.agngal
```

Do not use broad `SELECT s.*` or `SELECT e.*` production joins until required fields and array-valued columns are explicitly documented.

## Known DR1 issue noted during verification

The current NOIRLab DESI page records a 2026-07-21 patch to `desi_dr1.zpix` and `desi_dr1.ztile` correcting formatting of `desiname` for RA/Dec values very close to zero.

This does not invalidate the staged smoke query, but retrieval date must remain part of provenance.

## Current verification status

```text
DESI DR1 release: VERIFIED
zpix table: VERIFIED PRESENT
photometry table: VERIFIED PRESENT
stellar_mass_emline VAC: VERIFIED PRESENT
emfit VAC: VERIFIED PRESENT
agngal VAC: VERIFIED PRESENT
useful-spectrum semantics: VERIFIED
zpix coordinate fields for smoke v0.1: DOCUMENTED / RESOLVED TO mean_fiber_ra, mean_fiber_dec
remaining live data-type/null checks: PENDING EXECUTION
VAC join cardinality: NOT YET TESTED
tiny smoke query SQL: READY
tiny smoke query execution: NOT YET RUN
environment estimator: NOT YET IMPLEMENTED
environment labels: NOT YET GENERATED
Pantheon+ crossmatch: NOT YET RUN
H0 environment test: NOT YET RUN
```

## Claim boundary

This verification establishes documented DESI DR1 resources, quality-selection semantics, and a reproducible coordinate choice for the first tiny query. It does not establish an environment effect, validate SoCT/PNT, show that gravity or dark matter is memory, or measure `H0_void > H0_filament`.
