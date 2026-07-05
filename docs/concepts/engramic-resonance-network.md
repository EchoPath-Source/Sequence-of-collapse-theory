# Engramic Resonance Network

**Status:** concept / prototype design note  
**Primary tracks:** simulations, P3 concept-to-equation, P7 unified framework  
**Related prototype:** `simulations/collapse-neural-network/`  
**Claim boundary:** This is a research architecture and visualization concept. It does not claim to replace neural networks or demonstrate machine consciousness.

## Core idea

An **Engramic Resonance Network** is a neural or agent architecture where activation depends on accumulated collapse history rather than only static weighted input.

Working sentence:

> Cognition emerges from accumulated collapse history rather than static weighted inference.

In this framing, each node acts as a local collapse site. A past event does not vanish after activation. It persists as an **engram**: a decaying, spatially distributed, phase-sensitive memory imprint that can bend future node behavior.

## Prototype kernel

The current prototype uses a SoCT-style memory kernel:

```text
K(r, tau, s) = A(s) * exp(-r/lambda_s) * exp(-tau/tau_s) * cos(omega_s * tau)
```

Where:

| Term | Meaning |
|---|---|
| `r` | spatial distance between source and target nodes |
| `tau` | elapsed time since the source collapse event |
| `s` | scale parameter for the source node/layer |
| `A(s)` | scale-weighted amplitude |
| `lambda_s` | spatial decay length |
| `tau_s` | temporal decay window |
| `omega_s` | resonant frequency term |

Each node computes a local memory field:

```text
M_i(t) = sum over prior collapse events K(r_ij, tau, s_j) * weight_j
```

The node collapses/fires when its potential crosses a threshold.

## Node state fields

A minimal node can carry:

```text
node = {
  memoryField,
  potential,
  threshold,
  collapseHistory,
  resonancePhase,
  spinState,
  dimensionalLayer
}
```

The prototype adds two hidden modulation channels:

- `spinState`: a two-state hidden degree of freedom that modulates threshold sensitivity.
- `dimensionalLayer`: an index such as d3/d4/d5 that shifts resonance timing.

These are not claims of physical spin or literal extra-dimensional access. They are prototype variables for testing hidden-state modulation and phase-shifted recurrence.

## Why this matters for SoCT

Traditional feedforward neural-network language often emphasizes weights and activations. The Engramic Resonance Network reframes node activity as a consequence of accumulated field history:

```text
Static weighted model:
current activation = weighted sum of current inputs

Engramic resonance model:
current activation = local response to compressed collapse history
```

This creates a direct bridge to existing SoCT terms:

- **Collapse event:** a node firing or field-localization event.
- **Engram:** the persistent residue of a collapse event.
- **Memory field:** the aggregate of prior residues affecting current behavior.
- **Resonance:** periodic or phase-sensitive reactivation of prior collapse structure.
- **Compression:** many prior events folded into one present potential.

## Application lanes

This architecture is useful first as a design pattern rather than a grand AI claim.

Potential lanes:

1. **Spatial memory for XR/game worlds**  
   Rooms, routes, NPCs, or hazards accumulate memory fields based on what happened there.

2. **Agent behavior with residue**  
   Agents do not merely react to the present. They act through local field history.

3. **Anomaly and weak-link detection**  
   Nodes or graph regions whose behavior cannot be explained by ordinary propagation can be scored as residue pressure or compression mismatch.

4. **Neuromorphic validation language**  
   Coherence, phase drift, weak-link deformation, and topology-aware memory signatures can be measured across dynamic hardware graphs.

5. **SoCT simulations**  
   Toy systems can test whether memory-field accumulation produces stable/recurrent structures distinct from simple weighted-sum propagation.

## Suggested diagnostics

Future simulation versions can track:

```text
mean_memory_field
collapse_rate
resonance_reactivation_rate
residue_pressure
compression_mismatch
boundary_tax
avalanche_residue
hidden_state_sensitivity
phase_lock_duration
```

## Public-facing summary

> The network remembers not by storing the past as a file, but by letting the past continue to bend the present.

## Repository links

- `simulations/collapse-neural-network/`
- `papers/math/soc-localization-memory-hamiltonian.md`
- `papers/p3-soc-concept-to-equation/`
- `papers/p7-unified-framework/`
