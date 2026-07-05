# P4 Lab Collaboration Brief

**Track:** SOC-MZI awareness-modulated decoherence  
**Audience:** Quantum optics collaborators, experimental physicists, lab partners  
**Claim level:** Preregistration-grade protocol basis; not experimental confirmation

---

## 1. What this collaboration would test

The proposed experiment asks whether an operationally defined observer-coherence variable can produce a measurable visibility difference in a Mach–Zehnder interferometer beyond controlled environmental decoherence.

This is a narrow question about **rate modulation**, not a claim that outcomes are arbitrarily chosen by consciousness.

---

## 2. Minimal equation under test

```text
lambda_eff = lambda_env + lambda_c · A(t)
```

Mapped to a phenomenological visibility form:

```text
V(tau, A) = V0 · exp[-lambda_eff · tau]
```

The experiment is designed to determine whether `lambda_c` is detectably non-zero or whether it can be bounded downward.

---

## 3. Why a Mach–Zehnder setup

A single-photon Mach–Zehnder interferometer provides:

- a clean visibility observable,
- strong hardware control,
- interpretable timing structure,
- and a direct path for null-result constraints.

This makes it the clearest first laboratory target for the public SOC program.

---

## 4. What the lab would need

Baseline target stack:

- Mach–Zehnder interferometer with stable phase control
- single-photon source or equivalent visibility-sensitive quantum optics setup
- detector logging suitable for trial-wise visibility estimation
- environmental monitoring for temperature, motion, drift, and detector artifacts
- optional EEG and eye-tracking instrumentation for observer-state operationalization
- preregistered sham/null-information conditions

The current repo includes protocol and appendix material, but not yet a full procurement-grade apparatus document.

---

## 5. What counts as success or failure

### Supportive pattern

- low- and high-`A` conditions separate under blinded, preregistered analysis,
- early and late windows differ as predicted,
- sham/null-information controls collapse toward baseline,
- the effect survives adversarial or independent re-analysis.

### Non-supportive pattern

- no reproducible separation,
- no timing asymmetry,
- no `A(t)` relation,
- or effects fully explained by apparatus or physiological artifacts.

A null result is still valuable because it constrains the coupling term.

---

## 6. What this repo already provides

Relevant files already present:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md
papers/p4-soc-mzi-awareness-modulated-decoherence/materials-and-measures.md
papers/p4-soc-mzi-awareness-modulated-decoherence/statistical-analysis-plan.md
simulations/mzi-visibility-decay/model-summary.md
simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py
```

These should be enough for an initial scientific discussion.

---

## 7. Collaboration ask

An outside lab collaborator would be most useful for:

- apparatus realism review,
- artifact pathway identification,
- final operationalization of observer-state measurement,
- preregistration hardening,
- and execution of the experiment under normal scientific controls.

---

## 8. Claim boundary

Use:

> This brief invites collaboration on a falsifiable interferometer test of an observer-linked rate-law extension.

Avoid:

> This brief announces a confirmed consciousness effect in quantum optics.

That would be inaccurate.