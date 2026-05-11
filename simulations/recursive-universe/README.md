# Recursive Universe Simulation Package

**Status:** Exploratory toy-model package  
**Source files:** `recursive_universe_sim-3.py`, `RECURSIVE_UNIVERSE_ANALYSIS-4.md`, `recursive_universe_v2_testable-3.py`  
**Related theory track:** CIH / Kerr-to-Cosmos / parent-universe memory  
**Claim level:** Purely speculative simulation scaffold. No physical reality claim.

---

## Purpose

This package preserves exploratory simulations asking:

> If a parent universe collapses into a black-hole-like causal boundary, could some coarse-grained memory-field structure seed perturbations in a child universe, and what CMB-like signatures would such a transfer produce?

The simulations are not evidence for parent-universe memory transfer. They are mathematical playgrounds for identifying constraints and falsifiable signatures.

---

## Package Contents

Planned / current repo files:

```text
simulations/recursive-universe/
  README.md
  exploratory-analysis-v0-1.md
  testable-framework-v2-summary.md
  figure-provenance.md
```

Original source files referenced:

```text
recursive_universe_sim-3.py
RECURSIVE_UNIVERSE_ANALYSIS-4.md
recursive_universe_v2_testable-3.py
```

The original Python scripts should be committed later under:

```text
simulations/recursive-universe/src/
```

once code formatting and dependencies are checked.

---

## Core v1 Toy Model

The v1 simulator includes:

1. a parent-universe density field;
2. memory accumulation in regions above a collapse threshold;
3. a speculative transfer function from parent memory to child perturbations;
4. projection into a simplified 2D CMB-like map;
5. toy angular-power-spectrum calculation.

Working transfer form:

```text
T(k) = exp(-k/k0) * [1 + A * sin(omega * k)]
zeta_child(k) = M_parent(k) * T(k)
```

This is arbitrary and should be treated as exploratory only.

---

## Core v2 Testable Framework

The v2 script improves the framing by adding:

1. bounce-inspired transfer function;
2. inflation plus memory power-spectrum decomposition;
3. toy CMB angular-power calculation;
4. non-Gaussianity estimate;
5. Planck `f_NL` constraint check;
6. parameter-space scan for falsifiability.

Working v2 transfer form:

```text
T(k) = eta * exp[-(k / k_horizon)^2] * [1 + 0.3 * sin(omega * log(k / k_bounce) + phase)]
```

This moves the simulation closer to a real falsifiability framework, while still remaining a toy model.

---

## Key Constraint Identified

The exploratory analysis identifies non-Gaussianity as the strongest immediate constraint.

If parent memory transfer is too strong, it should generate large CMB non-Gaussianity.

Repo-safe statement:

> Strong parent-memory transfer is likely already constrained or ruled out by Planck non-Gaussianity limits. Any viable model must be weak, large-scale, and probably confined to low multipoles where cosmic variance is large.

---

## Relationship to CIH

This package supports the CIH / directional-memory track by clarifying what must be true for parent-universe memory to survive:

- transfer must be weak enough to satisfy non-Gaussianity limits;
- signal likely appears only at large angular scales;
- any observable effect must survive cosmic variance and foreground/systematic explanations;
- a real test requires CLASS/CAMB or equivalent Boltzmann-code implementation.

Related repo file:

```text
papers/cosmology/cih/cih-package-index.md
```

---

## Research Boundary

Use this package for:

- conceptual exploration;
- code scaffolding;
- identifying constraints;
- designing future CMB tests.

Do not use this package as:

- evidence for parent universes;
- evidence for CIH;
- evidence for SoCT;
- a replacement for real CMB analysis.

---

## Next Work

1. Commit cleaned Python scripts into `simulations/recursive-universe/src/`.
2. Convert static figures into reproducible notebook outputs.
3. Add exact parameter tables and random seeds.
4. Replace toy CMB calculator with CLASS/CAMB workflow.
5. Compute a real bispectrum or use published Planck `f_NL` constraints directly.
6. Define a low-ell anisotropy test only after deriving a quantitative parent-axis prediction.
