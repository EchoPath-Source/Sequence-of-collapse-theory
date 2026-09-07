# O-1D3b — Adaptive Self-Model Calibration Under Distribution Shift

## Question
Can a system detect that its own predictive model is wrong after its internal degradation dynamics change, update that model online, and thereby improve future regulation?

This is the next gate after O-1D3, where a fixed predictive controller failed to generalize cleanly across harsher degradation regimes.

## Design
The system begins with an assumed degradation probability of `0.02`. Halfway through each run, the true degradation probability shifts upward to one of:

- `0.04`
- `0.06`
- `0.08`
- `0.10`
- `0.15`

Repair success remains fixed at `0.90`. Diagnostic noise is `0.05`.

The adaptive controller classifies large observed work-state drops as degradation shocks and maintains a rolling Beta-smoothed estimate over the last 200 work events. That estimate is inserted into the same short-horizon planner used in O-1D3.

## Conditions
1. **reactive** — current-state threshold only; no predictive model.
2. **frozen predictive** — predictive controller that permanently assumes the pre-shift degradation rate `0.02`.
3. **adaptive internal** — updates its own estimated degradation rate from observed self-state transitions.
4. **adaptive external, zero latency** — identical update rule, diagnostic stream, and planner implemented outside the regulated system.

## Results
The adaptive estimator successfully tracks the changed degradation process in most regimes. Representative final estimates include:

- true post-shift `0.04` -> estimate `0.0446`
- true post-shift `0.06` -> estimate `0.0594`
- true post-shift `0.08` -> estimate `0.0842`
- true post-shift `0.15` -> estimate `0.1535`

The `0.10` run ended at `0.0743`, showing finite-window estimator variance and incomplete calibration in that seed.

However, improved model calibration did **not** produce a robust utility advantage. At post-shift degradation `0.08`:

| condition | total reward/step | post-shift reward | maintenance rate | low-health fraction |
|---|---:|---:|---:|---:|
| reactive | 0.78493 | 0.75194 | 0.08589 | 0.02861 |
| frozen predictive | 0.79011 | 0.75715 | 0.09699 | 0.01916 |
| adaptive internal | 0.78623 | 0.74642 | 0.11305 | 0.00554 |
| adaptive external | 0.78623 | 0.74642 | 0.11305 | 0.00554 |

At post-shift degradation `0.15`, the adaptive controller estimates the new degradation probability accurately but over-maintains strongly:

- frozen predictive post-shift reward: `0.69525`
- adaptive post-shift reward: `0.63795`
- frozen maintenance rate: `0.12487`
- adaptive maintenance rate: `0.16641`

The adaptive controller does keep the system out of low-health states more effectively, but pays too much opportunity/maintenance cost under the frozen planner objective.

## Central result

`better self-model calibration != better self-regulation`

and, again:

`adaptive internal controller == matched zero-latency external adaptive controller`

for every committed condition.

Thus O-1D3b establishes a useful separation among:

1. detecting model error,
2. updating an internal dynamics estimate,
3. translating that improved estimate into a better policy.

The first two can succeed while the third fails.

## Interpretation
This is a scientifically useful negative result. It prevents us from defining observer-like recursion merely as "the system updates a model of itself." A model update earns stronger functional significance only if its calibration improvement causally improves action selection under held-out conditions and matched resource costs.

The external-controller equality also remains decisive: nothing in this benchmark demonstrates a privileged role for internal implementation.

## Scope
This is ordinary online system identification and model-predictive control. It is not evidence for consciousness, agency, subjective experience, SoCT memory, objective collapse, or new physics.

## Revised next gate — O-1D3c
Before recursive model depth, separate **system identification** from **policy adaptation**.

O-1D3c should compare:

- accurate adaptive model + frozen policy,
- accurate adaptive model + policy recalibration,
- deliberately miscalibrated model + adaptive policy,
- oracle model + oracle-tuned policy,
- matched external adaptive controller.

The key quantity becomes whether reduced self-prediction error produces a held-out improvement in realized long-horizon utility after policy recalibration, rather than merely inducing more conservative behavior.

Only after that causal chain is demonstrated should Track 2 advance toward recursive modeling of the model/policy itself.
