# Simulation 4 — History-Matched Memory Feedback

**Status:** Exploratory SoCT-specific toy model  
**Purpose:** Convert the observation program into a clean null-vs-SoCT discriminator.

## Setup

Two qubits begin in the same standard quantum state

```math
|+> = (|0> + |1>)/sqrt(2)
```

with the same ordinary Hamiltonian, same current environment, and same present standard quantum description.

They differ only in the speculative SoCT memory variable inherited from earlier record-production history:

```math
M_A(0) = 0
M_B(0) = 1.
```

Memory decays as

```math
M(t) = M(0) exp(-beta t).
```

The exploratory Hamiltonian is

```math
H(t) = (omega/2) sigma_z + lambda_M M(t) sigma_z.
```

The null model is recovered exactly by

```math
lambda_M = 0.
```

## Analytic discriminator

For the memory-bearing arm, the additional accumulated phase is

```math
Delta phi_M(t)
    = lambda_M Delta M_0 [1 - exp(-beta t)] / beta.
```

Thus the null model predicts

```math
Delta phi_M = 0
```

for all times, while the exploratory SoCT arm predicts a history-dependent phase residual whenever

```math
lambda_M Delta M_0 != 0.
```

The measured return probability to `|+>` is

```math
P_+(t) = cos^2[ integral_0^t a(t') dt' ]
```

for `H=a(t) sigma_z`.

## Representative behavior

Using

```text
omega = 1
beta = 0.25
M_A0 = 0
M_B0 = 1
```

we obtain:

```text
lambda_M = 0.00 -> Delta P_+ = 0 at every sampled time
lambda_M = 0.01 -> small history-dependent oscillatory residual
lambda_M = 0.03 -> larger residual
lambda_M = 0.10 -> clearly separated toy trajectories
```

At `t=8`, the added phase is approximately:

```text
lambda_M=0.01 -> 0.0346 rad
lambda_M=0.03 -> 0.1038 rad
lambda_M=0.10 -> 0.3459 rad
```

Because memory decays, the additional phase approaches the finite limit

```math
Delta phi_M(infinity) = lambda_M Delta M_0 / beta.
```

## Why this matters

This is the first simulation in the observation ladder where SoCT makes a different prediction from the standard null by construction.

The discriminator is:

```text
same present standard quantum state
+ same ordinary Hamiltonian/environment
+ different prior durable-record history
-> different future evolution only if the extra memory variable is physically real and coupled.
```

That is a mathematically clean form of the SoCT statement `collapse leaves memory`.

## Critical caveat

The two arms are not literally identical in the full SoCT state description because `M_A != M_B`. They are matched only with respect to the ordinary quantum variables. This distinction must remain explicit in any paper or experimental proposal.

The simulation does not provide evidence that `M` exists. It demonstrates what an experimentally falsifiable history-dependent residual could look like if the proposed coupling exists.

## Next gates

1. Connect `M_0` quantitatively to `J_rec` from the v0.1 record-production source.
2. Explore other operators `O_M` and identify experimentally clean observables.
3. Add noise/drift and determine detectable coupling bounds.
4. Check whether equivalent effects can be absorbed into ordinary hidden environmental variables.
5. Only after those controls, translate the toy discriminator into a laboratory protocol.
