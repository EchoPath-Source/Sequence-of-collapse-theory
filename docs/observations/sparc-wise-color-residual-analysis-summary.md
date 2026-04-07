# SPARC / WISE color-dependent residual analysis

This note summarizes the public-data analysis run on SPARC rotation-curve decomposition files cross-matched to WISE stellar-mass / color data.

## Residual definition
For each radius point:
`fDM(r) = 1 - (Vgas^2 + Vdisk^2 + Vbulge^2) / Vobs^2`

Summary metrics tested:
- outer mean over the last 25 percent of measured radii
- outermost point
- interpolated value at `2 Reff`
- interpolated value at `2.2 Rdisk`

## Headline result
Across the SPARC / WISE overlap sample, the apparent dark residual shows a strong negative correlation with `g-W1`, and the signal strengthens when restricting to:
- SPARC `Q = 1` high-quality curves
- disk-dominated systems with low outer bulge contribution

## Strongest subset result
Disk-dominated + `Q = 1`:
- outer-mean residual vs `g-W1`
- Pearson `r = -0.588`, `p = 2.0e-6`
- Spearman `rho = -0.637`, `p = 1.30e-7`

## Robustness
The effect persists for:
- outermost-point residual
- residual at `2 Reff`
- residual at `2.2 Rdisk`

Mass-binned and partial-correlation checks indicate that stellar mass explains a large share of the covariance, but the color proxy still carries non-random structure.

## Caution
This is a phenomenological result. `g-W1` is a formation / stellar-population proxy, not a direct cosmological age measurement. Interpretation should remain conservative.

## Repository artifacts
- `docs/observations/data/sparc_wise_fdm_with_q_and_radii.csv`
