# O-1C — Self-Model Ablation

**Status:** COMPLETE adversarial observer-emergence toy test  
**Claim level:** ordinary information/control theory; no consciousness or novel-physics claim.

## Question

Does the apparent advantage of an explicit internal-state model survive controls that preserve channel capacity and computational structure while destroying actual self-information?

O-1B introduced an estimate of sensor reliability. O-1C compares three conditions on the same synthetic world/sensor stream:

1. `calibrated` — time-local reliability estimate;
2. `shuffled_placebo` — same estimate values shuffled in time, preserving marginal distribution but destroying alignment with true internal state;
3. `ablated` — same scalar policy input fixed at 0.5, carrying no self-state information.

## Metrics

- task accuracy;
- mutual information between world and chosen estimate;
- mutual information between true sensor state and the internal self-state channel.

The intended self-information criterion is

```math
I(Z_{self};Z_{internal}) > 0.
```

The intended causal-utility criterion is an ablation contrast

```math
Delta J_{self}=J_{calibrated}-J_{control}.
```

## Representative result

For a persistent world (`p=0.90`) and slowly changing sensor (`switch=0.01`), the calibrated channel does carry genuine self-state information:

```text
calibrated self-state MI ~= 0.1334 bits
shuffled placebo MI     ~= 0.000001 bits
ablated MI               = 0
```

However task performance does **not** establish a positive causal utility of that self-model in this policy:

```text
calibrated accuracy       ~= 0.7182
shuffled-placebo accuracy ~= 0.7151
ablated accuracy           ~= 0.7227
```

At `p=0.97`, `switch=0.01`, the same problem remains: the calibrated channel contains about `0.1367` bits of true self-state information, but the ablated condition performs better on the task.

## Interpretation

This is important negative evidence against an overly easy observer-emergence story.

A system can possess an internal variable that genuinely predicts its own sensor condition without that variable improving behavior under the chosen policy. Therefore:

```text
self-information != useful self-model
```

and

```text
useful self-model != consciousness
```

O-1B's simple policy is insufficient to establish the proposed R2 -> R3 transition from model of own state to model-conditioned self-regulation.

The correct response is not to tune the result until the calibrated condition wins. Instead the failure becomes a design constraint: a self-model earns observer-like significance only when its information is causally useful under a policy whose advantage survives placebo/ablation controls and out-of-sample environments.

## Revised criterion

A candidate functional self-model should require both:

```math
I(Z_{self};Z_{internal}) > 0
```

and a preregistered positive ablation effect:

```math
Delta J_{self} > delta_{min},
```

with the advantage absent when self-state labels are shuffled and replicated across held-out environmental regimes.

## Consequence for Track 1

Do not yet promote a `Gamma_self` term into the physical observation source. O-1C shows that measurable self-information alone is too weak. Track 2 must first establish a robust causal self-regulation quantity distinct from passive information storage and generic computational complexity.

## Next gate

O-1D should not simply add recursive depth. First repair the functional test by defining a decision problem in which knowledge of internal reliability has a normative value (for example, a sensing/action tradeoff with explicit costs), then freeze the policy and test calibrated vs shuffled vs ablated channels out of sample.

Only after causal self-regulation survives that test should recursive self-model depth be investigated.
