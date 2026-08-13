# DESI Notebook / Estimator Workspace

## Purpose

This directory contains the staged implementation for the DESI DR1 environment-label pipeline used by the P5 Hubble-tension / memory-gradient track.

Canonical implementation plan:

```text
notebooks/desi/DESI_ENVIRONMENT_NOTEBOOK_PLAN.md
```

Production coordinate/neighborhood contract:

```text
data/desi/DESI_DR1_COORDINATE_NEIGHBORHOOD_CONTRACT.md
```

## Current implementation

### Comoving coordinate converter

```text
notebooks/desi/desi_comoving_coordinates.py
```

Status:

```text
IMPLEMENTED / DETERMINISTIC
NOT YET RUN ON LIVE DESI DATA
```

The converter provides:

- validated RA/Dec/redshift inputs;
- flat-Lambda-CDM line-of-sight comoving distance;
- deterministic composite-Simpson integration;
- RA/Dec/redshift -> comoving Cartesian `x`, `y`, `z_cart` conversion;
- explicit `Mpc` units;
- coordinate-method and fiducial-cosmology provenance columns;
- configurable `H0` / `Omega_m` for sensitivity tests;
- deterministic self-test.

Primary geometry version:

```text
desi-comoving-planck18-v0.1
H0 = 67.4 km/s/Mpc
Omega_m = 0.315
flat Lambda-CDM
```

This geometry is a neighborhood-coordinate convention, not a scientific conclusion about the final cosmology.

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

### Tests

```text
notebooks/desi/test_desi_comoving_coordinates.py
notebooks/desi/test_desi_environment_estimator.py
```

The coordinate tests cover:

- zero and monotonic comoving distance;
- Cartesian axis transforms at known RA/Dec orientations;
- north-pole transform;
- expected inverse `H0` scaling of comoving distance;
- invalid-coordinate rejection.

The estimator tests cover:

- percentile midranks;
- candidate bin thresholds;
- shell boundaries;
- insufficient-neighbor behavior;
- dense-versus-sparse synthetic recovery.

Intended commands:

```bash
python notebooks/desi/desi_comoving_coordinates.py --self-test
python notebooks/desi/desi_environment_estimator.py --self-test
python -m unittest discover -s notebooks/desi -p 'test_*.py'
```

## Candidate environment method version

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

These labels are **density-percentile environment bins**, not full topological cosmic-web classifications.

## Locked sensitivity grid

The coordinate/neighborhood contract requires testing:

```text
k = 3, 5, 10
shell width = 0.01, 0.02, 0.04
geometry = Planck18 baseline plus documented LCDM sensitivity cases
candidate threshold shifts around the baseline 10/30/70/90 percent bins
edge-coverage thresholds = 0.70, 0.80, 0.90 once random-catalog coverage exists
```

The purpose is to quantify label stability. Settings must not be selected by maximizing the downstream Pantheon+ H0 contrast.

## Survey-edge gate

A low DESI target count at a survey boundary, mask, hole, or incompleteness region must not be interpreted as a physical void.

The production contract therefore requires DESI DR1 LSS random catalogs or an equivalently documented footprint/completeness mask before the full environment-label layer is promoted.

Current status:

```text
edge/footprint correction: NOT YET IMPLEMENTED
full-sample void_like claims: BLOCKED
```

Objects that fail the eventual coverage threshold should default to an explicit quality flag and `unclassified` in the primary analysis.

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

The converter and estimator may be developed and tested deterministically while that gate is blocked, but neither may be promoted to a DESI empirical result until live schema and row behavior are verified.

## Remaining implementation sequence

```text
1. Successful live 25-row DESI smoke retrieval.
2. Validate returned schema, values, nulls, and quality predicates.
3. Test VAC join cardinality where needed.
4. Run live coordinate conversion against the smoke rows.
5. Implement DESI random-catalog / footprint coverage control.
6. Run the locked k/shell/cosmology/threshold sensitivity grid.
7. Compare kNN with at least one alternative density estimator.
8. Quantify label stability and select the production method without reference to Pantheon+ H0 outcome.
9. Generate a small real-data environment smoke export.
10. Run quality and sensitivity checks.
11. Scale to full environment labels.
12. Crossmatch Pantheon+ only after the label layer is stable.
```

## Claim boundary

The coordinate and estimator code are infrastructure, not evidence. Synthetic recovery only shows that the implementation responds correctly to controlled geometry and deliberately dense/sparse toy point clouds. It does not establish that DESI contains the predicted environment pattern, that `H0_void > H0_filament`, or that SoCT/PNT is supported.
