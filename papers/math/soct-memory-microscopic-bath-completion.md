# SoCT Memory Microscopic-Bath Completion

**Status:** analytical open-system completion / microscopic damping scaffold  
**Claim level:** standard oscillator-bath methodology applied as a consistency gate; not evidence for a physical SoCT memory field

## Purpose

SIM-04J and SIM-04K introduced the effective causal memory equation

```math
\partial_t^2 M
+ \gamma\partial_tM
- c_M^2\nabla^2M
+ \omega_M^2M
= gC_{obs}.
```

The main unresolved term is the local damping term

```math
\gamma\partial_tM.
```

If this is only inserted phenomenologically, the bath/exchange sector remains arbitrary. The purpose of this note is to ask whether local damping can emerge from explicit reversible microscopic degrees of freedom and to identify when the local Markovian approximation must fail.

This construction follows the standard harmonic-oscillator-bath / generalized-Langevin lineage. No novelty claim is made for integrating out an oscillator bath. The SoCT-specific use is narrower: require the proposed memory sector to admit a microscopic completion whose reduced dynamics reproduces the phenomenological `gamma` only in the correct limit.

---

## 1. One-mode reduction

For a spatial Fourier mode of the candidate memory field, write the conservative system coordinate as `M(t)` with bare mode frequency `Omega_M`.

A standard counterterm oscillator-bath Hamiltonian is

```math
H
=
\frac{P_M^2}{2}
+\frac{\Omega_M^2M^2}{2}
+\sum_j\left[
\frac{p_j^2}{2}
+\frac{\omega_j^2}{2}
\left(q_j-\frac{c_j}{\omega_j^2}M\right)^2
\right]
-gC_{obs}(t)M.
```

The shifted bath coordinate includes the usual quadratic counterterm and prevents the static oscillator frequency from being arbitrarily renormalized by the coupling convention.

The equations of motion are

```math
\ddot M
+\Omega_M^2M
-\sum_j c_j\left(q_j-\frac{c_j}{\omega_j^2}M\right)
=gC_{obs}(t),
```

```math
\ddot q_j+\omega_j^2q_j=c_jM.
```

The combined driven system is Hamiltonian. After the external source is switched off, total system+bath energy is conserved.

---

## 2. Eliminating the bath

Solving the bath coordinates and substituting them back into the `M` equation gives a generalized Langevin / memory-kernel structure of the form

```math
\ddot M(t)
+\Omega_M^2M(t)
+\int_0^t K(t-s)\dot M(s)\,ds
=
gC_{obs}(t)+\xi(t)+\text{initial-slip terms},
```

where

```math
K(t)=\sum_j\frac{c_j^2}{\omega_j^2}\cos(\omega_j t).
```

The fluctuating term `xi(t)` depends on the initial bath state. In the zero-temperature / zero-displacement classical toy used in SIM-04M it vanishes initially, leaving deterministic non-Markovian reduced dynamics.

The important conceptual point is

```text
explicit bath -> memory kernel first,
local friction only as an approximation.
```

Thus a microscopic completion does **not** generically imply

```math
\int_0^t K(t-s)\dot M(s)ds
=\gamma\dot M(t).
```

That replacement requires a bath correlation time short compared with the resolved system timescale and a sufficiently broad/dense spectral distribution.

---

## 3. Spectral-density parameterization

Define the bath spectral density

```math
J(\omega)
=\frac{\pi}{2}\sum_j
\frac{c_j^2}{\omega_j}\delta(\omega-\omega_j).
```

Then

```math
K(t)
=\frac{2}{\pi}\int_0^\infty
\frac{J(\omega)}{\omega}\cos(\omega t)\,d\omega.
```

SIM-04M uses an Ohmic-like finite-cutoff envelope

```math
J(\omega)=\eta\,\omega e^{-\omega/\omega_c}
```

sampled by a finite set of bath modes.

The discrete couplings are chosen by

```math
c_j^2
\simeq
\frac{2}{\pi}
J(\omega_j)\omega_j\Delta\omega.
```

As bath sampling becomes denser over a broad band, the kernel becomes increasingly short lived on the resolved system timescale and the reduced motion approaches a local damped oscillator.

For sparse baths the kernel remains structured and long lived. Energy can coherently return from bath modes to `M`, producing revivals/recurrences that a monotonic local friction law cannot reproduce.

---

## 4. Microscopic energy ledger

With the external source present, define

```math
H_0
=
\frac{P_M^2}{2}
+\frac{\Omega_M^2M^2}{2}
+\sum_j\left[
\frac{p_j^2}{2}
+\frac{\omega_j^2}{2}
\left(q_j-\frac{c_j}{\omega_j^2}M\right)^2
\right].
```

The source work is

```math
W_{src}(t)=\int_0^t gC_{obs}(s)\dot M(s)\,ds.
```

The exact microscopic identity is

```math
H_0(t)-H_0(0)=W_{src}(t).
```

After `C_obs` is switched off,

```math
H_0=\text{constant}.
```

Thus the effective damping loss in SIM-04K/04L is not fundamental destruction of energy. In a microscopic completion it is energy transferred into bath/coupling degrees of freedom, and finite baths can return some of it later.

---

## 5. Effective Markovian limit

The reduced comparison model is

```math
\ddot M
+\gamma_{eff}\dot M
+\Omega_M^2M
=gC_{obs}(t).
```

`gamma_eff` is inferred only from an early post-source training window and then frozen before later-time prediction.

The microscopic completion passes the Markovian gate only if the same `gamma_eff` predicts:

```text
early local exponential damping,
late held-out trajectory,
approximate cumulative bath-energy transfer,
and suppression of large coherent recurrences.
```

Failure of any of these indicates that the local `gamma` description is outside its regime of validity.

---

## 6. SoCT interpretation boundary

This microscopic completion does not make `M` necessary and does not identify the bath as exotic.

In fact, it strengthens the conventional-null lesson:

> ordinary Hamiltonian environmental degrees of freedom can generate an apparently dissipative reduced memory coordinate without fundamental energy loss.

The SoCT causal memory model should therefore not treat a fitted `gamma` as evidence for a novel physical damping sector.

The stronger requirement is:

```text
if gamma is used,
its microscopic/environmental origin or controlled effective regime
must be specified and tested.
```

A real additional field would still have to survive the earlier reset, source-law, propagation, local exchange, and conventional-reservoir gates.

---

## 7. Falsification conditions

The local damping completion is falsified in a tested regime if:

1. a fixed `gamma_eff` fitted early fails strongly on held-out later times;
2. large bath-to-system recurrence appears where the local model predicts monotonic damping;
3. microscopic bath/coupling energy transfer disagrees strongly with the effective `gamma_eff dot(M)^2` heat ledger;
4. the inferred `gamma_eff` does not stabilize as bath spectral sampling becomes denser;
5. different modes require unrelated friction parameters where one common bath model predicted otherwise.

Failure of the Markovian limit does not falsify the existence of a memory coordinate; it falsifies the **local-damping approximation** in that regime.

---

## 8. Literature position

This note uses standard open-system structure associated with harmonic oscillator baths and generalized Langevin equations. Relevant lineage includes Caldeira and Leggett's dissipative-system work and later explicit generalized-Langevin derivations from harmonic environments.

The research contribution being tested in this repository is not the oscillator-bath method itself. It is the use of that method as a consistency/falsification gate on the proposed SoCT memory-sector damping term.

---

## 9. Next step

SIM-04M tests finite bath-size convergence directly:

```text
sparse bath
-> structured long-memory kernel
-> recurrences
-> local gamma fails

versus

dense broad bath
-> short effective kernel
-> stable gamma_eff
-> local damping becomes a useful reduced description.
```

The following gate after SIM-04M is the covariant/open-system problem: whether the required bath/rest-frame structure can be embedded consistently into a relativistic stress-energy description without introducing an unjustified preferred frame.