# PNT / SoCT Covariance, Conservation, and Timescale Audit

**Status:** FORMAL AUDIT / PEER-REVIEW READINESS PLAN  
**Claim level:** OPEN ISSUES + CANDIDATE RESOLUTION PATHS

## Purpose

This document tracks four mathematical vulnerabilities that must be resolved before the PNT / SoCT field sector is peer-review ready:

1. gauge/covariance safety of the memory kernel;
2. stress-energy conservation;
3. complete junction-surface tensor definitions;
4. decoherence and long-timescale memory survival.

Passing toy simulations does not close these gates.

## Readiness table

| Gate | Main risk | Current status |
|---|---|---|
| Gauge / covariance safety | coordinate kernels / preferred structures may violate covariance | **OPEN** |
| Stress-energy conservation | phenomenological memory/exchange terms may violate total conservation | **OPEN — flat global/local ledgers and a microscopic oscillator-bath toy are now derived/tested through SIM-04M; covariant total tensor still missing** |
| Junction-surface tensors | parent-child / inversion surfaces need explicit null/non-null tensor treatment | **PARTIALLY ADDRESSED** |
| Long-timescale survival | ordinary decoherence may erase the proposed memory channel | **OPEN** |

---

## Gate 1 — Gauge / covariance safety

Earlier heuristic kernels may be written schematically as

```math
K(|x-x'|,t-t').
```

A fundamental relativistic formulation cannot rely on coordinate separation alone.

A candidate covariant form is

```math
K(x,x')=K_\sigma(\sigma(x,x'),\tau_M,\ell_{Pl})P(x,x'),
```

with invariant separation `sigma`, an appropriate spacetime measure, and a parallel-transport / dressing object `P(x,x')` when fields at separated points must be compared.

This remains OPEN until the exact tensor/gauge content of `P` and the domain of the kernel are defined.

---

## Gate 2 — Stress-energy conservation

### Requirement

Any gravitationally coupled memory sector must participate in a total conservation law compatible with the Bianchi identity:

```math
\nabla_\mu T_{total}^{\mu\nu}=0.
```

A candidate action-first organization is

```math
S_{total}=S_{EH}+S_{matter}+S_M+S_{int}+S_{env}.
```

The memory stress tensor should ultimately be obtained by metric variation rather than inserted phenomenologically.

### Progress through SIM-04J

The first-order reaction-diffusion law is treated as an effective low-frequency equation. A candidate causal completion is

```math
\partial_t^2M
+\gamma\partial_tM
-c_M^2\nabla^2M
+\omega_M^2M
=gC_{obs}.
```

In the overdamped regime,

```math
\alpha=g/\gamma,
\qquad
\beta=\omega_M^2/\gamma,
\qquad
D_M=c_M^2/\gamma.
```

This imposes cross-regime constraints rather than adding independent parameters.

### Progress through SIM-04K

The conservative field terms give the flat-background energy density

```math
\rho_M
=\frac12\dot M^2
+\frac12c_M^2|\nabla M|^2
+\frac12\omega_M^2M^2.
```

The effective exchange identity is

```math
\partial_t\rho_M+\nabla\cdot\mathbf S_M
=gC_{obs}\dot M-\gamma\dot M^2.
```

For periodic/no-flux boundaries,

```math
\frac{dE_M}{dt}=P_{source}-P_{damp}.
```

SIM-04K verifies the discrete global identity and shows that the same field parameters fitted from probes must predict an independent heat/backreaction channel.

### Progress through SIM-04L

SIM-04L strengthens the global ledger to the spatially resolved local exchange law

```math
P_{src}(x,t)=gC_{obs}(x,t)\dot M(x,t),
```

```math
P_{bath}(x,t)=\gamma\dot M(x,t)^2.
```

A globally balanced but spatially scrambled adversary passes integrated calorimetry while failing the local continuity pattern. Therefore global conservation is necessary but not sufficient.

### Progress through SIM-04M — explicit microscopic bath

SIM-04M replaces phenomenological damping for one field-mode surrogate with explicit harmonic environment modes using

```math
H
=\frac{P_M^2}{2}
+\frac{\Omega_M^2M^2}{2}
+\sum_j\left[
\frac{p_j^2}{2}
+\frac{\omega_j^2}{2}
\left(q_j-\frac{c_j}{\omega_j^2}M\right)^2
\right]
-gC_{obs}(t)M.
```

The full microscopic source+system+bath model is Hamiltonian. After the source ends, total energy is conserved.

Eliminating the bath gives a generalized memory-kernel equation with

```math
K(t)=\sum_j\frac{c_j^2}{\omega_j^2}\cos(\omega_jt).
```

Thus local damping is not fundamental in this completion. It is a short-memory approximation to explicit environment dynamics.

SIM-04M finds:

```text
sparse bath -> strong recurrence -> local gamma fails;
dense broad bath -> stable gamma_eff ~ 0.46-0.47 over the tested window
                  -> held-out local damping improves strongly.
```

Microscopic energy closure remains at approximately `1e-7` or better across the tested bath resolutions.

This is meaningful progress because the damping sink is no longer merely named; one explicit conventional mechanism can generate it while preserving exact microscopic energy.

It also raises the burden on SoCT:

> a measured `gamma` cannot itself be treated as evidence for a new memory sector, because ordinary unresolved bath modes can generate the same reduced damping.

### Why Gate 2 remains OPEN

SIM-04M is a nonrelativistic flat-background oscillator-bath toy. It does not yet provide

```text
a covariant environment action,
a bath stress-energy tensor,
exchange four-currents,
a proof of Lorentz/diffeomorphism consistency,
or a demonstration that the effective damping introduces no unjustified preferred frame.
```

Required next steps:

1. extend the bath construction to multiple spatial/momentum modes;
2. derive the corresponding nonlocal effective kernel in spacetime;
3. identify whether the environment defines a physical four-velocity / medium;
4. construct `T_M^{mu nu}`, `T_env^{mu nu}`, and `T_int^{mu nu}`;
5. derive explicit exchange currents;
6. verify

   ```math
   \nabla_\mu(T_{matter}^{\mu\nu}+T_M^{\mu\nu}+T_{env}^{\mu\nu}+T_{int}^{\mu\nu})=0.
   ```

Until then, the stress-energy/Bianchi gate remains OPEN.

---

## Gate 3 — Junction-surface tensors

The repository contains a non-null Israel-junction-style scaffold with

```math
S_{GR,uv}
=-\frac{1}{8\pi G}([K_{uv}]-h_{uv}[K])
```

and candidate memory corrections.

This remains only a scaffold. If the relevant boundary is horizon-like or null, a dedicated null-shell formalism is required with explicit null normal/tangent conventions, transverse curvature, and surface stress-energy definitions.

Status: **PARTIALLY ADDRESSED**.

---

## Gate 4 — Decoherence / long-timescale memory survival

If `M` is ordinary local quantum coherence, environmental decoherence is a major survival problem.

The current phenomenological placeholder separates

```text
M = M_f + M_p
```

with

```math
\partial_tM_f=\alpha_fC-\beta_fM_f+D_f\nabla^2M_f,
```

```math
\partial_tM_p=\alpha_pQ[C]-\beta_pM_p+D_p\nabla^2M_p,
```

and

```text
beta_p << beta_f.
```

But the protected source `Q[C]` and protection mechanism remain undefined.

SIM-04M reinforces that an environment can both dissipate and return information/energy depending on spectral structure. Therefore a long-lived channel cannot be justified merely by writing a small `beta_p`; the microscopic protection mechanism must be specified.

Status: **OPEN**.

---

## Claim boundary

This audit does not prove PNT, SoCT, memory gravity, Engramons, parent-child universe transfer, or a dark-energy mechanism.

The current defensible statement is:

> The memory-sector program now has progressively stronger flat-background causal, energetic, local-continuity, and microscopic-bath consistency gates. These reduce arbitrariness and expose conventional explanations, but they do not yet supply the covariant conserved field theory required for a fundamental gravitational claim.

Use `RESOLVED` only when the full derivation is complete and independently checked.
