# DESI Environment Notebook Plan

## Purpose

This document locks the intended notebook sequence for DESI environment-label construction before implementation begins.

It is a planning and reproducibility artifact, not an analysis result.

Canonical query plan:

```text
papers/p5-hubble-tension-memory-gradient/DESI_ENVIRONMENT_QUERY_PLAN.md
```

Data-staging contract:

```text
data/desi/README.md
```

The notebook should eventually produce a reproducible DESI-derived environment layer that can be used for later Pantheon+ crossmatching. It must not skip directly from exploratory querying to H0 claims.

## Inputs

Planned inputs include:

- DESI DR1 spectroscopic galaxy data;
- verified table and column names from the current NOIRLab Data Lab schema;
- the exact SQL query or retrieval script version;
- documented sample cuts;
- cosmological coordinate-conversion assumptions if comoving coordinates are used;
- optional DESI value-added catalog fields for later controlled comparisons.

No large raw catalog should be committed to the repository as part of notebook development.

## Stage 1 — Schema verification

Before any production query:

1. verify the expected DESI DR1 tables;
2. verify required columns;
3. verify identifier behavior for `targetid`;
4. verify `zcat_primary`, `zwarn`, `spectype`, coordinate, redshift, and HEALPix fields where used;
5. verify any joinable value-added catalogs and their join keys;
6. record the schema verification date and release.

Expected resources from the planning document must be treated as assumptions until verified.

If table or column names differ from the plan, stop and update the query plan/data contract before scaling further.

## Stage 2 — Tiny sky-patch smoke query

Run a deliberately small query against a limited sky region or row count.

Purpose:

- confirm authenticated/access path;
- confirm schema assumptions;
- inspect returned coordinate and redshift fields;
- confirm galaxy quality cuts;
- validate query provenance capture;
- identify null/missing-value behavior.

The smoke test should not be interpreted statistically.

No conclusion about voids, filaments, PNT, SoCT, or H0 may be drawn from this stage.

## Stage 3 — Reliable galaxy sample cuts

Define the base selection explicitly before density work begins.

Candidate planning cuts from the DESI query plan include:

```text
zcat_primary = true
zwarn = 0
spectype = 'GALAXY'
0.01 <= z <= 0.5
```

These must be confirmed against the current schema and DESI documentation before production use.

Record:

- final redshift limits;
- quality flags;
- duplicate handling;
- primary-target logic;
- missing-value policy;
- row counts before and after each cut.

## Stage 4 — Redshift shelling

Define redshift shells before local-density estimation so redshift-dependent sampling density does not get conflated with environment.

The notebook should document:

- shell boundaries;
- shell widths;
- minimum objects per shell;
- edge treatment;
- whether shells are fixed-width, adaptive, or sensitivity-tested;
- why the chosen scheme is appropriate for the available sample.

Store the assigned shell in:

```text
redshift_shell
```

## Stage 5 — Coordinate handling

The notebook must explicitly define how sky position and redshift are converted into a neighborhood metric.

Candidate approaches include:

1. RA/Dec plus redshift-window angular neighborhoods;
2. approximate comoving Cartesian coordinates under a documented fiducial cosmology;
3. HEALPix-assisted sky partitioning combined with redshift shells;
4. another validated three-dimensional neighborhood construction.

Whichever method is chosen, document:

- angular units;
- redshift-to-distance assumptions;
- fiducial cosmological parameters if used;
- coordinate frame;
- periodicity assumptions, if any;
- survey-boundary handling.

The coordinate method must be methodological, not chosen to force an expected SoCT/PNT sign.

## Stage 6 — Local density estimator

Evaluate one or more reproducible density estimators before fixing the final method.

Candidate options:

- fixed-radius neighbor count;
- k-nearest-neighbor density;
- adaptive kernel density;
- Voronoi-based local density;
- shell-normalized angular/redshift density.

For each candidate, document:

- free parameters;
- sensitivity to sampling density;
- redshift dependence;
- survey-edge behavior;
- computational cost;
- robustness under small perturbations.

The selected estimator must populate:

```text
local_density
```

and be identified in:

```text
environment_method
```

## Stage 7 — Density percentile

Within the chosen redshift-control scheme, convert local density into a relative rank or percentile.

Store as:

```text
density_percentile
```

The notebook should specify whether percentiles are calculated:

- globally;
- within each redshift shell;
- within footprint subregions;
- or under another controlled normalization.

The choice must be documented before environment labels are generated at scale.

## Stage 8 — Environment classification

Assign environment labels only after the density metric and percentile normalization are fixed.

Candidate labels:

```text
void_like
low_density
sheet_like
filament_like
cluster_like
unclassified
```

The classification rule must be quantitative and versioned.

Do not assign labels solely because a region is narratively described as low-memory or high-memory in SoCT/PNT language.

The notebook must record:

- percentile or density thresholds;
- shell dependence, if any;
- ambiguity handling;
- unclassified policy;
- environment-method version.

## Stage 9 — Quality checks

Before any full export, run checks for:

- unexpected redshift-density trends;
- strong shell-size dependence;
- edge/footprint artifacts;
- duplicate targets;
- missing coordinates or redshifts;
- implausible density outliers;
- label instability under small parameter changes;
- excessive sensitivity to estimator choice;
- HEALPix or survey-geometry artifacts where relevant.

At minimum, generate a summary table of:

```text
redshift_shell
row_count
density_median
density_percentiles
environment_bin_counts
unclassified_fraction
quality_flag_counts
```

A failed quality check blocks scaling or crossmatching until understood.

## Stage 10 — Small smoke-test export

Before generating the full environment-label catalog, export only a small reproducible artifact.

The smoke-test export should validate:

- schema;
- serialization;
- provenance fields;
- environment-method identifiers;
- quality flags;
- downstream readability.

It should be clearly labeled:

```text
SMOKE_TEST
```

and must not be presented as the planned full catalog.

## Stage 11 — Full environment-label export

Only after schema verification, estimator selection, environment classification, and quality checks are stable should the notebook generate the planned catalog.

Expected schema:

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

Planned full output path:

```text
data/desi/desi_dr1_environment_labels.csv
```

Current status:

```text
PLANNED / NOT YET GENERATED
```

## Stage 12 — Pantheon+ coordinate-crossmatch interface

Pantheon+ crossmatching begins only after a reproducible DESI environment catalog exists.

The intended interface is:

```text
Pantheon+ SN RA/Dec/redshift
  -> DESI environment-label catalog
  -> documented spatial/redshift matching rule
  -> matched environment label
  -> match distance / confidence metadata
  -> unmatched or ambiguous status where necessary
```

The crossmatch layer should preserve enough metadata to audit every assignment.

Candidate crossmatch fields may include:

```text
pantheon_id
desi_match_targetid
angular_separation
redshift_separation
match_method
match_quality
environment_bin
environment_method
source_release
```

The final schema should be locked before any covariance-aware H0 fit.

## Expected diagnostic plots

Diagnostic figures should be generated only after the relevant stage exists and should be treated as validation aids unless explicitly promoted later.

Candidate plots:

- sky footprint of smoke-test galaxies;
- redshift distribution before/after cuts;
- local density versus redshift;
- density percentile distribution by shell;
- environment-bin counts by shell;
- map of environment labels for a small validation region;
- estimator-sensitivity comparison;
- survey-edge/quality-flag map.

Planned eventual figure path from the query plan:

```text
figures/desi/desi_density_environment_map.png
```

Current status:

```text
PLANNED / NOT YET GENERATED
```

## Failure modes and blocking conditions

Stop rather than silently continuing if any of the following occurs:

- expected table or column names do not match the live schema;
- join multiplicity is not understood;
- coordinate fields are inconsistent;
- redshift cuts produce unexpected or invalid rows;
- density estimates are dominated by redshift selection effects;
- survey boundaries create uncorrected false low-density regions;
- environment labels are unstable under modest parameter changes;
- query provenance cannot be reconstructed;
- smoke-test artifacts cannot be regenerated;
- Pantheon+ matches are ambiguous without a documented policy.

A failure or inconclusive stage should be recorded as such. It must not be reinterpreted as support for SoCT/PNT.

## Claim boundary

This notebook plan defines a future analysis sequence. It contains no DESI result and no Pantheon+ H0 result.

Safe framing:

> The notebook is designed to construct and validate a reproducible DESI environment-label layer before any downstream Pantheon+ test is attempted.

Do not claim from this plan that:

- DESI proves SoCT;
- DESI proves PNT;
- gravity is memory;
- dark matter is memory;
- voids are confirmed to have a higher H0;
- `H0_void > H0_filament` has been measured;
- the Hubble tension is solved.

## Locked implementation sequence

```text
1. Verify DESI DR1 table/column names against current NOIRLab Data Lab schema.
2. Run a tiny sky-patch query.
3. Confirm reliable galaxy cuts.
4. Define redshift shells.
5. Define coordinate/neighborhood handling.
6. Estimate local density.
7. Assign density percentile.
8. Bin environment.
9. Run quality checks.
10. Export only a small smoke-test artifact first.
11. Later scale to the full environment-label catalog.
12. Only after DESI labels exist, crossmatch Pantheon+ coordinates.
```
