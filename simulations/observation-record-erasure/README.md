# Simulation 3 — Observation Record Creation and Erasure

**Status:** Implemented baseline toy model  
**Physics level:** Standard closed-system quantum dynamics; no SoCT memory feedback  
**Purpose:** Distinguish current record strength from record-creation history

## Question

If a measurement-like interaction creates an accessible record and a later inverse interaction erases that record, what quantity should a proposed SoCT memory source track?

Candidate possibilities include:

```text
A. current correlation only
B. current accessible record only
C. time-integrated record persistence
D. positive record-production history
E. an effectively irreversible record-production functional
```

This simulation does not choose among them. It exposes how differently they behave under exact reversible erasure.

## Model

System qubit:

```math
|+>_S = (|0> + |1>)/sqrt(2)
```

Pointer begins in:

```math
|0>_P.
```

A measurement-like unitary produces conditional pointer states

```math
|0>_S|0>_P -> |0>_S|0>_P
```

and

```math
|1>_S|0>_P -> |1>_S[cos(theta)|0> + sin(theta)|1>]_P.
```

The conditional pointer-state trace distance is

```math
D_P(theta) = |sin(theta)|.
```

For an equal-prior binary source ensemble, the pointer Holevo information is

```math
chi_P(theta)
  = H_2[(1 + |cos(theta)|)/2],
```

where `H_2` is binary entropy in bits.

For this exploratory benchmark we use

```math
Omega_P = D_P chi_P.
```

This factorized `Omega` remains a diagnostic proxy, not a proposed physical law.

## Erasure step

After record creation, the exact inverse unitary is applied.

In the ideal isolated model,

```text
U(theta) -> U(theta)^dagger
```

returns the total state to its pre-measurement product state.

Therefore after erasure:

```math
D_P = 0,
chi_P = 0,
Omega_P = 0.
```

This is an intentional closed-system benchmark. No irreversible environment is included yet.

## History functional

To expose the SoCT ambiguity, define an exploratory positive record-production history

```math
J_rec(t) = integral [d Omega / dt]_+ dt.
```

For an instantaneous create-then-erase protocol,

```math
J_rec = Omega_created
```

while

```math
Omega_final = 0.
```

Thus the two candidate source philosophies differ sharply:

```text
present-record source:        C_obs ~ Omega(t)
                              -> returns to zero after exact erasure

record-history source:        C_obs or M source ~ positive record production
                              -> retains a nonzero history value after erasure
```

The simulation does not establish that the second quantity is physical. It simply identifies it as a clean discriminating choice that future SoCT work must justify or reject.

## Baseline result

At maximum record strength

```math
theta = pi/2,
```

creation gives

```math
D_P = 1,
chi_P = 1 bit,
Omega_P = 1.
```

After exact inverse erasure:

```math
D_P = 0,
chi_P = 0,
Omega_P = 0,
```

but the bookkeeping functional remains

```math
J_rec = 1.
```

This is the central result of Simulation 3.

## Interpretation

Standard unitary quantum mechanics permits the record to be created and then completely removed in this closed-system model. Therefore a SoCT theory that claims `collapse leaves memory` must answer a precise question:

> Does `M` source from currently existing records, durable/irreversible records, or the historical creation of records even when the microscopic record is later reversed?

Those alternatives are not equivalent.

A physically serious SoCT model cannot choose the history-retaining option merely because it matches the phrase `collapse leaves memory`; it must derive or empirically motivate the irreversibility/persistence rule.

## Next gate

Simulation 3b / Simulation 4 preparation should add an environment or controlled dephasing channel between record creation and attempted erasure.

That permits comparison of:

```text
exactly reversible record
partially reversible record
effectively irreversible distributed record
```

and provides the natural bridge to a candidate source functional such as

```math
Gamma_rec = G(dI/dt, persistence, redundancy, irreversibility).
```

Only after that should the repo introduce a nonzero exploratory SoCT memory-feedback term.

## Files

```text
simulate_record_erasure.py
results.csv
README.md
```

## Claim boundary

This simulation demonstrates a distinction between current record state and cumulative record history in a toy model. It does **not** demonstrate a physical residual after quantum erasure and does not validate SoCT memory.
