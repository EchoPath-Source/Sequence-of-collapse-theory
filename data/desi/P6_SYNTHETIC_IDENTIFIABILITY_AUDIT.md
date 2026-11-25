# P6 conditional-template synthetic identifiability audit

2026-11-25. PR40 merged at ba5a9c003d492e043ddb8a6672bee22487ef9112. Synthetic experiment only. No astronomy files or distance outcomes loaded. This is not a selection-matched LCDM mock light cone, a physical PNT distance prediction, or a test of the original binary P6.

## Fixed design

Use the existing toy_mu(delta) conditional distance template from PR40, with injected dimensionless amplitude a=0 or 1. Two wholly synthetic spatial designs (1483 and 688 groups, corresponding only to previously reported sample sizes; not actual positions or density distributions), 64 clustered spatial centers, two synthetic angular regions, approximate z=r/2997.92458, selected covariate z range [.023,.15]. Bounded matter density delta=-.2+.69*tanh(latent); true matter density known in ideal case. Proxy adds shared cluster and individual latent errors. FP-like standard errors drawn around .52 mag. Selection probability logistic in z and delta; no outcome-dependent truncation, actual FP population calibration or Malmquist likelihood. Reported uncertainty scales motivate but do not calibrate these synthetic choices.

Simulate mean baseline with intercept, z and z^2 nuisance, cap zero point, exactly known projected bulk flow (150,-100,80) km/s. Covariance known exactly: diagonal reported-error-like noise plus 150 km/s independent velocity term; correlated vector-field stress with radial projection dot(u_i,u_j), 300 km/s and exponential spatial scale 50 h^-1 Mpc. These are illustrative assumptions, not GR velocity predictions. Confounded scenarios add an omitted population/flow-like mean response .15*delta+.10*delta^2 mag, chosen for an adversarial stress, not estimated from CF4. No claim that conventional systematics actually have this amplitude.

Fit GLS amplitude with identical nuisance baseline, then with free linear density term, then linear and quadratic terms. Whiten by exact Cholesky L; h=(I-QQ^T)L^-1*g, where Q spans whitened nuisance columns. Information I=h^Th, SE=1/sqrt(I); a_hat=h^T L^-1 y/I. Minimum detectable amplitude (MDA80) approx 2.8016*SE. For each fixed geometry, draw 2000 Gaussian whitened-noise realizations, shared across cases; these are not 2000 independent universes. Two-sided normal rejection at 5%, nominal 95% intervals. Injection true matter template, fit either true or noisy proxy. Report false rejection for a=0, detection for a=1, interval coverage for the injected amplitude; no empirically estimated covariance, selection or proxy calibration. Information fraction relative to true-density fixed-baseline model within each geometry.

## Executed results: N=1483, seed 20261125

True density IQR endpoints [-.633918,.178413]; proxy RMSE .130538. All rates conditional on synthetic design. Mean amplitude in unconfounded injected trials fixed/linear/quadratic: .99697/1.01655/.62195 (last with SE 52.24, dominated by noise).

| Predictor / nuisance | Information fraction | SE amplitude | MDA80 | Clean null rejection | Clean injection detection | Confounded null rejection | Clean injected interval coverage |
|---|---:|---:|---:|---:|---:|---:|---:|
| truth / fixed | 1 | .18702 | .52397 | 5.25% | 99.95% | 93.65% | 94.75% |
| truth / linear | .0203424 | 1.31129 | 3.67371 | 5.35% | 11.95% | 20.15% | 94.65% |
| truth / quadratic | .0000128 | 52.24274 | 146.36325 | 5.45% | 5.35% | 5.45% | 94.55% |
| noisy / fixed | 1.0456541 | .18290 | .51240 | 4.95% | 99.80% | 91.50% | 93.50% |
| noisy / linear | .0210432 | 1.28927 | 3.61202 | 5.00% | 7.50% | 12.20% | 93.30% |
| noisy / quadratic | .0000144 | 49.33727 | 138.22330 | 4.80% | 4.90% | 4.85% | 95.25% |

Noisy fixed injection mean .93226; noisy linear .57018. Confounded truth fixed null mean .65361, injection mean 1.65361, both coverage 6.35%. Quadratic nuisance absorbs the injected confounding polynomial exactly with known true density but also nearly all toy-template information. Noisy proxy can increase nominal information through variance while biasing recovered amplitude. No inference that it improves actual precision.

## Second synthetic design: N=688, seed 20261126

True density IQR endpoints [-.645520,.113482]; proxy RMSE .143165.

| Predictor / nuisance | Information fraction | MDA80 | Clean null rejection | Clean injection detection | Confounded null rejection |
|---|---:|---:|---:|---:|---:|
| truth / fixed | 1 | .80027 | 4.90% | 93.20% | 60.45% |
| truth / linear | .019544 | 5.72442 | 5.30% | 7.95% | 11.45% |
| truth / quadratic | .0000133 | 219.41598 | 4.60% | 4.70% | 4.60% |
| noisy / fixed | 1.1105924 | .75938 | 5.30% | 90.70% | 56.80% |
| noisy / linear | .0218343 | 5.41588 | 5.25% | 7.15% | 9.10% |
| noisy / quadratic | .0000142 | 212.03420 | 5.30% | 4.95% | 5.00% |

## Decision

Identifiability gate **failed for current conditional template under free conventional density-response nuisances in these synthetic designs**. Fixed-flow optimistic precision is conditional on knowing the baseline and does not establish scientific discriminability. The same sign and smooth shape are largely absorbed by conventional density trends; merely increasing random sample size or choosing the more sensitive aperture is not a resolution. These are deliberately constructed scenarios, not actual false-positive rates of a CF4 pipeline. They do not falsify the underlying physical mechanism or quantify real data power.

Do not unblind, fit H0, promote a primary scale, or preregister a confirmatory continuous-density amplitude test yet. Next: derive physically distinguishable light-cone response or independently constrain conventional mean flows and density-dependent FP calibration/selection with external data or selection-matched mocks, and quantify predictor uncertainties. Test any new discriminator for weighted projection, coverage and power under justified nuisance models before unblinding. If that cannot be done, report continuous-density branch as exploratory/blocked. Preserve original strict P6 separately; no change to its prediction. Do not request more large raw catalogs on the basis of this synthetic result alone.

## Reproduction

    OPENBLAS_NUM_THREADS=1 python -m unittest discover -s notebooks/desi -p test_pnt_mock_injection.py -v
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/pnt_mock_injection.py
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/pnt_mock_injection.py --n 688 --seed 20261126

Exact new standalone scripts tested locally, four tests passed, both runs completed (NumPy 2.3.5 / SciPy 1.17.0). CI pending. No real outcomes read. No final physical forward model or calibrated covariance implemented.
