# O-1D4j — Information-Source Selection

## Question
Can a self-modeling controller use autobiographical state to choose among no additional self-probe, a cheap weak probe, and an expensive strong probe in a way that improves held-out regulation?

## Design
Initial own-history: 70 steps. Hidden self-dynamics d in {0.02, 0.07} with equal prevalence.

Available information actions:
- none: 0 extra steps, cost 0
- cheap: 70-step self-probe, cost 0.25
- strong: 210-step self-probe, cost 0.75

An independent 24,000-episode training set estimates mean realized downstream value for each source conditional on the initial self-estimate bin. The source with highest training value is frozen per bin. Evaluation uses 20,000 independent paired episodes.

Controls: always-none, always-cheap, always-strong, shuffled self-state source selection, fixed random mixture, and per-episode oracle-source upper bound.

## Frozen held-out results
| arm | mean value | none | cheap | strong |
|---|---:|---:|---:|---:|
| adaptive | 300.9786 | .5799 | .1182 | .3020 |
| always none | 300.7929 | 1 | 0 | 0 |
| always cheap | 301.1193 | 0 | 1 | 0 |
| always strong | 300.8905 | 0 | 0 | 1 |
| shuffled selection | 300.8179 | .5913 | .0891 | .3197 |
| fixed mixture | 301.0149 | .3327 | .3406 | .3267 |
| oracle source | 307.6146 | .8753 | .0929 | .0319 |

Adaptive minus controls, paired 95% CI:
- vs none: +0.1857 [-0.3416, 0.7131]
- vs cheap: -0.1406 [-0.6370, 0.3558]
- vs strong: +0.0882 [-0.2873, 0.4636]
- vs shuffled: +0.1607 [-0.3227, 0.6442]
- vs fixed mixture: -0.0362 [-0.5009, 0.4284]
- vs oracle: -6.6360 [-7.1295, -6.1424]

## Interpretation
The adaptive controller does vary its information source with its autobiographical self-estimate, but it does not outperform the strongest fixed or shuffled controls on held-out episodes. Active functional metacognitive control remains withheld.

The large oracle-source gap shows that source-selection value exists in the environment; the learned mapping simply fails to identify it reliably enough.

## Next gate
Test whether the learned source-selection map itself is stable across independent training replications before changing the controller.
