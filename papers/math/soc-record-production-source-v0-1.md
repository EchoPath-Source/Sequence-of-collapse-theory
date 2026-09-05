# SoCT Record-Production Source v0.1

**Status:** Candidate operational source definition / not established physics  
**Role:** Replace the unspecified observation-strength placeholder with a testable record-production quantity before adding SoCT memory feedback  
**Related:** `soc-operational-observation-model.md`, `soc-localization-memory-hamiltonian.md`, `simulations/observation-record-erasure/`, `simulations/observation-redundancy-irreversibility/`

---

## 1. Motivation

The current memory equation is

```math
partial_t M = alpha C - beta M + D_M nabla^2 M.
```

The observation project asks what physically determines the source `C`.

Simulation 1 established that measurement-like interaction can generate distinguishable accessible records. Simulation 2 separated environmental decoherence from record acquisition by a designated subsystem. Simulation 3 showed that an ideal microscopic record can be created and exactly erased. Simulation 3b showed that copying records into multiple degrees of freedom makes partial erasure insufficient to remove all accessible record structure.

The resulting source candidate should therefore not count every transient correlation equally.

---

## 2. Candidate ingredients

For a specified observable distinction, define:

```text
I_acc(x,t)   accessible information carried by the record
P_R(x,t)     persistence / retention factor over the chosen timescale
R_d(x,t)     redundancy / distribution factor
Xi_irr(x,t)  resistance-to-reversal / residual-record factor
```

All four are operational placeholders whose final definitions must be fixed by the model and experiment.

A conservative record-strength quantity is

```math
Q_rec = I_acc P_R R_d Xi_irr.
```

The product form is provisional. Its primary purpose is to enforce the logical boundary that a source should be suppressed when accessible record information, persistence, distribution, or resistance to reversal vanish on the chosen scale.

---

## 3. Versioned record-production rate

Define the v0.1 record-production rate as the positive production of durable record strength:

```math
Gamma_rec^(0.1)(x,t)
    = [partial_t Q_rec(x,t)]_+,
```

with

```math
[z]_+ = max(z,0).
```

This definition distinguishes current durable-record strength from cumulative record-formation history.

The cumulative history variable is

```math
J_rec(x,t)
    = integral_{t0}^t Gamma_rec^(0.1)(x,t') dt'.
```

`J_rec` is bookkeeping at this stage. Standard quantum theory does not imply that it is a new physical field.

---

## 4. Candidate SoCT source bridge

The first SoCT-specific bridge is

```math
C_obs(x,t) = kappa_rec Gamma_rec^(0.1)(x,t).
```

Then the observation-sourced memory equation becomes

```math
partial_t M
    = alpha kappa_rec Gamma_rec^(0.1)
    - beta M
    + D_M nabla^2 M.
```

Equivalently, define

```math
alpha_rec = alpha kappa_rec
```

and write

```math
partial_t M
    = alpha_rec Gamma_rec^(0.1)
    - beta M
    + D_M nabla^2 M.
```

No claim is made yet that nature contains this additional `M` degree of freedom.

---

## 5. Dimensional sanity check

If accessible information and the factors `P_R`, `R_d`, and `Xi_irr` are normalized dimensionless quantities, then

```math
[Q_rec] = 1
```

and therefore

```math
[Gamma_rec] = T^-1.
```

From

```math
partial_t M = alpha_rec Gamma_rec - beta M + D_M nabla^2 M,
```

we require

```math
[beta] = T^-1,
[D_M] = L^2 T^-1.
```

If `M` has units `[M]`, then

```math
[alpha_rec] = [M].
```

because `alpha_rec Gamma_rec` must have units `[M] T^-1`.

This does not fix the physical units of `M`; that remains an explicit open gate tied to the later field/action construction.

---

## 6. Why v0.1 weights irreversibility/redudancy

A fully reversible microscopic unitary can generate correlation and then erase it exactly. Treating that temporary correlation as identical to a macroscopic distributed measurement would make the source definition too permissive.

Simulation 3b motivates the stricter distinction:

```text
correlation
  -> accessible record
  -> persistent record
  -> distributed / redundant record
  -> effectively hard-to-reverse record
```

The v0.1 source is therefore closer to `durable record production` than to raw entanglement production.

---

## 7. Null-model boundary

Under standard quantum mechanics, all quantities above can be used as diagnostics of measurement, information flow, record proliferation, and erasure without introducing a new memory field.

SoCT becomes distinct only when it adds the hypothesis:

```text
different durable-record histories can produce different future dynamics
```

even after ordinary present-state variables are matched.

That discriminator is the target of Simulation 4.

---

## 8. Simulation 4 gate

Simulation 4 should compare two systems satisfying, as closely as the toy model permits,

```math
rho_A(t0) = rho_B(t0)
```

with identical current Hamiltonian/environment parameters but different historical record integrals

```math
J_rec,A != J_rec,B.
```

The standard null model predicts no difference attributable to erased history once the complete current physical state is matched.

The exploratory SoCT extension assigns

```math
M_A(t0) != M_B(t0)
```

and evolves both under

```math
H = H_0 + lambda_M M O_M.
```

The measurable target is a history-dependent phase, frequency, visibility, or transition-probability residual proportional to `lambda_M Delta M`.

---

## 9. Falsification discipline

The observation program should abandon or revise this source form if:

- the proposed factors collapse into a redundant reparameterization of ordinary decoherence with no useful operational distinction;
- no stable definition survives changes in coarse-graining or record partition;
- the source depends arbitrarily on observer-chosen bookkeeping rather than physically specified degrees of freedom;
- the later memory-feedback model cannot be made conservation-compatible or experimentally distinguishable from drift/noise.

---

## 10. Claim boundary

Use:

> SoCT v0.1 explores whether durable, accessible, distributed record production can serve as the source variable for a speculative collapse-memory field.

Avoid:

> Quantum information automatically creates spacetime memory or proves objective collapse.
