# P4 Appendix — Materials and Measures

**Canonical track:** P4 — SOC-MZI awareness-modulated decoherence  
**Status:** Repo publication appendix draft  
**Purpose:** Provide a dedicated materials-and-measures companion to `SOC-MZI-01-preregistration.md`

---

## 1. Role of this appendix

This appendix isolates the physical apparatus, observer-state instrumentation, task structure, and measurement variables used in the current SOC-MZI protocol draft.

Its purpose is to make the protocol easier to review, refine, and replicate without forcing all implementation detail into the main preregistration narrative.

This appendix should be read together with:

- `papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md`
- `experiments/quantum/mach-zehnder-consciousness-test.md`
- `papers/math/soc-localization-memory-hamiltonian.md`

---

## 2. Optical apparatus target

Current target apparatus:

- Mach-Zehnder interferometer with 50:50 beamsplitters
- piezo-controlled phase stabilization
- path-length difference sweep range on the order of `0–100 μm`
- heralded single-photon source using SPDC near `810 nm`
- coincidence timing window on the order of `2 ns`
- silicon APDs or equivalent single-photon detectors
- acoustic shielding, vibration isolation, and temperature stabilization
- optional weak which-path polarization tagging with erasable markers

This list is the current protocol target, not yet a final procurement document.

---

## 3. Participant and observer-state instrumentation

Current human-observer instrumentation targets:

- EEG recording with sufficient temporal resolution for frontal-theta and related timing features
- eye-tracking capable of gaze-position tracking and fixation stability assessment
- pupilometry, if available through the same eye-tracking system
- optional auxiliary physiology channels for motion or state-quality monitoring

Operational observer variable used in the current draft:

```text
A(t) = [ MI(EEG, stimulus) / MI_max ] × PL(gaze, target)
```

Where:

- `MI(EEG, stimulus)` = task-linked mutual-information measure between EEG features and trial timing or stimulus timing
- `MI_max` = normalization constant from pre-task or baseline calibration
- `PL(gaze, target)` = gaze-target phase-locking or fixation-linked coherence term

This should remain explicitly labeled as an operational draft until the final implementation pipeline is frozen.

---

## 4. Task conditions

### High-A condition

Target characteristics:

- low-diversion fixation task
- sustained target engagement
- minimal competing cognitive load
- structured attention to the relevant task window without revealing actual which-path outcomes

### Low-A condition

Target characteristics:

- demanding secondary task or divided-attention condition
- stimulus present but de-emphasized
- lower expected observer-coherence metric under otherwise matched optical conditions

### Sham / null-information conditions

Required for serious testing:

- participant present but deprived of structured task-relevant information
- masking or attention conditions that preserve physical setup but collapse structured observer-linked coupling toward baseline
- no free-form reinterpretation after the fact; sham logic must be preregistered

---

## 5. Delay and timing structure

Current planned delay sweep:

```text
tau = [10, 20, 40, 80] microseconds
```

Timing windows:

- **early** = first third of trial window
- **late** = final third of trial window

Working interpretation:

- if the rate-law extension is meaningful, early windows may accumulate more effective observer-linked contribution than late windows under matched apparatus settings

---

## 6. Primary observables

### 6.1 Visibility

Primary observable:

```text
V = (N_max - N_min) / (N_max + N_min)
```

Measured per:

- participant
- condition
- delay
- timing window

### 6.2 Observer-state variables

Current operational measures of interest:

- EEG-derived task-linked coherence or information features
- gaze-target locking or fixation stability
- pupil diameter as arousal proxy
- trial-wise movement / motion quality metrics

### 6.3 Apparatus and environment covariates

Current covariate targets:

- piezo phase drift
- temperature fluctuations
- detector dark counts and saturation anomalies
- coincidence timing validity
- trial order and fatigue position

---

## 7. Exclusion implementation notes

### Trial-level exclusions

Planned examples:

- excessive motion
- fixation break beyond threshold
- detector saturation or spike anomaly
- invalid coincidence timing
- thermal instability within exclusion bounds

### Subject-level exclusions

Planned examples:

- excessive trial loss
- poor tracking quality
- EEG dropout or unusable signal fraction
- failed behavioral checks

Important boundary:

- exclusions are based on signal-quality or protocol-fidelity failure,
- not on whether a given outcome supports the hypothesis.

---

## 8. Synthetic-observer arm measurement notes

For SOC-AI-01 or equivalent control-arm work, the materials-and-measures analog should include:

- architecture type
- attention or representation metric definition
- perturbation method such as dropout or attention masking
- control conditions such as random observer and irrelevant-target sham tasks

The current repo should treat that as pending implementation detail until a dedicated AI appendix is added.

---

## 9. What still needs finalization

Before this appendix becomes a finalized lab handoff:

1. detector and source specifications should be frozen,
2. EEG and eye-tracking pipeline details should be fully versioned,
3. exact artifact thresholds should be fixed,
4. the final `A(t)` computation script should be archived,
5. and all sham conditions should be tied to preregistered logic.

---

## 10. Claim boundary

This appendix documents the current measurement and materials structure required to test the SOC-MZI rate-law hypothesis.

It should not be read as evidence that the hypothesis is already supported. Its value lies in making the protocol inspectable, criticizable, and reproducible.