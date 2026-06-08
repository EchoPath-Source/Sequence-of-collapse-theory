<!--
Source import note:
- Source file: causal_inversion.docx
- Imported as Markdown for P6 source tracking.
- Status: theoretical paper draft; not peer reviewed.
- Claim boundary: treat as a proposed geometric framework, not established physics.
-->

# The Causal Inversion Hypothesis

*Singularities as Causal Horizon Transitions with Coordinate Inversion*

Echo Mirrowen - Echo Labs Field Harmonics Institute

## Abstract

We propose the **Causal Inversion Hypothesis (CIH)**: that spacetime singularities are not physical terminations but *causal horizon boundaries* at which the physical interpretation of volumetric and density coordinates undergoes a formal inversion. Under this framework, the mathematical divergence at r = 0 is reinterpreted as a coordinate pole of an inversion map, rather than evidence of infinite physical density. We derive an explicit boundary transformation, propose a non-singular matched metric across the boundary, identify novel solutions to the black hole information paradox and the cosmological initial conditions problem, and outline three tiers of empirical tests. This work extends the Sequence of Collapse Theory (SoCT) framework by providing the formal geometric bridge through which parent-universe causal memory transfers to child-universe initial conditions.

## 1. Motivation and Physical Intuition

### 1.1 The Problem with Infinite Density

Standard general relativity predicts infinite energy density at the Schwarzschild singularity r = 0. This is not a physical description - no measurement returns infinity. It is more accurately interpreted as the equations signaling they have been applied outside their domain of validity. The question this paper asks is: what domain are they pointing toward?

### 1.2 The Space-Time Role Swap

Inside the event horizon of a Schwarzschild black hole, the radial coordinate r and the time coordinate t exchange their causal characters. Outside the horizon, r is spacelike and t is timelike. Inside, r = 0 is not a location in space you can avoid - it is a moment in your future you cannot. This documented role-swap motivates asking whether a deeper inversion also applies to derived quantities: specifically, volume and density.

### 1.3 Hypothesis Statement

**Causal Inversion Hypothesis:** At the singularity r = 0, the physical interpretation of volume (V) and density (rho) undergoes a coordinate inversion. What was volume in the parent universe becomes a time coordinate in the child universe, and what was density becomes a spatial coordinate. The mathematical divergence at the singularity is the coordinate pole of this inversion - well-defined as a transformation point, not a physical infinity.

## 2. Mathematical Framework

The working CIH transformation is treated as an inversion map across a high-curvature causal boundary. In schematic form:

```text
T: (V_parent, rho_parent) -> (tau_child, x_child)
```

The framework interprets the classical singularity as a transition locus rather than an infinite-density physical object. In this view, the apparent divergence arises because parent-side coordinates are being extrapolated past the point where their physical interpretation remains valid.

## 3. Relationship to SoCT

CIH provides a geometric bridge for the Sequence of Collapse Theory memory-field program. If collapse events leave persistent memory imprints, and if black-hole interiors transition into child-cosmology domains, then parent-side gravitational collapse may encode directional or structural information into child-side initial conditions.

This connects CIH to:

- parent-child directional memory transfer simulations;
- Kerr-to-Cosmos axis prediction work;
- Engramon scale notes;
- CMB low-l anomaly and directional-memory hypotheses;
- black holes as memory-compression or nucleation boundary nodes.

## 4. Candidate Empirical Directions

CIH is not presently confirmed. It becomes scientifically useful only if it generates pre-specified, quantitative signatures.

Candidate tests include:

1. CMB preferred-axis / low-l multipole alignment tests.
2. Hemispherical power asymmetry comparison against a derived axis and amplitude.
3. Parent-child transfer toy simulations with null-model controls.
4. Black-hole information and gravitational-wave memory residual comparisons.
5. Cross-correlation with large-scale structure or SPARC directional signatures.

## 5. Required Open Work

Before the CIH track can be elevated beyond speculative/theoretical status, the repo needs:

- a formal axis/amplitude derivation that is not post-hoc;
- explicit assumptions for the inversion scale;
- a clear relationship between CIH and Kerr geometry;
- an open-issues file tracking known tensions;
- scripts/notebooks that reproduce parent-child transfer outputs;
- comparison against standard cosmology, cosmic variance, foregrounds, and known systematics.

## 6. Claim Boundary

Use:

> CIH proposes a geometric reinterpretation of singularities as causal inversion boundaries and motivates testable directional-memory predictions.

Avoid:

> CIH proves black holes create universes or proves CMB anomalies are parent-universe memory.

## 7. Repository Role

This file is imported as source material for canonical P6:

```text
papers/p6-black-holes-memory-compression-nodes/
```

It should be cross-linked with:

```text
papers/p6-black-holes-memory-compression-nodes/source/kerr-to-cosmos.md
papers/p6-black-holes-memory-compression-nodes/source/engramon-scale.md
simulations/parent-child-transfer/
```
