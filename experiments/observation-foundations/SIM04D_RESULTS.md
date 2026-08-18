# SIM-04D — Identifiability Gate Results

**Status:** initial identifiability benchmark complete  
**Claim level:** toy-model methodology result only; not evidence for SoCT, a memory field, or emergent spacetime.

## Question

When inferred causal/effective geometry changes, can the underlying mechanism be identified uniquely, or can ordinary changes in propagation speed, receiver susceptibility, topology, hidden variables, or dynamical memory produce indistinguishable observations?

SIM-04D deliberately separates two questions:

1. **practical separability:** can a richer intervention protocol distinguish several common mechanism families in a controlled synthetic benchmark?
2. **structural identifiability:** are there pairs of physically different descriptions that remain exactly observationally equivalent under the restricted measurements?

The second question is the more important gate for later SoCT claims.

## Part A — Multi-protocol mechanism benchmark

A hidden feed-forward transmission network is generated for every sample. The estimator receives no mechanism label. Four perturbation families are applied:

```text
speed            edge-delay changes at fixed topology/gain
susceptibility   receiver-gain changes at fixed topology/delay
topology         edge additions/removals
memory           ordinary local dynamical response memory
```

The diagnostic fingerprint contains:

```text
relative response change
earliest-lag change
reachability-support change
direct-support change
peak-amplitude change
independent local-gain calibration
late-response / tail change
post-reset persistence
```

A multinomial logistic model is trained only on **moderate perturbations** (`strength 0.30–0.75`) and tested on withheld **weak** (`0.12–0.35`) and **strong** (`0.75–0.98`) perturbations.

Eight independent train/test repetitions are used, with 150 training examples and 100 held-out test examples per mechanism per repetition.

### Results

| Diagnostic panel | Held-out accuracy mean | Std. dev. |
|---|---:|---:|
| naive: response change + lag + reachability | 0.902 | 0.031 |
| response-shape panel | 0.983 | 0.006 |
| full panel incl. gain calibration + post-reset persistence | 0.993 | 0.005 |

### Interpretation

The simple global geometry/residual view is materially less identifiable than the richer mechanism-aware protocol.

The practical lesson is:

```text
an observed effective-distance change should not be interpreted in isolation.
```

Timing, support, amplitude, local calibration, response tails, and persistence provide complementary information.

However, the high classification accuracy is only a synthetic sanity check. The mechanism families were intentionally constructed to possess different diagnostic signatures. It does **not** show that arbitrary physical mechanisms are uniquely identifiable.

## Part B — Exact non-identifiability counterexamples

SIM-04D includes three explicit equivalence constructions.

### 1. Geometry length versus propagation speed

Operational delay is

```math
Delta t = L / v.
```

A geometric stretch

```math
L -> s L
```

and a medium slowdown

```math
v -> v / s
```

produce exactly the same measured delay:

```math
sL / v = L / (v/s).
```

Numerical maximum absolute difference in the benchmark:

```text
3.55e-15
```

which is floating-point roundoff.

Therefore timing alone cannot identify metric stretch separately from propagation-speed change without an independent speed/clock standard.

### 2. Hidden mediator versus delayed direct edge

For an unobserved mediator `H`,

```text
A --a--> H --b--> B
```

with one time step per edge produces an observed lag-2 transfer

```math
T_{A->B}^{(2)} = ab.
```

A directly represented delayed edge

```text
A --ab, delay 2--> B
```

produces the same restricted observed response.

Numerical maximum absolute difference:

```text
0.0
```

Thus an observed delayed causal relation does not by itself tell us whether the path contains an unresolved mediator or a primitive delayed connection.

### 3. Named memory variable versus hidden latent state

Consider

```math
m_{t+1}=rho m_t + beta x_t,
y_t=x_t+m_t.
```

Calling `m` a physical memory state or calling the mathematically identical variable an unobserved latent state produces the same input-output process.

Numerical maximum absolute output difference:

```text
0.0
```

This reproduces the deeper lesson from SIM-02:

```text
history dependence can establish state incompleteness,
but the ontology of the missing state requires additional evidence.
```

## Main result

SIM-04D therefore gives a two-level conclusion.

### Practical level

With multiple independent interventions/calibrations, several ordinary causes of causal-geometry distortion can be separated reliably in the controlled benchmark.

### Fundamental level

There are exact equivalence classes that restricted intervention-response data cannot break.

Therefore:

```text
causal-geometry change != uniquely identified physical mechanism.
```

No later SoCT simulation may claim a memory-induced geometry effect merely because an inferred distance or propagation pattern changes.

## Gate imposed on a SoCT-specific memory test

A later SoCT memory field `M` must earn identification through predictions that are not reducible to the above degeneracies.

At minimum the next simulation must predeclare and test all of the following:

1. **source law** — `M` is driven by a specified collapse/localization history `C`, not by arbitrary fitted residuals;
2. **persistence law** — after `C` stops, residual effects decay according to the predeclared `beta` term;
3. **spatial law** — if `D_M > 0`, residual effects spread according to the same diffusion parameter across protocols;
4. **feedback law** — the same `lambda_M` maps `M` into a specified causal observable across train and held-out histories;
5. **matched-present test** — histories with the same current ordinary conditions but different prior `C` must produce the predicted residual difference;
6. **null competition** — instantaneous speed/medium change, susceptibility change, topology change, hidden-state completion, and ordinary local memory must be fit and compared;
7. **cross-protocol transfer** — parameters fit on one source-history family must predict another without retuning.

Failure on any of these gates weakens or removes the need for a distinct SoCT memory interpretation.

## Next simulation — SIM-04E

The first SoCT-specific injection should therefore use the existing phenomenological field equation

```math
partial_t M = alpha C - beta M + D_M nabla^2 M
```

on a hidden spatial/causal network and test whether the resulting delayed geometry signature can be recovered against simpler nulls under held-out collapse-history protocols.

The first target should be **identifiability and parameter transfer**, not evidence for reality.

## Reproduction

Run:

```bash
python experiments/observation-foundations/sim04d_identifiability_gate.py
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim04d_identifiability_gate.py --json
```
