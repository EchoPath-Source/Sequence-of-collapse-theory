# SOC-HYS-01 — Collapse-Memory Hysteresis in Repeated Measurement Systems

**Status:** PROPOSED / LOW-COST PHYSICAL PROTOCOL / PREREGISTRATION CANDIDATE  
**Claim level:** Hypothesis-generating only; no physical effect has been demonstrated.  
**Theory connection:** Sequence of Collapse Theory memory-residue channel.  
**Primary principle:** Anomaly first. Application second. Product claim last.

## Purpose

SOC-HYS-01 defines a cheap, simple, falsifiable test of whether repeated measurement histories leave small order-dependent residuals in later physical measurement noise or relaxation.

The experiment is intentionally narrower than propulsion, gravity control, vacuum extraction, or consciousness-collapse claims. It asks one humble question:

> If collapse leaves a memory residue, does the order of prior measurement conditions produce a measurable post-switch residual after conventional drift and environmental effects are controlled?

## Core hypothesis

If collapse leaves a memory residue, then repeated measurement histories should produce small order-dependent residuals in later measurement noise or system relaxation, even after energy, temperature, sensor drift, electronics settling, and other conventional effects are controlled.

A minimal symbolic statement is:

```text
R_post(H -> L) != R_post(L -> H)
```

where:

- `H` = high-coherence / high-structure measurement condition;
- `L` = low-coherence / diffuse / control measurement condition;
- `R_post` = early post-switch residual after subtracting known conventional effects.

## Why this track matters

This is currently one of the simplest possible SoCT-facing tests because it is:

- cheap;
- simple;
- directly tied to SoCT memory-residue claims;
- not dependent on grand cosmology;
- not framed as free energy, antigravity, or propulsion;
- falsifiable;
- easy to preregister;
- compatible with code-driven blind analysis.

## Digital versus physical testing

Pure code can simulate the protocol, validate the statistics, stress-test false positives, and develop the preregistration pipeline. Pure code cannot test the physical SoCT claim by itself, because ordinary pseudorandom number generators are deterministic algorithms rather than independent physical collapse streams.

The recommended path is therefore:

```text
Code controls the sequence, blinding, capture, and analysis.
A simple physical sensor provides the measurement stream.
```

Candidate physical inputs include:

- photodiode dark noise;
- webcam/camera sensor noise in darkness;
- laser speckle camera frames;
- microphone/electronics noise in a sealed quiet box;
- Geiger counter pulse timing;
- magnetometer noise;
- photodiode exposure under coherent versus diffuse illumination.

## Minimal protocol concept

Protocol A:

```text
1000 trials H -> 1000 trials L
```

Protocol B:

```text
1000 trials L -> 1000 trials H
```

Primary comparison:

```text
first N trials after switching
```

Candidate values:

```text
N = 50, 100, or preregistered fraction of the post-switch block
```

Primary prediction:

> The early post-switch residual after `H -> L` differs directionally from the early post-switch residual after `L -> H`, after conventional controls.

## Suggested low-cost optical version

Condition H:

```text
coherent or highly structured optical condition
```

Examples:

- stable laser spot on photodiode;
- narrow-path LED/laser condition;
- coherent/speckle-forming illumination.

Condition L:

```text
low-coherence or diffuse optical condition
```

Examples:

- same average power through diffuser;
- scattered illumination;
- thermal/dummy-light control matched in power.

Measurement stream:

```text
photodiode / camera sensor / ADC samples
```

## Required controls

Minimum controls before any claim:

1. Same average power across H and L conditions, or power logged and modeled.
2. Temperature logging near sensor and source.
3. Randomized block order.
4. Blinded condition labels during analysis.
5. Dark/sham runs.
6. Cooldown or settling intervals, if preregistered.
7. Reversal of physical orientation or source/sensor placement where feasible.
8. Repetition across multiple days.
9. Predefined exclusion criteria.
10. Permutation or bootstrap test specified before looking at the data.

## Primary endpoint

A conservative endpoint is:

```text
mean residual shift in the first N post-switch trials
```

after regression or subtraction of:

- temperature;
- input power;
- sensor baseline;
- time drift;
- block index;
- electronics settling;
- environmental flags.

## Failure condition

The hypothesis is weakened or falsified for this setup if:

```text
R_post(H -> L) and R_post(L -> H) show no directionally consistent difference after controls.
```

A null result should be reported as a useful constraint, not hidden.

## Recommended files for this experiment

```text
experiments/soc-hys-01-collapse-memory-hysteresis/protocol-v0-1.md
experiments/soc-hys-01-collapse-memory-hysteresis/analysis/README.md
experiments/soc-hys-01-collapse-memory-hysteresis/analysis/simulate_hysteresis_protocol.py
```

## Related simple-observation candidates to keep in view

1. Astrophysical age-residual correlations.
2. Post-event relaxation asymmetry in physical systems.
3. Directional memory / sky-axis residual cross-correlations.
4. Observer-state quantum-noise residual tests.

These should remain secondary until SOC-HYS-01 has a clear preregistered protocol and analysis pipeline.

## Claim boundary

SOC-HYS-01 does not claim to prove SoCT, consciousness-driven collapse, memory fields, new physics, vacuum engineering, propulsion, gravity control, or quantum hardware advantages.

It only defines a controlled, low-cost way to ask whether repeated physical measurement histories produce order-dependent residuals beyond known drift and environmental effects.
