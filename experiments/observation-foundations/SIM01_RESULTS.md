# SIM-01 Results — Recursive Born Refinement

**Date:** 2026-08-17  
**Status:** first deterministic toy-model pass  
**Code:** `sim01_recursive_born_refinement.py`

## Question

Within the restricted probability family

```math
P_i \propto |\alpha_i|^p,
```

which exponent remains invariant when a record branch is recursively refined into equal orthogonal subrecords with amplitude

```math
\alpha \rightarrow \alpha/\sqrt m
```

and the refined probabilities are coarse-grained back to the original branch?

## Method

The simulation generated normalized random complex amplitude vectors, applied branch refinements, evaluated generalized `|alpha|^p` probabilities, and compared the original coarse branch probability with the sum of its refined descendants.

Two deterministic tests were run:

1. 5,000 random single-refinement cases; exponent grid `p = 0.5 ... 4.0` in steps of `0.025`.
2. 2,000 random cases with 12 nested refinements; selected exponents around and away from `p = 2`.

The same generated cases are reused across exponents within each test so exponent comparisons are not driven by different random samples.

## Single-refinement exponent scan

Best results by mean absolute coarse-graining error:

| p | mean abs coarse error | mean max branch error | worst max branch error |
|---:|---:|---:|---:|
| 2.000 | 1.29e-17 | 3.33e-17 | 3.33e-16 |
| 2.025 | 1.35e-03 | 2.53e-03 | 6.50e-03 |
| 1.975 | 1.37e-03 | 2.57e-03 | 6.50e-03 |
| 2.050 | 2.68e-03 | 5.03e-03 | 1.30e-02 |
| 1.950 | 2.76e-03 | 5.18e-03 | 1.30e-02 |
| 2.075 | 4.00e-03 | 7.48e-03 | 1.95e-02 |
| 1.925 | 4.18e-03 | 7.83e-03 | 1.95e-02 |

`p = 2` is the unique minimum on the scanned grid and is invariant up to floating-point roundoff.

## Twelve-step recursive refinement

| p | mean abs coarse error | mean max branch error | worst max branch error |
|---:|---:|---:|---:|
| 1.00 | 1.18e-01 | 2.04e-01 | 4.24e-01 |
| 1.50 | 5.28e-02 | 9.27e-02 | 2.16e-01 |
| 1.90 | 9.42e-03 | 1.69e-02 | 4.47e-02 |
| 1.99 | 9.17e-04 | 1.66e-03 | 4.45e-03 |
| **2.00** | **3.97e-17** | **1.04e-16** | **8.88e-16** |
| 2.01 | 9.11e-04 | 1.65e-03 | 4.45e-03 |
| 2.10 | 8.86e-03 | 1.61e-02 | 4.42e-02 |
| 2.50 | 3.92e-02 | 7.32e-02 | 2.05e-01 |
| 3.00 | 6.75e-02 | 1.30e-01 | 3.72e-01 |

Recursive splitting amplifies the inconsistency for `p != 2`, while `p = 2` remains invariant to numerical precision.

## Interpretation

The result matches the analytic refinement condition

```math
w(r)=m\,w(r/\sqrt m).
```

For the power family `w(r)=r^p`, this requires

```math
p=2.
```

The simulation therefore confirms the implementation and demonstrates the fixed-point property numerically across random branch structures.

## What this result does **not** show

This result must not be described as an empirical confirmation of the Born rule or a derivation of quantum mechanics from SoCT. The simulation already assumes:

- Hilbert-space complex amplitudes;
- norm-preserving equal splitting by `1/sqrt(m)`;
- mutually exclusive orthogonal record branches;
- additive probabilities under coarse-graining;
- probability weights depending only on amplitude magnitude;
- the restricted power-law family `|alpha|^p` for the numerical scan.

It does not explain:

- why Hilbert space is the correct state space;
- why unitary dynamics applies;
- why one outcome is realized or experienced;
- why record branches should be the fundamental ontology;
- whether SoCT adds any new physical effect to standard quantum theory.

## Surviving claim

A narrow, defensible statement is:

> Within the assumed Hilbert-space record-refinement framework, square-norm probability is the refinement-invariant member of the generalized power family, and repeated recursive refinement exposes deviations from the square norm rather than hiding them.

## Next action

Proceed to **SIM-02 — Hidden State vs Genuine Memory**, because it addresses the most important SoCT-specific methodological vulnerability: distinguishing an additional physical memory degree of freedom from ordinary omitted state variables.
