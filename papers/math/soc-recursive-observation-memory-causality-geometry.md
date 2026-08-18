# SoCT Recursive Observation–Memory–Causality–Geometry Probe

**Status:** exploratory mathematical scaffold  
**Claim level:** structural hypotheses and falsification targets; not established new physics  
**Method note:** this document records a closed-book representational probe. The correspondences were generated without literature search and must not be treated as novelty claims until prior-art review is performed.

## 1. Starting point

The operational observation model already defines a lower-than-consciousness ladder:

```text
interaction -> distinguishability -> record -> persistence -> downstream accessibility
```

The present probe asks whether the resulting structures close recursively:

```text
observation -> memory -> causal influence -> effective geometry -> observation
```

The key hypothesis is not that this loop is already a physical law. It is that every arrow can be assigned an operational quantity, simulated independently, and attacked with null models.

## 2. Observation as persistent informational distinction

Let `S` be a source system and `R` a record-bearing degree of freedom. A minimal observation requires more than correlation:

```math
I(S:R) > 0,
```

plus persistence and causal accessibility. A useful strength functional is

```math
\Omega_T = \int_0^T w(\tau) I(S_{t_0}:R_{t_0+\tau})\,d\tau,
```

with an additional intervention-based accessibility gate when needed.

This makes observation graded rather than binary: fleeting correlations can have small `Omega`, while robust records have larger `Omega`.

## 3. Recursive refinement and Born weighting

Assume a quantum record branch has amplitude magnitude `r` and unknown probability weight `w(r)`. If a record can be refined unitarily into `m` equal orthogonal subrecords, each subrecord has amplitude

```math
r/\sqrt{m}.
```

Coarse-grained probability should not depend on whether those internal subrecords are resolved. Therefore

```math
w(r)=m\,w\!\left(r/\sqrt{m}\right).
```

For the power family

```math
w(r)=r^p,
```

refinement invariance implies

```math
1=m^{1-p/2},
```

and therefore

```math
p=2.
```

Thus, **within Hilbert-space quantum mechanics and the stated assumptions**, square-norm weighting is the fixed point of equal orthogonal record refinement.

This is not a derivation of quantum theory from observation. It assumes Hilbert amplitudes, unitary splitting, orthogonality, additive probabilities, and refinement consistency. Its value is narrower: it turns the Born exponent into a testable recursive invariance property.

## 4. Memory as minimal predictive compression of history

A process exhibits observable history dependence when

```math
I(H_t;F\mid X_t)>0,
```

where `H_t` is prior history, `X_t` is the measured present state, and `F` denotes a future variable.

However, once the history relevant to prediction is encoded in a variable `M_t`, the enlarged present state can become Markov-complete:

```math
P(F\mid H_t)=P(F\mid X_t,M_t).
```

This produces the memory/state paradox:

> physical memory is history transformed into present state.

Accordingly, SoCT should not claim that a true memory degree of freedom can never be represented as hidden state. Instead, the stronger and cleaner hypothesis is:

> `M` is an additional physical state variable required to make collapse-history-dependent dynamics predictively complete after known state variables are controlled.

Define two histories `h1` and `h2` as predictively equivalent when

```math
P(F\mid h_1)=P(F\mid h_2)
```

for all relevant futures. Then a candidate minimal memory state is the equivalence class

```math
M(h)=[h]_{\rm predictive}.
```

This gives a falsification gate: if all apparent collapse-history effects vanish after conventional hidden variables are included, an additional SoCT memory field is unnecessary.

## 5. Stable facts as idempotent coarse-grainings

A robust record is not generally one exact microstate. Many microstates may encode the same macroscopic result. Let

```math
\mathcal O:X\rightarrow R
```

be an observation/coarse-graining map. For a stable fact, re-observation of the same unchanged record should approximately preserve the result:

```math
\mathcal O(\mathcal O(x))\approx \mathcal O(x).
```

This suggests a new candidate criterion:

> stable observable facts are approximate fixed points of recursive observation/coarse-graining.

The relation should fail for weak, invasive, or dynamically changing measurements, so approximate idempotence is proposed only as a property of stable records, not of all measurements.

## 6. Redundant records and the classicality constraint

A record that is accessible to many downstream systems must often be copied or redundantly encoded. But arbitrary unknown quantum states cannot be copied perfectly. Therefore widespread objective records cannot require faithful broadcasting of the entire microscopic quantum state.

A structural possibility follows:

```text
microscopic state
    -> selected distinguishable observable
    -> redundantly broadcast record
    -> perturbation-resistant equivalence class
    -> classical fact
```

This motivates a simulation target: determine which observables can generate high redundancy across environmental fragments while preserving their coarse-grained value.

The claim is deliberately operational: classical objectivity may track **redundant recoverability of selected information**, not replication of the complete state.

## 7. Causal influence as deformation of reachable futures

For systems `A` and `B`, define intervention-sensitive causal strength at lag `tau` by

```math
\kappa_{A\to B}(\tau)
= D\!\left[
P(B_{t+\tau}\mid do(A=a)),
P(B_{t+\tau}\mid do(A=a'))
\right].
```

If influence along a path approximately composes multiplicatively,

```math
\kappa_\gamma \approx \prod_{e\in\gamma}\kappa_e,
```

then the logarithmic cost

```math
L(\gamma)=-\sum_{e\in\gamma}\log \kappa_e
```

is additive. A candidate effective distance is

```math
d(A,B)=\min_{\gamma:A\to B}L(\gamma).
```

This creates a precise bridge from causal transmission to distance-like structure.

## 8. Critical confound: susceptibility is not geometry

Raw causal strength cannot equal physical distance universally. Two equally separated systems can respond very differently because of local gain, resonance, phase, critical susceptibility, noise, or state-dependent coupling.

A more defensible decomposition is

```math
\kappa_{ij}=\chi_i\,T_{ij}\,\chi_j + \epsilon_{ij},
```

where `chi` captures local responsiveness and `T` is the propagation/transmission structure to be reconstructed.

Therefore causal geometry should be inferred from a combination of:

```text
causal order
first-arrival / propagation delay
transmission after local-response normalization
path composition
```

rather than from correlation or raw influence magnitude alone.

This is an important adversarial benchmark. Critical or resonant systems should be used specifically to see whether a proposed geometry estimator hallucinates spatial shortcuts.

## 9. Joint emergence of objecthood and locality

Suppose object partitions are inferred from strong internal causal closure, while locality is inferred from causal transmission. This appears circular:

```text
objects require locality
locality is inferred from object interactions
```

A possible resolution is joint fixed-point reconstruction. Let `G_n` be candidate geometry and `P_n` a candidate partition into objects/subsystems:

```math
(G_n,P_n) \rightarrow (G_{n+1},P_{n+1}).
```

A stable world-description would satisfy approximately

```math
(G^*,P^*)=\mathcal F(G^*,P^*).
```

This does not show that real spacetime or objects emerge this way. It gives a concrete algorithmic hypothesis that can be tested in toy systems where ground truth is known.

## 10. Geometry/causality recursion

Standard physical modeling usually takes geometry as constraining causal propagation:

```text
geometry -> allowed propagation
```

The present reconstruction program proposes the inverse map:

```text
measured causal propagation -> inferred geometry.
```

The two directions can be reconciled by self-consistency:

```math
G^*=\mathcal G[C(G^*)].
```

A candidate emergent spacetime would therefore be a fixed point of the causal relations that the same effective geometry constrains.

## 11. Record arrow and time asymmetry

Memory introduces a directionality problem. Reversible microscopic laws can support correlations, yet physical records are ordinarily organized as records of prior interactions. SoCT must therefore distinguish among:

```text
ordinary thermodynamic record asymmetry
open-system irreversibility
boundary-condition effects
any genuinely additional collapse-memory asymmetry
```

If collapse sources memory through

```math
\partial_t M=\alpha C-\beta M+D_M\nabla^2M,
```

then any claimed fundamental time asymmetry must produce a residual beyond the standard nulls above. Otherwise the memory arrow is conventional rather than SoCT-specific.

## 12. Recursive closure candidate

The current structural loop is

```math
R \rightarrow M \rightarrow C \rightarrow G \rightarrow R,
```

where

```text
R = record / observation structure
M = predictive memory state
C = causal influence structure
G = effective geometry
```

A broader state may be written

```math
Z_t=(R_t,M_t,C_t,G_t)
```

with update law

```math
Z_{t+1}=\mathcal F_\theta(Z_t).
```

The next theoretical question is whether low-parameter choices of `F_theta` possess stable fixed points or attractors that reproduce useful features of measurement, memory, causal order, and effective geometry without inserting those outcomes separately.

This is a future simulation target, not yet a physical claim.

## 13. Seemingly unrelated systems that become useful adversarial data

The following domains are worth using as **null models or structural test beds**, not as evidence for SoCT:

1. **Hysteretic and aging materials** — demonstrate how conventional hidden state can mimic memory; useful for testing false-positive history detection.
2. **Error-correcting and redundant storage systems** — test whether record robustness, redundancy, and coarse-grained objectivity can be quantified independently of substrate.
3. **Critical and resonant networks** — adversarial test for causal-geometry estimators because long-range response can become strong without a literal shortening of geometric distance.
4. **Diffusive / propagation networks with hidden topology** — test whether intervention delays and transfer costs recover ground-truth adjacency and dimension.
5. **Neural or adaptive dynamical systems** — test the idea that stable functional categories can persist while detailed microstates drift, supporting the equivalence-class formulation without implying quantum collapse.
6. **Repeated coarse-graining / multiscale models** — test whether stable observables are fixed points or approximate eigenstructures of recursive observation maps.

## 14. Falsification discipline

The recursive program should be considered unsuccessful if any of the following occur:

- the observation functional adds no measurable distinction beyond ordinary correlation/decoherence;
- apparent memory is fully removed by conventional hidden-state completion;
- causal geometry reconstruction fails under modest state-dependent susceptibility or requires access to the hidden geometry it is supposed to derive;
- object/locality fixed points are non-unique or unstable without arbitrary tuning;
- recursive closure can fit any behavior because the update maps are unconstrained;
- SoCT-specific residual terms do not outperform simpler null models under held-out tests.

## 15. Simulation sequence

The immediate simulation program is:

```text
SIM-01 Recursive Born Refinement
SIM-02 Hidden State vs Genuine Memory
SIM-03 Emergent Objects and Locality
SIM-04 Causal Geometry Reconstruction
SIM-05 Redundant Record / Broadcastability
SIM-06 Observation Idempotence and Coarse-Graining
SIM-07 Recursive Closure Fixed-Point Toy Model
```

The first four directly correspond to the original probe set. SIM-05 through SIM-07 were added because recursion and attempted falsification exposed additional constraints.
