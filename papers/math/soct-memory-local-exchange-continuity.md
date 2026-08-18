# SoCT Memory Field — Local Exchange / Continuity Constraint

**Status:** analytical constraint program / flat-background local exchange scaffold  
**Claim level:** derived consequence of the candidate causal completion; not established new physics  
**Related files:** `papers/math/soct-memory-origin-constraints-and-causal-completion.md`, `papers/math/soct-memory-action-energy-exchange.md`, `papers/math/pnt-soct-covariance-conservation-and-timescale-audit.md`

## 1. Purpose

SIM-04K established a global flat-background energy ledger for the candidate causal memory equation. The next question is stronger:

> If `M` is a physical field, does the same trajectory predict **where** source energy leaves the record-producing sector, where energy is stored/transported by the field, and where damping energy enters an ordinary bath?

Global conservation alone is insufficient. A model could reproduce the total energy exchange while depositing energy in the wrong spatial locations.

## 2. Candidate causal equation

Use the current causal completion

```math
\partial_t^2 M
+ \gamma\partial_t M
- c_M^2\nabla^2M
+ \omega_M^2 M
= g C_{obs}.
```

The SIM-04J overdamped mapping remains

```math
\alpha=g/\gamma,
\qquad
\beta=\omega_M^2/\gamma,
\qquad
D_M=c_M^2/\gamma.
```

## 3. Local field energy density and flux

Multiply the equation by `\dot M` and use

```math
- c_M^2 \dot M\nabla^2M
= -c_M^2\nabla\cdot(\dot M\nabla M)
+ c_M^2\nabla\dot M\cdot\nabla M.
```

Define

```math
\rho_M
= \frac12\dot M^2
+ \frac12 c_M^2|\nabla M|^2
+ \frac12\omega_M^2 M^2,
```

and field-energy flux

```math
\mathbf S_M=-c_M^2\dot M\nabla M.
```

Then

```math
\partial_t\rho_M
+ \nabla\cdot\mathbf S_M
= g C_{obs}\dot M
- \gamma\dot M^2.
```

This is the local flat-background energy ledger for the effective damped field.

## 4. Explicit source and bath exchange bookkeeping

Introduce local exchange densities

```math
\partial_t\rho_{src}=-gC_{obs}\dot M,
```

```math
\partial_t\rho_{bath}=+\gamma\dot M^2.
```

If the source and bath sectors are taken as locally stationary bookkeeping channels in this first scaffold, then

```math
\partial_t(\rho_{src}+\rho_M+\rho_{bath})
+\nabla\cdot\mathbf S_M=0.
```

Thus the same `(g, gamma, beta, D_M)` that predicts the field trajectory also predicts two independent spatial exchange maps:

```text
source depletion / return:  g C_obs M_t
bath gain:                  gamma M_t^2.
```

No independent backreaction amplitude should be fitted after the field parameters are fixed.

## 5. Stronger falsification than global balance

Integrating over a closed or periodic domain recovers the SIM-04K global identity.

But local conservation makes a stronger prediction. Two models may satisfy the same total exchange

```math
\int dV\,P_{src}
\quad\text{and}\quad
\int dV\,P_{bath}
```

while disagreeing on the spatial fields

```math
P_{src}(x,t)=gC_{obs}(x,t)\dot M(x,t),
```

```math
P_{bath}(x,t)=\gamma\dot M(x,t)^2.
```

Therefore an experiment should not rely only on an integrated heat signal. Spatially resolved exchange or multiple independent local sensors can reject a model that passes only a global energy ledger.

## 6. What this does and does not accomplish

This scaffold does:

- make the exchange destination explicit at the level of energy bookkeeping;
- link source depletion, field transport, and bath gain locally;
- provide an additional held-out observable with no new exchange-scale fit;
- strengthen the physical burden on any conventional mimic.

It does **not** yet:

- derive a microscopic bath Hamiltonian that generates the damping term;
- define a covariant bath four-velocity or preferred-frame structure;
- derive a complete curved-spacetime `T^{mu nu}` for source + memory + bath;
- close the Bianchi/covariance gate;
- prove that the bath or memory sector exists in nature.

## 7. Next mathematical requirement

A full conservation-compatible completion should replace the bookkeeping bath by explicit dynamical degrees of freedom or an open-system derivation, then construct

```math
T^{\mu\nu}_{total}
= T^{\mu\nu}_{matter/source}
+ T^{\mu\nu}_M
+ T^{\mu\nu}_{bath/int}
```

with

```math
\nabla_\mu T^{\mu\nu}_{total}=0.
```

Until that derivation exists, the stress-energy gate remains OPEN.

## 8. Simulation gate

SIM-04L tests three synthetic possibilities while fitting field parameters only from probe trajectories:

```text
action_local    = local source and bath exchange follow the field ledger;
global_scramble = identical global exchange totals but spatial deposition is wrong;
no_exchange     = field-like probe trajectory with no corresponding source/bath exchange.
```

The key question is whether local exchange measurements distinguish the first case even when a globally balanced adversary remains indistinguishable after spatial integration.
