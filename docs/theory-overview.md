# Theory Overview

## One-sentence summary

Sequence of Collapse Theory proposes that reality resolves in stages: physical interaction/localization creates state-dependent records, consciousness is investigated as a possible additional finalization channel, and collapse-like events may leave a memory trace in spacetime.

## Core architecture

### 1. Pre-collapse / primordial field
A state of undifferentiated potential before localization.

### 2. First-stage physical observation / localization
Physical interaction generates state-dependent correlation, distinguishability, and potentially persistent records. Photons are one important carrier of such interactions but are not treated as the unique mathematical definition of an observer.

### 3. Conscious-access extension
Conscious observation is treated as a separable hypothesis: the research question is whether conscious access merely operates on already-formed records or contributes an additional physical term beyond ordinary interaction, measurement, and decoherence.

### 4. Memory field
SoCT proposes that some collapse/localization history may source an accumulated memory variable. Whether this `M(x,t)` represents physics beyond ordinary records and environmental correlations is an empirical question, not an assumption established by the observation model.

---

## Mathematical direction

The theory extends conventional quantum framing by proposing:

- an operational observation model derived from interaction, distinguishability, record persistence, and downstream accessibility;
- a consciousness-coupled term retained as a separable hypothesis rather than built into the definition of observation;
- a memory-coupled Hamiltonian at larger scales;
- a scale-sensitive memory kernel governing how past collapse/localization history may influence present states;
- operational variables for observer access, attention, and collapse-history conditioning.

### Current canonical Hamiltonian scaffold

The current repo-facing Hamiltonian scaffold is:

```text
H_SOC = H_free + H_loc + lambda_M M(x,t) O_M + lambda_c Phi_c(x,t) O_c
```

Related dynamic memory equation:

```text
partial M / partial t = alpha C(x,t) - beta M(x,t) + D_M nabla^2 M
```

Related collapse-intensity proxy:

```text
C(x,t) = A(x,t) |<Psi | O_c | Psi>|^2
```

Canonical files:

```text
papers/math/soc-localization-memory-hamiltonian.md
papers/math/soc-operational-observation-model.md
```

The observation project treats the currently unspecified `A(x,t)` / source structure as a derivation target. Its provisional chain is:

```text
H_int
  -> state-dependent correlation
  -> distinguishability
  -> record persistence
  -> downstream accessibility
  -> observation functional Omega
  -> record-production rate Gamma_rec
  -> candidate source C_obs
  -> memory M
```

Working interpretation:

- standard quantum/open-system dynamics govern the interaction and correlation baseline;
- the operational observation model asks when those interactions qualify as retained, accessible physical observation;
- memory-field formalism tests whether record/collapse history produces residual physics beyond standard environment models;
- observer-state variables provide a separate route to test the conscious-finalization branch;
- general relativity governs large-scale accumulated geometry, with SoCT exploring whether some residual gravitational behavior reflects collapse-memory structure.

---

## Active foundational refinement — Operational Observation Project

Path:

```text
papers/math/soc-operational-observation-model.md
```

Core question:

> What is the minimum physical transformation necessary and sufficient for one system to count as having observed another, and can record production be used to derive the source term that drives SoCT memory?

The current provisional hierarchy is:

```text
interaction
-> correlation
-> informational observation
-> persistent record
-> accessible record
-> integrated processing
-> conscious observation (optional later layer)
```

The project explicitly separates:

```text
observation != objective collapse != conscious observation
```

Its first goal is to reproduce sensible behavior in standard measurement/decoherence toy models before introducing any SoCT-specific memory feedback.

---

## Major theoretical claims / hypotheses

1. Observation can be operationalized below consciousness as state-dependent information transfer plus record formation/accessibility.
2. Consciousness is investigated as a possible additional physical channel rather than assumed to define all observation.
3. Gravity, dark matter effects, or spacetime structure may reflect accumulated collapse/localization memory.
4. Black holes may function as memory compression nodes rather than information-destroying sinks.
5. Higgs/localization language may help describe how stable local structures become available for observation, but direct Higgs-consciousness coupling is not currently established and should not be overclaimed.
6. Parent-child / causal-inversion cosmology is an extension branch, not the core SOC proof target.

---

## Empirical and simulation direction

Current planned or referenced tests include:

- qubit + pointer observation-functional toy models;
- record persistence / erasure / accessibility simulations;
- history-matched memory-feedback null tests;
- modified double-slit / interferometer designs with conscious access conditions;
- Mach-Zehnder style consciousness-coupled decoherence tests;
- quantum memory hysteresis / post-observation aftereffect tests;
- observer attention-state gradient tests;
- SPARC rotation curve re-analysis;
- Hubble tension environment analysis;
- Pantheon+ void-filament H0 test;
- CMB anomaly correlation with memory-field maps;
- parent-child directional transfer simulations;
- gravitational-wave memory comparisons;
- fine-structure variation re-analysis.

---

## Active formal branches

### 1. SOC localization-memory Hamiltonian

Path:

```text
papers/math/soc-localization-memory-hamiltonian.md
```

Role:

> Separates free dynamics, localization coupling, memory-field coupling, and observer-state coupling into a testable formal scaffold.

### 2. Operational observation model

Path:

```text
papers/math/soc-operational-observation-model.md
```

Role:

> Attempts to derive observation strength and record-production variables from standard interaction/information quantities before testing memory-field or conscious-access extensions.

### 3. Dark-sector taxonomy

Path:

```text
docs/dark-sector-taxonomy.md
```

Role:

> Keeps ordinary matter, dark matter, dark energy, PNT prompt exhaust, memory residue, and parent-child inheritance distinct.

### 4. Parent-child transfer simulations

Path:

```text
simulations/parent-child-transfer/
```

Role:

> Tests whether directional memory can survive bounce-like transfer in toy models. This is an extension branch and does not prove physical parent universes.

### 5. PNT dark-energy / Hubble-window package

Path:

```text
papers/pnt-dark-energy-hubble-window/
```

Role:

> Explores Planck nucleation exhaust and long-lived memory residue as a two-timescale dark-energy model.

### 6. SPARC / galaxy memory branch

Paths:

```text
experiments/cosmology/sparc-analysis-plan.md
observations/sparc/
```

Role:

> Tests whether galaxy collapse-history proxies correlate with missing-mass behavior after controls.

---

## Claim discipline

Use:

> SOC is a structured research framework investigating staged reality resolution, operational observation, possible collapse/localization memory, and a separable conscious-access extension, with experimental and cosmological branches under active testing.

Avoid:

> SOC has proven consciousness collapses reality, all observation creates a new physical memory field, dark matter is memory, or our universe is definitely inside a black hole.

---

## Repo use

This file is the short orientation layer.
Use it when onboarding collaborators or deciding where a new note, dataset, simulation, or paper belongs.
