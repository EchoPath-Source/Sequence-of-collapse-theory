# P3 Appendix — Derivation Note

**Canonical track:** P3 — SOC concept to equation  
**Status:** Repo publication appendix draft  
**Purpose:** Clarify what is assumed, what is phenomenological, and how the P3 rate-law is introduced

---

## 1. Role of this appendix

This appendix is not a full first-principles derivation. Its purpose is narrower:

- to show how the SOC paper moves from conceptual language to a testable density-matrix form,
- to make the modeling assumptions explicit,
- and to separate phenomenological choice from established physics.

---

## 2. Starting point

The starting point is ordinary open-system evolution for a reduced density matrix `rho`:

```text
rho_dot = -(i / hbar) [H, rho] + D_env(rho)
```

Where:

- `H` is the system Hamiltonian,
- `D_env(rho)` is the ordinary environmental decoherence contribution.

This baseline is assumed rather than re-derived here.

---

## 3. SOC phenomenological step

The SOC-inspired extension assumes that a bounded observer-linked variable can enter the effective dephasing rate through a pointer-basis channel.

The phenomenological substitution is:

```text
D_env(rho) -> D_env(rho) + D_soc(rho)
```

with

```text
D_soc(rho) = lambda_c · f(A) · (O rho O - rho)
```

This yields the P3 working form:

```text
rho_dot = -(i / hbar) [H, rho] + (lambda_env + lambda_c · f(A)) (O rho O - rho)
```

The key assumption is that the additional term modifies **rate**, not **outcome selection**.

---

## 4. Why this form is chosen

This form is chosen because it is the simplest way to express the intended claim:

- when `A = 0`, ordinary decoherence remains,
- when `A > 0`, decay toward the pointer basis accelerates,
- and the extension is bounded through `f(A)`.

This makes the hypothesis experimentally approachable while avoiding claims of arbitrary state selection.

---

## 5. Reduction to the MZI rate-law

For the interferometer-facing P4 track, the same idea is reduced to a scalar rate law:

```text
lambda_eff = lambda_env + lambda_c · A(t)
```

and then mapped to phenomenological visibility decay:

```text
V(tau, A) = V0 · exp[-lambda_eff · tau]
```

That reduction is not a proof that the interferometer exactly realizes the full density-matrix model. It is a practical bridge from operator language to measurable design signatures.

---

## 6. Relationship to the CCE note

A related operator-level expression is preserved in:

```text
papers/math/cce-master-equation-note.md
```

That note uses a Lindblad-style consciousness-coupled channel of the form:

```text
L_con(rho) = gamma(Phi) [L rho L† - 1/2 {L†L, rho}]
```

The present derivation note treats that expression as a compatible broader framing, while P3 keeps the narrower pointer-basis phenomenology as the main public-facing form.

---

## 7. What is not derived here

This appendix does **not** yet derive:

- a microscopic origin for `A(x,t)`,
- a first-principles mapping from consciousness to `f(A)`,
- a unique pointer observable for all systems,
- or a justified cosmological lift from the laboratory rate-law.

Those are open research problems, not hidden completed derivations.

---

## 8. Scientific value of this limited derivation

Even as a phenomenological note, this appendix is useful because it makes the modeling ladder explicit:

1. start with ordinary open-system dynamics,
2. add a bounded observer-linked rate contribution,
3. reduce it to experimentally measurable signatures,
4. constrain or reject it using preregistered tests.

That is sufficient for a legitimate early-stage scientific program.

---

## 9. Claim boundary

Use:

> This appendix explains how the P3 paper introduces the observer-linked term as a phenomenological extension.

Avoid:

> This appendix derives the SOC equation from first principles.

That stronger statement would be inaccurate.