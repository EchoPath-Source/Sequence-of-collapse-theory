# O-1D3u — Reproducible Policy-Basin Search

## Question
Can maintenance economics produce two reproducibly different threshold-style policy basins under the exact evaluator semantics?

## Design
Screen maintenance costs 0.20, 0.30, 0.40, and 0.50 at low degradation d=0.04 and higher degradation d=0.10. At each cell compare recovery targets 0.68, 0.72, 0.76, 0.80, and 0.84 with trigger fixed at 0.69. Use two independent 250-episode replications as a screening gate.

## Frozen result
The threshold family does not yield a robust low-vs-high separation. Winners change across independent replications in most cells. Examples:

- cost 0.20, d=0.04: replications favor 0.72 and 0.68
- cost 0.20, d=0.10: replications favor 0.76 and 0.68
- cost 0.30, d=0.10: replications favor 0.68 and 0.76
- cost 0.40, d=0.04: both favor 0.72, but d=0.10 splits between 0.76 and 0.68

## Interpretation
The threshold/recovery-target family remains too flat/noisy to support the desired provenance discriminator. The correct response is to abandon this policy parameterization rather than continue tuning it.

Next gate: test an interpretable discrete action-duration policy, where self-dynamics could change how long maintenance should continue after a trigger.
