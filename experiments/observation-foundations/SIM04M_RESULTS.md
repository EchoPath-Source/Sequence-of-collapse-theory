# SIM-04M — Microscopic Bath / Emergent Damping Results

**Status:** microscopic open-system toy benchmark complete  
**Claim level:** standard oscillator-bath methodology used as a consistency/falsification gate; not evidence for a physical SoCT memory field.

## Question

Can the phenomenological damping term

```math
\gamma\dot M
```

in the candidate causal memory equation emerge from explicit reversible microscopic bath degrees of freedom, and if so, under what conditions does the local Markovian approximation fail?

The benchmark replaces phenomenological damping with a finite Hamiltonian oscillator bath.

---

## Microscopic model

For one memory-field Fourier-mode surrogate `M(t)`, the simulated Hamiltonian is

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
-C_{obs}(t)M.
```

The full source+system+bath evolution is deterministic and reversible. Once the external source is switched off, total microscopic energy is conserved.

The bath uses the finite-cutoff Ohmic-like spectral envelope

```math
J(\omega)=\eta\omega e^{-\omega/\omega_c}
```

with

```text
eta       = 0.50
omega_c   = 12.0
omega_min = 0.10
omega_max = 30.0.
```

Bath spectral resolution is varied through

```text
N_bath = 8, 32, 128, 256 modes.
```

---

## Reduced comparison model

The microscopic trajectory is compared with the local-friction equation

```math
\ddot M
+\gamma_{eff}\dot M
+\Omega_M^2M
=C_{obs}(t).
```

`gamma_eff` is fitted only on the early post-source window

```text
t = 1.5 ... 7.0
```

and then frozen before held-out prediction on

```text
t = 7.0 ... 18.0.
```

No late-time retuning is allowed.

A second comparison asks whether the Markovian heat prediction

```math
Q_{eff}(t)=\int \gamma_{eff}\dot M_{eff}^2 dt
```

tracks the exact microscopic bath/coupling-sector energy gain.

---

## Results

| Bath modes | fitted `gamma_eff` | train RMSE | held-out RMSE | effective-heat RMSE | recurrence ratio | max energy-closure error |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.900* | 0.23412 | 0.20763 | 0.05655 | 1.029 | 1.01e-7 |
| 32 | 0.500 | 0.04402 | 0.20740 | 0.03638 | 0.965 | 1.05e-7 |
| 128 | 0.470 | 0.01872 | **0.01416** | **0.00707** | **0.102** | 1.06e-7 |
| 256 | 0.460 | 0.01445 | **0.01125** | **0.00701** | **0.099** | 1.06e-7 |

`*` The 8-mode fit reaches the upper exploratory `gamma` grid and remains poor; it should not be interpreted as a reliable local-friction estimate.

The recurrence ratio is

```text
max |M| at t=10..18
--------------------
max |M| at t=2..7.
```

---

## Interpretation

### 1. Dense baths produce an approximate emergent local damping law

As the same spectral envelope is sampled more densely, the fitted effective damping stabilizes:

```text
N=32  -> gamma_eff = 0.50
N=128 -> gamma_eff = 0.47
N=256 -> gamma_eff = 0.46.
```

At `N=128` and `N=256`, the frozen early-time local model predicts the held-out late trajectory with RMSE about

```text
0.0142 and 0.0113.
```

The result is not exact Markovianity; finite cutoff and finite bath size retain small nonlocal corrections. But the local friction law becomes a useful reduced description over the tested time window.

### 2. Sparse baths retain memory and defeat the local friction model

The 8- and 32-mode baths show large coherent recurrences.

Their late/early recurrence ratios are approximately

```text
8 modes  -> 1.03
32 modes -> 0.96
```

compared with

```text
128 modes -> 0.10
256 modes -> 0.10.
```

The 32-mode case is especially diagnostic: its early training fit is moderately good (`RMSE ~ 0.044`) but its held-out late error grows to

```text
RMSE ~ 0.207.
```

So an apparently acceptable early-time `gamma_eff` can fail catastrophically once finite-bath recurrence enters the test window.

### 3. Dissipation here is reduced dynamics, not fundamental energy loss

For every bath resolution, the microscopic identity

```math
H_0(t)-H_0(0)=W_{source}(t)
```

closes numerically to roughly

```text
1e-7
```

or better across the full integration.

After the source ends the full Hamiltonian energy is conserved.

Thus the apparent damping of `M` comes from energy transfer into explicit bath/coupling degrees of freedom. In a finite bath that energy can return, creating recurrence.

This is an important conventional explanation for any observed reduced damping.

### 4. The effective heat ledger improves only in the dense-bath regime

The cumulative Markovian heat prediction is compared with the exact bath/coupling-sector energy gain.

The RMSE falls from

```text
0.0566  at 8 modes
0.0364  at 32 modes
```

to

```text
0.00707 at 128 modes
0.00701 at 256 modes.
```

So the same bath-resolution transition that improves the reduced trajectory also improves the effective exchange ledger.

### 5. The current SoCT damping term is therefore an effective approximation

SIM-04M does **not** support interpreting `gamma` as an intrinsically new physical constant merely because a damped memory trajectory is observed.

The safer statement is

> `gamma` may summarize unresolved environmental/bath dynamics in a regime where the bath correlation time is short and recurrences are suppressed.

If recurrence or long memory is observed, the generalized memory-kernel description must replace local damping.

---

## What SIM-04M establishes

Only the following synthetic methodological result:

> A broad/densely sampled explicit oscillator bath can make reversible microscopic dynamics look approximately like local damping over a finite observation window, while sparse baths remain non-Markovian and produce recurrence that falsifies the local `gamma dot(M)` approximation.

This result makes the SoCT field model more constrained, not more confirmed.

---

## What it does not establish

It does not show that:

- `M` exists in nature;
- the bath is exotic;
- the oscillator bath is the unique microscopic completion;
- the fitted `gamma_eff` is fundamental;
- the full quantum or relativistic bath problem has been solved;
- a physical preferred frame is acceptable;
- the covariant stress-energy/Bianchi gate is closed.

---

## Consequence for the SoCT program

A future field model should distinguish three regimes:

```text
microscopic explicit bath
    -> exact reversible exchange

general reduced bath
    -> non-Markovian memory kernel

short-memory dense-bath limit
    -> local gamma dot(M) approximation.
```

Thus the phenomenological causal equation from SIM-04J should be treated as the lowest-level reduced model, not automatically as the fundamental equation.

The next theoretical gate is to ask whether the microscopic/environmental completion can be formulated covariantly and whether its bath/rest-frame structure can be reconciled with the required total stress-energy tensor.

## Reproduction

```bash
python experiments/observation-foundations/sim04m_microscopic_bath_emergent_damping.py
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim04m_microscopic_bath_emergent_damping.py --json
```
