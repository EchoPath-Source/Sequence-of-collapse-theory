# O-1D4h — Causal Information Gate

## Question
Can a controller improve future regulation by gathering more self-information only when that information is likely to change its action and avoid regret?

## Design
Use the regret-balanced hidden self-dynamics regimes `d in {0.02, 0.07}` with equal prevalence. A first 70-step autobiographical history yields a current policy choice. An optional second 70-step history may change that choice.

On an independent 26,000-episode training set, estimate for each first-history self-estimate bin:

- `P(action changes after more self-information | history bin)`;
- mean paired regret avoided conditional on an action change;
- unconditional mean paired benefit of gathering.

Define the causal-information score approximately as:

`P(action change | H) * max(E[regret avoided | H, action change], 0)`.

Gather if the score exceeds the fixed information cost `0.5`.

Held-out evaluation uses 18,000 paired episodes. Controls: confidence-only gate, never gather, always gather, shuffled causal gate, oracle hidden-regime policy.

## Frozen result
| arm | mean value | gather rate |
|---|---:|---:|
| causal information | 301.9987 | .3051 |
| confidence | 302.0715 | .6170 |
| never gather | 302.1402 | 0 |
| always gather | 301.9120 | 1.0 |
| shuffled causal | 302.3342 | .3228 |
| oracle | 303.0469 | 0 |

Paired contrasts for causal-information vs controls:

- vs confidence: `-0.073`, 95% CI `[-0.370, 0.225]`
- vs never gather: `-0.142`, 95% CI `[-0.646, 0.363]`
- vs always gather: `+0.087`, 95% CI `[-0.252, 0.426]`
- vs shuffled causal: `-0.336`, 95% CI `[-0.786, 0.115]`
- vs oracle: `-1.048`, 95% CI `[-1.602, -0.494]`

## Interpretation
The causal-information gate does not clear the strong control. It does not significantly beat never gathering, confidence gating, or shuffled causal gating. Shuffled causal gating is numerically better.

Therefore:

`action-change probability × conditional regret is not yet a robust provenance-sensitive value-of-self-information estimator in this environment.`

The active-functional-metacognition rung remains withheld.

The next experiment should vary **information quality**, not merely thresholding: provide an optional, more diagnostic self-probe and test whether selective acquisition of that probe improves value relative to always probing, never probing, confidence-only, and shuffled targeting.

This is ordinary adaptive decision/control modeling; it is not evidence of consciousness or novel physics.
