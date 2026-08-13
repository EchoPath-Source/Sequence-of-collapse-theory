# DESI DR1 Column Semantics Contract

## Purpose

This file freezes the DESI DR1 column assumptions used by the P5 environment-label pipeline before smoke-query execution, density-estimator work, environment-label generation, Pantheon+ crossmatching, or H0 analysis.

It consolidates and sharpens the existing schema-verification record rather than replacing it:

```text
data/desi/DESI_DR1_SCHEMA_VERIFICATION.md
```

No analysis result is created here.

## Source-of-truth resources

Column and selection assumptions must be checked against authoritative DESI / NSF NOIRLab Astro Data Lab resources:

- NSF NOIRLab Astro Data Lab DESI DR1 page: `https://datalab.noirlab.edu/data/desi`
- DESI public data documentation/access pages linked from the Data Lab DESI page
- Astro Data Lab Data Explorer / TAP schema for live table metadata
- any SQL/TAP query used to inspect table schemas

Verification date for this contract: `2026-08-13`.

The Data Lab DESI DR1 page identifies `desi_dr1.zpix` as the recommended primary spectroscopic catalog for most analyses. It defines useful spectra as `ZCAT_PRIMARY == True`, `OBJTYPE == 'TGT'`, and `ZWARN == 0`; Main Survey useful spectra additionally exclude `PROGRAM == 'other'`.

The page also records a 2026-07-21 patch to `desi_dr1.zpix` and `desi_dr1.ztile` correcting `desiname` formatting for RA/Dec values very close to zero. Retrieval dates must therefore remain part of provenance even though that patch does not currently alter the P5 environment-label logic.

## Primary table — `desi_dr1.zpix`

### Operational fields

| Field | Operational meaning in this pipeline | Status / rule |
|---|---|---|
| `targetid` | DESI target identifier and intended cross-table join key. Preserve in all row-level derived outputs. | Required; join cardinality must still be checked for each VAC. |
| `mean_fiber_ra` | Mean fiber right ascension associated with the coadded `zpix` spectrum. Used by smoke-query v0.1 as the documented positional RA field. | Required for current smoke query; do not silently call this target RA. |
| `mean_fiber_dec` | Mean fiber declination associated with the coadded `zpix` spectrum. Used by smoke-query v0.1 as the documented positional Dec field. | Required for current smoke query; do not silently call this target Dec. |
| `z` | DESI spectroscopic redshift. Used for redshift cuts, shelling, and later neighborhood/distance construction. | Required. |
| `zwarn` | Redshift warning bit mask. Baseline reliable sample requires `0`, consistent with the Data Lab useful-spectrum definition. | Required baseline filter. |
| `spectype` | Redrock spectral class. Baseline environment sample restricts to `GALAXY`. | Required baseline filter. |
| `healpix` | HEALPix grouping for the coadded spectrum. Useful for partitioning and sanity checks; not itself an environment label. | Required for planned output/support checks. |
| `zcat_primary` | Primary redshift-catalog row selector used to retain the primary/unique useful spectrum representation. | Require `true`. |
| `objtype` | Fiber/object type. Data Lab useful-spectrum definition uses `TGT` to select targets and exclude non-target/sky rows. | Require `TGT`. |
| `survey` | DESI survey phase. P5 baseline smoke query is restricted to the Main Survey. | Require `main` for baseline. |
| `program` | DESI observing program (`dark`, `bright`, `backup`, `other`, etc.). Data Lab excludes `other` for Main Survey useful spectra. | Require `<> 'other'` for baseline. |

### Coordinate-name correction relative to the original planning text

The original DESI query plan used normalized planning names `target_ra` and `target_dec`. Current Data Lab examples/documentation support `mean_fiber_ra` and `mean_fiber_dec` for `desi_dr1.zpix`, and the staged smoke query therefore uses those actual fields.

This distinction must remain explicit:

```text
source coordinates for smoke query v0.1:
  desi_dr1.zpix.mean_fiber_ra
  desi_dr1.zpix.mean_fiber_dec
```

A later derived environment catalog may expose normalized fields such as `target_ra` / `target_dec` only if their provenance is recorded explicitly. If true target-coordinate fields are required for the Pantheon+ interface, their exact source table/columns must be verified rather than inferred from the mean-fiber coordinates.

## Baseline reliable-galaxy filter

The staged baseline is:

```sql
WHERE zcat_primary = true
  AND objtype = 'TGT'
  AND zwarn = 0
  AND spectype = 'GALAXY'
  AND survey = 'main'
  AND program <> 'other'
```

The current smoke query additionally uses:

```sql
AND z BETWEEN 0.01 AND 0.5
```

plus a deliberately tiny sky patch and `LIMIT 25`.

SQL identifiers are currently written in the lowercase form accepted by the staged Data Lab query. If live execution shows a schema or syntax mismatch, execution must stop and the contract/query must be corrected explicitly rather than silently altered.

## Value-added catalog — `desi_dr1.stellar_mass_emline`

### Role

Optional galaxy-maturity / stellar-mass / emission-line proxy layer for later redshift-controlled comparisons. It is not required for the first `zpix` smoke query and is not part of the environment definition unless a later methodology explicitly adopts selected fields.

### Join key

Planned join key:

```text
targetid
```

Join cardinality is **NOT YET VERIFIED**. Before production use, test whether a selected `zpix.targetid` maps one-to-one, one-to-zero/one, or one-to-many in this VAC.

### Field-selection boundary

Do not use `SELECT *` in a production reproducibility query. Stellar-mass, emission-line, reliability, uncertainty, and any array-valued fields must be selected only after live schema inspection establishes exact names, units, descriptions, null behavior, and reliability flags.

Earlier planning material mentioned possible `xj_sl` array handling. That exact field and its storage/serialization semantics remain **UNVERIFIED IN THE CURRENT AUTHORITATIVE PAGE REVIEW** and must not be treated as locked until TAP/Data Explorer metadata confirms it.

## Value-added catalog — `desi_dr1.emfit`

### Role

Optional emission-line / star-formation / spectral-state proxy layer for later controlled comparisons.

The current Data Lab DESI page describes `emfit` as emission-line flux and width measurements for low-redshift DESI DR1 sources with:

```text
z <= 0.45
```

This applicability boundary must be respected when the VAC is used.

### Join key

Planned join key:

```text
targetid
```

Join cardinality is **NOT YET VERIFIED**.

### Field-selection boundary

Exact line-flux, line-width, uncertainty/error, component, and quality columns must be chosen only after schema inspection. Do not infer names from generic emission-line conventions and do not use `SELECT *` in a production reproducibility query.

## Planned schema-verification query

The preferred TAP metadata inspection is conceptually:

```sql
SELECT
  table_schema,
  table_name,
  column_name,
  datatype,
  description
FROM tap_schema.columns
WHERE table_schema = 'desi_dr1'
  AND table_name IN ('zpix', 'stellar_mass_emline', 'emfit')
ORDER BY table_name, column_name;
```

This query is **PLANNED / NOT YET EXECUTED** in the current environment. TAP metadata implementations can vary in exposed column names. If Data Lab's live TAP schema uses different metadata-field names, record the corrected query and its retrieval date rather than silently treating this draft as executed.

At minimum, archive or summarize the metadata for:

```text
zpix:
  targetid
  mean_fiber_ra
  mean_fiber_dec
  z
  zwarn
  spectype
  healpix
  zcat_primary
  objtype
  survey
  program

stellar_mass_emline:
  targetid
  selected stellar-mass fields
  selected emission-line proxy fields
  uncertainty / reliability fields
  any array-valued fields actually used

emfit:
  targetid
  selected line-flux fields
  selected line-width fields
  uncertainty/error fields
  quality/component fields actually used
```

## Tiny smoke-query readiness criteria

The existing staged query is:

```text
data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql
```

It may be treated as a successful plumbing check only when all of the following are true:

1. every required `zpix` column in the query is accepted by the live service;
2. the reliable-galaxy filter executes without schema/syntax failure;
3. the tiny sky patch returns a nonzero row count, or a zero count is explicitly diagnosed and the patch changed transparently;
4. `mean_fiber_ra`, `mean_fiber_dec`, and `z` values are finite and fall in the requested ranges;
5. `zwarn`, `zcat_primary`, `objtype`, `survey`, `program`, and `spectype` satisfy the requested cuts;
6. `healpix` is present and usable;
7. returned data types/null behavior are inspected;
8. the exact query, release, retrieval date, row count, and any exported smoke artifact/checksum are archived or summarized.

A smoke query tests plumbing only. It is not an environment measurement.

## Derived environment-label schema dependency

Current source-to-derived mapping is:

```text
targetid              <- zpix.targetid
target_ra             <- normalized derived coordinate with explicit source provenance;
                         smoke v0.1 source is zpix.mean_fiber_ra
target_dec            <- normalized derived coordinate with explicit source provenance;
                         smoke v0.1 source is zpix.mean_fiber_dec
z                     <- zpix.z
healpix               <- zpix.healpix
redshift_shell        <- derived from z
local_density         <- derived by the selected estimator
density_percentile    <- derived by shell-controlled density ranking
environment_bin       <- derived from quantitative density/classification method
environment_method    <- estimator/classifier name and version
query_version         <- query provenance string
source_release        <- DESI DR1
quality_flags         <- derived from filters, missingness, edge checks, and validation
```

The normalized names `target_ra` and `target_dec` must not erase the distinction between target coordinates and mean-fiber coordinates. The coordinate source used for the eventual Pantheon+ crossmatch must be explicitly frozen before crossmatching begins.

## Current gate status

```text
DESI DR1 resource existence: VERIFIED
zpix useful-spectrum semantics: VERIFIED FROM DATA LAB DOCUMENTATION
zpix smoke-query coordinate fields: LOCKED TO mean_fiber_ra / mean_fiber_dec
baseline reliable-galaxy filter: LOCKED FOR SMOKE QUERY
live data-type/null inspection: PENDING
stellar_mass_emline exact selected fields: PENDING LIVE SCHEMA INSPECTION
stellar_mass_emline join cardinality: PENDING
emfit exact selected fields: PENDING LIVE SCHEMA INSPECTION
emfit join cardinality: PENDING
smoke SQL: READY / NOT YET RUN
```

The optional VAC details do not block the first `zpix`-only smoke query. They do block later VAC joins and any analysis that depends on those fields.

## Claim boundary

This document locks data semantics and unresolved verification requirements. It creates no empirical evidence for SoCT/PNT and no DESI environment result.

It does not establish that:

- DESI proves SoCT or PNT;
- gravity is memory;
- dark matter is memory;
- any particular galaxy lies in a void or filament;
- `H0_void > H0_filament` has been measured;
- the Hubble tension is solved.

DESI remains a planned, reproducible environment/cosmic-web scaffold for later Pantheon+ testing.

## Next step

Run only the staged 25-row `zpix` smoke query and archive its schema/provenance result. Do not implement the environment estimator or generate environment labels until that plumbing check is complete.