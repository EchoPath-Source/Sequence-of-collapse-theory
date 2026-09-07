# O-1D3f — Causal Closure / Controller Relocation

## Question
Does instrumental self-preservation depend on where the controller is physically instantiated, or on the causal organization of the sensing-estimation-planning-actuation loop?

O-1D3e showed that preservation can emerge instrumentally when failure destroys future task access, but a matched external controller reproduced the behavior exactly. O-1D3f therefore progressively relocates and perturbs the loop.

## Conditions
1. `closed_internal` — reference closed loop.
2. `relocated_zero_latency` — estimator/planner treated as externally located but receives the same diagnostic and has the same immediate actuation authority.
3. `relocated_sense_latency_4` — external controller receives stale state information.
4. `relocated_actuation_latency_4` — action reaches the regulated system after a delay.
5. `relocated_channel_error_02` — 2% control-channel action flips.
6. `relocated_disconnect_02` — 2% communication failures; disconnected trials default to work.

The first two are intentionally computationally identical. If they differ, the implementation is not actually matched. The other arms intervene on causal connectivity rather than computational sophistication.

## Primary discriminator
Let `J` be realized task reward and `L` continuation/lifetime.

A location-specific effect would require

`J_internal != J_relocated_zero_latency`

under matched information, computation, and actuation.

A causal-connectivity effect is instead indicated when zero-latency relocation is neutral but latency, channel corruption, or disconnection degrades `J` or `L`.

## Interpretation boundary
If internal and perfectly connected external controllers are equivalent, physical controller location is not sufficient to define functional selfhood in this benchmark.

If perturbing the loop degrades preservation, the supported statement is only that **closed-loop causal connectivity matters**. This is ordinary control theory and does not establish intrinsic agency, consciousness, phenomenology, or a privileged metaphysical boundary of the self.

## Stronger future criterion
A later observer criterion would need to operationalize a boundary that is not merely spatial. Candidate quantities include causal dependence of future sensing on the loop's own maintained variables, intervention-based closure measures, and whether removing a component destroys the loop's capacity to reconstruct itself. These require matched external controls before any observer-like interpretation.
