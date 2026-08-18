# Observation Foundations Simulation Program

**Status:** active exploratory simulation track  
**Scope:** operational observation, predictive memory, causal structure, and effective geometry  
**Claim level:** methodology and toy-model tests only; passing a simulation does not establish new physics.

Related theory / status documents:

- `papers/math/soc-operational-observation-model.md`
- `papers/math/soc-recursive-observation-memory-causality-geometry.md`
- `papers/math/soc-localization-memory-hamiltonian.md`
- `docs/operational-observation-current-formulation.md`
- `docs/observation-foundations-literature-crosswalk-2026-08-17.md`

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

## Current status

- **SIM-01 complete:** recursive Born-refinement consistency benchmark.
- **SIM-02 complete:** history dependence alone cannot distinguish omitted hidden state from a special memory ontology.
- **SIM-03A complete:** intervention-defined object recovery survives a latent common-cause confound that degrades correlation clustering.
- **SIM-03B complete:** raw response amplitude fails as a transmission/distance proxy under susceptibility and near-critical recurrent amplification.
- **SIM-04A complete:** causal reachability and earliest response are recoverable at high precision from finite noisy interventions in the initial DAG benchmark.
- **SIM-04B complete:** causal order + calibrated interval count recovers useful timelike scale in flat-spacetime toy models; calibrated delay adds spatial information.
- **SIM-04C complete:** no universal scalar causal-distance rule emerged; calibrated propagation delay generalized best among simple estimators in several withheld geometry families.
- **SIM-04D complete:** practical mechanism identification improves with multi-protocol diagnostics, but exact non-identifiability classes remain.
- **SIM-04E complete:** the canonical source-decay-diffusion equation defines a transferable synthetic signature when diffusion is truly present and collapses to simpler nested nulls when it is not.
- **SIM-04F complete:** an observation/record-production source can be derived from interaction, distinguishability, information, record acquisition, persistence, and accessibility rather than supplied as arbitrary pulses.
- **SIM-04G complete:** explicit unitary quantum dynamics separates transient decoherence, persistent environmental records, erasure, and redundancy without any SoCT-specific term.
- **SIM-04H complete:** after an exact reset of all explicitly modeled ordinary quantum degrees of freedom, H0 and H1 predict no fresh-probe history residual; an added H2 state can generate a transferable post-reset residual, but hidden conventional reservoirs remain a fundamental ontology confound.
- **Next:** SIM-04I — incomplete-reset / hidden-reservoir adversary.

The literature-informed detailed SIM-03/04 plan is in `SIM03_04_REVISED_PLAN.md`.

---

## SIM-01 — Recursive Born Refinement

**Question:** Within Hilbert-space quantum mechanics, does square-norm weighting emerge as the unique member of the family `P proportional |alpha|^p` that is invariant under arbitrary equal orthogonal refinement and subsequent coarse-graining of record branches?

**Result:** `p = 2` is the refinement-invariant fixed point within the tested power-law family under the supplied Hilbert-space assumptions.

**Boundary:** this does not derive Hilbert space, unitarity, orthogonality, additivity, or single-outcome selection.

Files:

- `sim01_recursive_born_refinement.py`
- `SIM01_RESULTS.md`

---

## SIM-02 — Hidden State vs Genuine Memory

**Question:** What evidence distinguishes history dependence caused by omitted conventional variables from a genuinely required additional memory state?

Primary statistic:

```math
I(H;F|X).
```

**Result:** the statistic detects incomplete state descriptions but does not identify the ontology of the missing predictive state. Once the correct latent/memory state is supplied, both hidden-variable and memory processes can become Markov-complete.

Files:

- `sim02_hidden_state_vs_memory.py`
- `SIM02_RESULTS.md`

---

## SIM-03 — Emergent Objects, Susceptibility, and Locality

### SIM-03A — Emergent Object Benchmark

Intervention-defined modules remain recoverable under a latent common-cause confound that substantially degrades ordinary correlation clustering.

Files:

- `sim03a_emergent_object_benchmark.py`
- `SIM03A_RESULTS.md`

### SIM-03B — Susceptibility and Criticality Adversary

Raw response amplitude is unsafe as a transmission or distance proxy. Local susceptibility normalization improves direct/small-lag transmission recovery, but near criticality long-time response becomes dominated by indirect recurrent paths.

Surviving rule:

```text
large response != strong direct transmission != short effective distance.
```

Files:

- `sim03b_susceptibility_criticality_adversary.py`
- `SIM03B_RESULTS.md`

---

## SIM-04 — Causal Geometry and Memory Identifiability

### SIM-04A — Causal Order / Earliest Response

Finite noisy interventions recover causal reachability and earliest response at high precision in the initial hidden-DAG benchmark. Heterogeneous susceptibility mainly creates false negatives on weak paths rather than false proximity.

Files:

- `sim04a_causal_order_earliest_response.py`
- `SIM04A_RESULTS.md`

### SIM-04B — Geometry From Order + Count + Delay

Homogeneous flat-spacetime sprinklings demonstrate that causal interval count plus calibrated event density carries timelike metric information. Calibrated delay contributes additional spatial-separation information.

Boundaries:

```text
interval count requires density calibration
raw delay requires clock / medium calibration
real shortcut relations define a different effective causal geometry
```

Files:

- `sim04b_order_count_delay_geometry.py`
- `SIM04B_RESULTS.md`

### SIM-04C — Candidate Distance Constructions

No universal scalar distance rule emerged. Calibrated propagation delay was the strongest simple generalizer on several withheld families. A learned combination trained on chain/grid data did not universally beat simpler physics-informed estimators.

The program now reports separately against:

```text
background embedding geometry
versus
effective causal/path geometry.
```

Files:

- `sim04c_candidate_distance_comparison.py`
- `SIM04C_RESULTS.md`

### SIM-04D — Identifiability Gate

A multi-protocol diagnostic panel can distinguish several synthetic mechanism families, but exact equivalence classes remain:

```text
metric length change <-> propagation-speed change
hidden mediator <-> delayed direct edge
named memory state <-> equivalent hidden latent state.
```

Therefore effective-geometry change alone never uniquely identifies a physical mechanism.

Files:

- `sim04d_identifiability_gate.py`
- `SIM04D_RESULTS.md`

### SIM-04E — SoCT Memory Injection / Cross-Protocol Gate

Synthetic data generated by

```math
partial_t M = alpha C - beta M + D_M nabla^2 M
```

can be recovered on held-out source histories using fixed parameters. On local-memory data the general model returns `D_M = 0`; on instantaneous generators, the corresponding instantaneous nulls remain preferred.

Files:

- `sim04e_soct_memory_injection.py`
- `SIM04E_RESULTS.md`

### SIM-04F — Operational Observation -> Memory Source Bridge

The source is no longer supplied as arbitrary pulses. A measurement-like interaction produces distinguishability and accessible information, an ordinary detector record carries acquisition/persistence, and competing source models drive the same downstream memory equation.

The persistence-aware source reaches the planted noise floor on held-out protocols and survives a fragile-record adversary, but `Omega` remains a serious competing functional. The result supports a record-aware source family more strongly than any unique final formula.

Files:

- `sim04f_observation_derived_memory_source.py`
- `SIM04F_RESULTS.md`

### SIM-04G — Explicit Qubit + Detector + Environment Gate

A five-qubit unitary model demonstrates, without any SoCT term, that

```text
peak decoherence != persistent record formation
```

and

```text
record persistence != redundancy.
```

Environment record escape blocks local recoherence; reversing the environment-copy operations before local unmeasurement restores coherence. Thus much of the operational observation hierarchy is already standard open-system physics.

Files:

- `sim04g_qubit_detector_environment_records.py`
- `SIM04G_RESULTS.md`

### SIM-04H — H0/H1/H2 Complete Reset-and-Probe

Nested hypotheses:

```text
H0 = complete ordinary quantum/open-system model
H1 = same physics plus an operational observation summary, no new state
H2 = H0/H1 plus an additional state M with fixed source/relaxation/spatial/feedback laws.
```

After a complete reset of all explicitly modeled ordinary S/D/E degrees of freedom, H0 and H1 make the same post-reset physical prediction: no history-dependent residual on a fresh probe.

For H2-generated synthetic data, H2 recovers the planted `(beta,D_M,lambda)` and reaches the shot-noise floor on held-out protocols. For H0-generated data, the extra model is rejected by the complexity penalty. For an ordinary local-reservoir generator, H2 collapses to `D_M = 0` and the simpler local null is preferred.

Fundamental boundary:

```text
an identically parameterized conventional hidden diffusive field
is observationally equivalent to a state called M
under the restricted reset-and-probe measurements.
```

Files:

- `sim04h_h0_h1_h2_reset_probe.py`
- `SIM04H_RESULTS.md`

### SIM-04I — Incomplete-Reset / Hidden-Reservoir Adversary — next

Next question:

> How complete must reset verification be before an H2-like post-reset residual can be distinguished from conventional environmental memory?

Required adversaries:

```text
partially reset environment fragments
hidden mediator/reservoir modes
finite reservoir correlation times
conventional diffusive hidden state
independent reset-fidelity diagnostics
varying diagnostic sensitivity.
```

This gate should be completed before any laboratory-scale interpretation of the reset-and-probe signature.

---

## SIM-05 — Redundant Record / Broadcastability

Benchmark explicitly against Quantum Darwinism / Spectrum Broadcast Structure ideas.

**Question:** Which coarse-grained observables can be redundantly recovered from many downstream fragments while preserving consistent readout?

---

## SIM-06 — Observation Idempotence and Coarse-Graining

**Question:** Are stable recorded facts approximate fixed points of repeated observation/coarse-graining?

Candidate property:

```math
O(O(x)) ~= O(x).
```

---

## SIM-07 — Recursive Closure Fixed-Point Toy Model

**Question:** Can a low-parameter update system

```math
Z_t=(R_t,M_t,C_t,G_t)
```

with

```math
Z_{t+1}=F_theta(Z_t)
```

produce stable self-consistent observation-memory-causality-geometry fixed points without separately hard-coding each target structure?

This remains downstream of the identifiability gates.

---

## Research discipline

For every simulation:

1. record the standard/null explanation first;
2. state which assumptions are supplied rather than derived;
3. separate mathematical viability from physical evidence;
4. use held-out parameter regimes where possible;
5. prefer a failed clean prediction over post-hoc retuning;
6. do not label a toy-model effect as evidence for SoCT unless a SoCT-specific residual has been defined against simpler alternatives;
7. preserve the distinction between ordinary record memory `R` and any proposed additional state `M`;
8. treat reset/environmental closure as an empirical requirement, not an assumption that can be hidden in the model.
