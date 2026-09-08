# O-1D4a — Empirical Self-Uncertainty Calibration

## Question
Can an autobiographical self-dynamics estimator support an empirically calibrated estimate of its own reliability, rather than returning only a point estimate?

## Design
Use the regret-balanced hidden regimes from O-1D3y/z: `d in {0.02, 0.07}`. Generate an independent 10,000-history calibration set with equal regime prevalence. Estimate hidden degradation from paired own action–outcome records, then learn empirical `P(high | d_hat bin)` with Laplace smoothing.

## Frozen result
Calibration bins show strongly varying reliability rather than a binary correct/incorrect classifier. Representative bins:

| d_hat bin | n | P(high) | confidence | empirical accuracy |
|---|---:|---:|---:|---:|
| < .025 | 2405 | .0062 | .9938 | .9942 |
| .025-.035 | 1251 | .0423 | .9577 | .9584 |
| .035-.045 | 1349 | .2302 | .7698 | .7702 |
| .045-.055 | 762 | .6348 | .6348 | .6352 |
| .055-.065 | 636 | .8903 | .8903 | .8915 |
| .065-.080 | 1417 | .9824 | .9824 | .9831 |
| .080-.110 | 1805 | .9994 | .9994 | 1.0000 |

The estimator therefore contains usable information not only about which self-dynamics regime is likely, but about how reliable that classification is expected to be.

This is an externally calibrated reliability model over an internal/self-history estimator. It is not yet evidence that the system actively uses uncertainty about itself.

## Next gate
Test calibration on a completely independent held-out set. Confidence must predict actual self-classification error before uncertainty-sensitive action is attempted.
