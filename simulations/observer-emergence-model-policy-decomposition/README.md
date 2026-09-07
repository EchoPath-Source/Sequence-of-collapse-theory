# O-1D3c — System Identification vs Policy Adaptation

## Question
O-1D3b showed that a controller can improve its estimate of changed internal dynamics yet still make worse decisions. O-1D3c explicitly separates model adaptation from policy adaptation.

The experiment applies an abrupt shift in degradation rate after a common pre-shift period and compares six arms:

1. `frozen_model_frozen_policy`
2. `adaptive_model_frozen_policy`
3. `frozen_model_adaptive_policy`
4. `adaptive_model_adaptive_policy_internal`
5. `adaptive_model_adaptive_policy_external`
6. `oracle`

The internal and external adaptive arms are intentionally algorithmically identical. Their equality is a control on claims that internal implementation itself has functional privilege.

## Primary decomposition
Let `M` denote the transition/self-dynamics model and `pi` the action policy.

- Model value at fixed policy:
  `Delta J_model = J(M_adapt, pi_fixed) - J(M_fixed, pi_fixed)`
- Policy value at fixed model:
  `Delta J_policy = J(M_fixed, pi_adapt) - J(M_fixed, pi_fixed)`
- Joint adaptation value:
  `Delta J_joint = J(M_adapt, pi_adapt) - J(M_fixed, pi_fixed)`
- Internality discriminator:
  `Delta J_internal = J(internal adaptive) - J(external zero-latency adaptive)`

## Frozen result
The result does **not** support the simple claim that better system identification automatically improves control.

At post-shift degradation `0.08`:

- frozen model + frozen policy: reward `0.7553792`
- adaptive model + frozen policy: reward `0.7252720`
- frozen model + adaptive policy: reward `0.7492624`
- adaptive model + adaptive policy: reward `0.7486984`

At degradation `0.12`:

- frozen/frozen: `0.7198536`
- adaptive-model/frozen-policy: `0.6561536`
- frozen-model/adaptive-policy: `0.6718336`
- adaptive-model/adaptive-policy: `0.7094824`

At degradation `0.15`:

- frozen/frozen: `0.6937680`
- adaptive-model/frozen-policy: `0.6139096`
- frozen-model/adaptive-policy: `0.6443112`
- adaptive-model/adaptive-policy: `0.6875304`

The adaptive model often reduces low-health exposure while reducing reward because the fixed or adapting decision rule over-values preservation relative to immediate work opportunity.

## Central constraint

`better self-dynamics estimate != better policy`

and therefore

`self-model accuracy != functional observer advantage`.

A system can become more accurate about its own dynamics and still become behaviorally worse if the objective, cost model, or policy mapping is poorly calibrated.

## Internality control
The internal and zero-latency external adaptive arms are numerically identical across the full frozen grid:

`Delta J_internal = 0`.

Thus this benchmark provides no evidence that internal location of the adaptive model has unique causal value beyond ordinary information access and control architecture.

## Important caveat
The online estimator and policy updater are deliberately simple. The purpose is decomposition, not optimal control. The `oracle` arm is only a reference and shares the same imperfect policy family; it is not a globally optimal controller.

The result should therefore be read as a failure of the current model-policy architecture to establish a robust observer-like rung, not as evidence that adaptive model-based control cannot work.

## Revised observer criterion
A stronger candidate requires all of the following to survive held-out regimes:

1. measurable internal-state/system-dynamics information,
2. calibrated prediction improvement after distribution shift,
3. policy adaptation that converts that improvement into utility or future-capability gain,
4. placebo/ablation controls,
5. matched external-controller control,
6. explicit cost/resource accounting.

Only then should recursive model depth be tested.

## Next gate: O-1D3d
The next useful test is **objective-aware policy adaptation**: hold the learned self-dynamics model fixed while allowing the controller to learn the tradeoff between immediate reward and preservation cost from outcomes. This distinguishes learning `what happens to me` from learning `what I should do about it`.

This remains ordinary control/decision theory. It does not establish consciousness, agency, SoCT memory, objective collapse, or new physics.
