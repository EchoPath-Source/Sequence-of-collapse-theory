# DESI Notebook / Estimator Workspace

## Purpose

This directory contains the staged implementation for the DESI DR1 environment-label pipeline used by the P5 Hubble-tension / memory-gradient track.

Canonical implementation plan:

```text
notebooks/desi/DESI_ENVIRONMENT_NOTEBOOK_PLAN.md
```

## Current implementation

### Environment estimator prototype

```text
notebooks/desi/desi_environment_estimator.py
```

Status:

```text
IMPLEMENTED AS SYNTHETIC / GENERIC CARTESIAN PROTOTYPE
NOT YET RUN ON LIVE DESI DATA
```

The prototype provides:

- deterministic fixed-width redshift shell assignment;
- k-nearest-neighbor density on precomputed Cartesian coordinates;
- within-shell midrank density percentiles;
- versioned candidate percentile environment bins;
- small-shell and undefined-density quality flags;
- CSV input/output helpers;
- deterministic synthetic self-test.

It intentionally does **not** perform RA/Dec/redshift-to-Cartesian conversion. The production coordinate/cosmology contract must be selected and documented separately after the DESI smoke query validates the live coordinate/redshift fields.

### Tests

```text
notebooks/desi/test_desi_environment_estimator.py
```

The regression tests cover:

- percentile midranks;
- candidate bin thresholds;
- shell boundaries;
- insufficient-neighbor behavior;
- dense-versus-sparse synthetic recovery.

Intended commands:

```bash
python notebooks/desi/desi_environment_estimator.py --self-test
python -m unittest notebooks/desi/test_desi_environment_estimator.py
```

## Candidate method version

```text
desi-knn-shell-v0.1
```

Current default exploratory settings:

```text
redshift shell width = 0.02
k = 5 neighbors
minimum shell size = 20
void_like <= 10th percentile
low_density <= 30th percentile
sheet_like <= 70th percentile
filament_like <= 90th percentile
cluster_like > 90th percentile
```

These settings are **candidate defaults, not frozen production choices**. Production use requires sensitivity testing and survey-edge treatment.

## Live-data gate

The staged DESI DR1 smoke query remains the production gate:

```text
data/desi/DESI_DR1_SMOKE_QUERY_v0_1.sql
data/desi/DESI_DR1_SMOKE_EXECUTION_STATUS.md
```

Current runtime status:

```text
smoke SQL: READY
live execution: BLOCKED BY CURRENT RUNTIME DNS/NETWORK
live rows: NOT GENERATED
```

The prototype may be developed and tested synthetically while that gate is blocked, but it must not be promoted to a DESI result until live schema and row behavior are verified.

## Remaining implementation sequence

```text
1. Successful live 25-row DESI smoke retrieval.
2. Validate returned schema, values, nulls, and quality predicates.
3. Test VAC join cardinality where needed.
4. Freeze production redshift shell sensitivity grid.
5. Freeze RA/Dec/z -> neighborhood-coordinate method and fiducial cosmology if applicable.
6. Add survey footprint / edge correction.
7. Compare kNN with at least one alternative density estimator.
8. Freeze percentile normalization and environment thresholds.
9. Generate a small real-data environment smoke export.
10. Run quality and sensitivity checks.
11. Scale to full environment labels.
12. Crossmatch Pantheon+ only after the label layer is stable.
```

## Claim boundary

The estimator code is infrastructure, not evidence. Synthetic recovery only shows that the implementation responds correctly to deliberately dense and sparse toy point clouds. It does not establish that DESI contains the predicted environment pattern, that `H0_void > H0_filament`, or that SoCT/PNT is supported.
