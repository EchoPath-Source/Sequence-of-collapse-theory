# DESI DR1 Schema Verification

## Purpose

Record the pre-query schema verification required by the DESI reproducibility contract before any smoke query, environment estimator, environment-label generation, Pantheon+ crossmatch, or H0 analysis.

Verification date:

```text
2026-08-13
```

Authoritative source checked:

```text
NSF NOIRLab Astro Data Lab — DESI data-release documentation
https://datalab.noirlab.edu/data/desi
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

The documentation also lists `target`, `ztile`, `fiberassign`, `potential`, `tile`, `exposure`, `frame`, and the `mws` VAC, but these are not currently required by the first P5 smoke query.

## Verified quality-selection semantics

The current NOIRLab DESI DR1 documentation defines "useful spectra" using:

```text
ZCAT_PRIMARY == True
OBJTYPE == 'TGT'
ZWARN == 0
```

For the Main Survey, the documentation additionally excludes:

```text
PROGRAM == 'other'
```

The P5 plan also proposes:

```text
SPECTYPE == 'GALAXY'
```

as the science-object restriction for the base galaxy sample. The DESI DR1 documentation explicitly reports galaxy counts using `SPECTYPE==GALAXY`, so that semantic use is supported.

The exact production sample cut is **NOT YET LOCKED**. In particular, the current starter queries omit `OBJTYPE == 'TGT'` and the Main Survey `PROGRAM != 'other'` condition used by NOIRLab's documented useful-spectrum definition. The smoke-query stage should test and record whether those conditions should be adopted for the P5 base sample rather than silently changing the query.

## HEALPix verification

The DESI documentation confirms that `zpix` contains spectra grouped/coadded per sky position by HEALPix and describes the DR1 `zpix` table as the primary spectroscopic catalog.

This supports the planned use of HEALPix information for sky partitioning, subject to exact column-name verification before execution.

## Coordinate-column verification status

**BLOCKING DETAIL BEFORE SMOKE QUERY**

The high-level DESI documentation verifies that `zpix` is position based, but this verification pass does not establish that the starter-query coordinate names:

```text
target_ra
target_dec
```

are the correct current `desi_dr1.zpix` column names.

Current NOIRLab examples and help material also use coordinate fields such as:

```text
mean_fiber_ra
mean_fiber_dec
```

for `desi_dr1.zpix` queries.

Therefore the starter queries must not be executed unchanged until the live table schema confirms the intended RA/Dec fields and their semantics.

## Column-level verification still required

Before the first smoke query, verify directly in the Data Lab table schema/TAP metadata:

```text
targetid
z
zwarn
zcat_primary
objtype
program
spectype
healpix
<chosen RA field>
<chosen Dec field>
```

Also verify:

- data types;
- nullability or sentinel behavior where relevant;
- coordinate units;
- whether `targetid` is unique after the intended `zcat_primary` selection;
- whether `healpix` is available under the expected name;
- whether the selected coordinate pair represents target coordinates, mean fiber coordinates, or another positional definition.

## Value-added catalog join verification still required

The VAC table names are verified present, but join cardinality has **NOT YET BEEN VERIFIED**.

Before production joins, test whether `targetid` is one-to-one, one-to-zero/one, or one-to-many for:

```text
desi_dr1.stellar_mass_emline
desi_dr1.emfit
desi_dr1.agngal
```

Do not use `SELECT s.*` or `SELECT e.*` in a production reproducibility query until the required fields and array-valued columns are explicitly documented.

The NOIRLab documentation notes that `stellar_mass_emline` contains an array-valued `xj_sl` field, which requires special handling when parsed from CSV.

## Known DR1 issue noted during verification

The current NOIRLab DESI page records a 2026-07-21 patch to `desi_dr1.zpix` and `desi_dr1.ztile` correcting formatting of `desiname` for RA/Dec values very close to zero.

This does not currently invalidate the P5 plan, but the schema/query provenance should record the retrieval date so later runs can distinguish pre- and post-patch catalog states if necessary.

## Smoke-query gate

The first smoke query remains **NOT YET RUN**.

It may proceed only after the coordinate columns and remaining required column names above are confirmed from live schema metadata.

The smoke query must remain deliberately small and should validate only:

- table/column access;
- selected RA/Dec semantics;
- redshift and quality fields;
- galaxy selection;
- HEALPix field availability;
- row retrieval;
- provenance capture.

It must not be used to estimate environment statistics or any H0 differential.

## Current verification status

```text
DESI DR1 release: VERIFIED
zpix table: VERIFIED PRESENT
photometry table: VERIFIED PRESENT
stellar_mass_emline VAC: VERIFIED PRESENT
emfit VAC: VERIFIED PRESENT
agngal VAC: VERIFIED PRESENT
high-level useful-spectrum semantics: VERIFIED
exact coordinate columns: PENDING LIVE SCHEMA CHECK
remaining required column metadata: PENDING LIVE SCHEMA CHECK
VAC join cardinality: NOT YET TESTED
tiny smoke query: NOT YET RUN
environment estimator: NOT YET IMPLEMENTED
environment labels: NOT YET GENERATED
Pantheon+ crossmatch: NOT YET RUN
H0 environment test: NOT YET RUN
```

## Claim boundary

This verification establishes that the planned DESI DR1 resources exist in current NOIRLab documentation and identifies unresolved schema details that must be checked before querying.

It does not establish an environment effect, validate SoCT/PNT, show that gravity or dark matter is memory, or measure `H0_void > H0_filament`.
