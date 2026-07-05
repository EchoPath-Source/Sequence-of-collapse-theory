# SOC Scientist Brief — Equation, Signatures, Falsifiers

**Purpose:** Fast scientist-facing summary of the public SOC research program  
**Claim level:** Testable equation set; not theory confirmation

---

## 1. Narrow claim under test

The public SOC program is currently testing a narrow phenomenological claim:

> An operationally defined observer-linked or information-coherence variable may modulate the **rate** of decoherence or pointer-basis stabilization without altering Born-rule outcome frequencies.

This is a rate-law claim, not an outcome-selection claim.

---

## 2. Core equation forms

### Phenomenological rate-law form

```text
lambda_eff = lambda_env + lambda_c · A(t)
```

### Density-matrix form

```text
rho_dot = -(i / hbar) [H, rho] + (lambda_env + lambda_c · f(A)) (O rho O - rho)
```

Where:

- `lambda_env` = environmental decoherence baseline
- `lambda_c` = observer-linked coupling coefficient
- `A(t)` = operational observer-coherence variable
- `O` = pointer observable
- `f(A)` = bounded gating function

---

## 3. What counts as admissible `A(t)`

`A(t)` must be operational, measurable, and preregisterable.

Current candidate families:

- EEG-linked coherence / phase-locking
- eye-tracking fixation or gaze-target locking
- HRV-linked synchrony
- stimulus-linked mutual information
- synthetic-observer coherence metrics in AI/control systems

If `A(t)` cannot be defined reproducibly, the model does not become an empirical theory.

---

## 4. Main predicted signatures

The public equation set motivates searching for:

1. **Main effect**  
   Visibility or coherence retention differs between low- and high-`A` conditions.

2. **Timing asymmetry**  
   Early vs late structured observer-coupled windows differ under fixed apparatus settings.

3. **Dose response**  
   Visibility suppression scales monotonically with measured `A(t)`.

4. **Sham separation**  
   Null-information or sham conditions relax toward baseline.

5. **Bounded control window**  
   Real-time observer-linked feedback improves stability only in a narrow non-oscillatory gain range.

---

## 5. Primary direct experiment

### SOC-MZI-01

A Mach–Zehnder interferometer is the clearest table-top test.

Phenomenological visibility form:

```text
V(tau, A) = V0 · exp[-lambda_eff · tau]
```

Main empirical value of the experiment:

- a positive result supports the rate-law extension,
- a null result places a quantitative bound on `lambda_c`.

---

## 6. Secondary / support tracks

- **Synthetic-observer control arm** to test substrate-general vs consciousness-specific interpretations
- **Distributed chain tests** for topology sensitivity, sham separation, and bounded feedback control
- **Cosmological memory discussion** only as a speculative downstream extension after laboratory constraints

---

## 7. What would count against the model

The current public mathematical program should be weakened or rejected if carefully controlled experiments show:

- no reproducible low- vs high-`A` separation,
- no early/late asymmetry,
- no monotonic `A(t)` relation,
- no sham/null-information separation,
- or no bounded gain window beyond ordinary engineering artifacts.

That is the intended scientific standard.

---

## 8. Repository guide

Core files:

```text
docs/equations-and-testable-hypotheses.md
papers/p3-soc-concept-to-equation/P3-sequence-of-collapse-from-concept-to-equation.md
papers/math/cce-master-equation-note.md
papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md
simulations/mzi-visibility-decay/model-summary.md
```

---

## 9. One-line framing

> The present SOC repository should be read as a structured proposal for equation testing and falsification, not as proof that consciousness-linked collapse has already been established.