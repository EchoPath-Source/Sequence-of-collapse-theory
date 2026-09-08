# O-1D3v — Maintenance-Burst Policy

## Question
Can a discrete maintenance-duration policy create reproducibly different optimal responses to different hidden self-dynamics?

## Design
Use the same synthetic continuation environment, trigger self-maintenance when the smoothed self-state drops below 0.69, and compare fixed maintenance burst lengths of 1–5 steps. Maintenance cost is 0.30. Evaluate degradation d=0.04, 0.06, 0.08, 0.10, and 0.12 across two independent 600-episode replications.

## Frozen result
Two reproducibly distinct basins appear:

- d=0.04 favors burst length 1 in both replications.
- d=0.08 favors burst length 2 in both replications.

Intermediate and harsher regimes remain less stable: d=0.06 splits between 1 and 2; d=0.10 splits between 3 and 2; d=0.12 splits between 3 and 2.

## Interpretation
This is the first policy family in this branch to provide two clear, independently reproduced self-dynamics-dependent actions suitable for a provenance test. The next gate should therefore use only d=0.04 and d=0.08 and ask whether autobiographical action–outcome history selects burst 1 vs burst 2 correctly on held-out paired futures.
