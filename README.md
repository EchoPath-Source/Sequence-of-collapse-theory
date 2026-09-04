# Sequence of Collapse Theory

## Current repository audit

Current empirical/theory repository audit and reconciliation documents are available at:

```text
docs/repo-audit-current-state.md
docs/repo-reconciliation-current-state.md
```

A structured research repository for the **Sequence of Collapse (SoC / SoCT)** framework by Antoine L. Shephard.

## Core positioning

> **SoCT asks whether one generative principle — collapse leaves memory — can connect quantum-to-classical transition, gravitational memory, cosmological structure, black-hole information, and conscious observation without sacrificing falsifiability.**

The stronger research formulation is:

> **SoCT is compelling because it offers a single generative pattern — collapse leaves memory — that naturally links quantum-to-classical transition, gravitational memory, cosmological structure, black-hole information, and conscious observation, while producing distinct falsifiable empirical tracks.**

This is a research-program statement, not a claim that every proposed connection has been established. The individual tracks must stand or fail on their own empirical and mathematical tests. In particular, the observer/consciousness channel is separable from the gravitational, cosmological, and black-hole tracks: failure of one extension does not by itself establish or refute every other SoCT hypothesis.

This repo is intended to become the central home for:

- core theory documents
- mathematical frameworks
- experimental proposals
- simulation notes and validation logs
- literature/references
- OSF-linked preregistrations and study drafts
- future datasets, notebooks, figures, and publication-ready papers

## Active Observation and Observer-Emergence Program

A new foundational program now asks two deliberately separate questions.

### O-0 — Operational Observation

> **What is the minimum physical transformation necessary for one system to count as having observed another?**

The working hierarchy is:

```text
interaction
  -> state-dependent correlation
  -> distinguishability
  -> physical record
  -> record persistence
  -> downstream accessibility
  -> operational observation
```

The goal is to derive the currently phenomenological observation/collapse source variables from ordinary quantum interaction and information-bearing record formation rather than assuming a conscious observer at the start.

Canonical files:

```text
papers/math/soc-operational-observation-model.md
papers/math/soc-localization-memory-hamiltonian.md
papers/math/soc-observation-to-spacetime-derivation-ladder.md
```

The intended derivation chain is:

```text
quantum state
  -> interaction Hamiltonian H_int
  -> correlated state rho_SO
  -> distinguishability / accessible information
  -> observation functional Omega or record-production rate Gamma_rec
  -> SoCT source C_obs
  -> memory field M
  -> candidate memory feedback
  -> candidate covariant spacetime response
```

Only the first portion is standard quantum/information-theoretic machinery. The steps from record production to persistent SoCT memory and from memory to spacetime response remain hypotheses to derive and test.

### O-1 — Observer Emergence / "First Tuning Fork"

> **What measurable conditions convert persistent records into a recursively self-updating, observer-like system?**

This track is intentionally downstream of O-0. It does not equate memory, observerhood, or consciousness.

Working ladder:

```text
record
  -> persistence
  -> feedback
  -> adaptive feedback
  -> integrated state/history
  -> recursive self-modeling
  -> self-maintaining observer-like organization
  -> conscious access? (separate empirical question)
```

Canonical file:

```text
papers/math/soc-observer-emergence-first-tuning-fork.md
```

This program is expected to support P3 (concept to equation), P4 (observer/conscious-access tests), and P7 (unified framework) while preserving nested falsifiability.

### Observation simulation ladder

```text
simulations/observation-qubit-pointer/
simulations/observation-qubit-pointer-environment/
simulations/observation-record-erasure/
```

Current status:

- Simulation 1: qubit + pointer baseline — implemented.
- Simulation 2: qubit + pointer + environment — implemented; demonstrates that environmental decoherence and a designated pointer record can be varied separately.
- Simulation 3: record creation / erasure — active next gate.
- Simulation 4: history-matched memory feedback — planned first explicitly SoCT-specific discriminator.
- Simulation 5: conscious-access layer — deferred until lower-level physical observation variables are stable.

Claim boundary:

> These simulations validate definitions and mechanism separation inside toy quantum models. They do not establish a new physical memory field, consciousness-driven collapse, or an observation-derived spacetime theory.

## Research-to-product boundary

SoCT provides theoretical primitives, empirical hypotheses, experimental proposals, mathematical scaffolds, and publication tracks that may inspire EchoGenesis architecture and EchoPath research directions. SoCT does not directly certify product claims.

Any product-facing use of SoCT concepts must pass through a claim-boundary filter, reproducibility review, and architecture handoff before appearing in public marketing or product documentation.

Canonical boundary docs:

```text
docs/research_to_product_handoff.md
docs/claim_boundaries_for_products.md
docs/reproducibility_checklist.md
```

Product-safe translation principle:

```text
SoCT research source
  -> reproducibility status
  -> claim boundary
  -> EchoGenesis architecture handoff
  -> product-safe translation
  -> Vision Codex positioning
```

Product repos may use engineering terms like adaptive memory, spatial memory, field-inspired routing, persistence, replay-derived tuning, and topology-aware diagnostics when those features are actually implemented. They should not claim proven new physics, consciousness-driven collapse, dark matter replacement, or experimentally confirmed memory fields unless the corresponding empirical track has been reproduced and documented.

## Canonical publication roadmap

The repository is now aligned to the March 2026 **SOC Publication Roadmap**, which defines a seven-paper publication sequence:

1. **P1 — Age-Dependent Galactic Rotation Curves as Evidence for a Spacetime Memory Field**
2. **P2 — High-Redshift Disk Galaxies Do Not Require Dark Matter**
3. **P3 — Sequence of Collapse: From Concept to Equation**
4. **P4 — SOC-MZI-01: Awareness-Modulated Decoherence in Mach-Zehnder Interferometry**
5. **P5 — Memory Field Density Variation and the Hubble Tension**
6. **P6 — Black Holes as Memory Compression Nodes**
7. **P7 — Sequence of Collapse: A Unified Framework for Quantum Mechanics, General Relativity, and Consciousness**

Canonical roadmap summary:

```text
docs/publication-roadmap-march-2026.md
```

Papers index:

```text
papers/README.md
```

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

The observation program treats `A(x,t)` and `C(x,t)` as derivation targets. The current working bridge is to derive an operational observation functional `Omega` and/or record-production rate `Gamma_rec` from the quantum interaction, then test whether either can legitimately source the SoCT memory variable.

Claim boundary:

> This Hamiltonian is a formal scaffold for separating memory-field and observer-state hypotheses into testable channels. It does not prove the theory.

## Canonical paper folders

### P1 — Age-Dependent Galactic Rotation Curves / SPARC

```text
papers/p1-age-dependent-rotation-curves-sparc/
```

Roadmap status: data in hand / write now.

Reproducibility/status docs:

```text
data/SPARC_IMPORT_STATUS.md
papers/p1-age-dependent-rotation-curves-sparc/REPRODUCIBILITY.md
```

Support folder:

```text
papers/p1-memory-field-gravity-sparc/
```

### P2 — High-Redshift Disk Galaxies & Time-Dependent Gravity

```text
papers/p2-high-redshift-time-dependent-gravity/
```

Roadmap status: published on Medium / import full text or PDF.

### P3 — SOC: From Concept to Equation

```text
papers/p3-soc-concept-to-equation/
```

Roadmap status: published on Medium / import full text or PDF.

Related math scaffold:

```text
papers/math/
```

The O-0 operational-observation program and O-1 observer-emergence program are now core mathematical support tracks for P3.

### P4 — SOC-MZI-01 Pre-Registration Protocol

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/
```

Roadmap status: pre-registered on OSF / full protocol import needed.

Experiment status:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/EXPERIMENT_STATUS.md
```

Support folder:

```text
papers/p4-observer-dependent-decoherence-cgds/
```

P4 should treat conscious-access effects as downstream of matched physical observation/record variables defined by O-0.

### P5 — Hubble Tension as Memory Field Gradient

```text
papers/p5-hubble-tension-memory-gradient/
```

Roadmap status: outlined / write after P1.

Pantheon import/status doc:

```text
data/PANTHEON_IMPORT_STATUS.md
```

DESI environment-query support:

```text
papers/p5-hubble-tension-memory-gradient/DESI_ENVIRONMENT_QUERY_PLAN.md
```

Support package:

```text
papers/pnt-dark-energy-hubble-window/
```

### P6 — Black Holes as Memory Compression Nodes

```text
papers/p6-black-holes-memory-compression-nodes/
```

Roadmap status: outlined / write after P1 + P2 land.

Support folder:

```text
papers/p3-causal-inversion-directional-memory/
```

Simulation support:

```text
simulations/parent-child-transfer/
```

### P7 — Sequence of Collapse Unified Framework

```text
papers/p7-unified-framework/
```

Roadmap status: foundation built / write last.

Superseded synthesis scaffold preserved for reference:

```text
papers/p5-soct-synthesis/
```

O-0, the observation-to-spacetime derivation ladder, and O-1 are expected to provide part of the quantum-to-observer-to-memory structure needed before P7 can claim a coherent unified mathematical narrative.

## Active support packages

### Dark-sector taxonomy

```text
docs/dark-sector-taxonomy.md
```

Purpose:

> Keep ordinary matter, dark matter, dark energy, PNT prompt exhaust, memory residue, and parent-child inheritance distinct so the framework does not conflate separate mechanisms.

### Empirical exploration package

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

```text
references/consensus-pnt-soct-literature-positioning.md
```

This file preserves the current claim calibration for SoCT, SOC-MZI, PNT, and the PNT dark-energy track.

### Adjacent research threads

SoCT is positioned as a speculative but falsifiable framework adjacent to objective-collapse theories, Penrose/Diósi-Penrose gravitational collapse proposals, Orch OR, ER=EPR, black-hole information preservation, gravitational memory effects, holography, emergent spacetime, and cosmic-web dark-sector phenomenology.

These fields do not validate SoCT, but they define the research neighborhood in which SoCT can be compared, constrained, or falsified.

```text
references/adjacent-theories-map.md
```

### Discriminating comparison scaffolds

The adjacency map is paired with two research-facing discriminator matrices:

```text
references/collapse-decoherence-observer-discriminants.md
references/gravity-model-discriminants.md
```

The first separates standard decoherence, GRW/CSL-like objective collapse, gravity-related collapse, and the current SoCT observer-state channel. The second compares Lambda-CDM/halo interpretations, MOND-like phenomenology, emergent-gravity proposals, and the current SoCT history-dependent memory-field hypothesis.

These files are intended to define what would actually distinguish SoCT from neighboring explanations. They are not evidence that SoCT has already passed those tests.

## OSF alignment

The OSF mapping file is preserved under:

```text
osf/OSF_PROJECT_MAP.md
```

Roadmap-canonical OSF projects:

- `SOC-P1: Age-Dependent Rotation Curves`
- `SOC-P2: High-Redshift Time-Dependent Gravity`
- `SOC-P3: SOC Concept to Equation`
- `SOC-MZI-01: Pre-Registration Protocol`
- `SOC-AGENDA: Research Agenda`
- `SOC-P5: Hubble Tension Memory Gradient`
- `SOC-P7: Unified Framework Working Paper`

## Proposed long-term repo structure

```text
Sequence-of-collapse-theory/
├─ README.md
├─ PREDICTIONS.md
├─ docs/
│  ├─ publication-roadmap-march-2026.md
│  ├─ repo-map.md
│  ├─ source-corpus.md
│  ├─ theory-overview.md
│  ├─ book-of-collapse-article-map.md
│  ├─ dark-sector-taxonomy.md
│  ├─ canonical-parameter-ledger.md
│  ├─ empirical-exploration-thread-summary-v0-1.md
│  ├─ research_to_product_handoff.md
│  ├─ claim_boundaries_for_products.md
│  └─ reproducibility_checklist.md
├─ experiments/
├─ simulations/
│  ├─ observation-qubit-pointer/
│  ├─ observation-qubit-pointer-environment/
│  ├─ observation-record-erasure/
│  └─ parent-child-transfer/
├─ references/
├─ osf/
├─ data/
│  ├─ SPARC_IMPORT_STATUS.md
│  └─ PANTHEON_IMPORT_STATUS.md
├─ notebooks/
├─ figures/
└─ papers/
   ├─ README.md
   ├─ math/
   │  ├─ soc-operational-observation-model.md
   │  ├─ soc-observation-to-spacetime-derivation-ladder.md
   │  └─ soc-observer-emergence-first-tuning-fork.md
   ├─ p1-age-dependent-rotation-curves-sparc/
   ├─ p2-high-redshift-time-dependent-gravity/
   ├─ p3-soc-concept-to-equation/
   ├─ p4-soc-mzi-awareness-modulated-decoherence/
   ├─ p5-hubble-tension-memory-gradient/
   ├─ p6-black-holes-memory-compression-nodes/
   └─ p7-unified-framework/
```

## Support folders retained from earlier scaffold

The following folders are intentionally preserved rather than deleted:

```text
papers/p1-memory-field-gravity-sparc/
papers/pnt-dark-energy-hubble-window/
papers/p3-causal-inversion-directional-memory/
papers/p4-observer-dependent-decoherence-cgds/
papers/p5-soct-synthesis/
```

These now function as support packages for the canonical P1, P5, P6, P4, and P7 tracks respectively.

## Immediate import needs

Tracked import/status docs now preserve the immediate needs:

1. P2 Medium article export / full text.
2. P3 Medium article export / full text.
3. P4 full SOC-MZI-01 preregistration protocol and appendices — see `papers/p4-soc-mzi-awareness-modulated-decoherence/EXPERIMENT_STATUS.md`.
4. P1 SPARC analysis outputs, tables, plots, code, and confidence intervals — see `data/SPARC_IMPORT_STATUS.md` and `papers/p1-age-dependent-rotation-curves-sparc/REPRODUCIBILITY.md`.
5. SOC Research Agenda export if the OSF agenda project is preserved.
6. Pantheon+ SN table, covariance, and environment-label imports for P5 — see `data/PANTHEON_IMPORT_STATUS.md`.

## Status

Initial theory repo scaffold created and expanded.

The repository is now realigned to the March 2026 seven-paper publication roadmap while preserving earlier PNT, causal-inversion, CGDS, synthesis scaffold work, and the active Observation / Observer-Emergence mathematical program as supporting research infrastructure.
