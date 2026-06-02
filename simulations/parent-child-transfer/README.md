# Parent-Child Transfer Simulations

**Status:** Exploratory simulation branch  
**Related tracks:** CIH, Kerr-to-Cosmos, recursive-universe models, CMB directional-memory tests  
**Claim level:** Toy/exploratory until code, parameters, nulls, and likelihood tests are reproducible.

---

## Purpose

This folder organizes simulations exploring whether a parent-universe collapse / bounce boundary could transfer coarse-grained memory structure into child-universe initial conditions.

The motivating question is:

> If a parent universe compresses into a black-hole-like boundary, can any directional or memory-like structure survive into a child universe in a way that produces testable cosmological signatures?

The narrower v4.1 question is:

> Does parent collapse-axis orientation survive real-space bounce transfer into a child field more strongly than matched nulls?

---

## Relationship to Existing Repo Material

Related existing package:

```text
simulations/recursive-universe/
```

That package documents earlier parent-memory transfer toy models and non-Gaussianity constraints.

This folder is reserved for the newer directional / real-space / bounce-transfer branch, including v4.0/v4.1 metric correction, kernel robustness, null-model planning, and future reproducibility logs.

---

## Current Folder Structure

```text
simulations/parent-child-transfer/
  README.md
  real-space-bounce-transfer-v4-1.md
  kernel-robustness-summary.md
  null-models.md
  parameter-log.md
  src/        # future
  figures/    # future
  results/    # future
```

Future data/notebook locations:

```text
data/parent-child-transfer/kernel_scan_v4_1.csv
notebooks/parent_child_directional_transfer.ipynb
figures/parent-child-transfer/
```

---

## Core Simulation Idea

A parent memory field is passed through a transfer kernel representing a collapse/bounce/horizon boundary.

Generic form:

```text
zeta_child(x) = Integral K_transfer(x, x'; theta) M_parent(x') dx'
```

Where:

| Term | Meaning |
|---|---|
| `M_parent` | Parent-universe memory or collapse-history field. |
| `K_transfer` | Boundary / bounce / horizon transfer kernel. |
| `theta` | Parameter set: coupling, smoothing scale, anisotropy, spin axis, damping. |
| `zeta_child` | Child-universe initial perturbation or memory-seeded field. |

---

## Current v4.1 Result Summary

The real-space branch found that anisotropy ratio was a poor primary metric because it could be contaminated by kernel smoothing geometry.

The preferred primary metric is:

```text
quadrupole-axis alignment delta = alignment_signal - alignment_null
```

Current recorded values:

```text
v4.0 quadrupole alignment signal = 0.968
v4.0 quadrupole alignment null   = 0.073
v4.0 quadrupole alignment delta  = +0.894

v4.1 kernel configurations tested = 20
strong positive deltas             = 19/20
weak positive deltas               = 1/20
negative deltas                    = 0/20
mean alignment delta               = approximately +0.583
```

Claim boundary:

> These values document an exploratory toy-model signal. They should not be treated as empirical evidence until code, random seeds, null models, CSV outputs, and multi-seed tests are committed.

---

## Current Documents

| File | Role |
|---|---|
| `real-space-bounce-transfer-v4-1.md` | Documents the real-space transfer architecture, v4.0 metric split, and v4.1 robustness interpretation. |
| `kernel-robustness-summary.md` | Preserves the 20-kernel robustness scan and follow-up requirements. |
| `null-models.md` | Defines required controls: isotropic parent, axis shuffle, phase randomization, rotated parent, kernel-only, multi-seed, and anisotropy sweep. |
| `parameter-log.md` | Defines the run log schema, current summary values, metric thresholds, and reproducibility requirements. |

---

## Candidate Observables

- low-ell CMB anomalies;
- hemispherical asymmetry;
- parity asymmetry;
- quadrupole/octopole alignment;
- preferred direction linked to Kerr spin axis;
- non-Gaussianity constraints;
- polarization cross-checks.

---

## Hard Constraints

Any viable transfer model must satisfy:

1. Planck non-Gaussianity limits;
2. CMB angular power constraints;
3. cosmic variance limits at low ell;
4. look-elsewhere corrections;
5. foreground/systematics robustness;
6. no post-hoc axis fitting after inspecting the CMB;
7. pre-defined statistic before observational comparison;
8. null-model survival before CMB-facing interpretation.

---

## Required Next Tests

1. Run multi-seed robustness test.
2. Run isotropic-parent control.
3. Run axis-shuffle null.
4. Run phase-randomized parent test.
5. Run rotated-parent control.
6. Run kernel-only artifact control.
7. Run parent anisotropy sweep.
8. Commit raw code under `src/`.
9. Commit parameter scan CSV.
10. Add reproducible notebook.
11. Define a pre-registered CMB-facing statistic before comparing to real CMB data.

---

## Research Boundary

Use:

> This simulation branch explores whether parent-child memory transfer can be converted into falsifiable CMB-scale predictions.

Avoid:

> This proves parent universes or memory transfer.

---

## Repo-Safe Summary

> The parent-child transfer branch currently contains a positive exploratory real-space toy result and the scaffolding needed to test whether that result survives stricter nulls and reproducibility requirements.
