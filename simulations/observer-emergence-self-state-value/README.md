# O-1C2 — Decision-Theoretic Value of Self-State Information

**Status:** Complete synthetic observer-emergence simulation  
**Claim level:** Ordinary information/control theory; no consciousness claim and no novel-physics claim.

## Question

Does calibrated information about a system's own internal sensor reliability become functionally useful when that information can guide a real resource-allocation decision?

O-1C showed that self-information alone was not sufficient: an informative self-state channel did not reliably beat ablation. O-1C2 therefore changes the task so that self-knowledge has a defined decision-theoretic use.

## Architecture

The agent operates in a binary world with temporal persistence. Its cheap sensor switches between two hidden internal reliability states:

```text
good state:     90% accuracy
degraded state: 55% accuracy
```

The agent may instead pay for a reliable sensor:

```text
reliable sensor: 96% accuracy
cost:            0.12 utility units/use
```

The calibrated agent estimates its own current sensor reliability and uses the expensive sensor when that estimate drops below a fixed threshold.

## Controls

Three conditions receive the same external world and raw sensor stream.

### Calibrated

The self-state estimate remains temporally aligned with the true internal reliability state.

### Shuffled placebo

The exact same self-state values are randomly permuted across time. This preserves the channel's marginal distribution and decision rate while destroying self-state alignment.

### Ablated, budget matched

The agent receives no self-state information. Expensive-sensor uses are assigned independently at random, but the total expensive-sensor usage rate is forced to match the calibrated agent exactly.

Thus the main comparison holds sensing budget fixed:

```text
same world
same cheap-sensor stream
same expensive sensor
same expensive-sensor cost
same number of expensive-sensor uses
```

The intended difference is only **when** the expensive sensor is used.

## Primary metrics

- utility per step;
- raw accuracy;
- reliable-sensor usage rate;
- mutual information between world and selected observation;
- mutual information between true internal sensor state and sensing action.

The last quantity tests whether the agent's resource-allocation action is actually coupled to its own internal state.

## Representative result

For

```text
world persistence = 0.90
sensor switch probability = 0.01
expensive-sensor cost = 0.12
```

all conditions use the reliable sensor at the same rate:

```text
0.23431
```

Results:

| condition | utility | accuracy | I(sensor state; action) |
|---|---:|---:|---:|
| calibrated | 0.79331 | 0.82143 | 0.19113 bits |
| shuffled placebo | 0.75515 | 0.78327 | ~0 |
| ablated, budget matched | 0.75497 | 0.78309 | ~0 |

So in this task the value does **not** come from spending more sensing resources. It comes from allocating the same resources conditionally on informative self-state knowledge.

A useful ablation quantity is therefore

```math
\Delta J_{\rm self}
=
J_{\rm calibrated}-J_{\rm budget\ matched\ ablation}.
```

For the representative condition,

```math
\Delta J_{\rm self}\approx0.03834
```

utility units per step.

## Across the tested grid

The calibrated policy beats both controls in every committed condition, but the size of the advantage declines as the hidden sensor state switches more quickly.

That behavior is expected: the self-state estimate becomes less temporally informative when the internal condition changes faster than the estimator can track it.

For example, at world persistence 0.97:

```text
switch 0.01: calibrated utility 0.79167 vs ablated 0.75333
switch 0.05: calibrated utility 0.75921 vs ablated 0.74132
switch 0.15: calibrated utility 0.74807 vs ablated 0.73777
```

The self-state/action mutual information falls simultaneously from about 0.198 bits to about 0.0066 bits.

## Main conclusion

O-1C2 establishes a stronger functional criterion than O-1B/O-1C:

```text
self-representation
+ calibration to true internal state
+ causal use in action selection
+ advantage over shuffled placebo
+ advantage over budget-matched ablation
```

is meaningfully different from merely storing self-related information.

A candidate operational criterion is therefore:

```math
I(Z_{\rm self};Z_{\rm internal})>0
```

together with

```math
\Delta J_{\rm self}>\delta_{\min}
```

under capacity- and resource-matched ablations.

## What this does not show

It does not show:

- consciousness;
- subjective experience;
- fundamental selfhood;
- objective quantum collapse;
- SoCT memory feedback;
- any new physical law.

The result is fully compatible with ordinary adaptive control and information theory.

## Relevance to the broader observer-emergence track

The current hierarchy is now better resolved:

```text
record
-> persistent memory
-> causal reuse
-> internal-state estimation
-> calibrated self-state-dependent resource allocation
-> self-regulation
-> recursive self-modeling? (later)
```

The next useful question is whether the self-model can regulate not merely sensing expenditure but the system's **own future integrity or capability**. That is the proposed O-1D-prep gate before attempting deeper recursive self-modeling.
