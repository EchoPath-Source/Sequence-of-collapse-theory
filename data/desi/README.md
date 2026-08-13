# DESI Data Staging and Reproducibility Contract

## Purpose

This directory defines the data-staging and reproducibility rules for DESI use in the P5 Hubble-tension / memory-gradient track.

Canonical DESI plan:

```text
papers/p5-hubble-tension-memory-gradient/DESI_ENVIRONMENT_QUERY_PLAN.md
```

Notebook implementation plan:

```text
notebooks/desi/DESI_ENVIRONMENT_NOTEBOOK_PLAN.md
```

Schema, semantics, staged smoke query, and execution status:

```text
data/desi/DESI_DR1_SCHEMA_VERIFICATION.md
data/desi/DESI_DR1_COLUMN_SEMANTICS.md
data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql
data/desi/DESI_DR1_SMOKE_EXECUTION_STATUS.md
```

DESI is used here as an environment and cosmic-web scaffold that may support later Pantheon+ crossmatching. This directory does not contain evidence that SoCT/PNT is correct, and no DESI-derived empirical claim should be made before the documented staging, verification, labeling, and crossmatch steps are completed.

## DESI role in the repository

DESI may support construction of reproducible galaxy-density and environment labels such as void-like, sheet-like, filament-like, and cluster-like classifications.

The intended sequence is:

```text
DESI schema verification
  -> small query validation
  -> reproducible sample definition
  -> density estimation
  -> environment classification
  -> environment-label export
  -> Pantheon+ coordinate crossmatch
  -> later covariance-aware H0 analysis
```

No large-scale DESI analysis should begin until the schema, provenance, and output contract in this document are satisfied.

## Data provenance policy

Every DESI-derived artifact committed to this repository should record enough provenance to reproduce its origin.

At minimum, record:

- DESI data release and sub-release where applicable;
- source service or catalog endpoint;
- source table names;
- query text or query-script version;
- query date;
- sample cuts;
- join keys;
- coordinate conventions;
- redshift range;
- environment-classification method;
- software/notebook version;
- any filtering or quality-mask logic applied after retrieval.

Provenance should live in the notebook, a companion metadata file, or both. Derived CSVs should never appear without a documented path back to their source query and transformation logic.

## Data-release and version pinning

Production work must pin the DESI release explicitly.

Current planning target:

```text
DESI DR1
```

Do not use an unversioned description such as "current DESI catalog" in a reproducibility record.

If a table, column, value-added catalog, or selection definition changes across releases, update the relevant query/notebook version and preserve the earlier provenance record rather than silently replacing it.

## NOIRLab Data Lab schema verification

Before any production query is treated as valid, verify the expected DESI DR1 tables and columns against current NSF NOIRLab Astro Data Lab documentation and, where possible, live schema/query metadata.

Current verification records:

```text
data/desi/DESI_DR1_SCHEMA_VERIFICATION.md
data/desi/DESI_DR1_COLUMN_SEMANTICS.md
```

The verified planning resources include:

```text
desi_dr1.zpix
desi_dr1.photometry
desi_dr1.stellar_mass_emline
desi_dr1.emfit
desi_dr1.agngal
```

The first staged smoke query uses documented `zpix` fields including `mean_fiber_ra` and `mean_fiber_dec`; it preserves those semantics rather than silently relabeling them as target coordinates.

A schema mismatch during execution is a blocking condition, not a reason to silently rewrite the analysis.

## Raw-versus-derived policy

### Raw data

Do not commit large DESI raw catalogs, bulk spectra, or survey-scale downloads to this repository.

Raw or externally staged material should remain outside version control unless it is intentionally tiny, redistribution-safe, and necessary for a reproducible smoke test.

For any non-committed external input, record:

- source URL/service;
- data release;
- retrieval command/query;
- retrieval date;
- expected file name;
- checksum where feasible.

### Derived data

Small, reproducible derived artifacts may be committed when they are useful for validation or paper reproducibility and can be regenerated from documented inputs and code.

Derived artifacts should be clearly labeled as one of:

```text
SMOKE_TEST
PRELIMINARY
REPRODUCIBLE_DERIVED
PUBLICATION_CANDIDATE
```

No derived artifact should be labeled publication-grade until the full methodology, quality checks, and claim boundary are satisfied.

## Query provenance requirements

Every query used beyond ad hoc exploration should have a stable provenance record.

Recommended fields:

```text
query_version
source_release
source_tables
query_text_or_script
query_date
row_limit
sky_region
redshift_range
quality_cuts
join_keys
post_query_filters
```

When query logic changes materially, increment `query_version` and preserve the previous version in repository history.

## Checksum policy

Use checksums where feasible for external files, staged snapshots, or committed smoke-test artifacts.

Preferred checksum:

```text
SHA-256
```

Checksums are especially important when:

- a downloaded file is not committed to the repository;
- a Pantheon+ crossmatch depends on row-stable external input;
- a small DESI snapshot is used as a regression or smoke-test fixture;
- an externally hosted catalog may be updated in place.

For live SQL query results that are expected to be regenerated rather than preserved, store the exact query/version and consider a checksum of the exported result when a stable snapshot is intentionally retained.

## Expected environment-label schema

The planned DESI environment-label catalog should use, at minimum, fields compatible with:

```text
targetid
target_ra
target_dec
z
healpix
redshift_shell
local_density
density_percentile
environment_bin
environment_method
query_version
source_release
quality_flags
```

Field meanings should be documented before the full catalog is generated. Any normalized `target_ra` / `target_dec` fields must retain explicit provenance to their actual DESI coordinate source.

### Candidate environment bins

Planned values:

```text
void_like
low_density
sheet_like
filament_like
cluster_like
unclassified
```

The final classification method must define quantitative boundaries for these labels. The labels must not be inferred from narrative SoCT/PNT terminology alone.

## Planned output locations

The following paths are reserved but are **PLANNED / NOT YET GENERATED**:

```text
data/desi/desi_dr1_environment_labels.csv
data/desi/desi_dr1_density_shell_summary.csv
figures/desi/desi_density_environment_map.png
notebooks/desi/desi_environment_density_map.ipynb
```

No file at these paths should be interpreted as existing until it is actually generated, validated, and committed.

## Smoke-test artifacts

The first executable DESI step is staged as:

```text
data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql
```

It is deliberately limited to 25 rows and is intended only to validate:

- table/column availability;
- documented quality cuts;
- coordinate fields;
- redshift handling;
- HEALPix field access;
- row retrieval;
- provenance capture.

The first live execution attempt is recorded in:

```text
data/desi/DESI_DR1_SMOKE_EXECUTION_STATUS.md
```

Current execution status:

```text
ATTEMPTED / BLOCKED BEFORE SERVICE CONTACT BY RUNTIME DNS/NETWORK
```

The observed blocker was inability of the current runtime to resolve `datalab.noirlab.edu`. No NOIRLab response was received and no query rows were generated. This must not be interpreted as a schema failure or empty-result condition.

The smoke query must not be used to estimate the final void/filament H0 differential or as evidence for any SoCT/PNT claim.

## Relationship to Pantheon+

The intended interface is:

```text
Pantheon+ SN coordinates
  -> DESI-derived environment-label layer
  -> coordinate/redshift crossmatch
  -> matched environment class + method metadata
  -> environment-stratified Pantheon+ analysis
```

Pantheon+ crossmatching must wait until:

1. DESI DR1 schema verification is complete;
2. the density/environment method is explicitly defined;
3. environment labels have been generated reproducibly;
4. DESI label quality checks pass;
5. the exported schema is stable enough for row-level crossmatch provenance.

Pantheon+ covariance handling, row-order validation, and H0 fitting remain separate downstream requirements tracked in:

```text
data/PANTHEON_IMPORT_STATUS.md
```

## Claim boundary

This directory defines a data contract and staging policy. It does not create empirical confirmation.

Safe framing:

> DESI may provide a reproducible galaxy-density and cosmic-web environment layer that can later be crossmatched to Pantheon+ for an environment-dependent H0 test.

Do not claim from this staging layer that:

- DESI proves SoCT;
- DESI proves PNT;
- gravity is proven to be memory;
- dark matter is proven to be memory;
- voids contain no dark matter;
- `H0_void > H0_filament` has been observed;
- the Hubble tension has been solved.

## Current status

```text
DESI data contract: PRESENT
DESI schema/documentation verification: COMPLETE FOR SMOKE-QUERY FIELD SELECTION
DESI column semantics contract: PRESENT
DESI live data-type/null verification: PENDING SUCCESSFUL SMOKE EXECUTION
DESI smoke query SQL: READY
DESI smoke execution attempt: BLOCKED BY RUNTIME DNS/NETWORK
DESI smoke query result: NOT GENERATED
DESI environment estimator: NOT YET IMPLEMENTED
DESI environment-label catalog: NOT YET GENERATED
Pantheon+ crossmatch: NOT YET RUN
H0 environment test: NOT YET RUN
```
