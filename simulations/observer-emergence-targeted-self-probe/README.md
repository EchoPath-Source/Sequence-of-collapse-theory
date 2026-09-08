# O-1D4i — Targeted High-Information Self-Probe

## Question
If weak additional autobiography is not valuable enough, can a controller selectively request a more diagnostic self-probe and improve future regulation?

## Design
The initial autobiographical sample remains 70 steps. The optional probe is a longer 210-step diagnostic self-history with explicit cost `0.75`.

An independent 26,000-episode training set estimates, by current self-estimate bin:

- probability that the probe changes the selected maintenance-burst policy;
- paired value gain conditional on policy change;
- unconditional paired value of probing.

Held-out evaluation uses 18,000 paired episodes. Controls: empirical probe-value gate, confidence-only gate, never probe, always probe, shuffled targeting, and oracle.

## Frozen result
| arm | mean value | probe rate |
|---|---:|---:|
| targeted causal | 302.3086 | .7804 |
| targeted empirical | 302.2530 | .5817 |
| confidence | 302.4499 | .6199 |
| never probe | 302.1304 | 0 |
| always probe | 302.2001 | 1.0 |
| shuffled target | 302.1701 | .7677 |
| oracle | 302.9562 | 0 |

Paired contrasts for targeted causal vs controls:

- vs targeted empirical: `+0.056`, 95% CI `[-0.148, 0.259]`
- vs confidence: `-0.141`, 95% CI `[-0.347, 0.065]`
- vs never probe: `+0.178`, 95% CI `[-0.430, 0.787]`
- vs always probe: `+0.109`, 95% CI `[0.024, 0.194]`
- vs shuffled target: `+0.139`, 95% CI `[-0.157, 0.435]`
- vs oracle: `-0.648`, 95% CI `[-1.102, -0.193]`

## Interpretation
Selective probing significantly beats **always probing**, so indiscriminate introspection is demonstrably wasteful in this environment. However, the targeted causal policy does not significantly beat never probing, confidence-only gating, or shuffled targeting.

The defensible result is therefore narrow:

`some self-estimate regions predict when an expensive diagnostic self-probe should be avoided.`

But the stronger provenance-sensitive claim remains unearned:

`the system does not yet robustly demonstrate that its own current uncertainty state uniquely determines when to inspect itself further.`

The active-functional-metacognition rung remains withheld.

A useful next discriminator is **information-source selection**: offer multiple probes with different informativeness/cost and ask whether the controller selects among them according to expected downstream regret rather than merely probe/no-probe. This should be preregistered against never, always-cheap, always-expensive, shuffled-selection, confidence-only, and oracle-information controls.

This remains ordinary Bayesian/adaptive control, not evidence of consciousness.
