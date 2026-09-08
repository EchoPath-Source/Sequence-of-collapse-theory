# O-1D3l Frozen Interpretation

The first held-out calibration attempt fails as a useful observer-emergence discriminator.

The training sweep selected the same boundary value (`threshold = .66`) for all three hidden degradation regimes. Consequently the learned policy mapping collapsed to a constant and discarded the very self-dynamics information O-1D3k had shown to be recoverable.

The held-out evaluation therefore does not support `self-history -> calibrated policy advantage`. In the moderate and harsh regimes all memory/model arms become identical and fail rapidly. This is not evidence against autobiographical information itself; it is evidence that the chosen one-dimensional threshold policy family is too impoverished and that the benchmark's pre-gap controller is not robust enough under this reimplementation.

The result is frozen rather than tuned away.

## Constraint earned

`better self-model + degenerate policy family != adaptive advantage`

A stronger next test must first establish a policy family capable of expressing different optimal responses to different self-dynamics, while preventing direct tuning on held-out outcomes.

## Next gate
O-1D3m should separate **policy expressivity** from **memory provenance**. Use a small two-parameter policy (maintenance trigger + recovery target or maintenance burst length), train it only on independent oracle-labeled episodes, verify that distinct degradation regimes genuinely select distinct policies, freeze those policies, and only then feed own/shuffled/donor/zero estimates into the frozen mapping on held-out paired episodes.
