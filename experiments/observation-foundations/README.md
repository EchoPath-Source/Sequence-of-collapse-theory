# Observation Foundations Simulation Program

**Status:** active exploratory simulation track  
**Scope:** operational observation, predictive memory, causal structure, effective geometry, and SoCT-specific memory identifiability  
**Claim level:** methodology and toy-model tests only; passing a simulation does not establish new physics.

## Related theory / status documents

- `papers/math/soc-operational-observation-model.md`
- `papers/math/soc-recursive-observation-memory-causality-geometry.md`
- `papers/math/soc-localization-memory-hamiltonian.md`
- `papers/math/soct-memory-origin-constraints-and-causal-completion.md`
- `papers/math/soct-memory-action-energy-exchange.md`
- `papers/math/soct-memory-local-exchange-continuity.md`
- `papers/math/soct-memory-microscopic-bath-completion.md`
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
ordinary microscopic baths can also generate reduced damping and recurrence;
the SoCT M equation is a viable and increasingly constrained extra-state model;
but M is not empirically required or uniquely identifiable.
```

SIM-04J through SIM-04M progressively remove arbitrariness rather than add flexibility:

```text
J -> causal/high-k completion
K -> global energy/backreaction ledger
L -> local exchange/flux continuity
M -> microscopic bath origin of effective damping.
```

## Simulation status

- **SIM-01 — Recursive Born Refinement — complete**  
  `p = 2` is the refinement-invariant fixed point within the tested `|alpha|^p` family under supplied Hilbert-space assumptions. This is a structural benchmark, not a new Born-rule derivation.  
  Files: `sim01_recursive_born_refinement.py`, `SIM01_RESULTS.md`

- **SIM-02 — Hidden State vs Genuine Memory — complete**  
  History dependence detects state incompleteness but does not identify the ontology of the missing state.  
  Files: `sim02_hidden_state_vs_memory.py`, `SIM02_RESULTS.md`

- **SIM-03A — Emergent Object Benchmark — complete**  
  Intervention-defined modules survive a latent common-cause confound that degrades ordinary correlation clustering.  
  Files: `sim03a_emergent_object_benchmark.py`, `SIM03A_RESULTS.md`

- **SIM-03B — Susceptibility / Criticality Adversary — complete**  
  Raw response amplitude is unsafe as a transmission or distance proxy; near criticality integrated response becomes dominated by indirect recurrent paths.  
  Files: `sim03b_susceptibility_criticality_adversary.py`, `SIM03B_RESULTS.md`

- **SIM-04A — Causal Order / Earliest Response — complete**  
  Finite noisy interventions recover reachability and earliest influence at high precision in the initial DAG benchmark.  
  Files: `sim04a_causal_order_earliest_response.py`, `SIM04A_RESULTS.md`

- **SIM-04B — Geometry From Order + Count + Delay — complete**  
  Causal interval count plus calibrated density carries timelike metric information in flat toy models; calibrated delay adds spatial information.  
  Files: `sim04b_order_count_delay_geometry.py`, `SIM04B_RESULTS.md`

- **SIM-04C — Candidate Causal-Distance Comparison — complete**  
  No universal scalar distance rule emerged. Background embedding geometry and effective causal/path geometry must be reported separately.  
  Files: `sim04c_candidate_distance_comparison.py`, `SIM04C_RESULTS.md`

- **SIM-04D — Identifiability Gate — complete**  
  Multi-protocol diagnostics separate several mechanism families, but exact equivalence classes remain: metric length vs propagation speed, hidden mediator vs delayed direct edge, and named memory state vs equivalent latent state.  
  Files: `sim04d_identifiability_gate.py`, `SIM04D_RESULTS.md`

- **SIM-04E — SoCT Memory Injection / Cross-Protocol Gate — complete**  
  The source-decay-diffusion equation produces a transferable synthetic signature when diffusion is truly present. On local-memory data it collapses to `D_M = 0`.  
  Files: `sim04e_soct_memory_injection.py`, `SIM04E_RESULTS.md`

- **SIM-04F — Observation-Derived Memory Source — complete**  
  The source can be derived from interaction, distinguishability, accessible information, record acquisition, persistence, and downstream accessibility rather than supplied as arbitrary pulses. `Omega` remains a serious competing functional.  
  Files: `sim04f_observation_derived_memory_source.py`, `SIM04F_RESULTS.md`

- **SIM-04G — Explicit Qubit + Detector + Environment — complete**  
  Standard unitary quantum mechanics already distinguishes transient decoherence, persistent environmental records, record erasure, and redundancy.  
  Files: `sim04g_qubit_detector_environment_records.py`, `SIM04G_RESULTS.md`

- **SIM-04H — H0/H1/H2 Complete Reset-and-Probe — complete**  
  After exact reset of all explicitly modeled ordinary degrees of freedom, H0 and H1 make the same physical prediction. H2 can generate a transferable post-reset signal when the synthetic generator includes an extra state, but a matched conventional hidden diffusive state remains observationally equivalent.  
  Files: `sim04h_h0_h1_h2_reset_probe.py`, `SIM04H_RESULTS.md`

- **SIM-04I — Incomplete Reset / Hidden Reservoir Adversary — complete**  
  Independent reset diagnostics can expose an ordinary leftover reservoir when they couple strongly enough. Weakly visible reservoirs can masquerade as H2; a diagnostic-blind matched reservoir is exactly unresolved.  
  Files: `sim04i_incomplete_reset_hidden_reservoir.py`, `SIM04I_RESULTS.md`

- **SIM-04J — Memory-Origin Constraint / Causal Completion — complete**  
  The reaction-diffusion memory equation is tested as the overdamped limit of a damped causal field. Late/low-k parameters plus independently calibrated `gamma` predict finite propagation speed, mode crossover, and high-k response without new high-k fit parameters.  
  Files: `sim04j_memory_origin_constraints.py`, `SIM04J_RESULTS.md`

- **SIM-04K — Action / Conservation / Backreaction Gate — complete**  
  Probe-only fitting is frozen before an independent damping-heat channel is predicted. Action-consistent synthetic data reach the heat-noise floor; otherwise identical probe trajectories with no heat or a different heat mechanism reject the field-energy interpretation.  
  Files: `sim04k_action_conservation_backreaction.py`, `SIM04K_RESULTS.md`

- **SIM-04L — Local Source / Field / Bath Exchange Continuity — complete**  
  The global energy requirement is strengthened to a spatially resolved continuity law. A spatially scrambled adversary preserves every global exchange total but fails the predicted local source/bath pattern by more than an order of magnitude above sensor noise.  
  Files: `sim04l_local_exchange_continuity.py`, `SIM04L_RESULTS.md`

- **SIM-04M — Microscopic Bath / Emergent Damping — complete**  
  The phenomenological `gamma dot(M)` term is replaced by explicit reversible harmonic bath modes. Sparse baths retain a long memory kernel and show strong energy return/recurrence, causing the local-friction model to fail on held-out late times. Dense broad baths suppress large recurrence over the tested window, produce a stable `gamma_eff ~ 0.46-0.47`, and substantially improve both held-out trajectory and effective heat prediction. Full microscopic energy closes to about `1e-7` across bath resolutions.  
  Files: `sim04m_microscopic_bath_emergent_damping.py`, `SIM04M_RESULTS.md`

## Observation program

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

These should be judged against established measurement, instrument, trajectory, Quantum Darwinism, Spectrum Broadcast Structure, and process-tensor formalisms without assuming new physics.

## SoCT extension

The optional SoCT layer begins only after ordinary record formation:

```text
ordinary retained record R
-> C_obs
-> additional state M
-> fixed feedback law
-> additional held-out residual.
```

The current first-order effective model is

```math
partial_t M = alpha C_obs - beta M + D_M nabla^2 M.
```

The candidate causal reduced model is

```math
partial_t^2 M
+ gamma partial_t M
- c_M^2 nabla^2 M
+ omega_M^2 M
= g C_obs,
```

with

```math
alpha=g/gamma,
qquad
beta=omega_M^2/gamma,
qquad
D_M=c_M^2/gamma.
```

SIM-04M adds an important hierarchy below this equation:

```text
explicit microscopic bath
-> exact reversible source/system/bath dynamics
-> generalized non-Markovian memory kernel
-> local gamma dot(M) only in a short-memory dense-bath limit.
```

Therefore `gamma` is not automatically a fundamental parameter or evidence for new physics.

## Current nested hypotheses

```text
H0 = complete standard quantum/open-system model
H1 = H0 plus a useful operational observation summary, no new state
H2 = H0/H1 plus an additional persistent state M.
```

In a true post-reset experiment, H0 and H1 are physically identical. The contest is H2 versus the strongest conventional state completion of H0/H1.

## Current identifiability boundary

A persuasive new-physics signature would now require, at minimum:

```text
verified matched ordinary state
+ different retained-record histories
+ fixed record-derived source law
+ transferable beta and D_M
+ controlled/derived damping or full non-Markovian kernel
+ predicted causal front / mode crossover
+ fixed probe/feedback coupling
+ held-out protocol and wavelength prediction
+ no-retuning global energy/backreaction prediction
+ spatially resolved local source/bath exchange consistency
+ failure of independently constrained conventional reservoirs.
```

A conventional physical degree of freedom with the same complete source, dynamics, microscopic environment, stress/energy exchange, and coupling law remains an ontology ambiguity. Statistics cannot resolve a pure naming difference.

## Next research gates

### Track A — covariant microscopic/open-system completion

SIM-04M supplies an explicit Hamiltonian bath in a nonrelativistic flat-background toy. Determine whether a corresponding environment/exchange sector can be embedded covariantly without inserting an unjustified preferred frame.

The eventual target remains

```math
nabla_mu T_total^{mu nu}=0.
```

### Track B — multi-mode / spatial microscopic bath

Extend the one-mode oscillator-bath gate to several field modes or a spatial lattice and test whether one bath spectral model predicts a common effective damping/kernel structure across wavelength.

### Track C — reset / environmental-closure budget

Continue quantifying conventional modes that can survive reset and the diagnostic sensitivity required to exclude them.

### Track D — standalone operational-observation manuscript

Continue the observation/record-formation model independently of H2. Its value should not depend on whether the memory-field extension survives.

## Research discipline

1. state the strongest conventional/null model first;
2. separate supplied assumptions from derived results;
3. separate mathematical viability from physical evidence;
4. use held-out histories, wavelengths, and parameter regimes;
5. prefer failed clean predictions over post-hoc retuning;
6. prefer simpler nested nulls when `D_M -> 0` or `lambda_M -> 0`;
7. preserve the distinction between ordinary record memory `R` and proposed state `M`;
8. never treat a hidden-state naming difference as physical evidence;
9. treat reset/environmental closure as an empirical measurement problem;
10. treat the first-order memory PDE and local damping as effective laws until their causal/microscopic/covariant regime is established;
11. require independently measured exchange/backreaction observables;
12. require local exchange consistency, not only integrated energy balance;
13. if bath recurrence or long memory is present, replace local `gamma` with the full non-Markovian kernel rather than retuning `gamma` after the fact.
