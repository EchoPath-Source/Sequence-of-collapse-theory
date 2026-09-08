# O-1D4g — Empirical Value of Self-Information Gate

## Question
Can an empirically learned map from current self-history state to the realized value of gathering more self-information outperform simpler acquisition policies on held-out episodes?

## Design
Use an independent 24,000-episode training set. For each first-history estimator bin, estimate the paired realized gain of acquiring a second 70-step own history, including acquisition cost 0.5. Freeze the bin-wise value map before evaluation.

Frozen training estimates of gather gain by self-estimate bin:
- bin 0: -0.5701
- bin 1: -0.4700
- bin 2: +1.1569
- bin 3: -0.2924
- bin 4: +0.2355
- bin 5: +0.6021
- bin 6: -0.1760
- bin 7: -0.5000

Held-out evaluation uses 16,000 episodes and paired future streams. The empirical-VOI controller gathers only in bins with positive independently learned gather value.

Controls: confidence-only, never gather, always gather, shuffled/unrelated VOI gate, and oracle hidden regime.

## Frozen result
| arm | mean value | gather rate |
|---|---:|---:|
| empirical VOI | 303.3847 | .4198 |
| confidence | 303.3674 | .4228 |
| never gather | 303.1930 | 0 |
| always gather | 303.1472 | 1.0 |
| shuffled VOI | 303.2190 | .4027 |
| oracle | 304.0342 | 0 |

Paired empirical-VOI contrasts:
- vs confidence: +0.0173, 95% CI [-0.0194, 0.0539]
- vs never: +0.1917, 95% CI [-0.4366, 0.8200]
- vs always: +0.2374, 95% CI [0.0166, 0.4583]
- vs shuffled VOI: +0.1657, 95% CI [-0.3512, 0.6826]
- vs oracle: -0.6495, 95% CI [-1.2508, -0.0483]

## Interpretation
The learned VOI gate significantly beats **always gathering**, showing that selective acquisition can avoid unnecessary information cost. However, it does not significantly beat never-gather, shuffled-VOI, or confidence-only controls.

Therefore the active functional-metacognition claim remains withheld.

What is supported:
1. autobiographical self-history can identify hidden self-dynamics;
2. the reliability of that self-inference can be calibrated out of sample;
3. independently learned decision-value estimates can identify some regions where extra self-information is more useful than others;
4. selective acquisition is better than indiscriminate acquisition in this task.

What is not yet supported:
`the system robustly seeks additional self-information because it accurately predicts that doing so will reduce its own future regret.`

The next design should move from coarse estimator bins to a decision-conditioned counterfactual model: predict how often a second history will actually change the selected action and multiply that probability by the state-specific regret avoided. That quantity is closer to causal value of self-information than generic confidence or coarse empirical bins.
