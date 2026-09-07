# O-1D3f — Causal Closure / Controller Relocation

## Question
Does instrumental self-preservation depend on where the controller is physically instantiated, or on the causal organization of the sensing-estimation-planning-actuation loop?

O-1D3e showed that preservation can emerge instrumentally when failure destroys future task access, but a matched external controller reproduced the behavior exactly. O-1D3f therefore progressively relocates and perturbs the loop.

## Conditions
1. `closed_internal` — reference closed loop.
2. `relocated_zero_latency` — estimator/planner treated as externally located but receives the same diagnostic and has the same immediate actuation authority.
3. `relocated_sense_latency_4` — external controller receives state information four steps late.
4. `relocated_actuation_latency_4` — action reaches the regulated system four steps late.
5. `relocated_channel_error_02` — 2% control-channel action flips.
6. `relocated_disconnect_02` — 2% communication failures; disconnected trials default to work.

The first two are intentionally computationally identical. If they differ, the implementation is not actually matched. The other arms intervene on causal connectivity rather than computational sophistication.

## Frozen result
Across every tested degradation regime,

`closed_internal == relocated_zero_latency`

for all reported outcome metrics. Physical relocation alone therefore produced no functional difference when information, computation, timing, and action authority were matched.

Representative results:

| degradation | condition | reward / episode | mean lifetime | failure rate |
|---:|---|---:|---:|---:|
| 0.02 | closed internal | 418.623 | 500.0 | 0.000 |
| 0.02 | relocated zero latency | 418.623 | 500.0 | 0.000 |
| 0.02 | sense latency 4 | 329.734 | 448.871 | 0.196 |
| 0.05 | closed internal | 402.726 | 500.0 | 0.000 |
| 0.05 | relocated zero latency | 402.726 | 500.0 | 0.000 |
| 0.05 | sense latency 4 | 241.346 | 351.164 | 0.522 |
| 0.08 | closed internal | 381.698 | 500.0 | 0.000 |
| 0.08 | relocated zero latency | 381.698 | 500.0 | 0.000 |
| 0.08 | sense latency 4 | 186.114 | 294.011 | 0.687 |
| 0.12 | closed internal | 295.303 | 500.0 | 0.000 |
| 0.12 | relocated zero latency | 295.303 | 500.0 | 0.000 |
| 0.12 | sense latency 4 | 170.228 | 333.698 | 0.580 |

Four-step sensing latency and four-step actuation latency are numerically identical in this benchmark because both create an equivalent four-step delay between the current diagnostic and the executed action under the deterministic policy.

Small channel corruption is much less damaging than four-step latency. At degradation 0.08, a 2% action-flip channel still achieved reward/episode 378.095 with failure rate 0.00067, while four-step latency reduced reward/episode to 186.114 and raised failure rate to 0.687. A 2% disconnection intervention also produced only modest degradation under the frozen default-to-work rule.

## Primary discriminator
Let `J` be realized task reward and `L` continuation/lifetime.

A location-specific effect would require

`J_internal != J_relocated_zero_latency`

under matched information, computation, and actuation.

That discriminator failed: no location-specific advantage appeared.

A causal-connectivity effect is instead indicated because delays that interrupt timely closure sharply degrade `J` and `L`.

## Interpretation
The frozen result supports:

**functional preservation depends more on timely closed-loop causal organization than on whether the controller is physically inside or outside the regulated system.**

It does **not** establish intrinsic agency, consciousness, phenomenology, a metaphysical self-boundary, or any novel SoCT physics. The result is compatible with ordinary control theory.

This is nevertheless an important negative discriminator for observer emergence:

`internal location != sufficient observer criterion`

and a useful positive engineering constraint:

`causal closure + timely access + action authority -> robust persistent regulation`

## EchoForm cross-application
The practical implications for persistent NPC / EchoForm design are documented separately in:

`docs/applied/echoform-persistent-agent-architecture.md`

That engineering track deliberately uses the observer-emergence results without claiming the resulting systems are conscious.

## Next gate — O-1D3g: intervention-defined causal boundary
The next experiment should stop using spatial location as the candidate self-boundary.

Instead define a candidate agent boundary by intervention: which variables form a mutually dependent loop such that severing or replacing one part destroys the system's capacity to preserve future sensing/action?

Required controls should include:

1. intact closed loop;
2. external zero-latency computational replica;
3. internal-state intervention with matched sensory input;
4. action-channel intervention with matched computation;
5. memory/state-estimator replacement;
6. a reconstruction/recovery arm testing whether the loop can restore a disrupted internal model from its own remaining records.

The strongest future criterion would not be 'computation is inside.' It would be that a temporally extended set of variables forms an intervention-sensitive causal organization that maintains and reconstructs the capacities required for its own future operation.
