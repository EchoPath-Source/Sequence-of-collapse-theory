# DESI DR1 Smoke Execution Record

**Query version:** `desi-dr1-smoke-v0.1`  
**Canonical SQL:** `data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql`  
**Runner:** `data/desi/run_desi_dr1_smoke.py`

## Purpose

Record the first successful live execution of the canonical 25-row DESI DR1 smoke query before any estimator, environment labels, Pantheon+ crossmatch, or H0 analysis.

This file must contain observed values only. Do not populate it from documentation or simulated rows.

## Execution command

```bash
python data/desi/run_desi_dr1_smoke.py
```

The runner uses anonymous synchronous HTTP access to the NSF NOIRLab Astro Data Lab Query Manager and requires only the Python standard library.

## Current execution status

```text
READY / NOT YET EXECUTED FROM A NETWORK-ENABLED RUNTIME
```

Attempt from the ChatGPT container on 2026-08-13:

```text
FAILED BEFORE SERVICE CONTACT
reason: DNS resolution unavailable for datalab.noirlab.edu in the container runtime
```

This is an environment/network failure, not a DESI query failure.

## Required successful-run record

Populate from the generated provenance JSON and returned CSV only after a live run succeeds.

```text
execution_timestamp_utc: PENDING
service_root: https://datalab.noirlab.edu/query
profile: default
execution_mode: anonymous synchronous HTTP
http_status: PENDING
row_count: PENDING
csv_sha256: PENDING
sql_sha256: PENDING
```

### Returned columns

Expected, but not yet live-confirmed:

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

Live result:

```text
PENDING
```

### Row-level validation

After execution, verify and record:

- all rows satisfy `zcat_primary = true`;
- all rows satisfy `objtype = 'TGT'`;
- all rows satisfy `zwarn = 0`;
- all rows satisfy `spectype = 'GALAXY'`;
- all rows satisfy `survey = 'main'`;
- no row has `program = 'other'`;
- all redshifts lie in `0.01 <= z <= 0.5`;
- all `mean_fiber_ra` values lie in `[55.5, 56.5]`;
- all `mean_fiber_dec` values lie in `[-9.5, -8.5]`;
- note any nulls, sentinels, unexpected encodings, or data-type surprises.

## Generated artifacts

Successful execution should create locally:

```text
data/desi/desi_dr1_smoke_v0_1.csv
data/desi/desi_dr1_smoke_v0_1.provenance.json
```

Do not commit the CSV automatically. Review its size, licensing/provenance, row content, and whether retaining the tiny snapshot adds reproducibility value before committing it.

The provenance JSON may be committed after successful execution if it contains no credentials or sensitive information.

## Gate to next step

Do not begin the production environment estimator until this record confirms:

```text
live row retrieval: PASS
expected columns: PASS
quality predicates: PASS
coordinate bounds: PASS
redshift bounds: PASS
```

Once those pass, proceed to VAC join-cardinality smoke tests, then the density/environment estimator.

## Claim boundary

A successful smoke query establishes access and schema behavior only. It is not evidence for an environment effect, `H0_void > H0_filament`, SoCT, PNT, gravitational memory, or a dark-sector mechanism.
