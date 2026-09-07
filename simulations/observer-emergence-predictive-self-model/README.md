# O-1D3 — Predictive Self-Model vs Model-Predictive Control

## Question
Does modeling one's *future internal state under candidate actions* add a distinct observer-like capability, and is that capability privileged when the model is internal?

The system chooses between `WORK` and `MAINTAIN`. Working yields immediate sensing reward but accelerates wear. Maintenance sacrifices immediate opportunity and may restore future capability.

## Arms
1. **Reactive** — maintenance from current health threshold only.
2. **Predictive internal** — short-horizon rollout predicts the system's own future health under candidate actions.
3. **Predictive external, zero latency** — same model, state information, horizon, and action rule implemented outside the regulated system.
4. **Predictive external, latency 2 / 8** — stale-state stress tests.

## Primary functional quantities
Let

`J = realized reward under work-maintenance tradeoff`.

Predictive-model advantage:

`G_pred = J_predictive - J_reactive`.

Internality advantage:

`G_internal = J_predictive_internal - J_predictive_external_zero_latency`.

## Frozen result
The predictive controller helps in the two mild regimes but fails to generalize as degradation becomes harsher.

Representative reward per step:

| degradation | reactive | predictive internal | external zero-latency |
|---:|---:|---:|---:|
| 0.01 | 0.826234 | 0.836112 | 0.836112 |
| 0.03 | 0.806762 | 0.811827 | 0.811827 |
| 0.06 | 0.766216 | 0.748129 | 0.748129 |
| 0.10 | 0.698658 | 0.577393 | 0.577393 |

Therefore:

- `G_pred > 0` for degradation 0.01 and 0.03;
- `G_pred < 0` for degradation 0.06 and 0.10;
- `G_internal = 0` in every tested regime.

The fixed predictive rollout increasingly over-maintains in harsher regimes. At degradation 0.10, maintenance rises from 17.393% for the reactive controller to 32.606% for predictive control. Work accuracy rises, but total reward falls sharply because opportunity/maintenance costs dominate.

This is a useful negative result: predictive self-modeling does not automatically confer robust adaptive value. A model can be internally predictive yet systematically misallocate resources when its assumptions or planning horizon are mismatched to the environment.

## Internal-versus-external boundary
The internal predictive controller and zero-latency external predictive controller are numerically identical across the complete frozen grid. Thus the present benchmark provides no evidence for a functional privilege of internally instantiated predictive state modeling.

A delayed external controller performs worse, but this is adequately explained by stale information/locality. It should not be interpreted as intrinsic agency or observerhood.

## Interpretation
O-1D3 does **not** earn a new observer-emergence rung under the current criterion.

The supported conclusion is:

`predictive model != robust self-model`

and separately:

`internal predictive computation != uniquely observer-like computation`.

For an observer-like predictive model to earn significance, its advantage should survive held-out regimes, matched external implementation, model misspecification, and resource-cost controls.

## Failure/withholding rules
Do not interpret predictive success as uniquely self-directed if a zero-latency external controller reproduces it. Do not interpret a delayed-external deficit as intrinsic agency; latency/locality is sufficient. Do not tune the rollout after seeing the held-out failures and then present the corrected policy as if the original discriminator succeeded.

## Scope
This benchmark is ordinary stochastic/model-predictive control. It does not establish consciousness, phenomenology, SoCT memory, objective collapse, or new physics.

## Next gate
Before recursive-depth O-1D4, the stronger next step is **O-1D3b — adaptive model calibration under distribution shift**.

The agent should be allowed to update its own transition/model parameters from experience, but the update rule must be frozen before held-out evaluation. Compare:

1. fixed predictive model,
2. adaptive internal predictive model,
3. adaptive external zero-latency model,
4. shuffled/model-update placebo,
5. oracle model upper bound.

The question becomes whether the system can detect that its self-model is wrong and improve the model governing its own future-state predictions. Only after that capability survives controls should recursive model depth be tested.
