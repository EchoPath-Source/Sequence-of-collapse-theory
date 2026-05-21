# Pantheon+ Data Notes

**Status:** Scaffold / pending data import

This folder is reserved for Pantheon+ supernova data notes, covariance documentation, environment-label schemas, and small derived result summaries for the SoCT environment-dependent H0 test.

## Current Role

The Pantheon+ track tests the expansion-side prediction of the collapse-memory model:

```text
H0_void > H0_filament
```

Primary statistic:

```math
Delta H0 = H0_void - H0_filament
```

## Expected Files

```text
data/pantheon/
├─ README.md
├─ covariance-notes.md
├─ environment-labels-schema.md
├─ source-notes.md
├─ environment_labels.csv              # derived cross-match table, if appropriate
└─ results/
   ├─ h0-environment-fit-summary.md
   ├─ permutation-test-summary.md
   └─ jackknife-summary.md
```

## Required Provenance Before Data Import

Before committing any Pantheon+ table or covariance artifact, document:

- exact Pantheon+ release/version;
- source URL or DOI;
- citation requirement;
- whether redistribution is allowed;
- any columns removed or renamed;
- redshift cut used;
- matching between covariance row order and SN table row order.

## Environment Cross-Match Requirement

Environment labels should be created outside the raw Pantheon table and stored as a separate derived table with a documented method.

Required columns are described in:

```text
data/pantheon/environment-labels-schema.md
```

## Claim Boundary

This folder currently contains schema and provenance scaffolding only. No real-data Pantheon+ environment-H0 result should be claimed until the covariance-aware fitting notebook and cross-match output are committed.
