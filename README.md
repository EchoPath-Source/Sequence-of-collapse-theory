# Sequence of Collapse Theory

A structured research repository for the **Sequence of Collapse (SoC / SoCT)** framework by Antoine L. Shephard.

This repo is intended to become the central home for:

- core theory documents
- mathematical frameworks
- experimental proposals
- simulation notes and validation logs
- literature/references
- OSF-linked preregistrations and study drafts
- future datasets, notebooks, figures, and publication-ready papers

## Current scope

This setup organizes the theory into a clean research structure using existing project materials already available across the working corpus.

At this stage, the repo includes:

- a repo map
- a source corpus index
- a theory overview
- an article/book map
- an experiments hub
- a simulations hub
- validation and bibliography notes
- an empirical exploration summary for the SPARC / effective-G / Pantheon+ phase
- data and notebook scaffolds for reproducible cosmology tests
- OSF companion text files
- paper/protocol hubs for P1, P2, P3, and P4

## Working core claims

1. **First Collapse**: light / photon-mediated decoherence begins the narrowing of possibility into structure.
2. **Second Collapse**: conscious observation finalizes experienced reality.
3. **Memory Field**: collapse events leave accumulated spacetime imprint, modeled as a memory field.
4. **Shephard-Mirrowen Hamiltonian**: extension of standard Hamiltonian formalism with memory coupling.
5. **Cross-domain implication**: the theory propagates into cosmology, gravity, measurement theory, cognition, spatial computation, and experimental design.

## Active research packages

### P1 — Memory-Field Gravity / SPARC / SoCT-PM

P1 is the empirical-gravity track. It explores whether gravity can be modeled as an accumulated collapse-memory effect and uses SPARC rotation curves as an initial validation anchor.

Repo hub:

```text
papers/p1-memory-field-gravity-sparc/
```

OSF companion text:

```text
osf/p1-memory-field-gravity-sparc.md
```

Primary focus:

- gravity as accumulated collapse history;
- memory-field residuals and effective gravitational behavior;
- SPARC rotation-curve analysis;
- SoCT-PM simulation planning;
- comparison against baryons-only, dark-matter-halo, and MOND-like baselines.

### P2 — PNT Dark Energy / Hubble Window

P2 is the Planck Nucleation Theory dark-energy and Hubble-window track.

Repo hub:

```text
papers/pnt-dark-energy-hubble-window/
```

It currently includes:

- `working-draft-v0-1.md` — physics-first P2 paper skeleton for Planck Nucleation Theory as a two-timescale dark-energy model.
- `toy-model-results-v0-1.md` — summary of the prompt-exhaust / Early-Dark-Energy feasibility toy calculations.

Core conclusion of this package:

> PNT naturally separates into a short-lived prompt exhaust channel and a long-lived memory-residue channel. The prompt channel can produce an EDE-like transient but does not yet demonstrate full Hubble-tension resolution in minimal toy models. The late memory component is the stronger near-term publishable track, with predicted w(z) evolution and void-versus-filament differentials.

### P3 — Causal Inversion / Directional Memory Cosmology

P3 is the parent-universe, bounce, and directional-memory cosmology track.

Repo hub:

```text
papers/p3-causal-inversion-directional-memory/
```

OSF companion text:

```text
osf/p3-causal-inversion-directional-memory.md
```

Primary focus:

- Causal Inversion Hypothesis;
- Kerr-to-Cosmos geometry;
- parent-universe memory;
- CMB preferred-axis and anisotropy tests;
- parity asymmetry, hemispherical power imbalance, and low-l alignment questions.

### P4 — Observer-Dependent Decoherence / CGDS / SOC-MZI

P4 is the quantum-observer and consciousness-gated measurement track.

Repo hub:

```text
papers/p4-observer-dependent-decoherence-cgds/
```

OSF companion text:

```text
osf/p4-cgds-observer-decoherence.md
```

Primary focus:

- Consciousness-Gated Double-Slit (CGDS);
- machine-only versus conscious-access measurement conditions;
- SOC-MZI / Mach-Zehnder extensions;
- delayed-choice and quantum-eraser reinterpretations;
- awareness-conditioned quantum computing;
- quantum brain-field coupling proposals.

### Empirical exploration package

The current empirical synthesis is preserved under:

```text
docs/empirical-exploration-thread-summary-v0-1.md
```

This package records the transition from conceptual SoCT cosmology into a measurable research program centered on:

- SPARC age versus outer dark-matter-fraction analysis;
- effective-G / memory-kernel gravity formulation;
- PM simulation interpretation of void-filament expansion differentials;
- Pantheon+ environment-dependent H0 testing.

Working phenomenological model:

```math
G_eff(x,t) = G_0 [1 + alpha M(x,t)]
```

with a minimal memory accumulation form:

```math
M(t) = 1 - exp(-t/tau)
```

Primary observational tracks:

```text
SPARC: older systems -> higher outer f_DM
Pantheon+: H0_void > H0_filament
```

Claim boundary:

> This package is internal and pre-publication. It records modest empirical signals, simulation alignment, and locked pipeline logic, but does not claim confirmation of SoCT, PNT, or modified gravity.

Related scaffolds:

```text
data/README.md
data/sparc/README.md
data/pantheon/README.md
data/pantheon/covariance-notes.md
data/pantheon/environment-labels-schema.md
notebooks/README.md
notebooks/sparc_memory_fit_plan.md
notebooks/pantheon_environment_h0_fit_plan.md
```

### Literature-positioning note

The repo includes a literature-positioning note:

```text
references/consensus-pnt-soct-literature-positioning.md
```

This file preserves the current Consensus-based claim calibration for SoCT, SOC-MZI, PNT, and the PNT dark-energy track.

## OSF alignment

The OSF mapping file is preserved under:

```text
osf/OSF_PROJECT_MAP.md
```

Current OSF/repo alignment:

- **P1** — Memory-Field Gravity / SPARC / SoCT-PM
- **P2** — PNT Dark Energy / Hubble Window
- **P3** — Causal Inversion / Directional Memory Cosmology
- **P4** — CGDS / Observer-Dependent Decoherence / SOC-MZI
- **P5** — future SoCT comprehensive synthesis

## Proposed long-term repo structure

```text
Sequence-of-collapse-theory/
├─ README.md
├─ docs/
│  ├─ repo-map.md
│  ├─ source-corpus.md
│  ├─ theory-overview.md
│  ├─ book-of-collapse-article-map.md
│  └─ empirical-exploration-thread-summary-v0-1.md
├─ experiments/
│  ├─ README.md
│  └─ cosmology/
│     ├─ sparc-analysis-plan.md
│     └─ pantheon-environment-h0-test.md
├─ simulations/
│  └─ README.md
├─ references/
│  ├─ bibliography-and-validation-notes.md
│  └─ consensus-pnt-soct-literature-positioning.md
├─ osf/
│  ├─ OSF_PROJECT_MAP.md
│  ├─ p1-memory-field-gravity-sparc.md
│  ├─ p3-causal-inversion-directional-memory.md
│  └─ p4-cgds-observer-decoherence.md
├─ data/
│  ├─ README.md
│  ├─ sparc/
│  └─ pantheon/
├─ notebooks/
│  ├─ README.md
│  ├─ sparc_memory_fit_plan.md
│  └─ pantheon_environment_h0_fit_plan.md
├─ figures/              # future charts, diagrams, render-ready visuals
└─ papers/
   ├─ p1-memory-field-gravity-sparc/
   ├─ pnt-dark-energy-hubble-window/
   ├─ p3-causal-inversion-directional-memory/
   ├─ p4-observer-dependent-decoherence-cgds/
   └─ p5-soct-synthesis/          # future
```

## Next recommended additions

1. Add repo-backed OSF links after the OSF pages are updated.
2. Add reproducible SPARC derived tables and nonlinear memory-fit notebook.
3. Add Pantheon+ source notes, environment cross-match output, and covariance-aware H0 fitting notebook.
4. Add PM simulation parameter logs and H-split result summaries.
5. Add any existing simulation charts, CSVs, notebooks, or screenshots.
6. Add a reproducible PNT-EDE toy-model notebook corresponding to `toy-model-results-v0-1.md`.
7. Add SPARC radial-decomposition plan and results folder for the P1 empirical anchor paper.
8. Add physics-facing outlines for P1, P3, and P4.
9. Create the future P5 comprehensive synthesis folder.

## Status

Initial theory repo scaffold created and expanded.

This is a **documentation-first baseline** ready for further imports from project threads, local files, Google Drive, OSF, and future simulation outputs.

The P1, P2, P3, and P4 tracks now have a clearer repo/OSF alignment, with P2 holding the most developed working-paper package and P1/P3/P4 now established as structured hubs ready for draft imports.
