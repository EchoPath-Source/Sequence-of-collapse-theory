# SOC Localization-Memory Hamiltonian

**Status:** Canonical equation block / theoretical scaffold  
**Claim level:** Proposed mathematical framework, not established physics  
**Related files:** `docs/theory-overview.md`, `docs/source-corpus.md`, `PREDICTIONS.md`, `papers/math/shephard-mirrowen-hamiltonian-dimensional-analysis.md`

---

## Purpose

This document upgrades the placeholder SoCT Hamiltonian into a cleaner localization-memory block that can support future derivations, simulations, and experiment design.

The goal is not to claim confirmation. The goal is to define the working mathematical language consistently enough that it can be tested or falsified.

---

## Core Hamiltonian Block

The proposed Sequence of Collapse Hamiltonian is:

```text
H_SOC = H_free + H_loc + lambda_M M(x,t) O_M + lambda_c Phi_c(x,t) O_c
```

Where:

| Term | Meaning |
|---|---|
| `H_free` | Standard free Hamiltonian for the system. |
| `H_loc` | Localizing / measurement / environment-coupling contribution. |
| `M(x,t)` | Collapse-memory field or accumulated memory density. |
| `O_M` | Operator through which matter/fields couple to memory. |
| `Phi_c(x,t)` | Consciousness / conscious-access field or operational observer-state variable. |
| `O_c` | Operator through which observer-state coupling enters the collapse channel. |
| `lambda_M` | Coupling strength for memory-field interaction. |
| `lambda_c` | Coupling strength for consciousness/observer-state interaction. |

Research-safe interpretation:

> `H_SOC` extends ordinary dynamics with two speculative channels: a collapse-memory channel and an observer-state channel. Both require empirical constraints before physical interpretation.

---

## Memory Evolution Equation

The memory field evolves according to a source-decay-diffusion form:

```text
partial M / partial t = alpha C(x,t) - beta M(x,t) + D_M nabla^2 M
```

Where:

| Symbol | Meaning |
|---|---|
| `M(x,t)` | Memory density / collapse-history field. |
| `C(x,t)` | Collapse intensity source. |
| `alpha` | Conversion rate from collapse activity into memory. |
| `beta` | Memory decay / relaxation rate. |
| `D_M` | Memory diffusion / propagation coefficient. |

Interpretation:

- collapse events source memory;
- memory can decay, relax, or dephase;
- memory can spread or smooth across the substrate;
- stable gravitational/cosmological effects require long-lived or slowly relaxing components.

---

## Collapse Intensity

A minimal collapse-intensity proxy is:

```text
C(x,t) = A(x,t) |<Psi | O_c | Psi>|^2
```

Where:

| Term | Meaning |
|---|---|
| `A(x,t)` | Attention / access / observation-strength index. |
| `Psi` | Quantum state. |
| `O_c` | Collapse-channel operator. |

This is not yet a physical law. It is a way to make the observer-state branch operational.

For MZI/decoherence tests, the related phenomenological form is:

```text
lambda_eff = lambda_env + lambda_c A(t)
V(tau,A) = V0 exp[-lambda_eff tau]
```

---

## Relationship to Prior Placeholder Hamiltonian

Earlier repo materials use:

```text
H_SOC = p^2/2m + V(x) + memory coupling term
```

This document refines that into:

```text
H_SOC = H_free + H_loc + lambda_M M(x,t) O_M + lambda_c Phi_c(x,t) O_c
```

The new form separates:

1. standard dynamics;
2. localization/environment dynamics;
3. memory-field coupling;
4. observer-state coupling.

That separation is necessary for falsifiability.

---

## Dimensional Consistency Appendix

The related dimensional-analysis appendix is:

```text
papers/math/shephard-mirrowen-hamiltonian-dimensional-analysis.md
```

It records the minimum unit constraint that any nonlocal memory-coupling version of the Hamiltonian must satisfy:

```text
[lambda * integral_t integral_s w_i K dt ds] = Energy
```

For the normalized-kernel case where `w_i` and `ds` are dimensionless and `K` has units `T^-1`, the integral is dimensionless and the coupling must carry units of energy:

```text
[lambda] = Energy
```

The appendix also separates the required dimensional statement from the stronger, still-speculative Engramon normalization:

```text
lambda = lambda_E * E_E
```

with `lambda_E = 1` treated only as a candidate parameter-fixed proposal, not as a proof of the Engramon-neutrino carrier hypothesis.

---

## Prediction Matrix

| Prediction | Equation source | Expected signature | Falsification condition |
|---|---|---|---|
| Quantum memory hysteresis | `M(x,t)` evolution | Prior collapse history changes later coherence/visibility beyond standard environment models. | No history-dependent residual after controls. |
| Conscious-access threshold | `lambda_c Phi_c O_c` | Visibility/decoherence residual scales with operational awareness/access variable. | Blinded MZI tests show no residual relation to `A(t)`. |
| Post-observation aftereffect | `M` source-decay | A collapse event leaves short-lived measurable aftereffect. | No temporal residual beyond apparatus drift/noise. |
| Attention-state gradient | `A(x,t)` | Different observer-state conditions produce graded rather than binary effects. | No monotonic or threshold relationship under preregistered conditions. |
| Collapse-memory contribution to gravity | `lambda_M M O_M` | Older/outer systems show stronger apparent missing-mass residuals after controls. | SPARC/extended samples erase age/radial signal under controls. |
| Nonlocal inheritance / directional memory | `M` across boundary or parent-child transfer | Large-scale directional anomalies have calculable axis/amplitude. | No derivable axis or no match beyond chance/systematics. |

---

## Required Empirical Anchors

This block connects to the following repo tracks:

```text
observations/sparc/
experiments/cosmology/pantheon-environment-h0-test.md
experiments/quantum/
papers/pnt-dark-energy-hubble-window/
simulations/parent-child-transfer/
```

Related reproducibility and claim-boundary docs:

```text
docs/reproducibility_checklist.md
docs/research_to_product_handoff.md
docs/claim_boundaries_for_products.md
data/SPARC_IMPORT_STATUS.md
data/PANTHEON_IMPORT_STATUS.md
papers/p1-age-dependent-rotation-curves-sparc/REPRODUCIBILITY.md
papers/p4-soc-mzi-awareness-modulated-decoherence/EXPERIMENT_STATUS.md
papers/math/shephard-mirrowen-hamiltonian-dimensional-analysis.md
```

---

## Product Translation Boundary

This Hamiltonian may inspire product-safe engineering primitives only after translation through the claim-boundary filter.

Allowed product-safe translations include:

- adaptive memory,
- spatial memory,
- event persistence,
- field-inspired routing,
- threshold-driven response,
- topology-aware diagnostics,
- replay-derived tuning.

Do not use this Hamiltonian to claim that a product proves new physics, detects physical memory fields, validates consciousness-driven collapse, replaces dark matter, or certifies quantum/neuromorphic hardware.

---

## Claim Boundary

Use:

> This Hamiltonian provides a formal scaffold for separating memory-field and observer-state hypotheses into testable channels.

Avoid:

> This Hamiltonian proves consciousness causes collapse or gravity is memory.

---

## Next Work

1. Define units for `M(x,t)` and `Phi_c(x,t)` in the canonical field/operator form.
2. Map `lambda_M` to SPARC/Pantheon/PNT constraints.
3. Map `lambda_c` to MZI visibility/decoherence experiments.
4. Derive conservation or continuity conditions for `M`.
5. Connect memory-kernel form to the Engramon scale and PNT substrate without treating dimensional consistency as proof of the carrier hypothesis.
6. Keep any product translation routed through `docs/research_to_product_handoff.md` and `docs/claim_boundaries_for_products.md`.
