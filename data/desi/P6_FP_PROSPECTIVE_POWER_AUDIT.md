# P6 complementary FP continuous-density prospective design audit

2026-11-25 UTC. PR38 merged at 752cf43a3531da3d249dd839c114249be479a37c. Outcome-blind. No measured modulus, distance, velocity residual or H0 outcomes read. Not the original void-versus-filament test; its 1–3 km/s/Mpc prediction is only a magnitude reference here, not a derived prediction for an interquartile tracer-density contrast.

## Method

Reuse PR38 weighted density, mask, redshift window, FP-only metadata proxy and exploratory point/block support gates. Positive finite density required for log transform. Separate each aperture and subset. Design columns: intercept, (ln rho - mean ln rho)/IQR(ln rho), centered z divided by .02, its square, and RA-based cap indicator if both caps represented. The slope is a model-implied modulus contrast between the 25th and 75th percentile of log tracer density, not a difference between fitted extreme-bin means. The IQR is sample- and random-product-specific; common-sample 1% and 5% slopes need not represent identical physical contrasts. Design includes only simple nuisance regressors, not a full calibration or selection model.

Use reported e_DMfp as diagonal Gaussian standard errors. Four fixed illustrative covariance scenarios: (A) reported errors alone; (B) add independent 300 km/s velocity dispersion; (C) independent 150 km/s plus spatially correlated 300 km/s, exponential correlation length 20 h^-1 Mpc; (D) same as C with 50 h^-1 Mpc length. Low-z linear conversion v_i=5/(ln(10)*c*z_i); covariance C_ij=delta_ij*(sigma_i^2+(v_i*s_ind)^2)+(v_i*s_corr)*(v_j*s_corr)*exp(-d_ij/L). This is a positive-definite sensitivity model, not a physically calibrated radial velocity covariance (no directional projection, survey window, coherent mean flow or verified CF4 error decomposition). Added dispersions may double-count error terms; interpret as stress scenarios only. GLS design covariance (X^T C^-1 X)^-1; use slope SE and normal approximation (1.95996+0.84162)*SE for two-sided alpha .05 and nominal 80% power. Convert magnitude to positive equivalent H increment at reference 70 via 70*(10^(2.8016*SE/5)-1). Negative increment has a different nonlinear magnitude. No actual fit, no p-values, no inferred effect.

## Executed results

MDE units km/s/Mpc, not measured H0 values.

| Radius | Support | N FP | Median reported error mag | IQR log density | Median other centers within 2R (excluding coincident coordinates) | A | B | C | D |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 20 | 5% | 1483 | .520 | .891 | 103 | 1.444 | 1.452 | 1.547 | 1.576 |
| 20 | 5% block>=10 | 306 | .500 | .555 | 38 | 2.903 | 2.954 | 3.034 | 3.016 |
| 20 | common, 5% density | 193 | .500 | .667 | 21 | 3.427 | 3.489 | 3.590 | 3.589 |
| 20 | common, 1% density | 193 | .500 | .648 | 21 | 3.638 | 3.720 | 3.826 | 3.803 |
| 30 | 5% | 815 | .520 | .797 | 213 | 2.716 | 2.728 | 2.862 | 2.905 |
| 30 | 5% block>=10 | 688 | .520 | .824 | 159.5 | 3.048 | 3.063 | 3.243 | 3.313 |
| 30 | common, 1% density | 815 | .520 | .576 | 213 | 2.495 | 2.504 | 2.608 | 2.616 |

30 common 5% identical to 30 full. Candidate counts are not independent sample size. Overlap count is descriptive of geometric proximity, not a covariance correction. Spatial velocity stress does not propagate shared aperture sampling errors or density measurement error. In particular, the 20 full result assumes the observed density predictor is known exactly, despite PR38's unresolved 1%/5% discrepancies. Even a high rank correlation does not guarantee unbiased slopes. No selection of a winning radius or gate.

The nominal 20 full design could resolve an equivalent contrast near 1.5 under these assumptions, but the common-support design cannot reach 3 under the same scenarios. Stronger block support yields marginal sensitivity near 3. The original strict void sample remains underpowered (PR37); this is not a rescue or confirmation of that test.

## Reproducibility

    python -m unittest discover -s notebooks/desi -p test_fp_design_power.py -v
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/fp_design_power.py STAGED RAW MASK1 MASK2 MASK3

4/4 new local unit tests passed. Real-data run completed. Local execution used the previously staged compact equivalent coverage_overlap helper, not an independent rerun of the exact committed dependency stack. Source files remain external.

## Gates before any outcome analysis

1. Obtain source block manifest and sampler for 5% randoms; validate independent selection and quantify density measurement error / shared-aperture covariance. No further large data request until precision target defined.
2. Define a specific SoCT/PNT continuous-density relation, sign, effect unit and scale dependence derived from the model rather than transplanting the binary 1–3 prediction. If no derivation exists, designate as exploratory with a separate protocol.
3. Establish conventional null (FP survey calibration, selection/Malmquist bias, redshift-space density, galaxy population dependence, coherent peculiar flows and correlated errors); calibrate covariance or use independent mocks. Check source FP metadata and population controls. Model uncertainties in the predictor; consider spatially blocked validation and mock injection of the specified effect.
4. Predefine primary scale/gate, effect direction, nuisance model, multiplicity and failure criteria; require prospective power under justified assumptions. Keep strict P6 void-versus-filament track separate and unresolved.
5. No unblinding or claim of support/falsification until protocol review and lock.
