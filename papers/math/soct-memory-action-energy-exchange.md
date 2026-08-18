# SoCT Memory Field — Action and Energy-Exchange Scaffold

**Status:** flat-background energetic-consistency scaffold / SIM-04K derivation  
**Claim level:** candidate completion; not established new physics and not a full covariant stress-energy derivation  
**Related files:** `papers/math/soct-memory-origin-constraints-and-causal-completion.md`, `papers/math/pnt-soct-covariance-conservation-and-timescale-audit.md`, `papers/math/soc-operational-observation-model.md`

## 1. Purpose

SIM-04J sharpened the phenomenological memory equation by treating

```math
\partial_t M=\alpha C_{obs}-\beta M+D_M\nabla^2M
```

as the overdamped/low-frequency limit of the causal completion

```math
\partial_t^2M+\gamma\partial_tM-c_M^2\nabla^2M+\omega_M^2M=gC_{obs}.
```

The next consistency requirement is energetic:

> If `M` is a physical field, its trajectory cannot be fitted independently of the work needed to source it, the energy stored in it, the energy carried across boundaries, and the energy dissipated by its damping channel.

This document derives that linked energy ledger in a flat-background effective model. It does **not** close the repository's full general-relativistic stress-energy / Bianchi-identity gate.

## 2. Conservative field sector

Ignoring damping for the moment, use the effective Lagrangian density

```math
\mathcal L_M
=\frac12(\partial_tM)^2
-\frac12c_M^2|\nabla M|^2
-\frac12\omega_M^2M^2
+gM C_{obs}.
```

Varying `M` gives

```math
\partial_t^2M-c_M^2\nabla^2M+\omega_M^2M=gC_{obs}.
```

The phenomenological damping term `gamma partial_t M` is then interpreted as effective exchange with unresolved bath/environment degrees of freedom:

```math
\partial_t^2M+\gamma\partial_tM-c_M^2\nabla^2M+\omega_M^2M=gC_{obs}.
```

A fundamental covariant theory would need to model that bath/exchange sector explicitly or replace it with a covariant construction. Damping is not being claimed to arise from the conservative single-field action by itself.

## 3. Field energy density and flux

For the conservative `M` sector define

```math
\rho_M
=\frac12(\partial_tM)^2
+\frac12c_M^2|\nabla M|^2
+\frac12\omega_M^2M^2.
```

The associated flat-background energy flux is

```math
\mathbf S_M=-c_M^2(\partial_tM)\nabla M.
```

Multiplying the damped field equation by `partial_t M` and using the product rule gives

```math
\partial_t\rho_M+\nabla\cdot\mathbf S_M
=gC_{obs}\,\partial_tM
-\gamma(\partial_tM)^2.
```

This is the key SIM-04K identity.

Interpretation:

```text
g C_obs partial_t M    = source work density
rho_M                   = stored memory-field energy density
gamma (partial_t M)^2  = damping / bath-loss density
S_M                     = boundary energy flux.
```

## 4. Integrated energy ledger

Define

```math
E_M(t)=\int_V\rho_M\,dV.
```

Then

```math
\frac{dE_M}{dt}
=g\int_V C_{obs}\,\partial_tM\,dV
-\gamma\int_V(\partial_tM)^2dV
-\oint_{\partial V}\mathbf S_M\cdot d\mathbf A.
```

For periodic or no-flux boundaries,

```math
\frac{dE_M}{dt}=P_{src}(t)-P_{damp}(t),
```

with

```math
P_{src}=g\int C_{obs}\,\partial_tM\,dV,
```

```math
P_{damp}=\gamma\int(\partial_tM)^2dV.
```

The cumulative closed-system ledger is therefore

```math
E_M(t)-E_M(t_0)=W_{src}(t_0,t)-Q_{damp}(t_0,t).
```

A claimed physical `M` trajectory that violates this ledger under the assumed completion falsifies the completion rather than inviting independent retuning of a backreaction channel.

## 5. Link to the overdamped parameters

SIM-04J derived

```math
\alpha=g/\gamma,
\qquad
\beta=\omega_M^2/\gamma,
\qquad
D_M=c_M^2/\gamma.
```

Thus, once `gamma` and the source normalization are independently fixed,

```math
g=\gamma\alpha,
\qquad
\omega_M^2=\gamma\beta,
\qquad
c_M^2=\gamma D_M.
```

The energy ledger is therefore linked to the same parameters already used to predict the field trajectory. In this scaffold there is no independent arbitrary `backreaction amplitude`.

## 6. Observation-derived source

For the current record-production route,

```math
C_{obs}=\kappa_{rec}\Gamma_{rec}
```

(or a competing predeclared record-aware functional such as `Omega`).

Then source work becomes

```math
P_{src}
=g\kappa_{rec}\int\Gamma_{rec}\,\partial_tM\,dV.
```

This creates a linked chain:

```text
ordinary record production
-> C_obs
-> M trajectory
-> field energy / damping heat / boundary flux
-> probe feedback.
```

A future empirical `M` interpretation should not be allowed to fit the last item while ignoring the middle energetic consequences.

## 7. What SIM-04K can test

SIM-04K uses a periodic one-dimensional field and an independently measured bath-heat observable

```math
Q_{damp}=\int dt\,\gamma\int dx\,(\partial_tM)^2.
```

The procedure is deliberately asymmetric:

1. fit the field parameters from probe trajectories on training histories;
2. freeze those parameters;
3. predict held-out probe trajectories;
4. **without an additional heat-scale fit**, predict damping heat on held-out histories;
5. compare against nulls in which probe history and energetic backreaction are not linked by the field equation.

If probe trajectories fit but the predicted heat/backreaction does not appear, the physical-field interpretation is weakened or falsified under this completion.

## 8. Remaining ontology boundary

This energetic constraint does not solve the hidden-state naming problem.

A conventional physical reservoir with the **same complete action/exchange structure** can reproduce the same

```text
source law
field trajectory
stored energy
damping heat
boundary flux
probe coupling.
```

Such a competitor is physically much more constrained than a generic hidden scalar fit, but it remains observationally degenerate under measurements of those same quantities.

The contribution of SIM-04K is therefore to raise the burden from

```text
"some hidden state can fit the probe residual"
```

to

```text
"a competing physical sector must reproduce the same trajectory and the same independently measured exchange ledger."
```

## 9. General-relativistic boundary

This file does **not** yet derive a covariant `T_M^{mu nu}` for the complete damped/open system, nor prove

```math
\nabla_\mu T_{total}^{\mu\nu}=0.
```

A full GR-compatible treatment still requires:

- a covariant action or effective metric for the propagation sector;
- an explicit bath/exchange sector if damping is physical;
- variation with respect to `g_{mu nu}`;
- an explicit exchange equation among matter/record, memory, and bath sectors;
- compatibility with the Bianchi identity.

Accordingly, the stress-energy gate remains **OPEN**, with the flat-background energy ledger now **PARTIALLY ADDRESSED** as a prerequisite scaffold.

## 10. Falsification rule

Under this candidate completion, use the following rule:

> A field-like probe residual is insufficient. The same fixed field parameters must also satisfy the independently measured source-work / stored-energy / damping-loss / flux ledger. Persistent failure of that linked prediction falsifies this physical completion even if the probe trajectory alone can still be fitted.
