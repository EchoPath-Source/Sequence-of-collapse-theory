# O-1D4r — Changing-Environment Adaptation

## Question
Can a self/world-modeling controller update its inferred environment after a base-rate reversal and alter its self-information policy accordingly?

## Design
Environment switches between p_low=0.25 and p_low=0.75. Separate 30-history population windows occur before and after the switch. The adaptive arm re-infers context after the switch; stale control retains the pre-switch context. Additional controls use balanced context, deliberately mismatched context, and the true post-switch context. Evaluation uses 5,000 new episodes.

## Frozen results
Post-switch context inference accuracy: 0.6930.

| arm | mean value |
|---|---:|
| adaptive | 304.6503 |
| stale | 304.3716 |
| balanced | 304.7003 |
| mismatched/shuffled | 303.9315 |
| true-context map | 304.2840 |

Adaptive minus controls, paired 95% CI:
- stale: +0.2787 [-0.9345, 1.4919]
- balanced: -0.0501 [-0.9795, 0.8794]
- mismatched: +0.7188 [-0.6048, 2.0423]
- true-context map: +0.3663 [-0.0605, 0.7931]

## Interpretation
The controller can update a coarse world-context estimate after a distribution change, but the resulting policy advantage is not statistically resolved. The large intervals and the fact that the true-context map is not uniformly best show that source-policy estimation remains a major bottleneck.

The earned architectural ladder is therefore limited to: autobiographical self-model + coarse world-model + updateable uncertainty/context representation. Reliable adaptive metacognitive control remains withheld.

## Next discriminator
Before adding another layer, increase reproducibility and diagnose the policy bottleneck: estimate source-action regret surfaces with larger independent training sets, quantify context-map stability, and test whether a Bayes-optimal source policy derived from a generative model can outperform the empirical bin maps. Do not tune against these held-out results.