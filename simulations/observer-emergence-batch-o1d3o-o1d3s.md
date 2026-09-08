# Observer-Emergence Batch Report — O-1D3o through O-1D3s

This batch followed the rule that each frozen result determines the next experiment.

## O-1D3o — Live-history held-out gate
Failed validity check because many episodes died before the intervention. Result frozen; no autobiographical claim made.

## O-1D3p — Matched-state history/evaluation separation
Separated history acquisition from evaluation and reset all arms to the same present state. Revealed that the transferred oracle policy from O-1D3n was not optimal under the smoothed-state evaluator.

## O-1D3q — Policy-transfer consistency
Refit oracle policies under the exact evaluation semantics. Recovered a nondegenerate map: low degradation prefers recovery target `.70`, while medium/high prefer `.76` at trigger `.69`.

## O-1D3r — Semantically matched held-out autobiography
Own action–outcome history improves value over zero/compressed controls in medium/high degradation, while matched external implementation remains identical. However, shuffled history often lands on the same coarse high-maintenance policy and can match the oracle despite poor self-model accuracy.

Supported limited statement:

`accurate autobiographical self-dynamics can improve policy selection relative to uninformative controls when the policy map is nondegenerate.`

Not supported:

`autobiographical provenance is uniquely privileged.`

## O-1D3s — Continuous policy-map stability
A denser oracle map failed replication: two independent fits agreed exactly at only 6/11 degradation points (54.5%). The continuous regret test was therefore withheld.

## Next gate — O-1D3t
Quantify policy-map uncertainty rather than selecting a single noisy winner. Estimate independent value distributions for candidate policies, define practical equivalence classes, and retain only degradation regions where policy separation is replicated and materially larger than Monte Carlo uncertainty. Only then resume autobiographical regret testing.
