# Observations data folder

This folder is intended to hold reproducibility artifacts for Sequence of Collapse observational tests.

## Current dataset referenced by the repository
### SPARC / WISE matched residual dataset
Working local artifact name:
- `sparc_wise_fdm_with_Q_and_radii.csv`

## Column meanings
- `Galaxy` — SPARC galaxy identifier
- `fDM_outer_mean` — mean apparent dark residual over the outer 25 percent of measured radii
- `fDM_last` — apparent dark residual at the outermost measured point
- `bulge_frac_outer` — outer bulge contribution fraction used for disk-dominated filtering
- `npts` — number of usable rotation-curve sample points
- `logL`, `logM`, `e_M`, `gW1`, `ML` — WISE luminosity, stellar mass, mass error, color proxy, and mass-to-light ratio
- `Reff`, `Rdisk`, `SBeff`, `Q` — SPARC structural and quality metadata
- `fDM_2Reff` — interpolated residual at `2 Reff`
- `fDM_2p2Rdisk` — interpolated residual at `2.2 Rdisk`

## Status
The repository already contains the analysis summary note in:
- `docs/observations/sparc-wise-color-residual-analysis-summary.md`

If the raw CSV is not yet present in this folder, it should be added in the next import batch together with any plotting scripts or notebooks.
