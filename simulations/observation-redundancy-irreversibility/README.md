# Simulation 3b — Redundancy, Partial Erasure, and Effective Irreversibility

**Status:** Standard-quantum benchmark / no SoCT feedback  
**Purpose:** Distinguish a single reversible record from distributed records that remain after partial erasure.

## Model

A system qubit imprints the same binary distinction into `N` environment fragments. Each fragment conditionally occupies

```math
|0>_E
```

or

```math
|e_1(phi)> = cos(phi)|0> + sin(phi)|1>.
```

For one fragment,

```math
D_E = |sin(phi)|
```

and the equal-prior Holevo information is

```math
chi_E = H_2[(1 + |cos(phi)|)/2].
```

If `m` fragments survive after exact erasure of the others, the overlap of the two surviving environment branches is

```math
B_m = |cos(phi)|^m.
```

The exploratory residual-record / effective-irreversibility proxy is

```math
Xi_irr = 1 - B_m.
```

This is not thermodynamic irreversibility. It is a toy diagnostic for how much branch-distinguishing record structure remains outside the sector that has been reversed.

## Redundancy diagnostics

Two redundancy measures are retained.

1. `redundancy_R09`: number of surviving fragments that individually carry at least `0.9` bits of accessible information.
2. A continuous durable-record score:

```math
D_durable = Xi_irr * (m/N) * chi_E.
```

The threshold count is useful for near-classical records but is deliberately not used as the only score because the `0.9 bit` threshold is arbitrary.

## Expected behavior

- With one perfectly distinguishable record and exact erasure, all record diagnostics fall to zero.
- With many copied records, erasing only a subset leaves substantial record structure in the remaining environment.
- Complete reversal of every record-bearing fragment is required to return the distributed-record diagnostics to zero in this toy model.
- The simulation therefore separates `record creation happened` from `a durable distributed record remains`.

## Representative results

For `N=4` and `phi=pi/2`, each fragment carries one accessible bit. The continuous durable-record score falls approximately

```text
1.00 -> 0.75 -> 0.50 -> 0.25 -> 0.00
```

as 0, 1, 2, 3, then all 4 fragments are erased.

For weaker `phi=pi/3`, no fragment crosses the arbitrary 0.9-bit redundancy threshold, yet the continuous score remains substantial and decays smoothly under erasure. This is why the observation project should avoid defining record durability from a hard threshold alone.

## Interpretation for SoCT

Simulation 3 showed that an ideal reversible record can be created and completely erased. Simulation 3b adds the missing distinction:

```text
transient microscopic correlation
    !=
record copied into multiple independent degrees of freedom.
```

This motivates a candidate SoCT record-production functional that weights record creation by persistence, accessible information, redundancy, and resistance to reversal rather than counting every temporary correlation equally.

A first versioned candidate is documented in:

```text
papers/math/soc-record-production-source-v0-1.md
```

## Claim boundary

This simulation does not demonstrate a physical SoCT memory field, objective collapse, or new irreversibility. It is a standard-quantum mechanism check used to decide what a future SoCT source term would need to distinguish.
