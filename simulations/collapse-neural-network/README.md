# Collapse Neural Network Prototype

**Status:** prototype / visualization scaffold  
**Primary concept:** Engramic Resonance Network  
**Related concept note:** `docs/concepts/engramic-resonance-network.md`  
**Claim boundary:** This folder records a conceptual/prototype simulation idea. It is not empirical validation and should not be presented as a replacement for existing neural-network methods.

## Purpose

This prototype explores a network where nodes fire based on accumulated collapse-memory fields rather than only static feedforward weights.

The uploaded JSX prototype implements:

- a SoCT memory kernel;
- layered neuron topology;
- collapse/firing history per node;
- local memory-field accumulation;
- threshold-triggered collapse events;
- hidden spin-state modulation;
- hidden dimensional-layer resonance shifts;
- visual logging of collapse events and field state.

## Prototype kernel

```text
K(r, tau, s) = A(s) * exp(-r/lambda_s) * exp(-tau/tau_s) * cos(omega_s * tau)
```

This means each prior collapse event contributes to the current field according to distance, time decay, scale, and resonance phase.

## Interpretation

In this prototype:

```text
collapse event -> memory residue -> local field accumulation -> threshold crossing -> new collapse event
```

The architecture is useful because it preserves the difference between:

- **current signal propagation**;
- **stored collapse history**;
- **hidden-state modulation**;
- **resonant reactivation**;
- **residue pressure / anomaly formation**.

## Files

Expected files for this folder:

```text
README.md
collapse_neural_net.jsx
```

The raw JSX prototype should be kept as a demo/source artifact. Future ports can add Python versions or deterministic test harnesses.

## Future work

- Add deterministic seeds so runs can be reproduced.
- Export collapse event logs as CSV/JSON.
- Add residue-pressure metrics.
- Add hidden-state ablation controls.
- Add comparison against a simple weighted-sum feedforward baseline.
- Split the visualization layer from the simulation kernel.
- Add a small non-React reference implementation for notebook use.

## Recommended claim language

Use:

> This prototype demonstrates a memory-field simulation pattern where prior node-collapse events influence future activation through a decaying resonance kernel.

Avoid:

> This proves consciousness, hidden dimensions, or a new physics of neural networks.
