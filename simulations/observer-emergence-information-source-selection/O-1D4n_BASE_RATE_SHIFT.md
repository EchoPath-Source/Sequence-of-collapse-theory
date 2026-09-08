# O-1D4n — Base-Rate Shift of the Frozen Stable Gate

## Purpose
Test whether the O-1D4l stable information-source gate is robust to changes in the population prevalence of hidden self-dynamics, without changing the gate itself.

Frozen source rule and probe costs are unchanged.

Two independent 12,000-episode conditions:
- `p(d=0.02)=0.25`
- `p(d=0.02)=0.75`

## Results
### Low-degradation prevalence = 0.25
| arm | mean value |
|---|---:|
| stable gate | 265.4523 |
| shuffled gate | 265.6312 |
| always none | 265.3763 |
| always cheap | 265.3332 |
| always strong | 264.9667 |

Stable minus shuffled: -0.1790, 95% CI [-0.8648, 0.5069].
Stable minus none: +0.0760, 95% CI [-0.7659, 0.9178].

No provenance-specific advantage is supported.

### Low-degradation prevalence = 0.75
| arm | mean value |
|---|---:|
| stable gate | 340.5270 |
| shuffled gate | 339.8804 |
| always none | 339.4776 |
| always cheap | 340.3675 |
| always strong | 339.9403 |

Paired stable-gate differences:
- vs shuffled: +0.6466, 95% CI [0.0960, 1.1973]
- vs none: +1.0494, 95% CI [0.4346, 1.6643]
- vs cheap: +0.1595, 95% CI [-0.1453, 0.4644]
- vs strong: +0.5867, 95% CI [0.0985, 1.0750]

## Interpretation
The frozen gate is **conditionally useful** under a changed base rate where the low-degradation regime is common: it beats shuffled provenance, no probe, and strong probe on held-out paired episodes. It does not beat the cheap-probe baseline cleanly.

When the low-degradation regime is uncommon, the effect disappears.

Therefore the result supports environment-conditional value of autobiographical information-source selection, not a universal metacognitive-control advantage.

This base-rate sensitivity is itself important: the rational value of introspection depends on the environment's latent-state distribution.