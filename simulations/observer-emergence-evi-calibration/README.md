# O-1D4f — Predicted EVI vs Realized Value of Gathering

## Question
Does the O-1D4e predicted expected value of self-information correspond to the actual paired gain produced by gathering an additional self-history?

## Design
Use 16,000 held-out episodes. For each episode, compute predicted EVI from the first 70-step history, then evaluate both actions on the same future stream:

- no additional history;
- acquire a second 70-step history and pay cost 0.5.

The realized target is `J(gather) - J(no-gather)`.

## Frozen result
Representative calibration bins:

| predicted EVI bin | n | mean predicted EVI | mean realized gather gain |
|---|---:|---:|---:|
| < 0 | 6334 | -2.8341 | +0.0721 |
| .50-.75 | 73 | .6315 | -5.7301 |
| 1.5-2.5 | 831 | 2.1726 | -0.2284 |
| > 2.5 | 8659 | 13.2041 | +0.7064 |

The predicted EVI is badly miscalibrated in both scale and, in several regions, sign. Very high predicted EVI does correspond to a positive average realized gain, but intermediate bins can be negative and negative predicted EVI is not reliably harmful.

## Interpretation
O-1D4e failed primarily because the controller's EVI model is not a calibrated estimator of intervention value.

This sharpens the distinction:

`self-model uncertainty -> calibrated classification reliability`

is supported, while

`self-model uncertainty -> calibrated value of acquiring more self-information`

is not.

The next gate learns the value-of-information mapping directly from independent paired training data, then freezes it before held-out evaluation. This avoids tuning the gate on evaluation outcomes.
