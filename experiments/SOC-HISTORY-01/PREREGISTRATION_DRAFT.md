# SOC-HISTORY-01 — Preregistration Draft

**Status:** Protocol-design draft; not yet registered and not evidence of a physical effect.  
**Program:** SoCT operational observation / history-dependent memory  
**Primary purpose:** Test whether prior durable-record history predicts a later quantum observable after ordinary present-state differences and plausible history-correlated carryover have been independently bounded.

## 1. Research question

Can two experimental ensembles that are matched with respect to the prespecified ordinary present-state description nevertheless show a reproducible later difference that follows randomized prior record-history dose?

This protocol does **not** assume that such a difference exists. The standard/null expectation is no history-specific residual once the relevant present physical state and ordinary nuisance channels are controlled.

## 2. Hypotheses

### H0 — ordinary-state sufficiency

After conditioning on the prespecified present-state variables, hardware assignment, run order, measured carryover, and sham controls, prior record-history dose has no independent predictive coefficient:

```math
lambda_H = 0.
```

### H1 — exploratory SoCT history-memory extension

A residual follows randomized durable-record history dose after the same controls:

```math
lambda_H != 0.
```

H1 is not accepted merely because the fitted coefficient is nonzero. All validity gates below must also pass.

## 3. Platform requirements

The first implementation should use a platform capable of:

- repeatable preparation of a two-level coherent state;
- controlled entangling/measurement-like interactions with a record-bearing ancilla or environment;
- reversal/reset operations sufficient to match a prespecified final target state;
- repeated phase/coherence readout;
- independent monitoring of preparation-induced nuisance channels;
- randomized and blinded trial assignment where practical.

Candidate platforms may include superconducting qubits, trapped ions, neutral atoms, photonic qubits, or another architecture satisfying the requirements. **No platform is selected in this draft.** Platform-specific pulse sequences and tolerances must be frozen in a later amendment before data collection.

## 4. Experimental conditions

Each trial receives a randomized condition label.

### 4.1 Target history

A record-producing interaction is applied with prespecified history dose `d`. The protocol then restores the target system to the prespecified present-state preparation before the probe interval.

### 4.2 Sham history

A preparation sequence matched as closely as possible in duration, control burden, energy/pulse exposure, and apparatus usage, but designed not to create the target durable record structure.

### 4.3 Zero-history control

The target present state is prepared without the target record-producing history.

### 4.4 Negative-control observable/channel

At least one observable or auxiliary channel is chosen a priori that should respond to broad apparatus/systematic contamination but is not predicted to carry the specific target-history effect.

## 5. History dose

The primary dose family is fixed conceptually as:

```text
0, 0.5, 1.0
```

with signed/crossed assignment between physical arms when the platform supports it. The physical meaning of one dose unit must be defined from the operational record-production source before registration, using quantities such as accessible record information, persistence, redundancy, and recoverability.

The dose definition may not be changed after outcome inspection.

## 6. Randomization and crossing

- Trial condition is randomized.
- History-bearing and control conditions are crossed between physical qubits/arms/devices where possible.
- Run order is randomized or blocked-randomized.
- Analysis labels should be blinded until state-matching and exclusion checks are finalized when operationally feasible.
- Hardware identity is included as a nuisance/block factor rather than allowed to define history condition.

## 7. Present-state matching gate

Before the primary history comparison, the experiment must demonstrate equivalence/bounded difference for a prespecified vector of ordinary present-state diagnostics.

Platform-specific diagnostics may include:

```text
population/state fidelity
phase/frequency
coherence/dephasing metric
temperature/heating proxy
pulse/control exposure
ancilla/environment reset quality
readout calibration
relevant local field/noise monitor
```

Equivalence margins must be fixed from calibration data **before** unblinding the target outcome.

Failure of the matching gate means the affected comparison is classified as `ordinary present-state mismatch`; it is not eligible for a SoCT-specific interpretation.

## 8. Primary observable

The primary observable should be a platform-appropriate phase/coherence statistic measured after a fixed probe interval or prespecified set of probe times.

The exact observable, units, probe time(s), and preprocessing pipeline must be frozen in the platform amendment.

A smooth exponential phase trajectory alone is explicitly **not** considered unique evidence, because Simulation 4b showed that low-order ordinary nuisance terms can closely mimic that shape over finite windows.

## 9. Primary statistical model

The core model is a randomized history-dose regression/mixed model of the form

```math
y_i = alpha
    + lambda_H H_i
    + beta_r R_i
    + beta_hw HW_i
    + sum_k gamma_k X_{ik}
    + epsilon_i,
```

where:

- `H_i` is the preregistered target history-dose regressor;
- `R_i` captures run order/block drift;
- `HW_i` captures crossed hardware/device identity;
- `X_ik` are prespecified measured ordinary carryover covariates.

If repeated measures/hierarchical hardware are used, the corresponding random-effects structure must be fixed before data collection.

## 10. Sham and negative-control tests

A target-history coefficient is not interpretable by itself.

Required companion tests:

1. sham-history coefficient;
2. negative-control observable/channel coefficient;
3. hardware-by-history interaction;
4. history-by-run-order interaction where relevant;
5. present-state diagnostic differences by history assignment.

A target residual that is mirrored by sham history or tracks hardware/preparation burden is treated as evidence for an ordinary confound, not as support for H1.

## 11. Measurement-error calibration

Covariate measurement error must be estimated from independent repeated calibration or replicate measurements where possible.

The analysis must report how the target-history coefficient changes under plausible calibration uncertainty. Known covariates are not treated as perfectly measured by default.

## 12. Hidden-variable sensitivity analysis

The primary report must quantify how strong an omitted history-correlated ordinary variable would need to be to reduce the target-history result below the prespecified evidentiary threshold.

A nominal target effect is classified as `ordinary explanation not sufficiently excluded` if a hidden carryover of a magnitude compatible with calibration/sham behavior could account for it.

## 13. Exclusions

Trial-level exclusions are allowed only for prespecified technical failures such as:

- failed state preparation outside the frozen tolerance;
- failed reset;
- readout/calibration failure;
- logged hardware fault;
- corrupted/missing trial record.

Exclusions may not depend on whether the outcome favors H0 or H1. Counts and reasons are reported by randomized condition.

## 14. Primary interpretation gates

A history-specific result is eligible for further SoCT interpretation only if **all** of the following pass:

1. randomized history-dose coefficient meets the frozen statistical/effect-size criterion;
2. ordinary present-state matching passes its equivalence margins;
3. sham-history channel does not show a comparable effect;
4. negative-control channel remains within its frozen bound;
5. the effect crosses with history assignment rather than physical hardware;
6. the result survives prespecified drift/block adjustment;
7. measurement-error sensitivity does not erase the result under calibrated uncertainty;
8. omitted-variable sensitivity indicates that an ordinary hidden carryover large enough to explain the result is inconsistent with independent bounds;
9. the effect replicates in a held-out block or independent run according to the frozen replication rule.

If any gate fails, the primary conclusion is **not** `SoCT memory detected`.

## 15. Outcome classifications

The analysis must use one of the following conservative labels:

- `consistent with H0 within sensitivity`;
- `inconclusive / underpowered`;
- `ordinary present-state mismatch`;
- `ordinary explanation not sufficiently excluded`;
- `history-associated residual surviving preregistered controls`.

Even the final label is not equivalent to proof of SoCT. It would justify replication and comparison against explicit alternative physical models.

## 16. Power and sample size

Sample size is **not yet frozen** because the physical platform, observable noise, equivalence margins, and smallest effect size of interest have not been selected.

Before registration:

1. obtain independent pilot/calibration noise estimates without testing the target history claim;
2. define the smallest effect size of scientific interest;
3. power the randomized history-dose coefficient and the state-matching equivalence tests;
4. include multiplicity/replication requirements;
5. freeze sample size before unblinding target-history outcomes.

No post-hoc sample extension based on the sign or significance of the target effect is allowed.

## 17. Relation to the simulation ladder

This protocol incorporates the failures and lessons of Simulations 1–4f:

- correlation is not automatically an accessible record;
- decoherence is not automatically the designated record;
- reversible record creation differs from durable distributed record formation;
- a smooth history phase is not a unique signature;
- randomization does not remove preparation carryover;
- regression adjustment does not remove unmeasured or mismeasured carryover;
- sham histories and negative controls are required to diagnose history-correlated ordinary structure.

## 18. Claim boundary

SOC-HISTORY-01 is designed to test a history-dependent residual. It does not directly test consciousness, subjective awareness, observer emergence, gravity, or spacetime curvature.

Conscious-access experiments remain downstream and should not begin until the lower physical history-memory channel has a stable operational definition and an experimentally defensible null comparison.

## 19. Items that must be frozen before external preregistration

- physical platform and apparatus;
- exact target-history operation;
- sham operation;
- operational history-dose calibration;
- target state and matching diagnostics;
- equivalence margins;
- primary observable and probe time(s);
- nuisance covariates;
- negative-control observable/channel;
- exact statistical model;
- smallest effect size of interest;
- alpha/error-control strategy;
- sample size/power;
- exclusion rules and replication criterion.

Until those fields are fixed, this document remains a **preregistration draft**, not a completed preregistration.
