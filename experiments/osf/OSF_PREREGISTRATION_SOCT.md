# OSF PREREGISTRATION: Memory-Field Gravity Phenomenology

**Project Title:** A Phenomenological Memory-Field Extension to Particle–Mesh Gravity Produces Cores, Environment-Dependent Expansion, and Environment-Dependent Dwarf Survival

**Authors:** Antoine Shephard (Echo Mirrowen) — Echo Labs / EchoPath XR Inc.

**Project Type:** Preregistration + accompanying preprint (methods-first)

**Status**
Evidence label: `theory-draft`

This file is the repository copy of the OSF preregistration draft preserved from the working thread. It should be treated as the clean upload/source text for external registration, subject to version control.

---

## 1. Summary

We introduce a minimal history-dependent scalar **memory field** `M(x,t)` coupled to gravity as a phenomenological extension of a standard particle–mesh solver. The model is designed to test whether a time-integrated, spatially smoothed collapse-history field can reproduce multiple astrophysical anomalies typically addressed by dark matter particles and/or tuned baryonic feedback.

### Scope Declaration
This preregistration does **not** claim a final fundamental theory of quantum measurement or modified gravity at the action level. It advances a **falsifiable computational hypothesis**: effective gravity depends on accumulated historical activity represented by `M`, with explicit simulation tests and observational follow-up tracks.

---

## 2. Preregistered Simulation Tracks

### Test A — Core Formation Without Tuned Feedback
Hypothesis: with negative memory coupling `α_core < 0`, inner density structure becomes less cuspy than a baseline `α_core = 0` run.

Primary metric:
- `core_ratio = <ρ_inner> / <ρ_outer>`

Pass condition:
- `core_ratio(SoCT) < core_ratio(baseline)` across preregistered seeds and time points.

### Test B — Environment-Dependent Expansion
Hypothesis: void-like regions and filament-like regions will show different local expansion behavior, measured from velocity divergence or equivalent preregistered proxy.

Pass condition:
- `H_void > H_fil` at late times under the preregistered operational definition.

### Test C — Dwarf Survivability Sandbox
Hypothesis: dwarf-like clumps in higher-memory environments show different survival outcomes than those in lower-memory environments.

Primary metric:
- bound fraction per clump

Pass condition:
- statistically meaningful environment contrast in the preregistered direction.

---

## 3. Model Definition

The memory field is written phenomenologically as a spacetime convolution:

```text
M(x,t) = ∫∫ K(x-x', t-t') · S[ρ(x',t')] dx' dt'
```

Where:
- `K` is decomposed into spatial and temporal kernels
- the temporal kernel is modeled with exponential decay
- the spatial kernel is implemented with a normalized Gaussian and FFT convolution
- the source is a smooth function of overdensity rather than a hard threshold

The effective density in the Poisson equation is modified via a saturating function of `M`:

```text
ρ_eff = ρ + α_core · f(M)
```

This is a phenomenological proposal intended for direct falsification through simulation behavior.

---

## 4. Comoving Cosmological Extension

The preregistered production line evolves particles in comoving coordinates under flat ΛCDM background expansion.

Key implementation elements:
- conformal-time integration
- standard Hubble friction term in comoving coordinates
- particle–mesh Poisson solve
- memory field update on the mesh
- environment masks derived from a running mean of `M`

The repository later treats **v0.6.1 final** as the active validated implementation line for this program.

---

## 5. Parameter Sweeps and Robustness

The preregistered plan includes sweeps over collapse threshold, memory timescale, and seed, with effect-size and consistency criteria used to determine whether a signal is robust or fragile.

The repo copy intentionally keeps the wording conservative:
- a signal that appears only in a narrow corner of parameter space is weak evidence
- a signal that flips sign under modest changes counts against the framework
- negative results must be preserved, not hidden

---

## 6. Observational Follow-Up Track: SPARC v2

The repository includes a planned real-data observational track using SPARC and external age proxies.

Core observational question:
- do apparent dark-matter-like signatures correlate with age-like proxies after proper controls?

This prereg copy emphasizes that:
- exploratory correlations are not publication-grade until provenance, controls, and scripts are clean
- synthetic demonstrations must never be mixed with real-data claims

---

## 7. Falsification Criteria

The framework is disfavored if one or more of the following hold robustly:
- no reproducible core-formation signature
- no stable environment-dependent expansion signature
- no meaningful dwarf environment contrast
- no age-linked observational pattern once proper controls are applied
- effect survives only through implausible tuning

The preregistration commits the project to preserving negative outcomes with equal honesty.

---

## 8. Data, Code, and Reproducibility

This repository is intended to house:
- preregistration materials
- code snapshots by version
- simulation outputs
- observational notes
- figure indices
- later manuscript drafts

The repository copy of the prereg exists so the external OSF submission can always be traced to a version-controlled internal source.

---

## 9. Important Limitation Preserved

The current preregistration line does **not** yet explain the CMB power spectrum or claim a full early-universe completion. CMB-era work and parent/child-universe transfer models remain separate exploratory tracks unless independently upgraded.

---

## 10. Repository Use Note

This markdown file is the canonical internal text draft for the OSF-facing preregistration. If externally uploaded, later amendments should be versioned rather than silently overwritten.
