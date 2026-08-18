# SIM-04L — Local Source / Field / Bath Exchange Results

**Status:** synthetic local-continuity benchmark complete  
**Claim level:** methodology only; not evidence for a physical SoCT memory field.

## Question

Does the candidate causal field predict not only the total energy exchange but also the **spatial pattern** of source depletion/return and bath gain, using the same parameters fitted from probe trajectories?

The tested equation is

```math
\partial_t^2 M
+ \gamma\partial_tM
- c_M^2\nabla^2M
+ \omega_M^2M
= gC_{obs},
```

with

```math
c_M^2=\gamma D_M,
\qquad
\omega_M^2=\gamma\beta.
```

Its local flat-background continuity identity is

```math
\partial_t\rho_M+\nabla\cdot\mathbf S_M
= gC_{obs}\dot M-\gamma\dot M^2.
```

Thus the field trajectory predicts

```math
P_{src}(x,t)=gC_{obs}(x,t)\dot M(x,t)
```

and

```math
P_{bath}(x,t)=\gamma\dot M(x,t)^2
```

with no separate exchange-amplitude fit.

## Design

The spatial lattice and source histories follow the SIM-04K family. Parameters are fitted **only from probe data** on histories `A/B`; histories `C/D` are held out.

True synthetic field parameters:

```text
gamma  = 5.0
beta   = 0.08
D_M    = 0.18
lambda = 0.70
```

Noise levels:

```text
probe sigma                 = 0.0015
local exchange sensor sigma = 0.0015
```

Fifty independent noise realizations are evaluated.

The held-out exchange observables are site-resolved integrals in five time windows on a 16-site periodic lattice.

## Generators

### `action_local`

Probe, source exchange, and bath exchange all come from the same field ledger.

### `global_scramble`

The probe trajectory is unchanged. The source and bath exchange maps are spatially shifted while preserving **every time-window global total**.

This is deliberately designed to pass global energy accounting while violating the field-predicted local deposition pattern.

### `no_exchange`

The same field-like probe trajectory is generated, but both excess source and bath exchange channels are zero apart from measurement noise.

## Mean results

| Generator | fitted beta | fitted D_M | fitted lambda | held-out probe RMSE | action source local RMSE | action bath local RMSE | zero-source RMSE | zero-bath RMSE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **action_local** | 0.0808 | 0.1780 | 0.7001 | 0.00149 | **0.00152** | **0.00151** | 0.01670 | 0.01503 |
| **global_scramble** | 0.0808 | 0.1780 | 0.7001 | 0.00149 | **0.02348** | **0.02110** | 0.01669 | 0.01503 |
| **no_exchange** | 0.0808 | 0.1780 | 0.7001 | 0.00149 | **0.01671** | **0.01505** | **0.00152** | **0.00151** |

The probe fit is intentionally identical across the three generators. The discriminator is the independent exchange measurement.

## Global-total check

For the action-consistent and spatially scrambled generators, the mean RMSE of the field prediction against the **global time-window totals** is the same:

```text
action_local source global RMSE   ~ 0.00592
action_local bath global RMSE     ~ 0.00598

global_scramble source global RMSE ~ 0.00592
global_scramble bath global RMSE   ~ 0.00598
```

The larger numerical scale relative to one local sensor is expected because each global value sums 16 independent noisy local measurements.

The key result is therefore

```text
global conservation can pass
while local continuity fails.
```

In the scrambled generator the locally predicted source/bath maps miss at roughly `0.02`, more than an order of magnitude above the `0.0015` local sensor noise, even though the global totals are unchanged.

## Local identity check

The semi-discrete local continuity identity closes to floating-point precision:

```text
max absolute local identity error ~ 3.82e-17.
```

This verifies that the lattice implementation is internally consistent with the stated local exchange equation.

## Interpretation

### 1. A physical-field interpretation carries spatial backreaction structure

A candidate `M` trajectory cannot be allowed to fit a probe residual while assigning source depletion and bath heating arbitrarily.

Once `(gamma,beta,D_M,g)` are fixed, the model predicts where exchange should occur.

### 2. Integrated calorimetry alone is insufficient

The `global_scramble` adversary demonstrates that correct total source/bath exchange does not establish the local field law.

A stronger empirical test would combine:

```text
probe trajectory
+ global energy ledger
+ spatially resolved exchange/backreaction.
```

### 3. The test can falsify the field interpretation

The `no_exchange` generator has the same field-like probe trajectory, yet the action-linked exchange prediction fails at approximately `0.015-0.017`, while the zero-exchange null reaches the local noise floor.

Thus a good probe fit is not sufficient evidence for a physical field.

### 4. Ontology ambiguity remains

A conventional hidden physical sector with the **same complete local equation, source coupling, energy density, flux, exchange law, and probe coupling** remains observationally identical under these observables:

```text
max prediction difference = 0.0.
```

The result therefore constrains the required physical structure; it does not uniquely establish the name or ontology `M`.

## What SIM-04L establishes

Only the following narrow synthetic result:

> The candidate causal field implies a local source/field/bath continuity pattern that can distinguish an action-consistent generator from both a no-exchange generator and a globally balanced but spatially incorrect adversary, without fitting separate exchange amplitudes.

It does not show that nature contains this field or that the bath/source bookkeeping is a complete microscopic model.

## Remaining conservation gate

The bath is still represented as an exchange-energy channel, not as microscopic dynamical degrees of freedom. A full theory must derive the damping/exchange structure from an explicit environment or covariant effective action and construct

```math
T^{\mu\nu}_{total}
= T^{\mu\nu}_{source/matter}
+ T^{\mu\nu}_M
+ T^{\mu\nu}_{bath/int}
```

with

```math
\nabla_\mu T^{\mu\nu}_{total}=0.
```

Therefore the GR/covariant conservation gate remains OPEN.

## Reproduction

```bash
python experiments/observation-foundations/sim04l_local_exchange_continuity.py
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim04l_local_exchange_continuity.py --json
```
