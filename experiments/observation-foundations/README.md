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

SIM-04J and SIM-04K strengthen the field hypothesis by adding constraints rather than flexibility. SIM-04J treats the first-order reaction-diffusion law as an effective low-frequency limit of a candidate causal field. SIM-04K then requires the same field parameters to satisfy a no-retuning energy/backreaction ledger.

## Simulation status

- **SIM-01 complete — Recursive Born Refinement**  
  `p = 2` is the refinement-invariant fixed point within the tested `|alpha|^p` family under supplied Hilbert-space assumptions.  
  Files: `sim01_recursive_born_refinement.py`, `SIM01_RESULTS.md`

- **SIM-02 complete — Hidden State vs Genuine Memory**  
  History dependence identifies state incompleteness but not the ontology of the missing state.  
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
  Causal interval count plus calibrated density carries timelike metric information in flat toy models; calibrated delay adds spatial information.  
  Files: `sim04b_order_count_delay_geometry.py`, `SIM04B_RESULTS.md`

- **SIM-04C complete — Candidate Causal-Distance Comparison**  
  No universal scalar distance rule emerged. Background embedding geometry and effective causal/path geometry must be reported separately.  
  Files: `sim04c_candidate_distance_comparison.py`, `SIM04C_RESULTS.md`

- **SIM-04D complete — Identifiability Gate**  
  Multi-protocol diagnostics separate several mechanism families, but exact equivalence classes remain: metric length vs propagation speed, hidden mediator vs delayed direct edge, and named memory state vs equivalent latent state.  
  Files: `sim04d_identifiability_gate.py`, `SIM04D_RESULTS.md`

- **SIM-04E complete — SoCT Memory Injection / Cross-Protocol Gate**  
  The source-decay-diffusion equation produces a transferable synthetic signature when diffusion is truly present. On local-memory data it collapses to `D_M = 0`.  
  Files: `sim04e_soct_memory_injection.py`, `SIM04E_RESULTS.md`

- **SIM-04F complete — Observation-Derived Memory Source**  
  The source can be derived from interaction, distinguishability, accessible information, record acquisition, persistence, and downstream accessibility rather than supplied as arbitrary pulses. `Omega` remains a serious competing functional.  
  Files: `sim04f_observation_derived_memory_source.py`, `SIM04F_RESULTS.md`

- **SIM-04G complete — Explicit Qubit + Detector + Environment**  
  Standard unitary quantum mechanics already distinguishes transient decoherence, persistent environmental records, record erasure, and redundancy.  
  Files: `sim04g_qubit_detector_environment_records.py`, `SIM04G_RESULTS.md`

- **SIM-04H complete — H0/H1/H2 Complete Reset-and-Probe**  
  After an exact reset of all explicitly modeled ordinary degrees of freedom, H0 and H1 make the same physical prediction: no fresh-probe history residual. H2 can generate a transferable post-reset signal when the synthetic generator includes an extra state, but a matched conventional hidden diffusive state remains observationally equivalent.  
  Files: `sim04h_h0_h1_h2_reset_probe.py`, `SIM04H_RESULTS.md`

- **SIM-04I complete — Incomplete Reset / Hidden Reservoir Adversary**  
  Independent reset diagnostics can expose an ordinary leftover reservoir when they couple strongly enough. Weakly visible reservoirs can masquerade as H2; a completely diagnostic-blind matched reservoir is exactly unresolved.  
  Files: `sim04i_incomplete_reset_hidden_reservoir.py`, `SIM04I_RESULTS.md`

- **SIM-04J complete — Memory-Origin Constraint / Causal Completion**  
  The reaction-diffusion memory equation is tested as the overdamped limit of a damped causal field. Late/low-k parameters plus an independently calibrated `gamma` predict finite propagation speed, a mode-crossover scale, and high-k response without new high-k fit parameters. The causal generator passes its held-out high-k test; a pure-diffusion generator instead selects the diffusion null.  
  Files: `sim04j_memory_origin_constraints.py`, `SIM04J_RESULTS.md`

- **SIM-04K complete — Action / Conservation / Backreaction Gate**  
  The candidate causal field implies the flat-background energy ledger

  ```math
  partial_t rho_M + div S_M
  = g C_obs partial_t M - gamma (partial_t M)^2.
  ```

  Parameters are fitted only from training probe trajectories and frozen before an independent damping-heat channel is predicted. For action-consistent synthetic data, held-out heat prediction reaches the heat-noise floor (`RMSE ~ 0.00194` for `sigma_heat = 0.002`). For an otherwise identical field-like probe generator with no heat signal, the action model fails strongly (`RMSE ~ 0.08643`) while the zero-heat null wins. A source-power heat generator is likewise best explained by its own simpler heat law.  
  Files: `sim04k_action_conservation_backreaction.py`, `SIM04K_RESULTS.md`

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

Current effective model:

```math
partial_t M = alpha C_obs - beta M + D_M nabla^2 M.
```

Candidate causal completion:

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

Cross-regime constraints include

```math
c_M=sqrt(gamma D_M)
```

and

```math
k_c^2=(gamma/4-beta)/D_M.
```

For overdamped Fourier modes,

```math
r_-(k)[gamma-r_-(k)]/gamma = beta + D_M k^2.
```

The candidate flat-background energy density is

```math
rho_M
= 1/2 (partial_t M)^2
+ 1/2 c_M^2 |grad M|^2
+ 1/2 omega_M^2 M^2,
```

with periodic/no-flux integrated exchange law

```math
dE_M/dt = P_source - P_damp.
```

The present simulations show mathematical viability and increasing falsifiability, not necessity.

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
+ independently calibrated fast scale gamma
+ predicted causal front / mode crossover
+ fixed probe/feedback coupling
+ held-out protocol and wavelength prediction
+ no-retuning energy/backreaction prediction
+ failure of independently constrained conventional reservoirs.
```

A conventional physical degree of freedom with exactly the same complete source, causal dynamics, energy exchange, and coupling law remains an ontology ambiguity. Statistics cannot resolve a pure naming difference.

## Next research gates

### Track A — explicit exchange / covariant conservation completion

SIM-04K still treats `gamma partial_t M` as effective damping. Introduce an explicit recipient/bath sector so the damping loss appears as energy gained elsewhere rather than disappearing phenomenologically. Derive a coupled total-energy ledger and then a covariant stress-energy scaffold.

The full target is eventually

```math
nabla_mu T_total^{mu nu}=0,
```

not merely a flat-space scalar energy balance.

### Track B — causal-completion audit

Determine whether the damped hyperbolic completion can be made covariant without inserting an unjustified preferred frame, and whether its low-frequency limit consistently reproduces the current phenomenological equation.

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
10. treat the first-order memory PDE as an effective law until causal/covariant completion is established;
11. do not interpret a field-like probe residual physically unless the same fixed parameters satisfy the independently measured exchange/backreaction ledger.
