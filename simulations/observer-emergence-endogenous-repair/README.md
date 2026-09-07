# O-1D3h — Paired Reconstruction and Endogenous Repair

## Question
After an unannounced disruption of its operative self-state estimate, can a persistent agent detect the resulting mismatch and reconstruct a useful state estimate from its own retained history better than matched controls?

This benchmark follows O-1D3g. It deliberately separates four claims:

1. failure detection;
2. reconstruction of latent self-state;
3. recovery of the regulation loop;
4. improvement in downstream reward/continuation.

Success at an earlier layer does not imply success at a later one.

## Paired stochastic design
The first implementation revealed a confound: arms with different actions consumed different random numbers and therefore could drift into different stochastic futures for reasons unrelated to reconstruction quality.

The frozen implementation fixes this by pre-generating **paired potential-outcome streams** for every episode and time step:

- diagnostic noise;
- damage opportunity;
- task-hit draw;
- repair-success draw.

All arms therefore see the same exogenous opportunities at the same time index. Shuffling uses a separate RNG so placebo construction does not alter later environment randomness.

This correction is part of the scientific result and should remain documented.

## Conditions
- `intact_internal` — no disruption.
- `disrupted_no_repair` — estimator is corrupted but receives no explicit repair routine.
- `own_history_internal` — detects persistent prediction error and reconstructs from its own recent ordered diagnostic ledger.
- `own_history_external_zero_latency` — same reconstruction performed by a perfectly matched external controller.
- `shuffled_history` — same recent diagnostic values but temporal order destroyed.
- `stale_history` — early-episode history substituted for recent history.
- `donor_history` — unrelated agent/trajectory history substituted.
- `zero_memory` — no retained history; reset prior used.
- `oracle_repair` — true hidden health supplied at detection; reference only.

The disruption is not explicitly announced to the controller. Detection requires two consecutive prediction residuals above the frozen threshold.

## Frozen results
The key positive result is at the reconstruction layer.

At degradation 0.08, mean absolute self-state reconstruction error was:

| condition | mean reconstruction error |
|---|---:|
| oracle | 0.0000 |
| own ordered history | 0.1271 |
| donor history | 0.1591 |
| stale history | 0.2049 |
| shuffled history | 0.2059 |
| zero memory | 0.2656 |

At degradation 0.05, own ordered history was again best among non-oracle memory controls:

- own history: 0.1231
- shuffled: 0.1868
- stale: 0.1914
- donor: 0.2147
- zero memory: 0.2084

At degradation 0.12 the same ordering is broadly present for state-estimation error, with own history at 0.1230 versus shuffled 0.1818, stale 0.1853, donor 0.1736, and zero memory 0.2076.

Thus the agent's **own recent temporal history contains useful information for reconstructing its latent current state**.

## But reconstruction accuracy did not robustly improve utility
The stronger claim failed.

At degradation 0.08:

| condition | reward / episode | lifetime | failure rate |
|---|---:|---:|---:|
| intact | 354.557 | 476.507 | 0.0800 |
| disrupted, no explicit repair | 352.187 | 473.500 | 0.0900 |
| own-history repair | 352.423 | 474.477 | 0.0867 |
| shuffled history | 353.397 | 475.363 | 0.0833 |
| zero memory | 349.467 | 469.990 | 0.0967 |
| oracle repair | 351.440 | 473.873 | 0.0867 |

Own-history reconstruction reduced state-estimation error substantially, but did not outperform all placebo controls on realized reward or continuation. Even the oracle state reset did not produce a utility advantage in this policy family.

This reproduces an important lesson from O-1D3c/O-1D3d:

`better self-state estimate != better policy value`

and now more specifically:

`better autobiographical reconstruction != guaranteed behavioral advantage`

## Matched external control
`own_history_internal` and `own_history_external_zero_latency` are numerically identical across the frozen grid.

Therefore:

`endogenous-looking reconstruction != evidence of internal computational privilege`

The result remains fully compatible with ordinary estimation and control theory.

## What O-1D3h earns
Supported:

1. an unannounced self-model error can be detected from prediction residuals;
2. recent ordered own-history reconstructs current latent self-state more accurately than shuffled, stale, donor, or no-history controls in this benchmark;
3. the reconstructed loop usually returns to a low estimation-error region;
4. the same mechanism can be implemented externally with no loss when causal access is matched.

Not supported:

1. a unique reward or survival advantage for own-history reconstruction;
2. intrinsic agency;
3. consciousness or phenomenology;
4. a privileged metaphysical self-boundary;
5. any novel SoCT physics.

## Interpretation for EchoForms
This is still directly useful for persistent-agent engineering. A ledger can serve a function stronger than storage: after state corruption or restart, the agent can replay its own ordered history to rebuild a more accurate working self-state.

However, the result also warns against equating state restoration with useful behavior. EchoForm architecture should test both:

`memory -> reconstructed self-state`

and

`reconstructed self-state -> improved downstream decisions`

as separate acceptance gates.

## Next gate — O-1D3i: memory indispensability under an observation gap
O-1D3h reveals why the utility discriminator is weak: after corruption, current diagnostics remain available and the ordinary estimator quickly overwrites a bad reconstruction. This makes retained history informative but often unnecessary.

The next benchmark should create a predeclared temporary **observation gap** immediately after disruption. During that gap, the controller cannot use fresh diagnostic evidence and must rely on retained records to estimate its current state.

Required controls:

1. own recent ordered history;
2. shuffled recent history;
3. stale history;
4. donor history;
5. zero memory;
6. oracle state reference;
7. matched external zero-latency reconstruction.

Primary tests:

- state-estimation error during the observation gap;
- action quality during the gap;
- post-gap continuation and reward;
- recovery after fresh sensing resumes.

A positive result would show that autobiographical memory is not merely correlated with better reconstruction but becomes **causally necessary when present observation is unavailable**. It would still be ordinary control/information theory, but it would justify a stronger functional-memory rung in the observer-emergence ladder.
