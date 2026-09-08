# O-1D3n — Maintenance Economics / Opportunity-Cost Gate

## Question
Can an interpretable maintenance cost create a nondegenerate task environment in which different hidden self-dynamics genuinely favor different policies?

This is an environment-identification benchmark, not an observer-emergence result.

## Design
Use the O-1D3m two-parameter policy family (maintenance trigger + recovery target) and subtract a fixed value cost from every maintenance action. Sweep costs `.05, .15, .30, .50, .80` across degradation regimes `.04, .08, .12`. Oracle-labeled independent episodes select the best policy on the fixed grid.

## Frozen result
A nondegenerate region appears at low-to-moderate maintenance cost. At cost `.15`, low and medium degradation select recovery target `.88`, while high degradation selects `.78` (all choose trigger `.63`). At cost `.30`, low degradation still selects `.88`, while medium/high select `.78`.

Thus the environment finally supports regime-dependent oracle policies without adding a direct health reward.

The separation is modest and only one policy dimension changes, so it should not be oversold. But it is enough to reopen the held-out provenance test under a frozen environment.

## Next gate — O-1D3o
Freeze maintenance cost `.30` as the primary nondegenerate environment (with `.15` as sensitivity). Train the oracle mapping on independent data, then evaluate own action–outcome estimates, shuffled pairing, donor estimates, compressed/zero memory, oracle, and matched external controller on held-out paired episodes. The key test is whether better autobiographical system identification now selects the correct policy often enough to improve held-out value.
