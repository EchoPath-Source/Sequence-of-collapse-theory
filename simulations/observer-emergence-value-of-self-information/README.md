# O-1D4d — Value of Additional Self-Information

## Purpose
O-1D4c showed that calibrated confidence predicts self-model correctness but a confidence-threshold acquisition rule did not improve value. O-1D4d tests whether that failure was merely caused by the explicit information cost.

## Design
Keep the O-1D4c confidence gate fixed (`gather if confidence < .90`) and sweep acquisition cost:

`0, .25, .50, 1.0, 1.5, 2.0`.

Use 5,000 paired episodes per cost arm. Compare confidence-gated acquisition with never gathering on identical future streams.

## Frozen result
| acquisition cost | gated - never mean value | 95% CI |
|---:|---:|---:|
| 0.00 | -0.441 | [-1.280, 0.397] |
| 0.25 | -0.517 | [-1.356, 0.322] |
| 0.50 | -0.593 | [-1.432, 0.246] |
| 1.00 | -0.745 | [-1.584, 0.094] |
| 1.50 | -0.896 | [-1.736, -0.057] |
| 2.00 | -1.048 | [-1.887, -0.208] |

Even at zero acquisition cost, the confidence-gated rule does not show positive value. Therefore the O-1D4c failure cannot be attributed solely to the explicit cost of gathering information.

The likely issue is conceptual: **classification uncertainty is not the same quantity as expected decision regret**. A controller may be uncertain about which hidden regime it occupies while both candidate actions have nearly equal expected value, or may be relatively confident while the downside of being wrong is large.

## Constraint earned

`self-model confidence != value of self-information.`

The active-metacognition rung is therefore **withheld**. O-1D4a/b support calibrated second-order self-model reliability, but O-1D4c/d do not support the stronger claim that the current system uses that uncertainty adaptively.

## Next experiment — O-1D4e
Replace the confidence gate with an explicit expected-value-of-information calculation. Given posterior `P(d | history)` and independently estimated policy values `J(d, burst)`, estimate current expected regret and acquire more self-information only when its expected reduction in decision regret exceeds acquisition cost. Compare against confidence-only, never-gather, always-gather, shuffled-value, and oracle-information policies on paired held-out episodes.

This remains ordinary Bayesian decision/control theory. A positive O-1D4e result would support uncertainty-sensitive self-regulation, not consciousness.
