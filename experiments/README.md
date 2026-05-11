# Experiments Hub

This folder is reserved for all experiment-facing SoCT material.

## Current experiment tracks referenced in the source corpus

### 1. Modified Double-Slit / Which-Path Access Test
Core question:
- Does collapse differ when which-path information is recorded but never consciously accessed?

Needed additions:
- apparatus sketch
- trial groups
- exclusion criteria
- storage/deletion protocol
- statistical plan

### 2. Mach-Zehnder Consciousness-Coupled Decoherence
Core question:
- Does observer coherence or conscious access measurably alter decoherence behavior?

Needed additions:
- OSF prereg text
- EEG / observer-state notes
- timing architecture
- randomization design
- analysis plan

### 3. Quantum Computing / Observer-Condition Tests
Core question:
- Do awareness-conditioned observation states alter collapse probabilities or system outputs?

Needed additions:
- use-case scope
- operational definitions of observer conditions
- quantum platform candidate list

### 4. Delayed-Choice / Conscious Access Reinterpretation
Core question:
- Is conscious integration the relevant completion condition rather than instrument registration alone?

Needed additions:
- theory note
- comparison with standard delayed-choice and quantum eraser literature

### 5. Cosmology / Observational Tests
Includes:
- SPARC age-dependent rotation curves
- Hubble tension memory-drag analysis
- CMB anomaly correlation tests
- fine-structure constant spatial variation re-analysis
- GW memory comparison to GR predictions
- PNT two-timescale dark-energy / Hubble-window feasibility modeling

Current linked package:

```text
papers/pnt-dark-energy-hubble-window/
```

This package currently frames PNT as a two-timescale dark-energy model:

- prompt exhaust channel: EDE-like transient, toy-model sound-horizon shift, Boltzmann-code follow-up target
- memory-residue channel: late-time w(z), void-filament differential, DESI-facing observational track

## Recommended file plan

```text
experiments/
├─ README.md
├─ osf/
│  ├─ prereg-summary.md
│  ├─ mzi-protocol-v1.md
│  └─ materials-and-measures.md
├─ quantum/
│  ├─ modified-double-slit.md
│  ├─ mach-zehnder-consciousness-test.md
│  └─ delayed-choice-notes.md
└─ cosmology/
   ├─ sparc-meta-analysis-plan.md
   ├─ hubble-memory-drag.md
   ├─ pnt-dark-energy-window.md
   ├─ cmb-anomaly-test.md
   └─ gw-memory-test.md
```

## Status note

No raw OSF artifacts have been imported yet.
This folder currently serves as the structural landing zone for those materials.

The PNT dark-energy / Hubble-window paper package has been added under `papers/`; the next experiment-side addition should be a reproducible cosmology notebook or an experiment-facing `experiments/cosmology/pnt-dark-energy-window.md` plan.
