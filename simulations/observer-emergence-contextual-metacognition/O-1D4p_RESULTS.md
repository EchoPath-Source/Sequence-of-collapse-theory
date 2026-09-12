# O-1D4p — Explicit Contextual Metacognition

## Question
Can a self-modeling controller condition its information-source policy jointly on autobiographical self-state and an explicit environment base-rate context?

## Design
Hidden self-dynamics d in {0.02, 0.07}. Environment context p_low is randomized across {0.25, 0.50, 0.75}. The controller receives the context explicitly. Independent training learns source maps over {none, cheap 70-step probe, strong 210-step probe} for each context and self-estimate bin. Held-out evaluation uses 12,000 episodes. Probe costs remain 0, 0.25, 0.75.

## Frozen results
| arm | mean value |
|---|---:|
| contextual | 302.0956 |
| balanced-map | 301.9877 |
| shuffled-context | 301.9348 |
| none | 301.8136 |
| cheap | 302.0321 |
| strong | 301.7008 |

Contextual minus controls, paired 95% CI:
- balanced map: +0.1079 [-0.2855, 0.5013]
- shuffled context: +0.1608 [-0.2357, 0.5574]
- none: +0.2820 [-0.2702, 0.8342]
- cheap: +0.0635 [-0.4391, 0.5661]
- strong: +0.3948 [-0.0900, 0.8796]

## Interpretation
Explicit environment context changes the learned information-source map, but the contextual policy does not cleanly outperform shuffled-context or strong fixed baselines. Therefore a general contextual metacognitive-control claim is withheld.

The experiment supports a narrower architectural point: self-information policy can be represented as pi_I(self estimate, environment context, information cost), but representing context is not sufficient to make the learned policy robustly valuable.