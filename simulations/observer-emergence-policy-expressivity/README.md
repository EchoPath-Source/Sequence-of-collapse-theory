# O-1D3m — Policy Expressivity Gate

## Purpose
Before attributing any held-out advantage to autobiographical self-modeling, verify that the policy class can actually express different optimal responses to different hidden self-dynamics.

O-1D3l failed because its one-dimensional threshold calibration collapsed to the same boundary value for every degradation regime.

O-1D3m expands the policy to two parameters:
- maintenance trigger;
- recovery target (continue maintenance until estimated state exceeds this target).

The grid is trained only on independent oracle-labeled episodes.

## Frozen result
The expanded policy still selected the same edge solution in every regime:

| degradation | best trigger | best recovery target | training reward |
|---:|---:|---:|---:|
| .04 | .63 | .88 | 397.308 |
| .08 | .63 | .88 | 381.260 |
| .12 | .63 | .88 | 364.432 |

Therefore the memory-provenance evaluation is **withheld**. Running own/shuffled/donor memory through a mapping that does not distinguish the regimes would manufacture an uninformative comparison.

## Interpretation
This is a second negative policy gate. The present environment makes aggressive maintenance broadly optimal because maintenance has too little opportunity cost relative to avoiding catastrophic degradation. The correct response is not to keep increasing policy complexity until a desired distinction appears.

Instead the next experiment must modify the task economics in a preregistered, interpretable way so that maintenance and productive work have a genuine tradeoff. Only after oracle policies separate across regimes should autobiographical estimates be evaluated.

## Next gate — O-1D3n
Introduce an explicit maintenance resource/opportunity budget or task deadline. Predeclare the budget/cost sweep and identify regions where oracle-optimal policies differ across degradation regimes. Treat this as environment-identification, not an observer result. Then freeze one nondegenerate regime family before testing memory provenance.
