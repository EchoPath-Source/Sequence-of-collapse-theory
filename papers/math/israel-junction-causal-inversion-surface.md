# Israel Junction Surface Formalism for the Causal Inversion Boundary

**Status:** FORMAL SCAFFOLD / GR-facing mathematical language  
**Claim level:** Proposed boundary formalism, not established physics  
**Related tracks:** `papers/p6-black-holes-memory-compression-nodes/`, `papers/p3-causal-inversion-directional-memory/`, `simulations/parent-child-transfer/`

---

## Purpose

This note introduces a conservative Israel-junction-style surface formalism for the Causal Inversion / parent-child transition boundary used in the Sequence of Collapse / Planck Nucleation research program.

The goal is not to claim that black holes create new universes or that singularities have been resolved. The goal is narrower: define a standard general-relativity-facing surface language in which a proposed non-singular transition boundary could be expressed, audited, and eventually tested.

---

## 1. Transition Hypersurface

Let `Sigma` denote the transition hypersurface separating two spacetime regions:

```text
M_plus   = exterior / parent-region spacetime
M_minus  = interior / descendant-region spacetime
```

with metrics:

```text
g_plus_mu_nu

g_minus_mu_nu
```

Intrinsic coordinates on `Sigma` are denoted:

```text
y^u = (y^0, y^1, y^2)
```

where Latin indices `u,v,...` label coordinates intrinsic to the hypersurface and Greek indices `mu,nu,...` label spacetime coordinates.

The embedding map is:

```text
x^mu = x^mu(y^u)
```

with tangent basis vectors:

```text
e_u^mu = partial x^mu / partial y^u
```

---

## 2. Induced Metric and First Junction Condition

The induced metric on the hypersurface is:

```text
h_uv = g_mu_nu e_u^mu e_v^nu
```

evaluated on each side of the boundary:

```text
h_plus_uv  = g_plus_mu_nu  e_u^mu e_v^nu
h_minus_uv = g_minus_mu_nu e_u^mu e_v^nu
```

The first Israel junction condition requires continuity of the induced metric:

```text
[h_uv] = h_plus_uv - h_minus_uv = 0
```

Physical interpretation: the intrinsic geometry of the transition surface is continuous even if the way it is embedded into each surrounding spacetime changes.

For Causal Inversion, this is the minimum mathematical requirement for treating the transition as a matched boundary rather than an uncontrolled singular cut.

---

## 3. Extrinsic Curvature

Let `n_mu^plus` and `n_mu^minus` denote unit normals to `Sigma` on each side.

The extrinsic curvature on each side is:

```text
K_plus_uv  = e_u^mu e_v^nu nabla_plus_mu  n_plus_nu
K_minus_uv = e_u^mu e_v^nu nabla_minus_mu n_minus_nu
```

The jump in extrinsic curvature is:

```text
[K_uv] = K_plus_uv - K_minus_uv
```

with hypersurface trace:

```text
[K] = h^uv [K_uv]
```

where `h^uv` is the inverse induced metric.

Physical interpretation: `[K_uv]` measures the discontinuity in how the same intrinsic surface bends into the two matched spacetime regions.

---

## 4. Israel Surface Stress-Energy Tensor

For a non-null hypersurface, the Israel surface stress-energy tensor is:

```text
S_uv = -(1 / 8 pi G) ( [K_uv] - h_uv [K] )
```

Equivalently, in compact matrix notation:

```text
S = -(1 / 8 pi G) ( [K]matrix - h Tr_h([K]matrix) )
```

where:

```text
Tr_h([K]matrix) = h^uv [K_uv]
```

This equation defines the effective stress-energy localized on the transition surface.

---

## 5. Diagonal Surface Matrix Form

For a highly symmetric boundary, one may use a diagonal intrinsic surface metric and diagonal extrinsic-curvature jump as a first toy scaffold:

```text
h_uv = diag(-1, R_Sigma^2, R_Sigma^2 sin^2 theta)
```

and

```text
[K_uv] = diag(k_tau, k_theta, k_phi)
```

The trace is then:

```text
[K] = h^tau_tau k_tau + h^theta_theta k_theta + h^phi_phi k_phi
```

and the surface tensor components become:

```text
S_tau_tau   = -(1 / 8 pi G) ( k_tau   - h_tau_tau   [K] )
S_theta_theta = -(1 / 8 pi G) ( k_theta - h_theta_theta [K] )
S_phi_phi   = -(1 / 8 pi G) ( k_phi   - h_phi_phi   [K] )
```

This matrix form is a placeholder for later model-specific choices of `g_plus_mu_nu`, `g_minus_mu_nu`, and `R_Sigma`.

---

## 6. SoCT / PNT Memory-Corrected Junction Ansatz

The standard GR surface tensor may be extended phenomenologically as:

```text
S_SOC_uv = S_GR_uv + S_M_uv
```

where:

```text
S_GR_uv = -(1 / 8 pi G) ( [K_uv] - h_uv [K] )
```

and `S_M_uv` represents a proposed memory/compression contribution localized on the transition surface.

A minimal memory ansatz is:

```text
S_M_uv = lambda_Sigma M_uv
```

where:

```text
M_uv = normalized surface-memory tensor
lambda_Sigma = memory-surface coupling scale
```

To preserve dimensional homogeneity:

```text
[lambda_Sigma M_uv] = [S_uv]
```

If `M_uv` is dimensionless, then `lambda_Sigma` must carry the same units as surface stress-energy.

If `M_uv` is assigned physical units, then `lambda_Sigma` must be adjusted accordingly.

---

## 7. Candidate Causal-Inversion Matching Statement

A conservative Causal-Inversion boundary condition can be stated as:

```text
[h_uv] = 0
```

and

```text
S_SOC_uv = -(1 / 8 pi G) ( [K_uv] - h_uv [K] ) + lambda_Sigma M_uv
```

This preserves the standard junction structure while making the SoCT/PNT addition explicit and separately auditable.

A future model-specific derivation must define:

1. the parent-side metric `g_plus_mu_nu`;
2. the descendant-side metric `g_minus_mu_nu`;
3. the hypersurface embedding `x^mu(y^u)`;
4. the normal vectors `n_mu^plus` and `n_mu^minus`;
5. the memory tensor `M_uv`;
6. the units and empirical normalization of `lambda_Sigma`.

---

## 8. Null-Surface Caveat

The ordinary Israel junction formalism applies to non-null hypersurfaces.

If the Causal Inversion boundary is treated as horizon-like or null, the standard `S_uv` expression above is not sufficient. A null-shell treatment, such as a Barrabes-Israel-type formalism, would be required.

Repository claim boundary:

```text
Use the current document only as a non-null junction scaffold unless and until a dedicated null-surface formalism is added.
```

---

## 9. Claim Boundary

Use:

```text
This document defines a GR-facing surface formalism for expressing a proposed non-singular transition boundary.
```

Avoid:

```text
This proves black holes create child universes.
This resolves singularities.
This proves Causal Inversion.
This replaces the singularity theorems.
```

The present scaffold makes the hypothesis more mathematically inspectable. It does not establish the physical mechanism.

---

## 10. Next Work

1. Choose a simple parent-side metric, such as Schwarzschild or Kerr exterior.
2. Choose a descendant-side toy metric, such as FLRW-like interior or bounce patch.
3. Compute `h_uv`, `K_plus_uv`, `K_minus_uv`, and `S_uv` explicitly.
4. Add a dimensional-analysis note for `lambda_Sigma` and `M_uv`.
5. Decide whether the relevant boundary is timelike, spacelike, or null.
6. If null, add a separate null-shell formalism instead of overusing the non-null Israel form.
