# O-1D3 — Predictive Self-Model vs Model-Predictive Control

## Question
Does modeling one's *future internal state under candidate actions* add a distinct observer-like capability, and is that capability privileged when the model is internal?

The system chooses between `WORK` and `MAINTAIN`. Working yields immediate sensing reward but accelerates wear. Maintenance sacrifices immediate opportunity and may restore future capability.

## Arms
1. **Reactive** — maintenance from current health threshold only.
2. **Predictive internal** — short-horizon rollout predicts the system's own future health under candidate actions.
3. **Predictive external, zero latency** — same model, state information, horizon, and action rule implemented outside the regulated system.
4. **Predictive external, latency 2 / 8** — stale-state stress tests.

## Primary functional quantity
Let

`J = expected discounted/realized reward under work-maintenance tradeoff`.

A predictive-model advantage requires

`G_pred = J_predictive - J_reactive > 0`

on held-out regimes.

But an *internality* advantage requires additionally

`G_internal = J_predictive_internal - J_predictive_external_zero_latency > 0`.

If `G_internal = 0`, predictive self-modeling is functionally reproducible by ordinary external model-predictive control. The correct interpretation is then predictive regulation, not observerhood.

## Important controls
- identical predictive model and horizon for internal/external arms
- same diagnostic quality
- same degradation and repair process
- latency isolated as a separate intervention
- policy frozen across held-out degradation/noise/repair regimes

## Failure/withholding rules
Do not interpret predictive success as uniquely self-directed if a zero-latency external controller reproduces it. Do not interpret a delayed-external deficit as intrinsic agency; latency/locality is sufficient. Do not interpret a reactive deficit as evidence of consciousness; model-predictive control routinely outperforms myopic control when future state matters.

## Scope
This benchmark is ordinary stochastic/model-predictive control. It does not establish consciousness, phenomenology, SoCT memory, objective collapse, or new physics.

## Next gate
If prediction proves useful but externally reproducible, O-1D4 should test **recursive model depth**: a controller that models not only future internal state but the future consequences of its own model/policy updates. This must again include matched external computation and ablation/placebo controls.
