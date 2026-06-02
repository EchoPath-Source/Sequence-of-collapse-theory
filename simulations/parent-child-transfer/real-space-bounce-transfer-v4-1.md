# Real-Space Bounce Transfer v4.1

**Status:** Exploratory simulation note / v4.1  
**Claim level:** Toy-model result only; not physical confirmation.  
**Primary question:** Does parent collapse-axis orientation survive real-space bounce transfer into a child field?

---

## 1. Background

Earlier k-space versions of the transfer test failed to detect a stable signal. Those failures are methodologically important: they showed that the original test architecture was insufficient for the intended question.

The v4.0/v4.1 real-space branch changed two things:

1. Transfer was performed in real space rather than k-space.
2. The main metric was changed from anisotropy power ratio to quadrupole-axis alignment.

This matters because the scientific question is not primarily:

```text
Which direction has more variance?
```

It is:

```text
Does the child field inherit the parent collapse-axis orientation?
```

Quadrupole alignment tests that question more directly.

---

## 2. Real-Space Transfer Model

Generic form:

```text
zeta_child(x) = Integral K_bounce(x, x'; theta) M_parent(x') dx'
```

Where:

| Term | Meaning |
|---|---|
| `M_parent` | Parent-universe memory or collapse-history field. |
| `K_bounce` | Real-space transfer kernel representing a bounce / horizon / inversion boundary. |
| `theta` | Kernel parameters: smoothing scale, anisotropy, damping, axis, retention. |
| `zeta_child` | Child perturbation or inherited memory-seeded field. |

The kernel may include:

- smoothing / horizon damping;
- anisotropic Kerr-axis weighting;
- parity-sensitive components;
- memory-retention coefficient;
- non-Gaussian suppression;
- low-ell preservation.

---

## 3. v4.0 Real-Space Result

The first real-space run produced a split result:

```text
Metric 1: anisotropy ratio
signal = 0.648
null   = 1.225
delta  = -0.577
verdict: failed / contaminated

Metric 2: quadrupole alignment
signal = 0.968
null   = 0.073
delta  = +0.894
verdict: strong positive alignment signal
```

Interpretation:

- The anisotropy-ratio metric was dominated by kernel smoothing geometry.
- The quadrupole-alignment metric directly tested orientation inheritance.
- The signal child field was nearly perfectly aligned with the parent collapse axis.
- The null field was close to random alignment.

---

## 4. Why the Ratio Metric Failed

The anisotropic transfer kernel can smooth variance along one direction while enhancing or preserving variance perpendicular to it.

Therefore, the ratio metric can report lower along-axis power even when the large-scale structure is correctly oriented.

This makes the ratio metric a poor primary statistic for directional inheritance.

Safe conclusion:

```text
Anisotropy power ratio is kernel-contaminated.
Quadrupole-axis alignment is the correct primary metric for this branch.
```

---

## 5. v4.1 Kernel Robustness Scan

The follow-up scan varied transfer-kernel shape to test whether the alignment signal was simply imposed by the kernel.

Reported result:

```text
20 kernel configurations tested
19/20 strong positive alignment deltas (> 0.1)
1/20 weak positive delta
0/20 negative deltas
mean delta approximately +0.583
```

Important feature:

Near-isotropic kernels, which should be hardest for an artifact-prone test, still produced positive signal in the reported scan.

Interpretation:

> Directional information appears to reside in the parent field itself and survive transfer under the tested real-space architecture, rather than being purely imposed by transfer-kernel anisotropy.

---

## 6. Current Scientific Statement

Use this wording:

> Under real-space bounce-transfer toy modeling, directional orientation of a parent collapse field is robustly inherited by the child field across 95% of tested kernel configurations, with mean alignment advantage of approximately +0.583 above null.

Do not state:

> This proves parent-universe transfer, dark matter leakage, or physical black-hole cosmology.

---

## 7. Interpretation for SOC

This result supports only a narrow methodological claim:

```text
The simulation architecture can detect directional memory transfer when such transfer is encoded in the toy model.
```

It strengthens the plausibility of exploring SOC extensions where collapse-memory structure survives causal inversion, black-hole bounce, or parent-child boundary transfer.

It does not establish the physical mechanism.

---

## 8. Required Next Tests

### 8.1 Multi-Seed Test

Run the same 20-kernel grid across many random seeds.

Required outputs:

```text
N_seeds
mean_delta
std_delta
min_delta
fraction_positive
fraction_strong_positive
seed_failure_cases
```

### 8.2 Parent Anisotropy Sweep

Vary parent anisotropy amplitude.

Goal:

```text
Find the threshold at which directional inheritance becomes detectable.
```

### 8.3 Expanded Nulls

Use multiple null models:

1. isotropic parent;
2. shuffled parent orientation;
3. phase-randomized parent;
4. rotated-axis control;
5. kernel-only control.

### 8.4 Pre-Registered Observable Statistic

Before comparing to CMB data, define the statistic, axis-handling rule, and look-elsewhere correction.

---

## 9. Relationship to Dark Sector Speculation

This simulation does **not** model dark matter or dark energy directly.

It may support a prerequisite for dark-sector inheritance models:

> structured gravitational or memory information can survive transfer in a toy architecture.

Possible future branches:

- inherited curvature as dark-matter-like hidden structure;
- post-bounce expansive curvature as dark-energy-like pressure;
- CMB low-ell preferred-axis inheritance;
- Kerr-spin-to-cosmic-axis mapping.

All remain speculative until linked to data.

---

## 10. Safe Repository Label

Recommended label:

```text
exploratory / simulation-methodology / parent-child-transfer / not-yet-observational
```
