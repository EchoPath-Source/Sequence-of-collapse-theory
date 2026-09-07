# O-1D-prep — Self-model-guided preservation of future sensing capability

**Status:** Complete synthetic baseline  
**Claim level:** Ordinary information/control theory only  
**Does not establish:** consciousness, sentience, objective collapse, or SoCT memory physics.

## Question

O-1C2 showed that calibrated self-state information can improve the timing of resource allocation under a fixed sensing budget.

O-1D-prep asks a stronger question:

> Can an agent use information about its own internal condition to preserve its future ability to observe?

This moves the observer-emergence program from immediate self-state-dependent action toward adaptive self-maintenance.

## Model

The agent has an internal sensing-health variable

```math
h_t \in [0,1].
```

Stochastic degradation events reduce health. Sensing accuracy depends on health:

```math
p_{\rm correct}(t)=0.50+0.45h_t.
```

A maintenance action increases health but has a fixed utility cost.

The calibrated agent observes a noisy diagnostic of its own health and maintains a smoothed estimate

```math
\hat h_t.
```

It applies maintenance when

```math
\hat h_t < h_*.
```

## Controls

Three conditions share the same degradation stream and sensing random numbers.

### Calibrated

Maintenance timing depends on the temporally aligned self-state estimate.

### Shuffled placebo

The complete calibrated estimate trace is randomly permuted across time. This preserves the marginal distribution and the number of threshold crossings while destroying temporal alignment between self-state information and actual internal state.

### Budget-matched ablation

Maintenance events are placed randomly, with exactly the same number of maintenance actions as the calibrated condition.

Thus the critical comparison is not total maintenance expenditure. It is whether state-informed timing preserves future capability better than equal-cost controls.

## Representative result

At degradation probability

```text
p_degrade = 0.03
```

all three conditions use maintenance at exactly

```text
0.01481 actions / step.
```

Results:

| condition | utility/step | accuracy | mean health | low-health fraction |
|---|---:|---:|---:|---:|
| calibrated | 0.89888 | 0.90006 | 0.88928 | 0.00120 |
| shuffled placebo | 0.76756 | 0.76874 | 0.59655 | 0.37293 |
| budget-matched ablation | 0.76199 | 0.76317 | 0.58290 | 0.40015 |

The effect is not driven by a larger maintenance budget.

The calibrated agent uses the same number of preservation actions but deploys them when its internal capability is actually degrading.

Across the committed degradation sweep (`0.01`, `0.03`, `0.06`, `0.10`), calibrated timing outperforms both controls in utility, sensing accuracy, mean retained health, and avoidance of prolonged low-health states.

## Functional interpretation

This gives a more demanding observer-like causal loop:

```text
internal state
-> self-state estimate
-> preservation action
-> altered future internal state
-> preserved future observation capability
```

or

```math
Z_{\rm internal,t}
\rightarrow
\hat Z_{\rm self,t}
\rightarrow
a_t
\rightarrow
Z_{\rm internal,t+1}
\rightarrow
I_{\rm future}.
```

A provisional self-regulation contribution can therefore be operationalized as a causal improvement in future information-acquisition capacity under matched resource cost:

```math
\Delta J_{\rm preserve}
=
J_{\rm calibrated}
-
J_{\rm matched\ control}.
```

This is stronger than merely having self-information or using it for an immediate action.

## Important limitation

The environment has been constructed so that self-state information has decision-theoretic value. The result therefore validates the discriminator, not a universal principle that self-modeling or self-preservation must emerge.

This also does not imply biological homeostasis, autopoiesis, agency, consciousness, or a desire to survive.

The agent follows a fixed policy in a designed control problem.

## Observer-emergence consequence

The working hierarchy can now be sharpened to:

```text
record
-> causal reuse
-> calibrated self-state model
-> state-dependent resource allocation
-> self-maintenance that preserves future observation capability
-> recursive / temporally extended self-model?  [next frontier]
```

The current result supports promotion of **adaptive self-regulation** as a legitimate functional component of observer-like organization, but not as a SoCT physical source term.

Do not promote it into Track 1 unless a later physical experiment specifically discriminates record production from causal reuse/self-regulation.

## Next adversarial step

Before moving directly to recursive depth, test whether the apparent preservation advantage survives:

1. maintenance latency;
2. imperfect repair;
3. false self-diagnostics;
4. changing degradation regimes;
5. held-out parameter regimes;
6. an external controller with access to the same state information.

The external-controller control is especially important: if an externally informed regulator performs identically, the result demonstrates useful state feedback, not uniquely self-directed organization.
