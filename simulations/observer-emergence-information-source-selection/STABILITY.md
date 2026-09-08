# O-1D4k — Source-Selection Map Stability

Four independent 12,000-episode training replications were used to relearn the best information source in each of the eight initial self-estimate bins.

Source choices by bin across replications:

| bin | rep1 | rep2 | rep3 | rep4 | consensus |
|---:|---|---|---|---|---:|
| 0 | none | none | none | none | 1.00 |
| 1 | none | strong | none | none | .75 |
| 2 | strong | none | strong | strong | .75 |
| 3 | strong | none | none | cheap | .50 |
| 4 | none | cheap | strong | strong | .50 |
| 5 | strong | cheap | none | cheap | .50 |
| 6 | cheap | none | strong | none | .50 |
| 7 | none | none | none | none | 1.00 |

Mean pairwise agreement across the full source map was only 0.4583 (individual pairwise agreements .25, .50, .50, .375, .50, .625).

## Interpretation
The apparent information-source policy is unstable across independent training sets. This explains why O-1D4j did not transfer cleanly: most intermediate self-estimate regions do not support a reproducible source optimum under the current environment and sample size.

Constraint:

`a metacognitive source policy cannot be claimed when the source-value landscape itself is unstable.`

This parallels the earlier O-1D3s policy-oracle stability failure and is frozen rather than tuned away.

## Next gate
Use only independently reproducible source-selection regions. For unstable bins, fall back to a fixed baseline. Then test whether the stable subset transfers on new held-out episodes.
