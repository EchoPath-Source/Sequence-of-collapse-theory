# O-1D3r — Semantically Matched Held-Out Autobiographical Policy Test

## Question
Once the oracle policy map is calibrated under the exact evaluator semantics, does autobiographical action–outcome history improve held-out value relative to compressed/zero/donor controls?

## Design
- history acquisition: 120-step exploratory prehistory;
- evaluation starts from matched present state `h=.95`;
- maintenance cost `.30`;
- paired future random streams;
- frozen policy map from O-1D3q: `.04 -> (.69,.70)`, `.08/.12 -> (.69,.76)`;
- 1,800 held-out episodes per arm/regime.

Arms: own, matched external own, shuffled pairing, compressed, donor, zero, oracle.

## Frozen result
Own history remains much more accurate about hidden degradation than shuffled/donor controls and improves held-out value over compressed/zero controls in the medium and harsh regimes:

- `d=.08`: own value `208.187` vs zero/compressed `202.332`;
- `d=.12`: own value `151.355` vs zero/compressed `134.753`.

However, shuffled pairing still maps almost always to the same medium/high policy and therefore matches or slightly exceeds own history in those regimes despite much worse self-model accuracy. At `d=.08`, shuffled/oracle value is `210.142`; at `d=.12`, shuffled/oracle value is `151.735`.

At low degradation, compressed/zero already map to the correct low policy, so own autobiography has little room to improve value.

The matched external own-history implementation is numerically identical to the internal implementation in all regimes.

## Interpretation
The positive claim earned is limited:

`accurate autobiographical self-dynamics can improve policy selection relative to uninformative controls when the policy map is nondegenerate.`

The stronger claim fails:

`autobiographical provenance is not yet uniquely privileged over a biased control that accidentally lands on the correct coarse policy.`

The remaining loophole is coarse policy binning. The next test must use a continuous/denser self-dynamics map and assess regret rather than category accuracy.
