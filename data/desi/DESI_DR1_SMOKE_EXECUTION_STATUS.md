# DESI DR1 Smoke Execution Status

## Purpose

Record the first live execution attempt for the staged DESI DR1 smoke query without overstating what was achieved.

Canonical smoke query:

```text
data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql
```

Execution attempt date:

```text
2026-08-13
```

## Intended service

NSF NOIRLab Astro Data Lab Query Manager / Query Client.

Official documentation confirms that synchronous anonymous queries against public datasets are supported by the Query Manager API, and the Query Client submits SQL to the Data Lab query service.

The documented service root used by the current Query Client implementation is:

```text
https://datalab.noirlab.edu/query
```

with SQL submitted through the query endpoint.

## Query attempted

The exact staged query remained unchanged:

```sql
SELECT
  targetid,
  mean_fiber_ra,
  mean_fiber_dec,
  z,
  zwarn,
  zcat_primary,
  objtype,
  survey,
  program,
  spectype,
  healpix
FROM desi_dr1.zpix
WHERE zcat_primary = true
  AND objtype = 'TGT'
  AND zwarn = 0
  AND spectype = 'GALAXY'
  AND survey = 'main'
  AND program <> 'other'
  AND z BETWEEN 0.01 AND 0.5
  AND mean_fiber_ra BETWEEN 55.5 AND 56.5
  AND mean_fiber_dec BETWEEN -9.5 AND -8.5
LIMIT 25;
```

## Execution method attempted

A direct synchronous HTTP request was constructed against the documented Data Lab Query Manager endpoint using the same SQL and CSV output parameters expected by the Query Client.

The runtime attempted to resolve:

```text
datalab.noirlab.edu
```

before any SQL could be submitted.

## Result

```text
EXECUTION BLOCKED BEFORE SERVICE CONTACT
```

Observed runtime error:

```text
curl: (6) Could not resolve host: datalab.noirlab.edu
```

This is an execution-environment DNS/network limitation. It is not a DESI query failure, schema failure, empty-result condition, or scientific result.

No response was received from NOIRLab, so the following remain unverified by execution:

- live column availability;
- live data types;
- null/sentinel behavior;
- nonzero row count for the chosen patch;
- returned coordinate ranges;
- returned redshift ranges;
- exact server-side interpretation of the staged filters.

## What this attempt does establish

The smoke query is fully staged and the official NOIRLab documentation supports the intended access mode: synchronous queries of public data may be made anonymously through the Query Manager / Query Client stack.

The current blocker is local runtime connectivity, not an unresolved analysis decision.

## Required next action

Execute `data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql` from an environment with network access to NSF NOIRLab Astro Data Lab, for example:

- the Data Lab Jupyter Notebook server;
- a local environment with `astro-datalab` / `dl.queryClient` installed and network access;
- another TAP/Query Manager-capable client that can reach `datalab.noirlab.edu`.

For Query Client use, the intended pattern is equivalent to:

```python
from dl import queryClient as qc

sql = open('data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql').read()
res = qc.query(sql=sql)
print(res)
```

The returned 25-row-or-smaller result should be archived or summarized with:

- execution timestamp;
- source release;
- exact query version;
- row count;
- returned column names;
- representative ranges / null checks;
- any server error or schema mismatch;
- checksum if a stable smoke CSV is retained.

## Pipeline status

```text
DESI plan: COMPLETE
DESI data contract: COMPLETE
DESI notebook plan: COMPLETE
DESI DR1 resource verification: COMPLETE
DESI smoke-query column semantics: LOCKED FOR v0.1
DESI smoke SQL: READY
DESI smoke execution attempt: BLOCKED BY RUNTIME DNS/NETWORK
DESI smoke result: NOT GENERATED
DESI estimator: NOT IMPLEMENTED
DESI environment labels: NOT GENERATED
Pantheon+ crossmatch: NOT RUN
H0 environment test: NOT RUN
```

## Claim boundary

This execution-status note contains no DESI measurement and no SoCT/PNT evidence.

It does not show that:

- DESI proves SoCT or PNT;
- gravity or dark matter is memory;
- voids have a higher H0;
- `H0_void > H0_filament` has been measured;
- the Hubble tension has been solved.

The smoke-query stage remains a plumbing and reproducibility check only.
