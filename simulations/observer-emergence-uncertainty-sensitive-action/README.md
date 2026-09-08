# O-1D4c — Uncertainty-Sensitive Information Gathering

## Question
Does calibrated uncertainty about the self-model causally improve behavior if the controller can acquire additional autobiographical evidence before committing to a maintenance policy?

## Design
Use `d in {0.02,0.07}` with equal prevalence. The first autobiographical sample is shortened to 70 steps to create meaningful uncertainty. The controller may acquire a second independent 70-step self-history before choosing burst 1 vs burst 2.

Primary confidence-gated rule: gather if empirical self-model confidence `< 0.90`. Additional information has an explicit value cost of 2.0 units.

Controls:
- never gather;
- always gather;
- shuffled/unrelated confidence gate;
- oracle hidden regime.

## Frozen result
| arm | mean value | gather rate |
|---|---:|---:|
| confidence gated | 299.2131 | .3055 |
| never gather | 300.0073 | 0 |
| always gather | 297.7314 | 1.0 |
| shuffled gate | 299.4892 | .3187 |
| oracle | 300.0610 | 0 |

The confidence-gated controller does **not** beat never gathering. It also does not beat the shuffled-confidence gate.

Therefore calibrated self-uncertainty is predictive, but the present acquisition rule does not convert that uncertainty into positive value of information.

`knowing when the self-model is uncertain != knowing when more self-information is worth acquiring.`

This negative result is frozen.

## Next gate
Separate uncertainty calibration from value-of-information calibration. Sweep information cost while keeping the confidence gate fixed, then determine whether any cost region supports a positive paired gain. If not, the active-metacognition rung is withheld and the next design must estimate expected decision regret, not confidence alone.
