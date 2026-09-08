# O-1D4e — Expected Value of Self-Information

## Question
Can the controller improve on confidence-only information seeking by explicitly estimating the expected value of acquiring more autobiographical evidence before choosing between maintenance burst policies?

## Design
Hidden dynamics remain `d in {0.02, 0.07}` with equal prevalence. The controller receives a 70-step own action–outcome history, computes an empirical posterior over hidden dynamics, and estimates the expected benefit of an additional independent 70-step history using independently estimated policy values `J(d, burst)` and a Monte Carlo posterior transition model.

Fresh policy-value estimates used by the EVI model:
- J(.02, burst 1) = 374.6015
- J(.02, burst 2) = 367.5980
- J(.07, burst 1) = 231.7251
- J(.07, burst 2) = 233.3776

The acquisition cost is fixed at 0.5 value units. Primary EVI rule: acquire the second history only if predicted EVI > 0.5.

Controls: confidence-only gate, never gather, always gather, shuffled/unrelated EVI gate, and oracle hidden regime. Evaluation uses 12,000 held-out episodes with paired future streams.

## Frozen result
| arm | mean value | gather rate |
|---|---:|---:|
| EVI gate | 301.9247 | .5967 |
| confidence gate | 302.0782 | .4159 |
| never gather | 301.5559 | 0 |
| always gather | 301.7381 | 1.0 |
| shuffled EVI | 301.9719 | .6077 |
| oracle | 302.5145 | 0 |

Paired EVI contrasts:
- vs confidence: -0.1535, 95% CI [-0.4660, 0.1590]
- vs never: +0.3688, 95% CI [-0.3031, 1.0408]
- vs always: +0.1866, 95% CI [-0.1243, 0.4975]
- vs shuffled EVI: -0.0472, 95% CI [-0.5263, 0.4318]
- vs oracle: -0.5898, 95% CI [-1.3602, 0.1807]

## Interpretation
The direct EVI gate does not clear the active-metacognition discriminator. Its mean exceeds never/always gathering slightly, but all key intervals cross zero, and it does not outperform confidence-only or shuffled-EVI controls.

The result is frozen rather than retuned. The next gate asks whether the failure is due to **EVI calibration**: does predicted EVI actually match the paired realized benefit of acquiring more self-information?

This remains ordinary Bayesian decision/control theory and is not evidence of consciousness.