# O-1D4o — Probe-Economics Shift of the Frozen Stable Gate

## Purpose
Test whether the O-1D4l source-selection rule remains useful when information acquisition costs change, without changing the source-selection mapping.

Balanced hidden dynamics prevalence (`p(d=0.02)=0.5`). Each condition uses 10,000 new paired episodes.

## Lower-cost information condition
- cheap cost: 0.125
- strong cost: 0.375

| arm | mean value |
|---|---:|
| stable gate | 302.5375 |
| shuffled gate | 302.4561 |
| always none | 301.8758 |
| always cheap | 302.7793 |
| always strong | 302.4746 |

Paired stable differences:
- vs shuffled: +0.0814, 95% CI [-0.6085, 0.7714]
- vs none: +0.6617, 95% CI [-0.1653, 1.4887]
- vs cheap: -0.2418, 95% CI [-0.7170, 0.2333]
- vs strong: +0.0629, 95% CI [-0.6796, 0.8053]

No clean adaptive advantage.

## Higher-cost information condition
- cheap cost: 0.50
- strong cost: 1.50

| arm | mean value |
|---|---:|
| stable gate | 301.3362 |
| shuffled gate | 300.8829 |
| always none | 300.7373 |
| always cheap | 301.3146 |
| always strong | 300.6520 |

Paired stable differences:
- vs shuffled: +0.4532, 95% CI [-0.2315, 1.1379]
- vs none: +0.5989, 95% CI [-0.2314, 1.4291]
- vs cheap: +0.0215, 95% CI [-0.4039, 0.4470]
- vs strong: +0.6841, 95% CI [-0.0401, 1.4083]

The higher-cost condition moves the provenance contrast in the expected direction but remains statistically unresolved at this sample size.

## Interpretation
The frozen source rule does not show a robust, cost-invariant advantage. Lower probe prices make a fixed cheap-probe strategy highly competitive; higher prices make selective probing more attractive, but the held-out contrast is still unresolved.

This reinforces a broader constraint: metacognitive control is inseparable from information economics. A source-selection policy cannot be characterized independently of the costs and stakes of information acquisition.

Active functional metacognitive control remains a conditional, not yet general, result.