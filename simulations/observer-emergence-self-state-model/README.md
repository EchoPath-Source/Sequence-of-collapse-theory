# O-1B — Explicit Self-State Model

**Status:** Complete exploratory synthetic simulation  
**Track:** O-1 Observer Emergence / First Tuning Fork  
**Claim level:** Information/control-theory mechanism study only; no consciousness claim.

## Question

Does an adaptive observer-like system gain anything from explicitly estimating its own internal sensing condition, beyond memory and feedback alone?

O-1A established that causally reusing memory can improve later sensing when the environment contains exploitable temporal structure. O-1B adds an explicit internal variable representing the agent's estimate of its own sensor reliability.

The comparison is:

```text
feedback-only agent
vs
feedback + self-state estimate
```

Both agents have the same memory capacity and action repertoire.

## World and sensor

The external world is a binary Markov process with persistence `p_world`.

The sensor has an unobserved internal reliability state:

```text
good sensor:     P(correct) = 0.90
degraded sensor: P(correct) = 0.55
```

The sensor switches between good and degraded states with probability `p_switch` each step.

The feedback-only agent always trusts its direct sensor.

The self-state agent maintains an internal estimate of sensor reliability and, when that estimate falls below threshold, shifts toward a memory-weighted sensing strategy.

The estimator is deliberately simple. It infers sensor quality from agreement between fresh direct evidence and the previous observation in a temporally persistent world.

## Metrics

- task accuracy;
- mutual information between world state and agent estimate;
- mutual information between true sensor state and the agent's estimated sensor state.

The last quantity is an operational measure of whether the self-state variable actually tracks something about the system's own internal condition.

## Main result

Adding a self-state representation is **not automatically beneficial**.

When the external world has little temporal persistence (`p_world = 0.5`), the estimator has almost no information about the true sensor state and the self-state policy performs substantially worse than the feedback-only baseline.

Representative example:

```text
p_world = 0.50
p_switch = 0.01

feedback-only accuracy = 0.71892
self-state accuracy     = 0.64854
self-state MI           ≈ 0.000023 bits
```

The self-model is effectively uncalibrated there, so acting on it is harmful.

When the world is strongly persistent and the sensor condition changes slowly, the internal estimate acquires measurable information about the sensor state and can produce a small performance gain.

Representative example:

```text
p_world = 0.90
p_switch = 0.01

feedback-only accuracy = 0.70842
self-state accuracy     = 0.71324
world MI:
  feedback-only = 0.12923 bits
  self-state    = 0.13539 bits
self-state MI   = 0.12163 bits
```

At `p_world = 0.97`, `p_switch = 0.01` the same qualitative pattern appears:

```text
feedback-only accuracy = 0.71556
self-state accuracy     = 0.72094
self-state MI           = 0.11977 bits
```

But as the hidden sensor state switches more rapidly, the estimator lags and the advantage disappears or reverses.

## Interpretation

The important result is not that self-modeling improves performance. It often does not.

The stronger finding is:

```text
an internal self-state variable becomes functionally useful only when
(1) it carries real information about the system's internal condition, and
(2) the policy uses that information in a regime where it remains predictive.
```

This gives O-1 a stronger operational criterion for the R2 level in the observer-emergence hierarchy.

Instead of defining a self-model merely by the existence of a variable labeled `self`, require:

```math
I(Z_{self}; Z_{internal}) > 0
```

and an ablation-sensitive causal contribution to performance or regulation:

```math
Delta J_{self} = J_{with\ self\ model} - J_{ablated}.
```

A self-state representation that is uninformative or behaviorally useless should not count as meaningful observer-like self-modeling.

## Pushback / failure mode

This first self-state estimator is intentionally crude and fails over much of the parameter space.

That failure is useful. It prevents the observer-emergence track from assuming that adding recursive or self-referential variables necessarily creates a more capable or more observer-like system.

A self-model can be:

- inaccurate;
- stale;
- confounded with external-state predictability;
- behaviorally harmful;
- merely decorative.

Therefore future O-1 work must distinguish **self-reference as representation** from **calibrated self-knowledge with causal utility**.

## Relation to Track 1

O-1B suggests a possible future Track-1 discriminator beyond record creation and record reuse.

Two systems could have similar durable-record production and similar feedback intensity while differing in whether they maintain a calibrated model of their own internal sensing/reliability state.

That motivates a future decomposition such as:

```text
Gamma_rec   = record production
Gamma_use   = causal reuse of stored records
Gamma_self  = calibrated self-state modeling / self-regulation contribution
```

No claim is made that `Gamma_self` sources SoCT memory. It is a candidate variable that Track 2 can offer to Track 1 for later falsification.

## Next gate — O-1C

The next clean experiment is **self-model ablation**.

Hold memory capacity, sensing hardware, and policy complexity as fixed as possible, then remove or scramble the self-state channel.

Test whether the apparent benefit follows the informational content of the self-state representation rather than merely the presence of additional computation or parameters.

A useful O-1C design should include:

1. calibrated self-state model;
2. shuffled/self-state placebo channel;
3. ablated self-state channel;
4. matched model capacity;
5. causal-performance comparison;
6. calibration curves for true versus estimated internal state.

This remains observer-emergence research, not a consciousness test.
