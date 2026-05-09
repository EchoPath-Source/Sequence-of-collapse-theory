# Planck Memory Substrate: Engramon Unit Model

**Status:** speculative mechanism proposal / working formalization  
**Scope:** Sequence of Collapse Theory (SoCT), Planck Nucleation Theory (PNT), memory-field formalism  
**Purpose:** define the candidate microscopic unit and state-variable basis for the SoCT memory field.

## Summary

This note formalizes a mechanistic translation layer that has been implicit in SoCT/PNT:

```text
Planck cell     -> fundamental unit substrate
Engramon state  -> persistent modified state of that unit
Memory gradient -> regional pattern of Engramon-modified cells
Memory field    -> coarse-grained macroscopic expression of those gradients
```

The goal is to avoid treating the memory field as an abstract primitive. Instead, the memory field is modeled as a coarse-grained statistical field derived from microscopic Planck-cell state modifications caused by collapse and nucleation events.

## Core hierarchy

| Level | SOC/PNT term | Meaning |
|---|---|---|
| Fundamental unit | **Planck cell** | Smallest meaningful spacetime information packet / compactified dimensional interior. |
| Modified unit-state | **Engramon state** | Persistent modification of a Planck cell's internal entanglement geometry after a collapse or nucleation event. |
| Local field texture | **Memory gradient** | Regional pattern of Engramon-modified Planck-cell states. |
| Macroscopic field | **SOC memory field** | Coarse-grained influence of memory gradients on gravity, decoherence, structure formation, and cosmological observables. |

## Named axiom

### Planck Memory Substrate Axiom

> The SoCT memory field is the coarse-grained macroscopic expression of microscopic state modifications in Planck-scale spacetime cells. Each collapse or nucleation event alters the internal entanglement geometry of affected cells; these persistent modifications are Engramon states. The memory field `M(x,t)` is the local statistical gradient of Engramon density, coherence, and orientation.

This axiom gives the Engramon a precise ontological status within the working theory:

- not a particle,
- not an independent field quantum,
- not only an abstract memory token,
- but a persistent state modification of a Planck-scale spacetime cell.

## Statistical-mechanical analogy

The structure is analogous to the kinetic theory of gases:

```text
Molecule        -> fundamental unit
Kinetic state   -> state after interaction
Temperature     -> coarse-grained average of kinetic states
Pressure        -> macroscopic consequence of gradients
```

SoCT/PNT translation:

```text
Planck cell     -> fundamental unit
Engramon state  -> state after collapse/nucleation event
Memory field    -> coarse-grained average of Engramon states
Gravity/dark sector effects -> macroscopic consequence of memory gradients
```

The analogy is structural rather than decorative. Temperature is not postulated as a primitive substance; it is derived by coarse-graining microscopic molecular states. Likewise, the SoCT memory field should be derived, where possible, from the statistical behavior of Engramon states across Planck-scale cells.

## Working field definition

Let `e_i(t)` denote the Engramon state of Planck cell `i` at time `t`.

A coarse-grained memory field can be written as:

```text
M(x,t) = < e_i(t) >_{N(x)}
```

where:

- `M(x,t)` is the local memory-field value,
- `e_i(t)` is the current Engramon state of Planck cell `i`,
- `N(x)` is a coarse-graining neighborhood around spacetime location `x`,
- `<...>` denotes a weighted local average over cells in that neighborhood.

## Source-update form

The Engramon state of a Planck cell may be modeled as an accumulated history of collapse/nucleation sources:

```text
e_i(t) = e_i^0 + sum_j w_j K(|x_i - x_j|, t - t_j)
```

where:

- `e_i^0` is the baseline unmodified Planck-cell state,
- `j` indexes collapse or nucleation events,
- `w_j` is the event weight or coupling strength,
- `K` is the memory kernel / entanglement correlation kernel,
- `x_i` is the Planck cell location,
- `x_j, t_j` are the location and time of event `j`.

This state-based formulation is equivalent in spirit to earlier event-source integrals, but it is more physically transparent: the field is not only sourced by past events; it is the current coarse-grained state of Planck cells that have been modified by those events.

## Relation to the original H_SOC memory term

Earlier SoCT formulations used a memory-coupled Hamiltonian direction of the form:

```text
H_SOC = p^2/2m + V(x) + memory coupling term
```

with the memory coupling often represented schematically as an event-source integral:

```text
lambda * integral sum_j w_j K(|x - x_j|, t - t_j) dt
```

The Planck Memory Substrate formulation rewrites the same conceptual source history as a cell-state field:

```text
H_SOC = H_0 + lambda M(x,t)
M(x,t) = < e_i(t) >_{N(x)}
```

This makes the memory term less abstract and creates a pathway toward conservation laws, symmetry analysis, renormalization behavior, and scale-dependent effective descriptions.

## Field-theory requirements now specified

Every field theory needs at least the following elements. This model gives working candidates for each:

| Requirement | Working SoCT/PNT answer |
|---|---|
| Field value | `M(x,t)`, local Engramon density/coherence/orientation gradient |
| Domain | Spacetime / Planck lattice |
| Microscopic unit | Planck cell |
| State variable | Engramon state `e_i(t)` |
| Source | Collapse and nucleation events |
| Propagation / correlation law | Memory kernel `K` |
| Decay law | `tau_memory` / memory decoherence timescale |
| Coupling | `lambda` in `H_SOC = H_0 + lambda M(x,t)` |
| Candidate observables | gravitational deviations, dark-sector phenomenology, decoherence shifts, structure-formation gradients |

## Complete ontological stack

A working SoCT/PNT stack can now be expressed as:

```text
Light substrate / primordial potential
    -> localization / dimensional expression
Planck cells
    -> collapse and nucleation events
Engramon states
    -> statistical averaging / coarse-graining
Memory field M(x,t)
    -> coupling lambda
Gravity / dark energy / rotation curves / decoherence observables
```

The remaining theoretical work is not to invent new layers, but to derive each arrow quantitatively.

## Falsifiability and constraints

This axiom adds constraint to the theory. If memory is stored as persistent Planck-cell state modification, then SoCT/PNT must eventually specify:

1. how collapse/nucleation events write Engramon states,
2. how those states persist or decay,
3. how the memory kernel `K` propagates or correlates modifications,
4. how `M(x,t)` couples to gravity and quantum dynamics,
5. how the same parameters constrain SPARC, dark-energy, and decoherence predictions.

Potential falsification path:

> If Planck-scale spacetime cells cannot persist modified internal states long enough to produce macroscopic gradients, or if such persistence cannot couple to observables without violating established constraints, then the memory-field mechanism fails.

## Scientific status

This document is a working formalization, not established physics. It should be used as a scaffold for deriving testable consequences and for keeping future SoCT/PNT writing internally consistent.

Preferred public framing:

> The memory field is modeled as a coarse-grained effective field arising from persistent Planck-scale state modifications, analogous to how temperature arises from molecular kinetic states.

Avoid overclaiming that Planck cells or Engramon states have been empirically detected.

## Next work items

- Derive candidate conservation law or continuity equation for Engramon density.
- Specify possible scalar/vector/tensor structure of `e_i(t)`.
- Connect `tau_memory` to galaxy-scale memory fits and SPARC age/missing-mass analysis.
- Connect `K` to the Shephard-Mirrowen Hamiltonian memory kernel.
- Explore whether PNT dark-energy exhaust can be written as a source term in the Engramon-state update equation.
- Identify observable predictions that differ from conventional dark matter, modified gravity, or standard decoherence models.
