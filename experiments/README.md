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
- Pantheon+ environment-dependent H0 test
- Hubble tension memory-drag analysis
- CMB anomaly correlation tests
- fine-structure constant spatial variation re-analysis
- GW memory comparison to GR predictions
- PNT two-timescale dark-energy / Hubble-window feasibility modeling

Current linked packages:

```text
papers/pnt-dark-energy-hubble-window/
experiments/cosmology/sparc-analysis-plan.md
experiments/cosmology/pantheon-environment-h0-test.md
```

The PNT package currently frames PNT as a two-timescale dark-energy model:

- prompt exhaust channel: EDE-like transient, toy-model sound-horizon shift, Boltzmann-code follow-up target
- memory-residue channel: late-time w(z), void-filament differential, DESI-facing observational track

The Pantheon+ environment test provides an independent expansion-side check of the void-versus-filament prediction:

```text
Delta_H0 = H0_void - H0_filament > 0
```

## Recommended file plan

```text
experiments/
├─ README.md
├─ osf/
│  ├─ preregistration-package-index.md
│  ├─ prereg-summary.md
│  ├─ mzi-protocol-v1.md
│  └─ materials-and-measures.md
├─ quantum/
│  ├─ modified-double-slit.md
│  ├─ mach-zehnder-consciousness-test.md
│  └─ delayed-choice-notes.md
└─ cosmology/
   ├─ sparc-analysis-plan.md
   ├─ pantheon-environment-h0-test.md
   ├─ hubble-memory-drag.md
   ├─ pnt-dark-energy-window.md
   ├─ cmb-anomaly-test.md
   └─ gw-memory-test.md
```

## Status note

Raw OSF artifacts are indexed but not yet fully converted into Markdown.
This folder currently serves as the structural landing zone for those materials.

The PNT dark-energy / Hubble-window paper package has been added under `papers/`; the next experiment-side additions should be reproducible cosmology notebooks and data-schema notes for SPARC and Pantheon+.
