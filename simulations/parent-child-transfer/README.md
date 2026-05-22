# Parent-Child Transfer Simulations

**Status:** Exploratory simulation branch  
**Related tracks:** CIH, Kerr-to-Cosmos, recursive-universe models, CMB directional-memory tests  
**Claim level:** Toy/exploratory until code, parameters, and likelihood tests are reproducible.

---

## Purpose

This folder organizes simulations exploring whether a parent-universe collapse / bounce boundary could transfer coarse-grained memory structure into child-universe initial conditions.

The motivating question is:

> If a parent universe compresses into a black-hole-like boundary, can any directional or memory-like structure survive into a child universe in a way that produces testable cosmological signatures?

---

## Relationship to Existing Repo Material

Related existing package:

```text
simulations/recursive-universe/
```

That package documents earlier parent-memory transfer toy models and non-Gaussianity constraints.

This folder is reserved for the newer directional / real-space / bounce-transfer branch, including any v4.1 robustness scans.

---

## Intended Folder Structure

```text
simulations/parent-child-transfer/
  README.md
  real-space-bounce-transfer-v4-1.md
  kernel-robustness-summary.md
  src/
  figures/
  results/
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
6. no post-hoc axis fitting after inspecting the CMB.

---

## Research Boundary

Use:

> This simulation branch explores whether parent-child memory transfer can be converted into falsifiable CMB-scale predictions.

Avoid:

> This proves parent universes or memory transfer.

---

## Next Required Artifacts

1. Import `SOC_Simulation_Documentation.docx` content as Markdown.
2. Add `real-space-bounce-transfer-v4-1.md`.
3. Add `kernel-robustness-summary.md`.
4. Add raw code under `src/`.
5. Add parameter scan CSV.
6. Add reproducible notebook.
7. Define a pre-registered statistic before comparing to real CMB data.
