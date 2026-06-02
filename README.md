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
- a canonical parameter ledger
- a dark-sector taxonomy
- an empirical exploration summary for the SPARC / effective-G / Pantheon+ phase
- a formal SOC localization-memory Hamiltonian scaffold
- parent-child directional-transfer simulation summaries
- data and notebook scaffolds for reproducible cosmology tests
- OSF companion text files
- paper/protocol hubs for P1, P2, P3, and P4

## Working core claims

1. **First Collapse**: light / photon-mediated decoherence begins the narrowing of possibility into structure.
2. **Second Collapse**: conscious observation finalizes experienced reality.
3. **Memory Field**: collapse events leave accumulated spacetime imprint, modeled as a memory field.
4. **SOC Localization-Memory Hamiltonian**: extension of standard Hamiltonian formalism with localization, memory coupling, and observer-state coupling.
5. **Cross-domain implication**: the theory propagates into cosmology, gravity, measurement theory, cognition, spatial computation, and experimental design.

## Current canonical equation scaffold

The current repo-facing Hamiltonian scaffold is:

```text
H_SOC = H_free + H_loc + lambda_M M(x,t) O_M + lambda_c Phi_c(x,t) O_c
```

with memory evolution:

```text
partial M / partial t = alpha C(x,t) - beta M(x,t) + D_M nabla^2 M
```

and collapse-intensity proxy:

```text
C(x,t) = A(x,t) |<Psi | O_c | Psi>|^2
```

Canonical file:

```text
papers/math/soc-localization-memory-hamiltonian.md
```

Claim boundary:

> This Hamiltonian is a formal scaffold for separating memory-field and observer-state hypotheses into testable channels. It does not prove the theory.

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

Simulation hub:

```text
simulations/parent-child-transfer/
```

Current simulation artifacts:

```text
simulations/parent-child-transfer/README.md
simulations/parent-child-transfer/real-space-bounce-transfer-v4-1.md
simulations/parent-child-transfer/kernel-robustness-summary.md
```

Current v4.1 simulation claim boundary:

> Real-space bounce-transfer toy models show robust directional inheritance across the tested kernel configurations, motivating multi-seed and null-model follow-up. This does not confirm physical parent-child universe transfer.

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
- quantum memory hysteresis;
- post-observation aftereffect tests;
- attention-state gradient tests;
- quantum brain-field coupling proposals.

### Dark-sector taxonomy

The current dark-sector taxonomy is preserved under:

```text
docs/dark-sector-taxonomy.md
```

Purpose:

> Keep ordinary matter, dark matter, dark energy, PNT prompt exhaust, memory residue, and parent-child inheritance distinct so the framework does not conflate separate mechanisms.

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

Primary observational tracks:

```text
SPARC: older systems -> higher outer f_DM
Pantheon+: H0_void > H0_filament
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
├─ PREDICTIONS.md
├─ docs/
│  ├─ repo-map.md
│  ├─ source-corpus.md
│  ├─ theory-overview.md
│  ├─ book-of-collapse-article-map.md
│  ├─ dark-sector-taxonomy.md
│  ├─ canonical-parameter-ledger.md
│  └─ empirical-exploration-thread-summary-v0-1.md
├─ experiments/
├─ simulations/
│  └─ parent-child-transfer/
├─ references/
├─ osf/
├─ data/
├─ notebooks/
├─ figures/
└─ papers/
   ├─ math/
   ├─ p1-memory-field-gravity-sparc/
   ├─ pnt-dark-energy-hubble-window/
   ├─ p3-causal-inversion-directional-memory/
   ├─ p4-observer-dependent-decoherence-cgds/
   └─ p5-soct-synthesis/
```

## Next recommended additions

1. Add repo-backed OSF links after the OSF pages are updated.
2. Add reproducible SPARC derived tables and nonlinear memory-fit notebook.
3. Add Pantheon+ source notes, environment cross-match output, and covariance-aware H0 fitting notebook.
4. Add PM simulation parameter logs and H-split result summaries.
5. Add parent-child transfer parameter logs, null-model definitions, and multi-seed outputs.
6. Add any existing simulation charts, CSVs, notebooks, or screenshots.
7. Add a reproducible PNT-EDE toy-model notebook corresponding to `toy-model-results-v0-1.md`.
8. Add SPARC radial-decomposition plan and results folder for the P1 empirical anchor paper.
9. Add physics-facing outlines for P1, P3, and P4.
10. Create the future P5 comprehensive synthesis folder.

## Status

Initial theory repo scaffold created and expanded.

This is a **documentation-first baseline** ready for further imports from project threads, local files, Google Drive, OSF, and future simulation outputs.

The P1, P2, P3, and P4 tracks now have a clearer repo/OSF alignment. P2 currently holds the most developed working-paper package, while P1/P3/P4 are structured hubs ready for draft imports, reproducible notebooks, and stronger validation artifacts.
