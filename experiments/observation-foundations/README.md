# Observation Foundations Simulation Program

**Status:** active exploratory simulation track  
**Scope:** operational observation, predictive memory, causal structure, effective geometry, and SoCT-specific memory identifiability  
**Claim level:** methodology and toy-model tests only; passing a simulation does not establish new physics.

## Related theory / status documents

- `papers/math/soc-operational-observation-model.md`
- `papers/math/soc-recursive-observation-memory-causality-geometry.md`
- `papers/math/soc-localization-memory-hamiltonian.md`
- `docs/operational-observation-current-formulation.md`
- `docs/soct-memory-necessity-status.md`
- `docs/observation-foundations-literature-crosswalk-2026-08-17.md`

## Purpose

This directory tests the proposed chain

```text
observation -> record -> memory -> causal influence -> effective geometry
```

and the recursive closure

```text
observation -> memory -> causality -> geometry -> observation.
```

Every simulation must include a conventional/null explanation, explicit failure criteria, and claim boundaries. Mathematical viability is kept separate from evidence that a physical SoCT memory field exists.

## Current scientific status

The simulation program does **not** currently show that a new memory field is necessary.

The conservative conclusion is:

```text
standard quantum/open-system physics explains much of observation and record formation;
ordinary hidden/local reservoirs explain some history-dependent residuals;
the SoCT M equation is a viable and falsifiable extra-state model;
but M is not yet empirically required or uniquely identifiable.
```

The current burden of proof is documented in `docs/soct-memory-necessity-status.md`.

## Simulation status

- **SIM-01 complete — Recursive Born Refinement**  
  `p = 2` is the refinement-invariant fixed point within the tested `|alpha|^p` family under supplied Hilbert-space assumptions. This is a structural benchmark, not a new derivation of quantum mechanics.  
  Files: `sim01_recursive_born_refinement.py`, `SIM01_RESULTS.md`

- **SIM-02 complete — Hidden State vs Genuine Memory**  
  History dependence identifies state incompleteness but not the ontology of the missing state. Markov completion can turn both ordinary hidden-state and explicit-memory processes into present-state dynamics.  
  Files: `sim02_hidden_state_vs_memory.py`, `SIM02_RESULTS.md`

- **SIM-03A complete — Emergent Object Benchmark**  
  Intervention-defined modules survive a latent common-cause confound that degrades ordinary correlation clustering.  
  Files: `sim03a_emergent_object_benchmark.py`, `SIM03A_RESULTS.md`

- **SIM-03B complete — Susceptibility / Criticality Adversary**  
  Raw response amplitude is unsafe as a transmission or distance proxy. Near criticality, integrated response is dominated by indirect recurrent paths.  
  Files: `sim03b_susceptibility_criticality_adversary.py`, `SIM03B_RESULTS.md`

- **SIM-04A complete — Causal Order / Earliest Response**  
  Finite noisy interventions recover reachability and earliest influence at high precision in the initial DAG benchmark.  
  Files: `sim04a_causal_order_earliest_response.py`, `SIM04A_RESULTS.md`

- **SIM-04B complete — Geometry From Order + Count + Delay**  
  In flat-spacetime toy models, causal interval count plus calibrated event density carries timelike metric information; calibrated delay adds spatial-separation information. Density gradients, shortcuts, and clock/medium changes define failure boundaries.  
  Files: `sim04b_order_count_delay_geometry.py`, `SIM04B_RESULTS.md`

- **SIM-04C complete — Candidate Causal-Distance Comparison**  
  No universal scalar distance rule emerged. Calibrated propagation delay generalized strongly on several withheld network families, while a learned combination did not universally beat simpler physics-informed estimators. Background embedding geometry and effective causal/path geometry must be reported separately.  
  Files: `sim04c_candidate_distance_comparison.py`, `SIM04C_RESULTS.md`

- **SIM-04D complete — Identifiability Gate**  
  Multi-protocol diagnostics separate several mechanism families, but exact equivalence classes remain: metric length vs propagation speed, hidden mediator vs delayed direct edge, and named memory state vs equivalent latent state.  
  Files: `sim04d_identifiability_gate.py`, `SIM04D_RESULTS.md`

- **SIM-04E complete — SoCT Memory Injection / Cross-Protocol Gate**  
  The source-decay-diffusion equation produces a transferable synthetic signature when diffusion is truly present. On local-memory data it collapses to `D_M = 0`; instantaneous nulls win when memory is absent.  
  Files: `sim04e_soct_memory_injection.py`, `SIM04E_RESULTS.md`

- **SIM-04F complete — Observation-Derived Memory Source**  
  The source can be derived from interaction, distinguishability, accessible information, record acquisition, persistence, and downstream accessibility rather than supplied as arbitrary pulses. Persistence-aware sources survive a fragile-record adversary, although `Omega` remains a serious competing functional.  
  Files: `sim04f_observation_derived_memory_source.py`, `SIM04F_RESULTS.md`

- **SIM-04G complete — Explicit Qubit + Detector + Environment**  
  Standard unitary quantum mechanics already distinguishes transient decoherence, persistent environmental records, record erasure, and redundancy. In particular:

  ```text
  peak decoherence != persistent record formation
  record persistence != record redundancy.
  ```

  Files: `sim04g_qubit_detector_environment_records.py`, `SIM04G_RESULTS.md`

- **SIM-04H complete — H0/H1/H2 Complete Reset-and-Probe**  
  After an exact reset of all explicitly modeled ordinary degrees of freedom, H0 and H1 make the same physical prediction: no fresh-probe history residual. H2 can generate a transferable post-reset signal when the synthetic generator includes an extra state. Exact-reset H0 data reject the extra model by complexity, while an ordinary local reservoir drives the general H2 fit to `D_M = 0`. A matched conventional hidden diffusive state remains observationally equivalent to `M`.  
  Files: `sim04h_h0_h1_h2_reset_probe.py`, `SIM04H_RESULTS.md`

- **SIM-04I complete — Incomplete Reset / Hidden Reservoir Adversary**  
  A conventional leftover reservoir is deliberately given the same source/decay/diffusion family as H2. Probe-only data cannot distinguish the two. Independent reset diagnostics can identify the conventional reservoir when they couple strongly enough and have sufficient sensitivity; weakly visible reservoirs can masquerade as H2, and a completely diagnostic-blind matched reservoir is exactly unresolved.  
  Files: `sim04i_incomplete_reset_hidden_reservoir.py`, `SIM04I_RESULTS.md`

## Central lessons through SIM-04I

### Observation program

The lower-level operational hierarchy remains viable independently of SoCT:

```text
interaction
-> correlation / distinguishability
-> information acquisition
-> retained physical record
-> downstream accessibility.
```

Candidate functionals include

```math
Omega = F(I_c,D,R,A_d)
```

and persistence-aware record-production forms such as

```math
Gamma_rec = G(partial_t I,R,A_d,Xi_irr).
```

These should be judged against established quantum measurement, instrument, trajectory, Quantum Darwinism, Spectrum Broadcast Structure, and process-tensor formalisms without assuming new physics.

### SoCT extension

The optional SoCT layer begins only after ordinary record formation:

```text
ordinary retained record R
-> C_obs
-> additional state M
-> fixed feedback law
-> additional held-out residual.
```

The current model is

```math
partial_t M = alpha C_obs - beta M + D_M nabla^2 M.
```

The current simulations show that this equation is **mathematically viable and falsifiable**, not that it is **necessary**.

## Current nested hypotheses

```text
H0 = complete standard quantum/open-system model
H1 = H0 plus a useful operational observation summary, no new state
H2 = H0/H1 plus an additional persistent state M.
```

In a true post-reset experiment, H0 and H1 are physically identical. The experimental contest is therefore H2 versus the strongest conventional state completion of H0/H1.

## Current identifiability boundary

A probe history residual alone is insufficient.

A persuasive new-physics signature would require, at minimum:

```text
verified matched ordinary state
+ different retained-record histories
+ fixed source law
+ transferable relaxation beta
+ transferable spatial term D_M
+ fixed probe/feedback coupling
+ held-out protocol prediction
+ failure of independently constrained conventional reservoirs.
```

Even then, a completely hidden conventional degree of freedom with exactly the same dynamics remains an ontology ambiguity until an additional discriminating prediction is derived.

## Next research gates

### Track A — SoCT-origin discriminator

Derive a prediction that follows from the **origin** of `M` in the SoCT Hamiltonian/record-production source rather than merely from assigning an arbitrary hidden field the same diffusion equation.

Promising targets:

```text
source-law constraints tied specifically to record production
parameter relations derived from the Hamiltonian
conservation / backreaction constraints
cross-observable coupling relations
universal scaling relations across different physical implementations.
```

### Track B — reset / environmental-closure budget

Before proposing a laboratory reset-and-probe experiment, quantify which conventional environment modes must be bounded, how reset fidelity would be diagnosed, what diagnostic couplings could remain blind, and how large an unobserved reservoir could remain consistent with the closure measurements.

### Track C — standalone operational-observation manuscript

Continue the observation/record-formation model independently of H2. Its value should not depend on whether the SoCT memory-field extension survives.

## Research discipline

For every future simulation:

1. state the strongest conventional/null model first;
2. separate supplied assumptions from derived results;
3. separate mathematical viability from physical evidence;
4. use held-out histories/parameter regimes where possible;
5. prefer a failed clean prediction over post-hoc retuning;
6. prefer simpler nested nulls when `D_M -> 0` or `lambda_M -> 0`;
7. preserve the distinction between ordinary record memory `R` and proposed state `M`;
8. never treat a hidden-state naming difference as physical evidence;
9. treat reset/environmental closure as an empirical measurement problem, not an assumption.
