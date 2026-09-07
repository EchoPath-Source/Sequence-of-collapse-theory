# O-1D3g — Intervention-Defined Causal Boundary

## Question
Can the candidate agent boundary be defined by intervention-sensitive causal organization rather than by where computation is physically located?

This benchmark preserves the continuation-constrained architecture from O-1D3e/O-1D3f and intervenes separately on access to self-state, action authority, temporary state loss, and reconstruction from the system's own action-history records.

## Pre-freeze pilot rejection
An earlier exploratory pilot used a slow EMA self-state estimator. The raw-current-state comparator outperformed that estimator, showing that the pilot primarily measured a poor estimator rather than a causal boundary. That pilot was rejected before any result set was frozen. O-1D3g therefore retains the validated continuation controller from O-1D3f and changes only the causal-access/reconstruction variables.

## Frozen arms
1. `intact_closed` — current diagnostic, continuation-value controller, immediate action.
2. `external_zero_latency` — matched external implementation with identical information and action timing.
3. `state_severed_post150` — after step 150 the controller loses access to current self-state and receives an erroneously healthy signal.
4. `action_severed_10` — after step 150, 10% of proposed maintenance actions are forced to work.
5. `blackout_hold` — during two 20-step diagnostic blackouts, the last observed self-state is simply held.
6. `blackout_reconstruct_internal` — during blackout, the state estimate is propagated from the last observation using the actual intervening action ledger and the known expected transition model.
7. `blackout_reconstruct_external` — exact matched external reconstruction.
8. `blackout_shuffled_ledger` — same reconstruction machinery, but temporal correspondence is disrupted by drawing actions from the recent action-history marginal rather than using the actual intervening sequence.

## Frozen result
Internal and zero-latency external implementations remain exactly equivalent across the full grid.

Severing current self-state after step 150 causes catastrophic failure: failure rate is 1.0 in all tested regimes and mean lifetime collapses to roughly 169–196 steps.

Temporary state loss is also strongly damaging when the controller merely holds its last observation. Reconstruction from the actual action-history record restores a large fraction of the lost continuation capacity.

Representative degradation=0.08 results:

| condition | reward/episode | mean lifetime | failure rate |
|---|---:|---:|---:|
| intact closed | 381.494 | 500.000 | 0.000 |
| external zero latency | 381.494 | 500.000 | 0.000 |
| state severed | 132.286 | 174.202 | 1.000 |
| blackout hold | 237.009 | 315.783 | 0.654 |
| blackout reconstruct internal | 335.707 | 441.721 | 0.220 |
| blackout reconstruct external | 335.707 | 441.721 | 0.220 |
| blackout shuffled ledger | 324.691 | 434.208 | 0.247 |

At degradation=0.12, blackout reconstruction raises mean lifetime from 296.357 (hold) to 466.997 and reduces failure from 0.714 to 0.128. Shuffling the action-history correspondence weakens that recovery.

## Interpretation
The supported result is:

**A temporally correct causal record of the system's own intervening actions can materially improve reconstruction of a temporarily unavailable self-state and thereby preserve future sensing/action capacity.**

This is stronger than mere passive memory because the record has counterfactual functional value under intervention. It is still ordinary model-based control and does not establish consciousness, intrinsic agency, or novel physics.

The matched external reconstruction remains identical:

`J_reconstruct_internal == J_reconstruct_external_zero_latency`

So physical internality is again not privileged.

The shuffled-history degradation is useful but should not be oversold. It shows temporal correspondence matters in this specific reconstruction rule; it is not proof of autobiographical selfhood.

## Observer-emergence consequence
O-1D3g supports a more defensible candidate rung:

`record -> causal reuse -> self-state -> continuation value -> instrumental preservation -> intervention-sensitive state reconstruction`

The new ingredient is not merely persistence. It is the ability to use the system's own temporally ordered history to restore a control-relevant representation after disruption.

## EchoForm consequence
For persistent NPC/EchoForm engineering, this suggests a concrete design requirement: a ledger should not merely archive events. It should retain enough temporally ordered state/action provenance to reconstruct an agent's working self-state after restart, context loss, or partial memory corruption.

## Next gate — O-1D3h
Test **self-model reconstruction under component replacement**, not just temporary sensory blackout.

A stronger experiment should replace or erase a component of the working self-model and ask whether the remaining memory/ledger/causal loop can rebuild a functionally equivalent model without an externally supplied ground-truth state. Required controls should distinguish true reconstruction from simple reload, oracle restore, or fixed fallback behavior.
