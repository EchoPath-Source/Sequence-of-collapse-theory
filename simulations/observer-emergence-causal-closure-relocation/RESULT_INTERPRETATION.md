# O-1D3f Frozen Interpretation

## Result
The controller-relocation benchmark rejects physical controller location as a sufficient functional criterion for observerhood in this model.

Across every frozen regime, the closed/internal controller and the zero-latency relocated controller are numerically identical. For example, at degradation 0.05 both achieve reward/episode 402.726, mean lifetime 500, failure rate 0, and maintenance rate 0.104196.

Thus the primary location contrast is

`Delta J_location = J_internal - J_relocated,zero-latency = 0`

throughout the grid.

## Causal connectivity matters
Perturbing information/action timing strongly degrades continuation. At degradation 0.05, four-step sensing latency reduces reward/episode from 402.726 to 241.346, mean lifetime from 500 to 351.164, and raises failure rate from 0 to 0.522. Four-step actuation latency gives the same frozen result in this discrete benchmark.

At degradation 0.08, four-step latency produces failure rate 0.6867 versus 0 for the closed reference.

Small 2% channel errors are much less destructive than four-step latency, while 2% disconnects have modest effects in these regimes. This shows that the *kind* of causal impairment matters; it is not simply an external-versus-internal label.

## Scientific conclusion
The supported statement is:

> Instrumental self-preservation in this benchmark depends on timely closed-loop causal organization, not on the spatial location of the controller.

This is ordinary control theory. It does not establish consciousness, intrinsic agency, phenomenology, a metaphysical self boundary, or novel SoCT physics.

## Important structural lesson
The observer-emergence program should stop treating `internal` as synonymous with `self`. A stronger operational candidate is **causal closure**: the extent to which the variables needed for continued sensing, estimation, decision, and actuation are mutually maintained by the loop itself.

However, ordinary feedback systems are causally closed in weak senses. Therefore causal closure alone is also too weak.

## Next discriminator: O-1D3g — reconstructive closure
The next test should ask whether the loop can restore a damaged component required for its own future operation.

Candidate comparison:
1. closed loop with no reconstruction capacity;
2. loop that detects degradation of its estimator/sensor/controller and restores it using retained internal structure;
3. matched external repair controller with identical information/resources;
4. shuffled or misdirected repair control;
5. component-ablation cases where reconstruction information itself is damaged.

A useful quantity is

`R_reconstruct = P(function restored | component damage, available retained model)`.

A stronger observer-like criterion would require not merely preserving a state variable but preserving or rebuilding the **causal machinery that performs preservation**.

Even a positive result remains ordinary adaptive/reconfigurable control unless it survives matched external reconstruction controls and demonstrates a nontrivial organizational distinction.
