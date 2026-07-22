# PNT / SoCT Covariance, Conservation, and Timescale Audit

**Status:** FORMAL AUDIT / PEER-REVIEW READINESS PLAN  
**Claim level:** OPEN ISSUES + CANDIDATE RESOLUTION PATHS  
**Related OSF node:** `https://osf.io/tb9nq/overview`  
**Related repo files:**

```text
papers/math/soc-localization-memory-hamiltonian.md
papers/math/shephard-mirrowen-hamiltonian-dimensional-analysis.md
papers/math/israel-junction-causal-inversion-surface.md
papers/p5-hubble-tension-memory-gradient/README.md
papers/p6-black-holes-memory-compression-nodes/README.md
```

---

## Purpose

This document converts four peer-review vulnerabilities in the Planck Nucleation Theory / Sequence of Collapse Theory math track into explicit mathematical gates.

The vulnerabilities are:

1. gauge/covariance safety of the memory kernel;
2. stress-energy conservation;
3. complete junction-surface tensor definitions;
4. decoherence and long-timescale memory survival.

This file is not a claim of resolution. It is a formal audit and resolution plan. Each item remains an open or partially addressed requirement until the corresponding derivation, simulation, or preregistered test is complete.

---

## Readiness table

| Gate | Risk before peer review | Candidate resolution path | Current status |
|---|---|---|---|
| Gauge / covariance safety | Coordinate-distance kernels can violate diffeomorphism covariance or gauge invariance. | Replace raw coordinate kernels with covariant kernels based on invariant intervals, bitensors, parallel transport, or gauge dressing. | OPEN |
| Stress-energy conservation | A phenomenological memory stress tensor can violate the Bianchi identity unless the full stress tensor is conserved. | Derive memory and interaction tensors from an action or impose coupled field equations that enforce total conservation. | OPEN |
| Junction-surface tensors | Parent-child / causal-inversion surfaces require explicit intrinsic metric, extrinsic curvature, jump tensor, and surface stress-energy definitions. | Use non-null Lanczos-Israel junction equations as the first scaffold; add a null-shell extension if the boundary is horizon-like. | PARTIALLY ADDRESSED |
| Decoherence / long-timescale memory | Ordinary quantum coherence decays too quickly to support cosmological inheritance unless a protected slow channel exists. | Split memory into fast local memory and slow/protected memory with explicit timescale hierarchy. | OPEN |

---

## Gate 1: Gauge / covariance safety of the memory kernel

### Vulnerability

Earlier heuristic language may write the memory kernel schematically as:

```text
K(|x - x_i|, t - t_i, s_i)
```

This is not safe as a fundamental covariant object because coordinate separations are chart-dependent. In curved spacetime or gauge-coupled settings, a nonlocal kernel must specify how fields at separated points are compared.

### Candidate covariant replacement

Replace the coordinate-distance kernel with a covariant bitensor or dressed nonlocal kernel:

```text
K(|x - x_i|, t - t_i, s_i)  ->  K(x, x')
```

with a minimal form:

```text
K(x, x') = K_sigma(sigma(x, x'), tau_M, l_Pl) P(x, x')
```

where:

| Symbol | Meaning | Status |
|---|---|---|
| `sigma(x, x')` | invariant interval / Synge-type world-function between points | Candidate formalization |
| `tau_M` | memory-kernel decay or relaxation scale | To be constrained |
| `l_Pl` | Planck length cutoff / nucleation scale | PNT scaffold |
| `P(x, x')` | parallel-transport, bitensor, or gauge-dressing factor | Required for nonlocal comparison |

A corresponding nonlocal memory contribution may be written schematically as:

```text
M(x) = integral dV_x' K(x, x') C(x')
```

where `dV_x' = sqrt(-g(x')) d^4x'` is the covariant spacetime volume element and `C(x')` is the local collapse-intensity source.

### Required next step

Define whether `P(x, x')` is:

1. a gravitational parallel propagator only;
2. a gauge Wilson-line-like dressing for internal gauge fields;
3. a phenomenological transport operator for the memory field;
4. a deliberately restricted object used only in an effective cosmological background.

Until this is defined, the memory kernel remains an OPEN mathematical vulnerability.

---

## Gate 2: Stress-energy conservation

### Vulnerability

Einstein-type field equations require compatibility with the contracted Bianchi identity. If a memory stress tensor is inserted by hand, the total stress-energy tensor may fail to satisfy:

```text
nabla_mu T_total^{mu nu} = 0
```

This would make the gravitational sector inconsistent unless the violation is explicitly treated as an effective open-system exchange with another sector.

### Candidate action-first structure

Use an action-level formulation:

```text
S_total = S_EH + S_matter + S_M + S_int
```

where:

| Term | Meaning |
|---|---|
| `S_EH` | Einstein-Hilbert gravitational action or modified-gravity base action |
| `S_matter` | ordinary matter/radiation sector |
| `S_M` | memory-field sector |
| `S_int` | interaction between memory, collapse source, and matter/geometry |

Then define the memory stress tensor by variation with respect to the metric:

```text
T_M_{mu nu} = -(2 / sqrt(-g)) delta S_M / delta g^{mu nu}
```

and require the coupled system to obey:

```text
nabla_mu (T_matter^{mu nu} + T_M^{mu nu} + T_int^{mu nu}) = 0
```

### Minimal scalar-field support model

A conservative support model can represent the memory substrate as a scalar field `phi_M`:

```text
S_M = integral d^4x sqrt(-g) [ -1/2 g^{mu nu} (nabla_mu phi_M)(nabla_nu phi_M) - V_M(phi_M) ]
```

with an interaction term:

```text
S_int = integral d^4x sqrt(-g) g_M phi_M C(x)
```

where `C(x)` is the collapse-intensity source and `g_M` is a coupling constant whose units must be audited separately.

This is only a candidate support model. It does not prove that `phi_M` exists, and it does not prove that PNT/SoCT modifies gravity.

### Required next step

Derive the Euler-Lagrange equation for `phi_M`, compute `T_M_{mu nu}`, and show the explicit exchange equation between matter, interaction, and memory sectors.

Until then, stress-energy conservation remains OPEN.

---

## Gate 3: Junction-surface tensor definitions

### Current scaffold

The repo now has a non-null Israel-junction-style scaffold:

```text
papers/math/israel-junction-causal-inversion-surface.md
```

The core standard junction expression is:

```text
S_GR_uv = -(1 / 8 pi G) ( [K_uv] - h_uv [K] )
```

and the conservative SoCT/PNT ansatz is:

```text
S_SOC_uv = S_GR_uv + S_M_uv
S_M_uv = lambda_Sigma M_uv
```

or:

```text
S_SOC_uv = -(1 / 8 pi G) ( [K_uv] - h_uv [K] ) + lambda_Sigma M_uv
```

### Remaining vulnerability

This is only a non-null hypersurface scaffold. It is appropriate for timelike or spacelike matching surfaces under standard assumptions. If the causal-inversion boundary is horizon-like or null, this scaffold is not sufficient.

### Required next step

Add a dedicated null-surface extension with:

1. null normal/tangent conventions;
2. transverse curvature or null extrinsic-curvature analogues;
3. surface stress tensor for lightlike shells;
4. explicit relationship between null-shell variables and `M_uv` or its null-surface analogue.

Until then, the junction-surface gate is PARTIALLY ADDRESSED, not resolved.

---

## Gate 4: Decoherence and long-timescale memory survival

### Vulnerability

If the memory channel is an ordinary local quantum coherence channel, environmental decoherence will generally suppress it rapidly. PNT/SoCT therefore needs a clear distinction between short-lived laboratory-scale coherence and long-lived cosmological memory.

### Two-timescale decomposition

Define:

```text
M(x,t) = M_f(x,t) + M_p(x,t)
```

where:

| Symbol | Meaning |
|---|---|
| `M_f` | fast local memory / ordinary decohering response |
| `M_p` | protected or slow memory channel |

A minimal phenomenological two-timescale system is:

```text
partial_t M_f = alpha_f C - beta_f M_f + D_f nabla^2 M_f
```

```text
partial_t M_p = alpha_p Q[C] - beta_p M_p + D_p nabla^2 M_p
```

with the hierarchy:

```text
beta_p << beta_f
```

and, for cosmological relevance:

```text
tau_p = 1 / beta_p >> tau_f = 1 / beta_f
```

### Topological-protection placeholder

The protected source term is written as `Q[C]`, not simply `C`, to keep the protection mechanism explicit and unresolved. Candidate interpretations include:

1. boundary winding or index-like collapse history;
2. horizon/surface encoded memory;
3. Planck-cell nucleation state class;
4. large-scale topological defect or domain structure;
5. effective coarse-grained memory invariant.

No topological protection claim is established until `Q[C]` is defined and shown to be stable under perturbations.

### Required next step

Define `Q[C]`, identify its conserved or approximately conserved quantity, and state the empirical failure condition for the protected channel.

Until then, the decoherence/timescale issue remains OPEN.

---

## Integration with P2 / P5 dark-energy framing

The two-timescale model is the most natural bridge into the dark-energy / Hubble-window track. A minimal PNT two-timescale dark-energy interpretation would treat the slow memory channel as contributing an effective background term:

```text
rho_eff(t) = rho_Lambda + rho_Mp(t)
```

with:

```text
rho_Mp(t) proportional_to M_p(t)
```

and a conservative equation-of-state placeholder:

```text
w_eff(a) = -1 + delta_w(M_p, dM_p/dt, environment)
```

This should remain a candidate phenomenological bridge until derived from an action or constrained by data.

---

## Peer-review status labels

Use these labels in related files:

| Label | Meaning |
|---|---|
| OPEN | known vulnerability; no full resolution yet |
| PARTIALLY ADDRESSED | scaffold exists but important cases remain |
| CANDIDATE | plausible resolution path; not yet derived or tested |
| FORMAL SCAFFOLD | math language exists, but not established physics |
| READY FOR TEST DESIGN | equations and assumptions are explicit enough to build a falsifiable analysis |
| RESOLVED | do not use unless the derivation is complete and independently checked |

---

## Claim boundary

This audit does not prove PNT, SoCT, memory gravity, Engramons, parent-child universe transfer, or a dark-energy mechanism.

It records what must be true mathematically for the framework to survive serious peer review:

1. nonlocal kernels must be covariant/gauge safe;
2. memory stress-energy must be conservation-compatible;
3. junction tensors must be explicitly defined for the relevant surface class;
4. long-timescale memory must have a protected or otherwise justified survival mechanism.

Until these gates are closed, all related claims should remain PRELIMINARY, FORMAL SCAFFOLD, or CANDIDATE.