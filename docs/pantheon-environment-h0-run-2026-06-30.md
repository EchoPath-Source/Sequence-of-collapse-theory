# Pantheon+ environment-H0 covariance-aware run note — 2026-06-30

## Status

**BLOCKED by missing local raw/covariance inputs.** The covariance-aware runner was added at `notebooks/pantheon/run_pantheon_environment_h0_analysis.py` and executed in the repository container. It exited cleanly and wrote `observations/pantheon-environment-h0/results/pantheon_environment_h0_run_summary.md` instead of producing a stack trace.

## Local input state

The derived label artifact `data/pantheon/environment_labels.csv` is present with 1701 row-aligned Pantheon+ rows and checksum `ff3006e8cbf7316db29b3760f39d02e911b99a86e814e1a698014a8242695a9d`.

The following raw/staged inputs were not present in this container run and remain external/ignored by policy:

- `data/pantheon/raw/Pantheon+SH0ES.dat`
- one covariance candidate, preferably `data/pantheon/raw/Pantheon+SH0ES_STAT+SYS.cov`

## Validation status

Because the raw Pantheon+ table and covariance were missing, the runner could not validate:

- Pantheon row count = 1701;
- covariance shape = `(1701, 1701)`;
- row-order safety for `CID`, `RA`, `DEC`, `zHD`, and `zCMB`;
- redshift-cut group counts;
- underpowered contrast skip behavior on live data.

The script is configured to perform those validations before fitting whenever the raw inputs are available.

## Expected grouping behavior

The runner predeclares these grouping modes before fitting:

1. strict `void` vs `filament`;
2. edge-inclusive `void` + `near_void_edge` vs `filament` + `near_filament`;
3. structure contrast `void` + `near_void_edge` vs `filament` + `near_filament` + `field_or_wall` + `sdss_nonvoid`;
4. catalog-covered contrast `void_like` vs `nonvoid_covered` using the same covered nonvoid labels.

Any grouping with fewer than 5 rows on either side after the locked `0.01 <= zHD <= 0.15` cut is marked `SKIPPED_UNDERPOWERED` and is not used for a primary claim.

## Generated artifacts in this pass

- `notebooks/pantheon/run_pantheon_environment_h0_analysis.py`
- `observations/pantheon-environment-h0/results/pantheon_environment_h0_run_summary.md`

No fit CSV tables were generated because the run was blocked before data loading and fitting.

## Claim boundary

This is a preliminary covariance-aware pipeline execution using derived SDSS void + Tempel/Bisous filament cross-match labels. It does not establish a Pantheon H0/environment detection. Results are candidate diagnostics only until the raw input provenance, covariance handling, grouping choices, and independent reproducibility audit are complete.
