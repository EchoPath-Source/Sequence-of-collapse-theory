# Observation Foundations — Literature Crosswalk (2026-08-17)

**Status:** external-literature confrontation after closed-book derivation pass  
**Purpose:** identify which structures in the observation/memory/causality/geometry program are already established, which are adjacent, and which questions remain worth testing in SoCT.  
**Claim discipline:** overlap with existing literature is not treated as independent confirmation of SoCT. It is used to sharpen null models, terminology, and simulation design.

## 1. Executive conclusion

The closed-book probing independently converged on several structures with substantial prior literature:

1. **Redundant records and objectivity** — already central to Quantum Darwinism and Spectrum Broadcast Structures (SBS).
2. **Memory as multi-time predictive structure** — already developed in open-quantum-system formalisms such as process tensors and quantum Markov order.
3. **Macroscopic object discovery by dynamical boundaries/coarse-graining** — actively studied through dynamic Markov blankets and causal-emergence formalisms.
4. **Spacetime reconstruction from causal structure** — a central causal-set idea, with a 2025 mathematical result showing reconstruction from chronological order plus sampled-point number in a smooth probabilistic setting.
5. **Born-rule derivation by symmetry/consistency** — already has major lines including envariance/Gleason-style approaches; a 2025/2026 GPT paper also derives linear predictive probabilities from causal consistency/no-signaling.

Therefore the observation-foundations program should **not** claim novelty for these ingredients individually.

The strongest remaining research value is the proposed **cross-layer synthesis and falsifiable bridge**:

```text
record formation
    -> predictive memory state
    -> altered transition law
    -> intervention-defined causal structure
    -> effective geometry
    -> constrained future record formation
```

with a distinct SoCT question inserted only where warranted:

```text
does collapse/localization history require an additional low-dimensional physical state M
beyond standard environmental/process-tensor descriptions,
and does M produce a predeclared measurable feedback?
```

## 2. Born weighting: revise SIM-01 from derivation claim to structural benchmark

### Literature overlap

Zurek's envariance program derives Born weighting from entanglement symmetries and extends equal-amplitude cases to general amplitudes. Earlier and later Gleason-style approaches likewise constrain admissible probability measures on Hilbert space. A recent generalized-probabilistic-theory result argues that nonlinear predictive probability assignments are incompatible with causal consistency/no-signaling under stated assumptions, recovering the standard quadratic quantum transition probability after reconstruction assumptions.

### Consequence for our track

Our result

```math
w(r)=m w(r/sqrt(m))
```

and the `w(r)=r^p` fixed point `p=2` should be retained as a **recursive-refinement sanity check**, not presented as a new derivation of the Born rule.

The useful local interpretation is narrower:

> square-norm weighting is the member of the chosen power-law family that remains invariant under equal orthogonal record refinement and coarse-graining.

### SIM-01 status

Keep current result; add literature note. No further priority unless later SoCT equations predict deviations from Born statistics.

## 3. Redundant records: SIM-05 is directly adjacent to Quantum Darwinism / SBS

### Literature overlap

Quantum Darwinism treats environmental redundancy as a route to objective classical information: many fragments of the environment independently carry recoverable information about selected system observables. Spectrum Broadcast Structures sharpen this into multipartite states in which different environment fragments encode perfectly distinguishable records of the same pointer information, with a non-disturbance/objectivity criterion. Recent mathematical work studies sufficient dynamical conditions for SBS formation under von Neumann-type measurement interactions.

This maps closely onto our closed-book chain:

```text
selected observable
    -> environmental imprint
    -> redundant recoverability
    -> robust fact / effective objectivity
```

### Consequence for our track

SIM-05 must benchmark directly against Quantum Darwinism/SBS metrics rather than invent a parallel vocabulary.

Recommended metrics:

- mutual information between system and environment fragments;
- Holevo-accessible information where appropriate;
- record redundancy versus fragment size;
- fidelity/trace-distance distinguishability of fragment-conditioned states;
- non-disturbance under repeated readout;
- persistence after fragment loss/noise.

### SoCT-specific question that remains

Standard Quantum Darwinism/SBS does **not by itself establish** a new physical memory field. The SoCT-specific test is therefore:

> after ordinary decoherence, redundant-record formation, and environmental memory are modeled, does a predeclared additional state `M` improve held-out prediction or create a reproducible history-dependent residual?

That is the legitimate boundary between established record-objectivity theory and the stronger SoCT hypothesis.

## 4. Predictive memory: SIM-02 aligns with process-tensor / quantum-Markov-order thinking

### Literature overlap

Process-tensor approaches encode multi-time open-system behavior and environmental influence without forcing a Markov approximation. Quantum Markov order further shows that memory in quantum processes can be **instrument dependent**: the observed memory structure depends on how the process is probed.

This strongly supports the methodological lesson of SIM-02:

```text
I(history; future | observed present) > 0
```

means that the current state description is predictively incomplete; it does not identify the ontology of the missing variable.

### Consequence for SoCT

A future quantum-memory test should not compare SoCT only to a memoryless Lindblad/null model. It should compare against at least:

1. Markovian open-system model;
2. conventional hidden environmental state;
3. finite-memory kernel;
4. process-tensor / multi-time environmental model;
5. SoCT-specific `M` state with predeclared update and feedback law.

If models 2-4 absorb the residual, there is no evidence for an additional SoCT memory degree of freedom.

### Stronger criterion for M

The SoCT memory field should earn its place only if it is:

- **predictively necessary** on held-out histories;
- **compressive** relative to arbitrary history storage;
- **dynamically autonomous enough** to admit a reusable update law;
- **source-specific** to the declared collapse/localization variable rather than generic environmental history;
- **intervention-sensitive** in the direction predicted by the model;
- **not replaceable** by a simpler conventional latent state at comparable predictive accuracy.

## 5. Objecthood and coarse-graining: revise SIM-03

### Literature overlap

Recent work on dynamic Markov-blanket detection explicitly attempts to infer macroscopic objects, boundaries, and object-specific rules from partially observed microscopic dynamics. Causal-emergence work studies when coarse-grained macrostates can exhibit stronger or cleaner effective causal structure than microscopic descriptions and develops optimization criteria for coarse-graining.

This means our proposed idea that object boundaries might be recovered from internally strong and externally weaker causal structure is not unique.

### Revised SIM-03 question

Do **different model-neutral boundary criteria** converge on the same emergent objects?

Rather than building one custom 'objectness' score, compare:

1. causal-closure partitioning;
2. predictive sufficiency/compression;
3. intervention-based effective information;
4. graph/community structure from dynamical coupling;
5. a simplified Markov-blanket-style boundary criterion.

### Key test

Create systems in which geometric proximity, causal coupling, and functional object membership can be deliberately dissociated.

Examples:

- two spatially adjacent but causally isolated clusters;
- long-range coupled components forming one functional object;
- moving object exchanging matter with background;
- near-critical region with high susceptibility but no stable boundary;
- nested objects at multiple scales.

**Success:** multiple independent criteria converge on stable partitions and recover withheld object labels without access to geometry.

**Failure:** inferred objects depend primarily on chosen score, threshold, or hidden geometric priors.

## 6. Causal geometry: revise SIM-04 substantially

### Literature overlap

Causal-set theory already treats causal order as fundamental geometric data. In continuum Lorentzian geometry, causal structure is known to determine substantial metric information up to scale under suitable conditions. A 2025 mathematical result by Mathias Braun makes a strong probabilistic reconstruction statement: random adjacency matrices generated by chronological relations and i.i.d. samples coincide in law only when the underlying smooth spacetimes are isometric; in that framework, 'order and number' suffice for reconstruction.

Therefore the broad statement

```text
causal structure can determine geometry
```

is **not novel** and should not be presented as a new SoCT insight.

### What remains useful

Our distinctive computational question can instead be:

> can an embedded observer recover effective geometry from finite, noisy intervention-response data when local susceptibility, resonance, heterogeneous coupling, missing nodes, and memory confound naive causal strength?

That is a concrete inverse problem rather than a foundational novelty claim.

### Replace the naive metric

Do not use

```math
d_ij = -log(kappa_ij)
```

as the primary geometry estimator.

Raw response strength is confounded by local susceptibility and amplification.

Use separate estimated channels:

```text
A. causal order / reachability
B. propagation delay or temporal ordering
C. event density / count / effective volume proxy
D. susceptibility-normalized transmission as an auxiliary metric
```

Then test which combinations recover withheld geometry.

### Adversarial cases

- 1D chain with homogeneous coupling;
- 2D lattice;
- irregular graph;
- bottleneck geometry;
- variable local gain/susceptibility;
- resonant/critical nodes;
- nonlocal shortcut edges;
- hidden nodes;
- delayed-memory edges;
- time-varying couplings.

### Important distinction

Correlation must remain separate from controllable causal influence. Entanglement or common-cause correlation alone must not be interpreted as geometric adjacency.

## 7. Recursion / fixed points: still worth pursuing, but later

The literature overlap above does not eliminate the proposed recursive closure:

```text
observation -> memory -> causal dynamics -> effective geometry -> possible observations
```

However, the components now have enough established mathematics that SIM-07 should not use arbitrary hand-written update equations.

Instead SIM-07 should compose validated operators from earlier simulations:

```text
record operator from SIM-05 / observation model
predictive-memory operator informed by SIM-02/process-tensor tests
causal estimator from revised SIM-03
geometry estimator from revised SIM-04
```

Then ask whether iterative closure converges, cycles, bifurcates, or becomes unstable.

The interesting question is no longer simply whether a fixed point can be manufactured; almost certainly it can. The useful question is whether the fixed point is **robust, low-parameter, and invariant under reasonable changes of representation**.

## 8. Recommended revised order

### Next: SIM-03A — Emergent object benchmark

First test object recovery on classical stochastic/dynamical networks, because this isolates the partition problem from quantum interpretation.

### Then: SIM-03B — susceptibility / criticality adversary

Determine whether inferred causal neighborhoods survive strong local amplification.

### Then: SIM-04A — order-only geometry baseline

Use hidden 1D/2D causal structures and recover reachability/order from intervention data.

### Then: SIM-04B — order + count/density + delay

Test whether adding volume and temporal information improves reconstruction, explicitly benchmarking the causal-set-inspired expectation.

### Then: SIM-05 — redundant record / SBS benchmark

Implement established Quantum-Darwinism/SBS quantities before attaching SoCT memory.

### Then: quantum SIM-02 extension

Use a process-tensor-compatible open-system null before claiming a nonstandard memory residual.

### Finally: SIM-07 recursive closure

Only after the component maps have survived independent null tests.

## 9. Literature anchors

Primary sources used for this crosswalk:

- W. H. Zurek, *Probabilities from Entanglement, Born's Rule from Envariance*, Phys. Rev. A 71, 052105 (2005), arXiv:quant-ph/0405161.
- A. Acevedo, J. Wehr, J. Korbicz, *Spectrum Broadcast Structures from von Neumann type interaction Hamiltonians*, arXiv:2403.01419 (2024).
- P. Taranto et al., *Quantum Markov Order*, arXiv:1805.11341 (2018).
- J. Keeling et al., *Process Tensor Approaches to Non-Markovian Quantum Dynamics*, arXiv:2509.07661 (2025).
- J. Beck, M. J. D. Ramstead, *Dynamic Markov Blanket Detection for Macroscopic Physics Discovery*, arXiv:2502.21217 (2025).
- K. Liu, B. Yuan, J. Zhang, *An Exact Theory of Causal Emergence for Linear Stochastic Iteration Systems*, arXiv:2405.09207 / Entropy 26, 618 (2024; rev. 2025).
- M. Braun, *Spacetime reconstruction by order and number*, arXiv:2507.01907 (2025).
- E. O. Torres Alegre, *Causal Consistency Selects the Born Rule: A Derivation from Steering in Generalized Probabilistic Theories*, arXiv:2512.12636 v3 (2026).

## 10. Bottom line for SoCT

The literature makes the track stronger by removing several accidental novelty claims.

The potentially distinctive scientific content is not:

```text
redundant records exist
memory can be non-Markovian
macroscopic objects can emerge under coarse-graining
causal structure contains geometric information
Born weighting can be constrained by consistency
```

Those ideas already have substantial literature.

The sharper SoCT question is:

> **Does collapse/localization history source a specific predictive state `M` that remains necessary after standard open-system, record-redundancy, latent-state, and causal-geometry explanations are exhausted, and does that state feed back according to a predeclared law?**

That is where future simulations and empirical work should concentrate.