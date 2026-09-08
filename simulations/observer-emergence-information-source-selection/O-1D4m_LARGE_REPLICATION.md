# O-1D4m — Large Independent Replication of the Frozen Stable Gate

## Frozen rule
No retuning from O-1D4l:
- bins 0, 1, 7 -> no probe
- bin 2 -> strong probe
- all other bins -> cheap probe

Probe economics unchanged from O-1D4j:
- none: 0 steps, cost 0
- cheap: 70 steps, cost 0.25
- strong: 210 steps, cost 0.75

Hidden self-dynamics remain `d in {0.02, 0.07}` at equal prevalence. Evaluation uses 30,000 new paired episodes.

## Results
| arm | mean value |
|---|---:|
| stable gate | 302.4912 |
| shuffled stable gate | 302.3683 |
| always none | 302.4894 |
| always cheap | 302.2785 |
| always strong | 302.0559 |

Stable-gate source rates:
- none: 0.4162
- cheap: 0.4179
- strong: 0.1659

Paired stable-gate differences:
- vs shuffled: +0.1229, 95% CI [-0.2527, 0.4984]
- vs none: +0.0018, 95% CI [-0.4621, 0.4656]
- vs cheap: +0.2127, 95% CI [-0.0390, 0.4644]
- vs strong: +0.4353, 95% CI [0.0161, 0.8544]

## Interpretation
The larger independent replication does **not** reproduce the near-significant provenance contrast from O-1D4l. The frozen gate again cleanly beats indiscriminate strong probing, but it ties the no-probe baseline and does not distinguish itself from shuffled provenance.

Therefore active provenance-specific functional metacognitive control remains withheld.

The next discriminator tests whether the gate is conditionally useful under changed environmental base rates rather than universally useful.