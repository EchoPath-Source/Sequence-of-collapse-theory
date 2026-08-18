# Observation Foundations Simulation Program

**Status:** active exploratory simulation track  
**Scope:** operational observation, predictive memory, causal structure, and effective geometry  
**Claim level:** methodology and toy-model tests only; passing a simulation does not establish new physics.

Related theory documents:

- `papers/math/soc-operational-observation-model.md`
- `papers/math/soc-recursive-observation-memory-causality-geometry.md`
- `papers/math/soc-localization-memory-hamiltonian.md`
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
- **SIM-04A complete:** causal reachability and earliest response are recoverable at high precision from finite noisy interventions in the initial DAG benchmark; heterogeneous susceptibility mainly reduces recall for weak paths.
- **SIM-04B complete:** in flat-spacetime toy models, causal order + calibrated interval count recovers useful timelike scale; adding calibrated delay recovers useful spatial-separation information. Density gradients, nonlocal shortcuts, and uncalibrated delay expose explicit failure boundaries.
- **SIM-04C complete:** candidate distance rules were compared across regular and withheld geometry families. Calibrated propagation delay was the strongest simple generalizer for effective path geometry; a learned combination did not universally outperform physics-informed estimators. Shortcut and variable-speed cases confirmed that background embedding distance and effective causal distance can legitimately diverge.
- **SIM-04D complete:** a multi-protocol fingerprint separates several ordinary mechanism families in a controlled held-out benchmark, but exact non-identifiability classes remain: geometry vs propagation speed, hidden mediator vs delayed direct edge, and named memory state vs latent-state realization.
- **SIM-04E complete:** the canonical source-decay-diffusion equation produces a transferable held-out synthetic signature when diffusion is truly present; on local-memory data the larger model collapses to `D_M = 0`, preserving the simpler null.
- **Next:** SIM-04F — replace arbitrary source pulses with an operational observation / record-production source derived from the existing `Omega` / `Gamma_rec` program.

The literature-informed detailed SIM-03/04 plan is in `SIM03_04_REVISED_PLAN.md`.

## SIM-01 — Recursive Born Refinement

**Question:** Within Hilbert-space quantum mechanics, does square-norm weighting emerge as the unique member of the family `P proportional |alpha|^p` that is invariant under arbitrary equal orthogonal refinement and subsequent coarse-graining of record branches?

**Prediction under the stated assumptions:** `p = 2` has zero refinement error up to floating-point precision.

**Failure / limitation:** This does not derive Hilbert space, unitarity, orthogonality, additivity, or single-outcome selection. It tests only refinement consistency inside that framework.

Files:

- `sim01_recursive_born_refinement.py`
- `SIM01_RESULTS.md`

## SIM-02 — Hidden State vs Genuine Memory

**Question:** What evidence distinguishes history dependence caused by omitted conventional variables from a genuinely required additional memory state?

**Primary statistic:**

```math
I(H;F|X)
```

followed by progressive state augmentation.

**Result:** the statistic detects incomplete state descriptions but does not by itself identify the missing predictive state as an SoCT-specific memory field.

Files:

- `sim02_hidden_state_vs_memory.py`
- `SIM02_RESULTS.md`

## SIM-03 — Emergent Objects, Susceptibility, and Locality

### SIM-03A — Emergent Object Benchmark

**Question:** Can hidden dynamical modules be recovered without coordinates or supplied labels, and does intervention structure remain informative when observational correlation is confounded?

**Result:** in the toy benchmark, intervention-based methods recover the hidden modules under a latent common-cause confound while ordinary correlation clustering degrades.

Files:

- `sim03a_emergent_object_benchmark.py`
- `SIM03A_RESULTS.md`

### SIM-03B — Susceptibility and Criticality Adversary

**Question:** Does large intervention response reliably identify strong transmission, same-object membership, or short effective distance when receiver gain and recurrent amplification vary?

**Result:** no. Local susceptibility normalization substantially improves direct/small-lag transmission recovery, but near criticality long-time integrated response becomes dominated by indirect recurrent paths and ceases to recover the underlying direct transmission graph.

The surviving methodological rule is:

```text
large response != strong direct transmission != short effective distance.
```

Files:

- `sim03b_susceptibility_criticality_adversary.py`
- `SIM03B_RESULTS.md`

## SIM-04 — Causal Geometry Reconstruction

The original raw-response path metric is no longer accepted as the primary reconstruction method.

**Revised question:** Can hidden causal/geometric structure be reconstructed from finite noisy interventions using information that is less vulnerable to susceptibility and recurrence confounds?

The input hierarchy is now:

1. causal order / reachability;
2. earliest detectable response;
3. first-response delay;
4. small-lag/direct response with local susceptibility calibrated separately;
5. event/count or effective-volume information;
6. integrated response only as an auxiliary dynamical observable.

### SIM-04A — Causal Order / Earliest Response

**Result:** the initial hidden-DAG benchmark passes. Reachability precision remains above `0.9995` across the tested finite-trial regimes. Heterogeneous susceptibility primarily creates false negatives on weak paths; increasing intervention count restores recall monotonically. Earliest-lag error falls toward zero with additional trials.

Files:

- `sim04a_causal_order_earliest_response.py`
- `SIM04A_RESULTS.md`

### SIM-04B — Geometry From Order + Count + Delay

**Result:** homogeneous flat-spacetime sprinklings provide a clean toy demonstration that causal interval count plus calibrated event density carries metric information beyond causal comparability alone. Adding calibrated delay allows a useful reconstruction of spatial separation for causally related pairs.

The adversarial results establish three important boundaries:

```text
interval count requires density calibration
raw delay requires clock / medium calibration
real shortcut relations define a different effective causal geometry
```

Files:

- `sim04b_order_count_delay_geometry.py`
- `SIM04B_RESULTS.md`

### SIM-04C — Candidate Distance Constructions

**Result:** no universal scalar distance rule emerged. Calibrated propagation delay was the strongest simple estimator for effective path geometry on irregular, bottleneck, and variable-speed networks. `-log(transmission)` behaved well under its expected exponential-channel assumption but was not uniquely privileged. Hop count remained an excellent topology baseline on regular networks and degraded as edge costs varied.

A learned combination trained only on chain + grid data did **not** universally beat simple physics-informed estimators on withheld geometry families, providing an explicit anti-overfitting result.

The shortcut and variable-speed families require separate reporting against:

```text
background embedding geometry
versus
effective causal/path geometry
```

because real low-cost causal routes can make the two disagree.

Files:

- `sim04c_candidate_distance_comparison.py`
- `SIM04C_RESULTS.md`

### SIM-04D — Identifiability Gate

**Result:** practical mechanism identification improves dramatically when geometry residuals are supplemented with response timing, support changes, amplitude, local gain calibration, tail structure, and post-reset persistence. Across held-out weak/strong parameter ranges, the full diagnostic panel reaches about `0.993 +/- 0.005` classification accuracy in the controlled synthetic benchmark.

But three exact equivalence classes impose hard boundaries:

```text
metric length change <-> propagation-speed change
hidden mediator <-> delayed direct edge
named memory state <-> equivalent hidden latent state
```

Therefore an apparent `G_eff` change is not sufficient evidence for a distinct memory field or spacetime modification.

Files:

- `sim04d_identifiability_gate.py`
- `SIM04D_RESULTS.md`

### SIM-04E — SoCT Memory Injection / Cross-Protocol Gate

**Result:** when synthetic delay-residual data are generated by

```math
partial_t M = alpha C - beta M + D_M nabla^2 M,
```

with `beta = 0.08` and `D_M = 0.18`, fitting on source histories `A/B` and freezing parameters before histories `C/D` recovers the held-out data at the measurement-noise floor (`RMSE ~ 0.0020`). Instantaneous and no-diffusion memory nulls remain substantially worse.

When the generator is ordinary local memory, the general diffusive model returns `D_M = 0` and becomes identical to the simpler nested null. Instantaneous and spatial-instantaneous generators are likewise best explained by their own nulls rather than by a stable nonzero memory law.

This validates only that the canonical equation defines a distinguishable and transferable synthetic signature under favorable conditions; it is not evidence that the field exists physically.

Files:

- `sim04e_soct_memory_injection.py`
- `SIM04E_RESULTS.md`

### SIM-04F — Operational Observation -> Memory Source Bridge

The next integration test should stop injecting arbitrary source pulses and derive the candidate source from the operational observation model:

```text
system-detector interaction
    -> state distinguishability / mutual information
    -> record persistence
    -> downstream accessibility
    -> Omega or Gamma_rec
    -> candidate C_obs
    -> M
    -> one causal residual
```

The primary null must remain standard interaction/decoherence/record formation with no additional `M` feedback.

## SIM-05 — Redundant Record / Broadcastability

This simulation is now explicitly benchmarked against Quantum Darwinism / Spectrum Broadcast Structure ideas identified in the literature confrontation.

**Question:** Which coarse-grained observables can be redundantly recovered from many downstream fragments while preserving consistent readout?

## SIM-06 — Observation Idempotence and Coarse-Graining

**Question:** Are stable recorded facts approximate fixed points of repeated observation/coarse-graining?

Candidate property:

```math
\mathcal O(\mathcal O(x))\approx \mathcal O(x).
```

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

This simulation should be attempted only after SIM-04 establishes sensible causal/geometry operators.

## Research discipline

For every simulation:

1. record the standard/null explanation first;
2. state which assumptions are supplied rather than derived;
3. separate mathematical viability from physical evidence;
4. use held-out parameter regimes where possible;
5. prefer a failed clean prediction over post-hoc retuning;
6. do not label a toy-model effect as evidence for SoCT unless a SoCT-specific residual has been defined against simpler alternatives.
