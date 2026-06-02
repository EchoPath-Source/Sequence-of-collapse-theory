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

This initial setup organizes the theory into a clean research structure using existing project materials already available across the working corpus.

At this stage, the repo includes:

- a repo map
- a source corpus index
- a theory overview
- an article/book map
- an experiments hub
- a simulations hub
- validation and bibliography notes
- a PNT dark-energy / Hubble-window working paper package
- an empirical exploration summary for the SPARC / effective-G / Pantheon+ phase
- data and notebook scaffolds for reproducible cosmology tests

## Working core claims

1. **First Collapse**: light / photon-mediated decoherence begins the narrowing of possibility into structure.
2. **Second Collapse**: conscious observation finalizes experienced reality.
3. **Memory Field**: collapse events leave accumulated spacetime imprint, modeled as a memory field.
4. **Shephard-Mirrowen Hamiltonian**: extension of standard Hamiltonian formalism with memory coupling.
5. **Cross-domain implication**: the theory propagates into cosmology, gravity, measurement theory, cognition, spatial computation, and experimental design.

## Active research packages

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

### PNT dark energy / Hubble-window package

The first dedicated paper package has been added under:

```text
papers/pnt-dark-energy-hubble-window/
```

It currently includes:

- `working-draft-v0-1.md` — physics-first P2 paper skeleton for Planck Nucleation Theory as a two-timescale dark-energy model.
- `toy-model-results-v0-1.md` — summary of the prompt-exhaust / Early-Dark-Energy feasibility toy calculations.

Core conclusion of this package:

> PNT naturally separates into a short-lived prompt exhaust channel and a long-lived memory-residue channel. The prompt channel can produce an EDE-like transient but does not yet demonstrate full Hubble-tension resolution in minimal toy models. The late memory component is the stronger near-term publishable track, with predicted w(z) evolution and void-versus-filament differentials.

The repo also includes a literature-positioning note:

```text
references/consensus-pnt-soct-literature-positioning.md
```

This file preserves the current Consensus-based claim calibration for SoCT, SOC-MZI, PNT, and the PNT dark-energy track.

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
   └─ pnt-dark-energy-hubble-window/
      ├─ working-draft-v0-1.md
      └─ toy-model-results-v0-1.md
```

## Next recommended additions

1. Add OSF preregistration text and links.
2. Add reproducible SPARC derived tables and nonlinear memory-fit notebook.
3. Add Pantheon+ source notes, environment cross-match output, and covariance-aware H0 fitting notebook.
4. Add PM simulation parameter logs and H-split result summaries.
5. Add any existing simulation charts, CSVs, notebooks, or screenshots.
6. Split the theory into publication-ready paper folders:
   - foundational theory
   - mathematical formalization
   - cosmology / gravity
   - consciousness experiments
7. Add a reproducible PNT-EDE toy-model notebook corresponding to `toy-model-results-v0-1.md`.
8. Add a SPARC radial-decomposition plan and results folder for the P1 empirical anchor paper.

## Status

Initial theory repo scaffold created.
This is a **documentation-first baseline** ready for further imports from project threads, local files, Google Drive, OSF, and future simulation outputs.

The first PNT/P2 package has now been added to preserve the two-timescale dark-energy framing, toy-model conclusions, and literature-positioning guidance.

The empirical exploration package now preserves the SPARC / effective-G / PM / Pantheon+ phase as an internal pre-publication research synthesis with data and notebook scaffolds for reproducibility.
