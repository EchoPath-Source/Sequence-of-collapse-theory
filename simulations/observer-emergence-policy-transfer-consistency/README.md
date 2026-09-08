# O-1D3q — Policy-Transfer Consistency Gate

## Question
Do oracle-optimal policies remain optimal when calibrated under the exact state-estimator/controller semantics used in matched-state evaluation?

## Design
Maintenance cost is fixed at `.30`. The evaluator uses the same exponentially smoothed state estimate as O-1D3p. A fixed grid is searched independently for degradation regimes `.04/.08/.12`:

- trigger grid: `.45,.51,.57,.63,.69`
- recovery targets: `.70,.76,.82,.88,.94`
- 500 independent training episodes per candidate

## Frozen result
The semantically matched oracle optima are:

| degradation | mean training value | trigger | recovery target |
|---:|---:|---:|---:|
| .04 | 313.543 | .69 | .70 |
| .08 | 208.697 | .69 | .76 |
| .12 | 143.905 | .69 | .76 |

Thus the earlier O-1D3n policy map does not transfer unchanged once the controller uses smoothed self-state. The corrected evaluator retains a nondegenerate low-vs-medium/high policy distinction.

## Constraint earned
`oracle calibration must be evaluator-specific; apparently minor estimator semantics can change the policy optimum.`

## Next gate
Repeat the matched-state autobiographical provenance test using this corrected frozen policy map.
