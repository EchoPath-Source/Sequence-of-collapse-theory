# Real-Space Bounce Transfer v4.1 — Summary

**Status:** Exploratory simulation documentation  
**Source:** Recent parent-child directional-transfer thread / pending `SOC_Simulation_Documentation.docx` import  
**Claim level:** Simulation scaffold, not empirical evidence.

---

## Purpose

This note preserves the working structure of the v4.1 parent-child transfer branch until full code and notebook outputs are committed.

The model explores whether a real-space transfer kernel can carry coarse parent-memory structure through a bounce/collapse boundary into child-universe perturbations while remaining compatible with CMB constraints.

---

## Conceptual Model

The real-space transfer model replaces purely arbitrary k-space transfer functions with a kernel acting on parent memory in position space:

```text
zeta_child(x) = Integral K_bounce(x, x'; theta) M_parent(x') dx'
```

Possible kernel ingredients:

- smoothing / horizon damping;
- anisotropic Kerr-axis weighting;
- parity-sensitive component;
- memory-retention coefficient;
- non-Gaussian suppression;
- low-ell preservation.

---

## Why Real Space Matters

A real-space model is useful because:

1. parent memory may be localized or directionally structured;
2. black-hole / bounce boundaries are geometric objects, not only spectral filters;
3. directional inheritance is easier to define before spherical projection;
4. kernel robustness can be tested before any CMB comparison.

---

## v4.1 Working Questions

1. Does the transfer preserve a preferred axis without over-amplifying small-scale structure?
2. Does the child field remain weakly non-Gaussian enough to evade Planck constraints?
3. Does the signal concentrate at low multipoles?
4. Is the result robust to kernel width, damping, and coupling strength?
5. Can a predicted axis be derived before comparing to the observed CMB?

---

## Candidate Robustness Scan

A v4.1 scan should vary:

| Parameter | Meaning |
|---|---|
| `eta` | parent-memory coupling strength |
| `sigma_kernel` | transfer smoothing scale |
| `k_cut` or horizon scale | small-scale suppression |
| `axis_vector` | Kerr/parent directional axis |
| `parity_weight` | odd/even asymmetry contribution |
| `noise_seed` | stochastic realization |
| `memory_retention` | fraction of parent memory surviving transfer |

Outputs should include:

```text
low_ell_power_ratio
quadrupole_octopole_alignment
hemispherical_asymmetry_score
predicted_fNL_proxy
axis_recovery_error
observability_score
```

---

## Interpretation of a Positive Toy Result

A positive toy result would mean only:

> A mathematically allowed transfer kernel can preserve weak, large-scale directional memory without immediately violating simple constraints.

It would not mean:

> Parent-universe memory has been detected.

---

## Required Before Scientific Use

1. Commit source code.
2. Commit parameter tables and random seeds.
3. Replace toy angular-power estimates with CLASS/CAMB or equivalent where relevant.
4. Use real Planck non-Gaussianity and anisotropy constraints.
5. Predefine axis/amplitude before comparing to observed anomalies.
6. Add look-elsewhere correction.

---

## Next Artifacts

```text
simulations/parent-child-transfer/kernel-robustness-summary.md
data/parent-child-transfer/kernel_scan_v4_1.csv
notebooks/parent_child_directional_transfer.ipynb
figures/parent-child-transfer/
```

---

## Claim Boundary

Use:

> The v4.1 real-space bounce-transfer branch defines a path toward falsifiable parent-child directional-memory tests.

Avoid:

> The v4.1 simulation confirms parent-child universe transfer.
