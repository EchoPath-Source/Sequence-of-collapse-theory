# SIM-02 Results — Hidden State vs Genuine Memory

**Date:** 2026-08-17  
**Status:** first deterministic toy-model pass  
**Code:** `sim02_hidden_state_vs_memory.py`

## Question

Can history dependence alone distinguish a genuinely required physical memory degree of freedom from an ordinary omitted hidden state?

The diagnostic statistic is empirical conditional mutual information:

```math
I(H;F\mid X),
```

where `H` is prior observed history, `X` is the currently observed state, and `F` is a future observation.

If the present observed state is predictively complete, then ideally

```math
I(H;F\mid X)=0.
```

A nonzero value means prior history carries predictive information not contained in the chosen current-state description.

The second statistic augments the current state by the model's known latent or memory variable `A`:

```math
I(H;F\mid X,A).
```

## Models

Four binary stochastic processes were simulated for 200,000 samples each:

1. **Fully observed Markov process** — the observed current state is sufficient.
2. **Hidden Markov state** — a persistent latent variable drives noisy observations.
3. **Finite second-order memory** — the future explicitly depends on the previous observed state as well as the present.
4. **Dynamic memory state** — an additional persistent memory bit has its own update rule and affects future dynamics.

## Results

| model | `I(H;F|X)` bits | `I(H;F|X,A)` bits | reduction |
|---|---:|---:|---:|
| fully observed Markov | 8.36e-06 | 8.36e-06 | 0 |
| hidden Markov state | 2.9916e-02 | 2.04e-05 | 2.9896e-02 |
| finite second-order memory | 3.8904e-01 | 0 | 3.8904e-01 |
| dynamic memory state | 1.2308e-01 | 2.56e-05 | 1.2305e-01 |

The tiny nonzero values near `1e-5` are finite-sample estimation noise in this toy setting.

## Main result

The experiment supports two distinct statements.

### 1. Conditional history information is a useful incompleteness detector

When

```math
I(H;F\mid X)>0,
```

history predicts the future beyond the chosen present observable. This correctly flags the hidden-state, finite-memory, and dynamic-memory models while remaining approximately zero for the fully observed Markov model.

### 2. The same statistic does **not** establish the ontology of the missing state

Adding the correct augmentation drives the residual toward zero in both:

- an ordinary hidden-state model; and
- an explicitly constructed memory-state model.

Therefore behavioral history dependence alone cannot establish that the missing predictive variable is a special physical memory field.

This is the key negative result:

> **Non-Markovian residuals can show that the measured present state is incomplete, but they cannot by themselves distinguish “ordinary hidden state” from “memory.”**

## Consequence for SoCT

The SoCT memory program should use history dependence as a **screening statistic**, not as sufficient evidence for a new memory field.

A stronger SoCT-specific case would require all of the following:

1. a pre-specified memory update law, for example

```math
\partial_t M=\alpha C-\beta M+D_M\nabla^2M;
```

2. a pre-specified coupling from `M` back into observable dynamics;
3. residual predictive value after known environmental and latent variables are controlled;
4. successful held-out prediction across different preparation histories;
5. ideally, an intervention or reset protocol that changes the candidate `M` while holding conventional present-state variables fixed.

## Memory/state paradox sharpened

This simulation operationalizes the conceptual result:

```text
history -> predictive compression -> additional present state
```

Once a history-dependent quantity is encoded into a sufficient `M_t`, the enlarged state can again be Markov-complete. Thus a physically real memory is not “outside the state.” It is a state variable whose value encodes predictive consequences of prior events.

The scientific question is consequently not whether memory can be represented as hidden state. It can. The question is whether SoCT predicts a **specific additional state variable, update law, and coupling** that simpler latent-state models fail to reproduce.

## Falsification gate

A proposed SoCT memory signature should be rejected as evidence for an additional field if a conventional latent-state model of comparable or lower complexity removes the history residual and predicts held-out data equally well or better.

## Next action

SIM-03 and SIM-04 can now be built with a stronger constraint: causal influence must be separated from local susceptibility before it is converted into object boundaries or effective distance. In parallel, the existing SoCT history-matched memory-feedback simulation should adopt the SIM-02 criterion so that conventional hidden-state completion is an explicit null model rather than an afterthought.
