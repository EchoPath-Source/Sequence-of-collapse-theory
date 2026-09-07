# O-1D3d — Objective-Aware Policy Adaptation

## Question
Can a system distinguish learning **what happens to it** from learning **what it should do about it** under distribution shift?

O-1D3b showed that a better self-dynamics estimate can reduce utility when an unchanged policy reacts too conservatively. O-1D3c separated model identification from policy adaptation. O-1D3d therefore asks whether an adaptive value policy can learn how much future health should matter relative to immediate productive sensing.

## Conditions
1. `frozen` — frozen wear model, frozen value policy.
2. `adaptive_model` — adaptive wear model, frozen value policy.
3. `adaptive_policy` — frozen wear model, adaptive health-value weight.
4. `joint_adaptive` — adaptive wear model plus adaptive health-value policy.
5. `external_joint` — zero-latency external implementation of the same joint adaptation.

All conditions face a baseline degradation rate of 0.03 until step 40,000, followed by a held-out post-shift degradation regime. Total length is 120,000 steps.

## Primary variables
The controller maintains:

- a degradation estimate, `deg_est`, representing its current self-dynamics model;
- a health-value weight, `health_weight`, controlling how strongly future capability is valued in the rollout policy.

These are deliberately separated. Better system identification does not automatically imply a better decision rule.

## Frozen results

| post-shift degradation | frozen J | adaptive-model J | adaptive-policy J | joint J | final joint health weight |
|---:|---:|---:|---:|---:|---:|
| 0.04 | 0.80151 | 0.80109 | 0.80287 | **0.80358** | 0.000 |
| 0.06 | 0.78957 | 0.77840 | **0.78997** | 0.78875 | 0.000 |
| 0.08 | 0.77507 | 0.73708 | **0.77780** | 0.76727 | 0.000 |
| 0.12 | **0.74882** | 0.68571 | 0.74790 | 0.68075 | 0.000 |
| 0.16 | 0.72536 | 0.71532 | **0.72612** | 0.68112 | 0.000 |

`external_joint` exactly matches `joint_adaptive` throughout the grid.

## Main result
The objective learner often drives the health-preservation weight toward zero. That is not automatically a bug: under the defined reward, health is instrumentally valuable only insofar as it supports continued productive sensing. The optimizer therefore learns that preserving health for its own sake is not the objective.

This yields the central distinction:

```text
self-preservation is not primitive value;
it is an instrumental strategy whose value depends on the objective.
```

The adaptive-policy-only arm modestly improves reward in several regimes by reducing excessive preservation pressure. In contrast, the joint adaptive arm often performs worse because the improved wear estimate still triggers excessive maintenance through the rollout dynamics.

Thus:

```text
better model + adaptive value weight != robust optimal regulation
```

A controller can correctly learn that its body/system is degrading faster, and can also learn that health itself should not be overvalued, yet still translate those two facts into a poor action policy.

## Internal vs external control
For every regime:

```text
J_joint_internal = J_joint_external_zero_latency
```

Therefore objective-aware adaptation remains reproducible by ordinary external control when information, timing, model, and policy are matched.

## Scientific interpretation
O-1D3d does **not** establish intrinsic goals, agency, consciousness, selfhood, or new physics. It shows only that observer-emergence work must distinguish at least four layers:

```text
self-state estimation
-> self-dynamics identification
-> value/objective representation
-> action-policy optimization
```

Success at one layer does not imply success at the next.

## Important negative result
A self-preserving system should not be defined merely as one that maximizes its own health. In this benchmark, maximizing health can lower the actual task objective. Any future claim about observer-like self-preservation must therefore specify **what future capability is being preserved and why it matters to the system's operational objective**.

## Revised next gate
The next benchmark should test **instrumental self-preservation under a survival/continuation constraint** without hard-coding self-preservation as a reward bonus.

Proposed O-1D3e:

- terminal loss of sensing capability if health crosses a failure boundary;
- no direct reward for health;
- reward only for successful future sensing/action;
- compare agents with and without a learned estimate of failure risk;
- match external zero-latency controller;
- test whether preservation emerges instrumentally from long-horizon task value.

That is a stronger discriminator than directly rewarding health, because continued self-maintenance would have to emerge as a consequence of preserving future access to the task rather than from an explicit self-preservation term.

## Scope
Synthetic stochastic control only. No SoCT memory source term is implied, and no Track-1 physical interpretation should be made from this result.
