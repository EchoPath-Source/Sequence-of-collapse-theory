# O-1D3t — Policy-Landscape Uncertainty

## Question
Where is the maintenance-policy landscape stable enough that a 'correct policy' is meaningfully defined?

## Design
Using the exact O-1D3r evaluator semantics and maintenance cost 0.30, compare recovery targets 0.68, 0.72, 0.76, 0.80, and 0.84 at trigger 0.69 across degradation d=0.03..0.13. Two independent 1,000-episode replications identify the best policy at each d. Candidate stable regions are then checked with paired 3,000-episode differences and 95% confidence intervals.

## Frozen result
Most low/mid degradation points do not reproduce the same winning policy across replications. Agreement occurs at d=0.09, 0.10, 0.11, and 0.13, all favoring target 0.76. Paired comparisons show the strongest stable margins at d=0.10, 0.11, and 0.13. At d=0.09, target 0.76 vs 0.72 remains practically/statistically ambiguous because the 95% CI crosses zero.

Representative paired differences for target 0.76:

- d=0.10 vs target 0.72: ΔJ=10.73, 95% CI [7.11, 14.35]
- d=0.11 vs target 0.72: ΔJ=6.19, 95% CI [2.59, 9.80]
- d=0.13 vs target 0.72: ΔJ=8.81, 95% CI [5.39, 12.23]

## Interpretation
A policy winner should not be treated as meaningful where independent replication changes the winner or paired differences are practically negligible. This invalidates broad autobiographical-regret tests across the full d range.

Constraint earned:

`self-knowledge can only reduce policy regret where policy regret is itself well-defined.`

The next gate should search for two reproducibly different policy basins rather than forcing provenance comparisons inside a flat landscape.
