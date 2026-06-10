# SOC-MZI-01 — Awareness-Modulated Decoherence in Mach-Zehnder Interferometry

**Canonical track:** P4 — SOC-MZI awareness-modulated decoherence  
**Status:** Repo publication draft / preregistration-ready protocol basis  
**Claim level:** Testable experimental proposal; not empirical confirmation  
**Source basis:** Rewritten from the October 27, 2025 public article and subsequent protocol refinements for repository publication

---

## Purpose

This document captures the current preregistration-ready framing for the SOC-MZI experiment in a format suitable for repository publication and scientist-facing review.

It is written to test a narrow empirical claim:

> An operationally defined observer-coherence variable may modulate the effective decoherence rate in a Mach-Zehnder interferometer without altering Born-rule outcome statistics.

This document does **not** claim that the Sequence of Collapse theory has been confirmed. Its purpose is to define the experiment cleanly enough that the underlying equation set can be tested, constrained, or falsified.

---

## 1. Theoretical background

Standard quantum mechanics predicts interference visibility decay under environmental decoherence. The working SOC-MZI extension adds an observer-linked rate term:

```text
lambda_eff = lambda_env + lambda_c · A(t)
```

Where:

- `lambda_eff` = effective decoherence / dephasing rate under the model
- `lambda_env` = environment-driven decoherence term
- `lambda_c` = free coupling coefficient to be estimated or bounded
- `A(t)` = normalized operational observer-coherence or information-coherence index

The protocol is designed around four model-level predictions:

1. **Rate modulation:** `V(tau, A_high) < V(tau, A_low)` at fixed delay `tau`
2. **Timing asymmetry:** early structured observer-coupled windows suppress visibility more strongly than late windows
3. **Born-rule preservation:** marginal outcome probabilities are unchanged on ensemble average
4. **No-signaling:** no superluminal information transfer is implied by the model

---

## 2. Primary hypotheses

### H1a — Main effect

At fixed interferometer delay:

```text
Delta V = V(A_low) - V(A_high) > 0
```

### H1b — Timing asymmetry

Early observer-coupled windows should show stronger suppression than late windows:

```text
Delta V_early > Delta V_late
```

### H1c — Dose response

Visibility suppression should scale monotonically with block-averaged or trial-level `A(t)`.

### Null model

The null expectation is:

- no separation between high- and low-`A(t)` conditions beyond measurement uncertainty,
- no early/late asymmetry,
- and no reproducible relationship between `A(t)` and residual visibility after apparatus and environment controls.

Primary confirmatory threshold in the current draft:

```text
Sidak-corrected alpha = 0.017
```

---

## 3. Experimental design

### 3.1 Apparatus

Planned baseline apparatus:

- Mach-Zehnder interferometer with 50:50 beamsplitters
- piezo-controlled phase-locked arms
- path-length difference range `Delta l = 0–100 micrometers`
- heralded single-photon source via SPDC at `lambda = 810 nm`
- coincidence window near `2 ns`
- silicon APDs with low dark count and sub-nanosecond jitter
- active thermal stabilization, vibration isolation, and acoustic shielding
- weak which-path polarization tags erasable via quarter-wave plates

This apparatus description should be treated as the current protocol target, not a fixed final build sheet.

### 3.2 Awareness modulation

Initial protocol target:

- `N = 24` human participants
- within-subject design
- QRNG-driven block assignment

Current proposed operationalization:

```text
A(t) = [ MI(EEG, stimulus) / MI_max ] × PL(gaze, target)
```

Where:

- `MI(EEG, stimulus)` = mutual information between neural signal features and task timing
- `MI_max` = normalization constant derived from baseline or pre-task distribution
- `PL(gaze, target)` = gaze-target phase-locking measure

High- vs low-`A` conditions are induced through a dual-task design:

- **High-A blocks:** simple fixation / low cognitive diversion
- **Low-A blocks:** cognitively demanding task with stimulus present but de-emphasized

Important protocol boundary:

- participants do **not** receive true which-path outcomes,
- displays should not function as ordinary measurement readout channels,
- and all operational mappings must be preregistered before confirmatory testing.

### 3.3 Timing manipulation

Current planned delay sweep:

```text
tau = [10, 20, 40, 80] microseconds
```

Early vs late events are defined relative to trial timing rather than wall-clock time.

The working prediction is that longer exposure to elevated `A(t)` produces stronger effective suppression in early windows than late windows.

---

## 4. Outcome measures

### 4.1 Primary observable

Interference visibility:

```text
V = (N_max - N_min) / (N_max + N_min)
```

Measured per:

- subject
- condition
- delay
- timing window

### 4.2 Primary contrasts

1. Mean visibility contrast between low- and high-`A` conditions
2. Timing interaction between early and late windows
3. Continuous dose-response relation between visibility and `A(t)`

### 4.3 Covariates

Current preregistration targets include:

- pupil diameter
- micro-motion / head translation
- temperature drift
- trial position / fatigue terms

Additional apparatus-specific covariates should be added once the build configuration is fixed.

---

## 5. Sample size and power

Current draft assumptions from the simulation-informed planning stage:

- expected effect size: `Delta V ≈ 0.03 ± 0.01`
- baseline visibility: `V0 ≈ 0.85`
- shot-noise scale target: `sigma_V ≈ 0.013`
- fixed-N design, no interim stopping

Current target totals in the draft protocol:

- 240 trials per condition per subject
- 4 delay conditions
- 24 participants
- pooled event count on the order of `~1.2 × 10^5` photon events per major analysis cell

These numbers should remain labeled as **planning assumptions** until tied to a finalized hardware specification and formal power re-check.

---

## 6. Blinding and randomization

### 6.1 QRNG assignment

The protocol assumes QRNG-controlled block assignment with the seed held by an independent party until analysis lock.

### 6.2 Analysis blinding

The intended analysis path is:

- automatic raw logging
- pre-written `A(t)` computation scripts
- scrambled condition labels for the primary analyst
- parallel adversarial analysis
- third-party unblinding only after both pipelines are locked

### 6.3 Subject blinding

Participants are not told that the protocol is testing consciousness-coupled decoherence specifically. The behavioral cover story should remain compatible with standard ethics review.

---

## 7. Exclusion criteria

### Trial-level exclusions

Planned exclusions include:

1. excessive micro-motion
2. large fixation breaks or saccades
3. detector saturation or dark-count spikes
4. temperature instability
5. invalid coincidence timing

### Subject-level exclusions

Planned exclusions include:

1. excessive trial loss
2. poor eye-tracking quality
3. EEG dropout
4. failed behavioral attention checks

Important boundary:

- no exclusions should be based on the direction or magnitude of the outcome itself

---

## 8. Statistical analysis plan

### 8.1 Confirmatory tests

Current analysis plan centers on linear mixed models:

#### Test 1 — Main effect

```text
V ~ condition + (1|subject) + covariates
```

Directional test:

```text
beta_condition > 0
```

#### Test 2 — Timing asymmetry

```text
V ~ condition × timing + (1|subject) + covariates
```

Directional test:

```text
beta_interaction > 0
```

#### Test 3 — Dose response

```text
V ~ A_continuous + (1|subject) + covariates
```

Directional expectation:

```text
beta_A < 0
```

### 8.2 Robustness checks

Planned robustness checks:

- permutation tests
- Bayesian sensitivity with skeptical priors
- adversarial analysis pipeline
- Winsorized or trimmed-tail re-analysis

### 8.3 Exploratory analyses

Exploratory components may include:

- EEG spectral decomposition
- pupil / visibility covariation
- classifier-based validation of `A(t)`
- delay extrapolation or nonlinear fit comparison

These should remain explicitly labeled as exploratory until preregistered.

---

## 9. Falsification criteria

The current protocol is intended to count strongly against the SOC-MZI rate-law hypothesis if the following occur under a clean, preregistered, blinded implementation:

1. `|Delta V| < 0.005` or otherwise practically null separation
2. no early/late asymmetry
3. non-monotonic or absent `A(t)` relationship
4. effect dependence on hypothesis belief or debrief timing
5. reversal under sham or null-information conditions
6. repeated cross-lab null results under comparable designs

Additional red flags requiring explanation:

- effect depends strongly on experimenter identity
- effect concentrates only in early acquisition periods
- covariates fully mediate the apparent signal

---

## 10. Data sharing and transparency

The repo-facing transparency commitments are:

- OSF or equivalent preregistration archive
- locked analysis code hash prior to unblinding
- full apparatus and timing documentation
- raw or appropriately controlled processed data release where ethics and licensing allow
- simultaneous preprint / reproducibility release for any confirmatory outcome

---

## 11. Synthetic observer control arm — SOC-AI-01

The P4 roadmap also includes a synthetic-observer branch.

Purpose:

- test whether the same effective-rate structure can be expressed in substrate-agnostic information-coherence terms
- distinguish a consciousness-specific interpretation from a broader information-coupling interpretation

Current AI-side operationalization draft:

```text
A_AI = [1 - H(attention)] × [1 / (1 + sigma_rep)]
```

Where:

- `H(attention)` = attention-entropy or representational diffuseness measure
- `sigma_rep` = representation instability across trials

Suggested modulation methods in the current draft:

- dropout sweeps
- temperature sweeps
- attention masking

Controls:

- random observer baseline
- deterministic perfect-readout control
- sham task on irrelevant target variables

This branch should remain explicitly labeled as a control-arm design until code and simulation outputs are imported into the canonical P4 folder.

---

## 12. Immediate repo-level next work

1. Cross-link this file from the P4 `README.md`
2. Import the full OSF-facing preregistration version if available
3. Add a separate statistical analysis appendix
4. Add a separate materials-and-measures appendix
5. Import the MZI simulation script into the canonical simulation folder
6. Link P4 explicitly to `papers/math/soc-localization-memory-hamiltonian.md`
7. Keep all scientist-facing wording constrained to equation testing and falsification, not theory confirmation

---

## Claim boundary for repository publication

Use:

> SOC-MZI-01 is a preregistration-grade protocol for testing whether an operational observer-coherence variable explains residual visibility behavior beyond controlled environmental decoherence.

Avoid:

> SOC-MZI-01 proves that consciousness collapses reality.
