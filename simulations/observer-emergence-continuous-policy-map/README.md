# O-1D3s — Continuous Self-Dynamics Policy-Map Stability Gate

## Question
Can the coarse policy-bin loophole from O-1D3r be removed by learning a denser mapping from hidden self-degradation to maintenance policy and evaluating regret?

## Design
Before running any autobiographical provenance comparison, the oracle policy map itself must replicate.

- degradation grid: `.03` through `.13` in `.01` increments;
- trigger fixed at `.69` from O-1D3q;
- recovery targets: `.68,.72,.76,.80,.84,.88`;
- maintenance cost `.30`;
- exact smoothed-state evaluator semantics;
- 180 independent training episodes per candidate;
- two independent seed families fit separate oracle maps.

## Frozen result
The first fitted map was highly non-monotonic:

`.03:.72, .04:.76, .05:.68, .06:.76, .07:.76, .08:.72, .09:.68, .10:.72, .11:.76, .12:.76, .13:.76`

An independent refit produced:

`.03:.68, .04:.68, .05:.68, .06:.76, .07:.72, .08:.76, .09:.68, .10:.76, .11:.76, .12:.76, .13:.76`

Exact policy agreement was only `6/11 = 54.5%`.

## Interpretation
The continuous provenance/regret test is **withheld**. The apparent local oracle optimum is not stable enough to serve as a trustworthy target. A flat/noisy policy landscape can make small Monte Carlo differences look like meaningful dynamics-dependent policy structure.

## Constraint earned
`a continuous self-model cannot be credited with policy regret reduction against an unstable oracle map.`

## Next gate
Map uncertainty itself must be characterized. Increase independent training replication and estimate value differences/confidence intervals between top candidate policies at each degradation value. Collapse neighboring policies into equivalence classes when their value differences are practically negligible. Only regions with replicated, practically meaningful policy separation should be used for the next autobiographical regret test.
