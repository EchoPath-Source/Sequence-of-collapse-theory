# O-1D3o — Held-Out Autobiographical Policy Selection (Live-History Gate)

## Intended question
With maintenance cost fixed at 0.30 and the O-1D3n regime-dependent policy map frozen, does an autobiographical estimate of hidden self-degradation improve held-out control?

## Frozen validity failure
The first implementation used a neutral pre-intervention controller until `t=220`. That controller was too weak: most medium/high-degradation episodes failed before the autobiographical estimate could be formed.

Representative reach behavior was effectively absent in the harsh regimes, with failure rates near 1.0 before the intended decision point. The resulting arm comparisons are therefore not interpretable as a test of autobiographical policy selection.

## Constraint earned
`a held-out self-model test is invalid if selection-on-survival determines which episodes reach the self-model intervention.`

The failure is preserved rather than tuned away.

## Next gate
Use a robust common pre-intervention policy, then repeat the test. If survival-to-intervention remains strongly regime-dependent, separate history acquisition from evaluation and reset all arms to a matched present state.
