# O-1D4a — Empirical Self-Model Confidence Calibration

## Question
Can a controller estimate not only its hidden self-dynamics but also the reliability of that estimate from independent autobiographical calibration data?

## Design
Use the regret-balanced hidden regimes from O-1D3y/z: `d in {0.02, 0.07}`. Generate independent 140-step action–outcome histories, estimate degradation from paired work outcomes, and learn empirical `P(d=high | d_hat-bin)` on a separate balanced calibration set. Freeze the bins before held-out evaluation.

## Frozen result
Held-out overall classification accuracy is 0.9285. Confidence is strongly calibrated:

| confidence band | n | mean confidence | empirical accuracy |
|---|---:|---:|---:|
| .70-.80 | 1540 | .7467 | .7481 |
| .80-.90 | 1224 | .8043 | .8031 |
| .90-1.00 | 7236 | .9865 | .9881 |

No held-out cases fell in the .50-.70 bands under the frozen estimator/binning scheme.

This establishes an ordinary statistical calibration result: the model's confidence score predicts whether its self-dynamics classification is correct. It does not establish subjective confidence, awareness, consciousness, or privileged internality.

## Next gate
O-1D4b asks whether confidence also predicts continuous self-model error, rather than only binary classification correctness.
