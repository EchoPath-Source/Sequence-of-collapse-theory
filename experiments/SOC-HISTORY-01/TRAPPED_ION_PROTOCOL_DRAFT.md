# SOC-HISTORY-01-TI — Trapped-Ion Protocol Draft

**Status:** Platform-specific protocol draft; not yet preregistered and not evidence of a physical effect.  
**Parent protocol:** `PREREGISTRATION_DRAFT.md`  
**Target question:** Does randomized prior durable-record history predict a later trapped-ion quantum observable after ordinary present-state mismatch, measurement crosstalk, motional heating, drift, and preparation carryover are independently bounded?

## 1. Why trapped ions are the current preferred first platform

Trapped-ion systems are a strong match for SOC-HISTORY-01 because recent experiments demonstrate the operations the protocol needs:

- mid-circuit measurement and reset of selected ions;
- shelving/hiding of protected data ions during fluorescence measurement;
- spectroscopic isolation of neighboring ions;
- reset and reuse of measured ancilla ions;
- recooling after measurement;
- long-lived coherent qubits suitable for Ramsey-style phase readout.

These capabilities do not imply that the proposed SoCT effect exists. They only make the null-vs-history experiment operationally plausible.

## 2. Minimal ion register

Preferred minimal register:

```text
D = data / probe ion
A = record-bearing ancilla ion
S = spectator / nuisance-monitor ion (strongly preferred)
```

A two-ion implementation `D+A` is possible, but a third spectator ion is preferred because it can monitor apparatus-wide phase shifts, heating, and measurement crosstalk without carrying the target history label.

The exact species is not frozen. Current candidate implementations include `171Yb+` single-species architectures or mixed/shelved architectures with comparable mid-circuit measurement/reset capability.

## 3. Baseline quantum state

Prepare the data ion in a coherent Ramsey state

```math
|+>_D = (|0>_D + |1>_D)/sqrt(2).
```

The ancilla begins in

```math
|0>_A.
```

The spectator, if present, is prepared in a fixed calibration state or its own Ramsey state depending on the chosen nuisance-monitor design.

## 4. Target record-history operation

The target-history condition must create a physical record that is state-dependent on `D` and becomes amplified into the ordinary measurement apparatus/environment.

A generic sequence is:

1. prepare `D` in the designated pre-history state;
2. entangle or map the chosen binary property of `D` onto `A` using a calibrated two-ion operation;
3. protect/shelve `D` (and `S`, if present) from ancilla fluorescence;
4. perform fluorescence measurement of `A`, creating a macroscopic record;
5. reset/reinitialize `A`;
6. restore/unhide `D`;
7. recool as required;
8. explicitly reset/reprepare `D` into the common post-history target state used by every condition;
9. run the fixed probe interval and Ramsey readout.

The experiment therefore does **not** compare a measured state against an unmeasured state directly. It compares systems after a common present-state re-preparation, conditioned on different prior histories.

## 5. Sham-history operation

The sham must reproduce the ordinary preparation burden without creating the target `D -> A -> apparatus` informational relation.

Preferred sham:

1. execute the same number and timing of gates/pulses;
2. prepare `A` with the same marginal bright/dark distribution expected in the target condition, but independently of `D`;
3. perform the same fluorescence measurement duration and collection sequence;
4. apply the same reset, hiding/unhiding, and recooling operations;
5. reprepare `D` into the same common post-history target state.

This is stronger than a simple 'no measurement' sham because it attempts to match photon scattering, pulse burden, reset burden, and heating while removing the target state-dependent record relation.

## 6. Zero-history control

Prepare the same final target state without the target record-producing interaction.

Where possible, apply time-matched idle/control pulses so sequence duration does not identify condition.

## 7. History dose

The physical dose should be implemented by a preregistered number/strength of record-producing cycles rather than an abstract label alone.

Candidate mapping:

```text
dose 0.0 = no target record cycle
dose 0.5 = lower prespecified number/strength of target record cycles
dose 1.0 = full prespecified number/strength of target record cycles
```

The exact cycle count or interaction strength must be frozen from calibration data before target-outcome unblinding.

Dose should be quantified, where possible, by an operational record metric derived from the lower observation track, such as accessible ancilla record information plus persistence/redundancy diagnostics, rather than by pulse count alone.

## 8. Crossed physical assignment

History condition must not remain tied to one physical ion.

Where hardware permits:

```text
Block A: ion 1 = D, ion 2 = A
Block B: ion 2 = D, ion 1 = A
```

or use equivalent role exchange across matched ion pairs.

A history-associated residual that follows a particular ion instead of the randomized history assignment fails the interpretation gate.

## 9. Mandatory present-state matching diagnostics

Before primary outcome unblinding, target, sham, and zero-history conditions must satisfy frozen equivalence margins for the ordinary present state.

At minimum evaluate:

### Internal qubit state

- population/state-preparation fidelity;
- Ramsey phase/frequency immediately after re-preparation;
- Ramsey visibility/coherence;
- leakage outside the computational manifold where measurable.

### Motional state

- sideband-thermometry or equivalent estimate of mean motional excitation `n_bar`;
- mode-dependent heating where relevant;
- recooling endpoint equivalence.

### Measurement crosstalk / optical burden

- phase shift on protected data/spectator ions caused by ancilla fluorescence;
- fluorescence/scattered-light exposure proxy;
- shelving/hiding error;
- reset-induced disturbance.

### Apparatus state

- relevant laser-frequency/intensity monitor;
- magnetic-field or clock-frequency drift proxy;
- readout calibration;
- run-order/time block;
- spectator-ion phase/coherence when available.

Failure of any prespecified critical matching metric invalidates the SoCT-specific interpretation for that comparison.

## 10. Primary observable

Preferred primary observable: **differential Ramsey phase** of `D` after a fixed probe interval `T_p`.

A full Ramsey scan may be used for calibration, but the confirmatory estimator should be fixed before data collection, ideally using quadrature points that estimate phase without post-hoc fringe-shape selection.

Secondary observables may include:

- Ramsey visibility/coherence;
- transition probability at a fixed phase point;
- spectator-ion phase;
- motional excitation;
- leakage/readout error.

A smooth phase-vs-time shape is not a unique signature and must not be used alone to distinguish SoCT from drift.

## 11. Negative controls

At least two negative controls are recommended.

### Spectator control

`S` experiences the apparatus timing and broad environmental conditions but not the target informational history. A history-correlated shift on `S` suggests ordinary apparatus carryover.

### Reversed-information control

Use a sequence with comparable fluorescence/pulse burden but deliberately break the state-dependent `D -> A` mapping before measurement. If the target residual survives unchanged, the effect is more consistent with preparation burden than with record history.

## 12. Measurement/heating control is primary, not optional

Fluorescence measurement can impart state-dependent photon-recoil heating and can disturb neighboring ions through scattered light. Therefore:

```text
motional heating
measurement crosstalk
recooling quality
```

must be treated as primary nuisance variables in SOC-HISTORY-01-TI.

They may not be relegated to post-hoc explanation after a target-history coefficient is seen.

## 13. Trial sequence

One confirmatory trial is conceptually:

```text
randomize condition
-> initialize D/A/S
-> apply target, sham, or zero-history preparation
-> ancilla measurement/reset as assigned
-> recool / restore protected ions
-> common D re-preparation
-> verify/log present-state diagnostics
-> fixed probe interval
-> Ramsey readout of D
-> read spectator/control channels
-> log calibration + run metadata
```

Condition labels should remain blinded during quality-control decisions where operationally possible.

## 14. Statistical structure

Primary model inherits the parent preregistration:

```math
y_i = alpha
    + lambda_H H_i
    + beta_r R_i
    + beta_{ion} I_i
    + sum_k gamma_k X_{ik}
    + epsilon_i,
```

where `X_ik` must include the frozen trapped-ion nuisance set, including relevant motional, crosstalk, phase/frequency, and readout diagnostics.

The target coefficient `lambda_H` is uninterpretable if sham, spectator, ion-identity, or present-state mismatch diagnostics indicate a comparable ordinary explanation.

## 15. Required falsification / withholding gates

Do **not** interpret a nominal target-history residual as SoCT-specific if any of the following occur:

- target vs control state-preparation equivalence fails;
- motional-state equivalence fails;
- spectator phase/coherence follows history assignment;
- sham history produces a comparable residual;
- the effect follows physical ion identity rather than randomized role/history;
- removing/reversing the informational `D -> A` relation does not materially change the residual;
- the result is explainable by calibrated measurement crosstalk or heating;
- omitted-variable sensitivity shows an ordinary hidden carryover of plausible size could explain the effect;
- held-out replication fails.

## 16. Interpretation hierarchy

Allowed reporting labels remain:

```text
consistent with H0 within sensitivity
inconclusive / underpowered
ordinary present-state mismatch
ordinary explanation not sufficiently excluded
history-associated residual surviving preregistered controls
```

Even the last label is not equivalent to proof of a SoCT memory field.

## 17. Current preferred experimental architecture

The strongest first-pass architecture is:

```text
3-ion trapped-ion register
D = Ramsey probe
A = record ancilla measured/reset mid-circuit
S = spectator nuisance monitor
```

with target and sham conditions matched for fluorescence, pulse burden, reset, and recooling, followed by common re-preparation of `D` and a randomized differential Ramsey measurement.

This architecture directly incorporates the main failure modes discovered in Simulations 4b-4f instead of treating them as secondary corrections.

## 18. Items still requiring a laboratory-specific freeze

Before external preregistration:

- ion species and qubit encoding;
- trap architecture and ion count;
- exact entangling/map gate;
- fluorescence duration and readout method;
- data-ion hiding/shelving method;
- recooling method;
- exact sham bright/dark distribution matching;
- history-dose cycle counts;
- Ramsey probe time and quadrature phases;
- sideband-thermometry cadence;
- spectator protocol;
- state-equivalence margins;
- smallest effect size of interest;
- expected noise and sample size;
- mixed-model/random-effects structure;
- replication block size and stopping rule.

## 19. Current literature basis

This protocol design is informed by current trapped-ion demonstrations including:

- Yu et al., *In situ midcircuit qubit measurement and reset in a single-species trapped-ion quantum computing system*, Phys. Rev. Research 7, 043355 (2025), DOI `10.1103/qfvd-93lw`.
- Chen et al., *Noninvasive mid-circuit measurement and reset on atomic qubits*, Phys. Rev. A 113, 012606 (2026), DOI `10.1103/ct8k-jgsn`.
- trapped-ion mid-circuit measurement/reset work using spectroscopic decoupling and recooling in measurement-based computation, Nature Communications (2024/2025-era implementation literature).
- measurement-crosstalk suppression and mid-circuit reset demonstrations in trapped-ion systems, including Phys. Rev. A 104, 062440 (2021).

These references establish relevant experimental capabilities and nuisance mechanisms. They do not support the existence of SoCT memory.
