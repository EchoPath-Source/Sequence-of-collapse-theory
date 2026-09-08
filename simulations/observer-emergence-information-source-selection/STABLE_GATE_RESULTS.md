# O-1D4l — Stable Source-Gate Transfer

## Purpose
O-1D4k showed that most learned information-source choices are unstable. O-1D4l therefore restricts adaptation to source choices reproduced in at least 3 of 4 independent training replications. Unstable bins fall back to the cheap-probe baseline.

Stable/near-stable consensus regions:
- bin 0: none, 4/4
- bin 1: none, 3/4
- bin 2: strong, 3/4
- bin 7: none, 4/4

All other bins: cheap baseline.

Evaluation: 20,000 new paired held-out episodes.

## Results
| arm | mean value |
|---|---:|
| stable gate | 301.5191 |
| always cheap | 301.3918 |
| shuffled stable gate | 301.1125 |
| always none | 301.5432 |
| always strong | 300.7992 |

Paired stable-gate differences:
- vs cheap: +0.1273, 95% CI [-0.1956, 0.4501]
- vs shuffled stable gate: +0.4066, 95% CI [-0.0798, 0.8929]
- vs none: -0.0241, 95% CI [-0.6052, 0.5570]
- vs strong: +0.7199, 95% CI [0.2038, 1.2359]

## Interpretation
Restricting adaptation to reproducible source regions materially improves the shuffled-provenance contrast and cleanly beats indiscriminate strong probing, but the key shuffled contrast still narrowly crosses zero and the policy does not beat always-none.

Therefore active functional metacognitive control is still withheld.

However, the direction is informative: stability filtering increased stable-gate minus shuffled from approximately +0.161 in O-1D4j to +0.407 here while avoiding post-hoc retuning on the held-out set.

The next discriminator should increase statistical and structural power without changing this frozen rule: preregister the stable gate and run a larger independent replication, preferably also under shifted regime prevalence and probe costs. A positive result must survive both provenance shuffling and a strong fixed baseline.
