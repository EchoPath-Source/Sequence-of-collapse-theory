# P6 paired BGS_ANY random-density convergence audit

2026-11-25 UTC. PR37 merged at 06423784cf318df3755055ca8233bac0df435de6. Executed the same outcome-blind BGS weighted density estimator with the 1% and 5% random files at identical mask-covered CF4 group centers. Scope: CF4 groups only, not Pantheon or CF4 individual galaxies. No measured distance moduli or peculiar velocity residuals read.

## Reproduction and method

    python -m unittest discover -s notebooks/desi -p test_density_convergence.py -v
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/density_convergence.py STAGED RAW MASK1 MASK2 MASK3

Four new synthetic tests passed locally. Real-data run completed at all three apertures. Local execution used a compact equivalent coverage_overlap helper with the same FITS reader, nested indexing, center check and coordinate integration as prior diagnostics; committed helper not independently rerun in this pass. The 1% and 5% input byte provenance is in P6_COVERAGE_PRODUCTS_INTAKE.md and P6_CF4_UNCERTAINTY_AND_RANDOM_BLOCK_AUDIT.md.

Use BGS_ANY galaxy data, [.01,.24] redshift range, WEIGHT not FKP, separate normalization by cap, PHOTSYS and .02 redshift shells before DONE mask restriction (same rule as PR35). Identical data numerator for both random samples at each center. CF4 Vcmb/c in [.01,.15]. Fixed radii 10/20/30 h^-1 Mpc. Nested Sobol 1024/2048 geometric coverage >=.80, normalized random N_eff>=25. These are exploratory gates, not frozen science thresholds. 5% block support calculated assuming sequential delivered 1000-row blocks match the selected source blocks. No source block IDs or selection manifest supplied. Effective block count is a concentration proxy, not independent N. >=10 is a sensitivity threshold only. No independent selection-function realization.

FP-only proxy: positive FP count and positive finite reported FP error; no positive counts for cal, tf, snIa, sbfo, sbfi and no positive snII error. Missing other counts treated as nonpositive for this proxy, not proof of an underlying homogeneous measurement. Confirm catalog selection and calibrations before modeling.

## Executed support counts

5008 covered CF4 groups; 4149 satisfy FP-only metadata proxy.

| Radius | Geometry eligible | 1% N_eff>=25 | 5% N_eff>=25 | Common | 5% FP | 5% block N_eff>=10 | 5% FP and block N_eff>=10 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2782 | 0 | 488 | 0 | 404 | 75 | 32 |
| 20 | 1514 | 200 | 1508 | 200 | 1483 | 320 | 306 |
| 30 | 821 | 821 | 821 | 821 | 815 | 691 | 688 |

Block gate counts differ slightly from PR37 because alpha-normalized weights are used here, rather than raw WEIGHT.

## Paired density results

For finite pairs with positive sum of ratios, symmetric discrepancy = 2*abs(rho5-rho1)/(rho5+rho1); median signed log ratio calculated on strictly positive pairs. Rank correlation is Spearman, not a precision estimate or hypothesis test. Max block share is the largest contribution of a delivered block to the 5% normalized denominator. All density ratios are dimensionless tracer contrasts.

| Radius | Subset | Pairs | Spearman | Median symmetric discrepancy | P90 discrepancy | Median log(5%/1%) | Median max block share |
|---|---|---:|---:|---:|---:|---:|---:|
| 10 | common support | 0 | — | — | — | — | — |
| 10 | 5% gate, finite 1% ratio | 486 | .7114 | .4628 | 1.2528 | -.4445 | .2706 |
| 20 | common support | 200 | .8948 | .1501 | .4065 | .0869 | .1365 |
| 20 | common FP | 193 | .8930 | .1529 | .4090 | .0858 | .1380 |
| 20 | common and 5% block>=10 | 128 | .9372 | .1172 | .2851 | .0498 | .1168 |
| 20 | 5% gate, finite 1% ratio | 1508 | .7717 | .2409 | .6010 | -.0015 | .1975 |
| 30 | common support | 821 | .8008 | .2134 | .4193 | .0165 | .1091 |
| 30 | common FP | 815 | .8003 | .2129 | .4196 | .0165 | .1090 |
| 30 | common and 5% block>=10 | 691 | .8350 | .1879 | .4033 | -.0424 | .1036 |

The 10 Mpc/h comparison is not converged. At 20 Mpc/h common supported centers agree better than the larger 5%-only eligible population; the latter has substantial sampling differences, and the shared gate selects a subset of the same spatial distribution. At 30 Mpc/h stronger block support retains more FP groups but does not establish convergence. Both samples share source random index 0 and are not independent realizations. Neither is treated as ground truth. No threshold/radius is promoted on this basis.

## Next gate

1. Obtain the compact 5% sampling JSON, sampler, source block IDs and ordering information from Muse (no further large download). Verify source block design before uncertainty estimation.
2. Define an outcome-blind precision target for the density proxy linked to the planned effect size; investigate design-aware random support, angular/radial selection fidelity and an independent spatially dispersed random projection if necessary. Evaluate sensitivity at fixed scales, not maximize apparent effect.
3. Use only the preselected FP metadata to derive error-only design bounds and spatial-correlation sensitivity, keeping the original void-vs-filament prediction separate from the complementary continuous-density test. A standardized density slope or contrast needs its own quantitative prediction and protocol; the original 1–3 km/s/Mpc void-filament prediction cannot simply be transplanted. Resolve FP source selection, calibration, peculiar-velocity modeling, covariance and aperture overlap. No power conclusion from candidate row counts alone.
4. No science fits, final environment labels or P6 claim before protocol lock. Existing mask/source verification and positive filament classification remain open.

Raw data stay external.
