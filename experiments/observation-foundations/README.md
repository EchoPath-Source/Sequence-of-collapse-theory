# Observation Foundations Simulation Program

**Status:** active exploratory simulation track  
**Scope:** operational observation, predictive memory, causal structure, and effective geometry  
**Claim level:** methodology and toy-model tests only; passing a simulation does not establish new physics.

Related theory documents:

- `papers/math/soc-operational-observation-model.md`
- `papers/math/soc-recursive-observation-memory-causality-geometry.md`
- `papers/math/soc-localization-memory-hamiltonian.md`

## Purpose

This directory tests the proposed chain

```text
observation -> record -> memory -> causal influence -> effective geometry
```

and, more importantly, the recursive closure

```text
observation -> memory -> causality -> geometry -> observation.
```

Every simulation must include a null model and a failure criterion. The goal is to discover which parts are mathematically viable before attaching SoCT-specific physical interpretation.

## SIM-01 — Recursive Born Refinement

**Question:** Within Hilbert-space quantum mechanics, does square-norm weighting emerge as the unique member of the family `P proportional |alpha|^p` that is invariant under arbitrary equal orthogonal refinement and subsequent coarse-graining of record branches?

**Method:**

1. Generate normalized random complex amplitude vectors.
2. Compute branch probabilities using `|alpha|^p` for a sweep of exponents `p`.
3. Select a branch and refine it into `m` equal orthogonal subbranches with amplitude `alpha/sqrt(m)`.
4. Sum the probabilities of the refined subbranches back to the original coarse branch.
5. Measure the change in coarse probability.
6. Repeat recursively with nested refinements.

**Prediction under the stated assumptions:** `p = 2` has zero refinement error up to floating-point precision.

**Failure / limitation:** This does not derive Hilbert space, unitarity, orthogonality, additivity, or single-outcome selection. It tests only refinement consistency inside that framework.

Files:

- `sim01_recursive_born_refinement.py`
- `SIM01_RESULTS.md`

## SIM-02 — Hidden State vs Genuine Memory

**Question:** What evidence distinguishes history dependence caused by omitted conventional variables from a genuinely required additional memory state?

**Models:**

1. fully observed Markov process;
2. Markov process with one hidden state variable;
3. explicit finite-memory kernel;
4. dynamical memory variable `M_t` with its own update law.

**Primary statistic:**

```math
I(H;F|X)
```

followed by progressive state augmentation.

**Success criterion:** A memory candidate is justified only if residual predictive information from history persists after known hidden variables are controlled and is removed or compressed by a low-dimensional `M_t` with held-out predictive value.

**Failure criterion:** If ordinary latent-state completion removes the effect, no extra memory degree of freedom is needed.

## SIM-03 — Emergent Objects and Locality

**Question:** Can stable subsystem boundaries and locality be recovered jointly from causal interactions without pre-labeling objects?

**Method:**

- generate interacting nodes with hidden ground-truth structure;
- infer intervention-based causal influence;
- partition nodes by internal causal closure;
- derive candidate distances from normalized transmission/delay;
- iterate partition and geometry estimates to a fixed point.

**Success criterion:** Recovered partitions and geometry converge and match withheld ground truth across perturbations.

**Failure criterion:** Multiple incompatible fixed points, extreme parameter sensitivity, or dependence on hidden labels.

## SIM-04 — Causal Geometry Reconstruction

**Question:** Can hidden geometry be reconstructed from causal order, propagation delay, and normalized transmission cost?

Candidate path metric:

```math
L(\gamma)=-\sum_{e\in\gamma}\log \tilde\kappa_e,
```

with

```math
d(A,B)=\min_{\gamma:A\to B}L(\gamma).
```

Raw influence `kappa` must not be used without testing local susceptibility confounds.

**Ground-truth test beds:**

- 1D chain;
- 2D lattice;
- irregular graph;
- curved / position-dependent coupling analogue;
- critical or resonant adversarial network.

**Failure criterion:** Reconstruction mistakes high susceptibility for short distance or fails when coupling strength varies independently of topology.

## SIM-05 — Redundant Record / Broadcastability

**Question:** Which coarse-grained observables can be copied into many downstream fragments while preserving consistent recoverability?

**Purpose:** Test whether robust classical records correspond to selected information that becomes redundantly accessible, rather than faithful copies of complete microscopic states.

**Metrics:** redundancy, recoverability, disturbance, mutual information per fragment, and stability under fragment loss.

## SIM-06 — Observation Idempotence and Coarse-Graining

**Question:** Are stable recorded facts approximate fixed points of repeated observation/coarse-graining?

Candidate property:

```math
\mathcal O(\mathcal O(x))\approx \mathcal O(x).
```

Compare strong/stable records against weak, invasive, noisy, and dynamically changing observations.

**Failure criterion:** Idempotence does not discriminate stable records from generic transformations.

## SIM-07 — Recursive Closure Fixed-Point Toy Model

**Question:** Can a low-parameter update system

```math
Z_t=(R_t,M_t,C_t,G_t)
```

with

```math
Z_{t+1}=\mathcal F_\theta(Z_t)
```

produce stable self-consistent observation-memory-causality-geometry fixed points without separately hard-coding each target structure?

This simulation should be attempted only after SIM-01 through SIM-04 establish sensible component operators.

## Research discipline

For every simulation:

1. record the standard/null explanation first;
2. state which assumptions are supplied rather than derived;
3. separate mathematical viability from physical evidence;
4. use held-out parameter regimes where possible;
5. prefer a failed clean prediction over post-hoc retuning;
6. do not label a toy-model effect as evidence for SoCT unless a SoCT-specific residual has been defined against simpler alternatives.
