# Shephard-Mirrowen Hamiltonian: Dimensional Analysis

**Status:** FORMAL SCAFFOLD / DIMENSIONAL CONSISTENCY CHECK  
**Claim level:** PRELIMINARY / theoretical hygiene, not established physics  
**Related file:** `papers/math/soc-localization-memory-hamiltonian.md`

---

## Purpose

This appendix checks the dimensional homogeneity of a nonlocal memory-coupling form sometimes used as an expanded Shephard-Mirrowen / SoCT Hamiltonian scaffold.

The goal is narrow: every term added to a Hamiltonian must carry units of energy. This document does not prove the physical reality of the memory term, the Engramon carrier hypothesis, memory gravity, or Sequence of Collapse Theory. It only states the unit constraints that any mathematically coherent version of the term must satisfy.

---

## Reference Form

A compact expanded form is:

```text
H_SOC = p^2/(2m) + V(x) + lambda * integral_t integral_s w_i K(|x-x_i|, t-t_i, s_i) dt ds
```

where the first two terms are the standard kinetic and potential contributions, and the third term is a proposed nonlocal memory contribution.

For a Hamiltonian, every term must resolve to energy:

```text
[H_SOC] = [Energy] = M L^2 T^-2
```

---

## Baseline Control Terms

The standard kinetic term has units:

```text
[p^2 / (2m)] = (M L T^-1)^2 / M = M L^2 T^-2
```

The potential term is already an energy term:

```text
[V(x)] = M L^2 T^-2
```

Therefore, the memory term must also satisfy:

```text
[lambda * integral_t integral_s w_i K dt ds] = M L^2 T^-2
```

---

## Minimal Dimensional Assignment

For the current formal scaffold, use the following minimal assignments:

| Quantity | Interpretation | Units |
|---|---|---|
| `w_i` | normalized collapse/information/context weight | dimensionless |
| `s` | internal compactified state index or state coordinate | dimensionless |
| `ds` | measure over internal state coordinate | dimensionless |
| `dt` | temporal integration measure | `T` |
| `K` | normalized temporal memory/correlation kernel | `T^-1` |
| `lambda` | coupling energy scale | `Energy` |

Under this assignment:

```text
[w_i K dt ds] = [1] * [T^-1] * [T] * [1] = [1]
```

so the double integral is dimensionless:

```text
[integral_t integral_s w_i K dt ds] = [1]
```

The coupling must therefore carry energy units:

```text
[lambda] = M L^2 T^-2
```

or, in particle-physics notation:

```text
[lambda] = eV
```

---

## Constraint on the Coupling Constant

The memory coupling cannot be treated as a dimensionless coefficient unless the kernel or integration measure is redefined to carry compensating energy units.

The cleanest dimensionally homogeneous form is:

```text
lambda = energy-scale coupling
```

Equivalently, for a proposed Engramon-normalized version:

```text
lambda = lambda_E * E_E
```

where:

| Quantity | Meaning | Units |
|---|---|---|
| `E_E` | candidate Engramon baseline energy | energy |
| `lambda_E` | dimensionless normalization factor | dimensionless |

The parameter-fixed proposal is the special case:

```text
lambda_E = 1
lambda = E_E
```

This is a candidate normalization, not a proof. Dimensional analysis permits the identification only if the rest of the physical model independently justifies `E_E` as the appropriate coupling scale.

---

## Candidate Engramon Assignment

Under Planck Nucleation Theory / Engramon language, one possible assignment is:

```text
lambda ≡ E_E ~ 0.034 eV
```

This would make the memory coupling a fixed energy scale rather than an arbitrary free parameter.

Conservative claim boundary:

> Dimensional analysis shows that the coupling must carry energy units. It does not prove that the coupling equals the Engramon energy, nor does it prove that the Engramon energy is physically real.

---

## Relationship to the Canonical Hamiltonian Scaffold

The current canonical repository scaffold is:

```text
H_SOC = H_free + H_loc + lambda_M M(x,t) O_M + lambda_c Phi_c(x,t) O_c
```

The same dimensional rule applies: the added channel terms must each resolve to energy.

Thus:

```text
[lambda_M M O_M] = Energy
[lambda_c Phi_c O_c] = Energy
```

If `M`, `Phi_c`, `O_M`, and `O_c` are taken to be dimensionless normalized fields/operators, then `lambda_M` and `lambda_c` must each carry energy units. If any of those fields/operators carry physical dimensions, then the corresponding coupling must be rescaled accordingly.

---

## Failure Modes / Required Caveats

This dimensional check depends on four assumptions:

1. `w_i` is dimensionless.
2. `s` is an internal dimensionless state coordinate.
3. `K` is normalized with units `T^-1`.
4. `lambda` carries energy units.

If `s` is later treated as a physical length, entropy measure, phase-space volume, or unnormalized continuous coordinate, the units of `K` and/or `lambda` must be updated.

If the kernel is defined as a spatial-temporal kernel rather than a purely temporal memory kernel, then `K` must absorb the inverse units of the full integration measure.

A general rule is:

```text
[lambda] = [Energy] / [integral_t integral_s w_i K dt ds]
```

The present appendix uses the normalized-kernel case because it yields a clean dimensionless memory integral and a physically interpretable energy-scale coupling.

---

## Claim Boundary

Use:

> The Shephard-Mirrowen Hamiltonian can be written in a dimensionally homogeneous form if the memory kernel is normalized and the coupling constant carries energy units.

Avoid:

> Dimensional analysis proves the Engramon-neutrino carrier hypothesis or proves SoCT.

---

## Next Work

1. Define the units of `M(x,t)`, `Phi_c(x,t)`, `O_M`, and `O_c` in the canonical Hamiltonian.
2. Decide whether `lambda_M` and `lambda_c` are independent energy scales or both derive from a shared Engramon baseline.
3. Add a small validation script that checks dimensional assignments symbolically for alternative kernel/measure definitions.
4. Keep the Engramon identification as a candidate normalization until independently constrained by empirical or theoretical derivation.
