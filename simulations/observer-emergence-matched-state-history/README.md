# O-1D3p — Matched-State History Acquisition / Evaluation Separation

## Question
Can autobiographical self-dynamics learned from a separate history phase improve future control when every evaluation arm starts from the exact same present physical state?

## Design
History acquisition is separated from evaluation. Each arm receives a 120-step prehistory generated under the same exploratory controller. The history produces a self-degradation estimate from recent WORK action–outcome pairs. Evaluation then resets all arms to `h=.95` and uses paired future random streams. Maintenance cost remains `.30`.

Arms: own history, matched external own-history implementation, shuffled action–outcome pairing, compressed state, donor estimate, zero memory, and oracle.

## Frozen result
Own history estimates degradation far more accurately than shuffled/donor controls and improves value over compressed/zero controls in medium and high degradation. However, the oracle policy transferred from O-1D3n was not actually optimal under this evaluator's smoothed-state controller semantics. In low degradation, a supposedly wrong policy achieved higher value than the transferred oracle policy.

Therefore the autobiographical-value comparison is not promoted as a positive result.

## Constraint earned
`policy calibration must be performed under exactly the same estimator/controller semantics used at evaluation.`

The next gate refits the oracle policy map under the exact matched-state evaluator before repeating the held-out provenance test.
