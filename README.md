# Sequence of Collapse Theory

A structured research repository for the **Sequence of Collapse (SoC / SoCT)** framework by Antoine L. Shephard.

## What SoCT proposes

The central SoCT hypothesis is:

> **Physical localization / collapse history may leave a persistent state that can influence later dynamics.**

The framework explores whether that generative principle can be made quantitative across several domains without requiring every proposed extension to succeed.

The current canonical scaffold separates ordinary dynamics, localization/environmental dynamics, a candidate persistent memory state, and a separately testable observer-state channel:

```math
H_SOC = H_0 + H_int + \lambda_M M(x,t) O_M + \lambda_c \Phi_c(x,t) O_c
```

with candidate memory evolution

```math
\partial_t M
= \alpha C_{obs}
- \beta M
+ D_M \nabla^2 M.
```

The observation foundations program is attempting to derive rather than assume the source `C_obs`.

A current candidate bridge is

```math
C_{obs}(x,t)=\kappa_{rec}\Gamma_{rec}(x,t),
```

so that

```math
\partial_t M
= \alpha_{rec}\Gamma_{rec}
- \beta M
+ D_M\nabla^2M,
```

where `\Gamma_rec` is a persistence-aware record-production rate and `\alpha_rec=\alpha\kappa_rec`.

This source law is a **versioned research hypothesis**, not established physics.

## What the repository is trying to determine

The repository is organized around three increasingly strong questions:

1. **Operational observation:** Can interaction, distinguishability, persistence, accessibility, and record production be given a substrate-independent quantitative description?
2. **SoCT memory:** Does record/localization history require an additional persistent physical state after complete ordinary state accounting?
3. **Cross-domain unification:** If such a state exists, do the quantum, gravitational, cosmological, and black-hole branches share quantitative laws or parameters rather than only a common analogy?

The third question is intentionally stronger than the first two. At present, **"collapse leaves memory" is a unifying research principle, not an empirically established unification law**. A genuine physical unification will require shared quantitative structure, parameter relations, or cross-domain predictions. If each domain ultimately requires unrelated mechanisms and freely independent parameters, the empirical unification claim fails even if individual models remain useful.

## Core claim boundaries

The repository does **not** currently establish that:

- observation causes objective wavefunction collapse;
- a new physical memory field exists in nature;
- gravity is produced by observation or consciousness;
- consciousness is necessary for ordinary physical observation;
- conscious access modifies quantum dynamics;
- the same memory variable has already been shown to govern quantum, galactic, cosmological, and black-hole behavior.

The scientific program is structured so these propositions can fail independently.

## Canonical architecture

```text
ordinary physics / observation foundations
interaction
  -> state-dependent correlation
  -> distinguishability
  -> accessible information
  -> retained / distributed record
  -> record-production functional Gamma_rec

candidate SoCT extension
Gamma_rec
  -> C_obs = kappa_rec Gamma_rec
  -> persistent state M
  -> decay / diffusion / propagation
  -> fixed feedback coupling
  -> history-dependent held-out prediction

separate downstream observer branch
accessible records
  -> recurrent / integrated processing
  -> recursive coupling accessibility
  -> observer-like organization
  -> conscious access? (independent empirical question)
```

This partition is important: the operational-observation program can survive if the additional `M` state is false, and the memory/gravity/cosmology branches do not depend on a positive consciousness result.

## Active empirical and mathematical tracks

### Memory-field gravity / galaxy dynamics

The SPARC track asks whether formation-history or age proxies correlate with inferred missing-mass structure after mass, morphology, surface-brightness, gas, and environmental controls.

A working phenomenological relation is

```math
G_{eff}(x,t)=G_0[1+\alpha M(x,t)].
```

This is a candidate effective model, not a demonstrated replacement for dark matter.

Primary locations:

```text
observations/sparc/
papers/p1-age-dependent-rotation-curves-sparc/
papers/p1-memory-field-gravity-sparc/
```

### Cosmology / environment-dependent expansion

The Pantheon+/PNT branch tests whether void/filament environment is associated with reproducible expansion-rate differences after standard cosmological and environmental controls.

Primary locations:

```text
papers/p5-hubble-tension-memory-gradient/
papers/pnt-dark-energy-hubble-window/
data/PANTHEON_IMPORT_STATUS.md
```

### Observation foundations

The operational observation program begins below consciousness.

Its current hierarchy is

```text
Level 0 — interaction
Level 1 — correlation
Level 2 — distinguishable information
Level 3 — retained physical record
Level 4 — downstream-accessible record
Level 5 — recurrent / recursively used record
Level 6 — conscious access, if separately operationalized
```

A provisional observation family is

```math
\Omega_{S\to O}=F(I_c,D,R,A_d),
```

and the current record-production work uses persistence-aware candidates such as

```math
\Gamma_{rec}=G(\partial_t I_{SO},R,A_d,\Xi_{irr}).
```

One versioned source model defines

```math
Q_{rec}=I_{acc}P_RR_d\Xi_{irr},
```

```math
\Gamma_{rec}^{(0.1)}=[\partial_tQ_{rec}]_+.
```

There is **not yet a universal threshold that turns decoherence into a record**. A record is operationally characterized by state-dependent accessible information plus specified persistence/accessibility criteria. Thresholds, when needed for a concrete experiment, must be preregistered relative to noise, timescale, and task rather than declared fundamental.

Canonical files:

```text
papers/math/soc-operational-observation-model.md
papers/math/soc-record-production-source-v0-1.md
docs/operational-observation-current-formulation.md
experiments/observation-foundations/
```

### SoCT memory discriminator

The first explicitly SoCT-specific distinction is not ordinary decoherence or record formation. Standard quantum dynamics already produces those.

The clean candidate discriminator is:

```text
matched explicitly modeled ordinary present state
+ different prior durable-record histories
+ fresh probe
-> reproducible history-dependent residual
```

Under H0/H1, a complete reset of all relevant ordinary degrees of freedom predicts no history-dependent fresh-probe residual.

Under the exploratory H2 model,

```math
\partial_tM=\alpha C_{obs}-\beta M+D_M\nabla^2M
```

and a predeclared probe coupling can produce a residual phase or other observable proportional to the surviving `M`.

SIM-04H demonstrated that this discriminator is recoverable **when synthetic data are generated from H2**, and that the extra model is not selected for exact-reset H0 synthetic data. This is methodology validation, not evidence that nature contains `M`.

SIM-04I then showed the central identifiability problem: an unobserved conventional reservoir with the same source/decay/diffusion/probe law can exactly mimic the H2 signal. Independent reset/environment diagnostics are therefore essential.

### Record erasure and irreversibility

Exact microscopic record creation followed by exact inverse evolution returns the ordinary record diagnostics to zero in the closed-system benchmark.

The current source hypothesis therefore weights durable/persistent record production rather than assuming every transient correlation creates physical `M`.

This gives a sharp empirical boundary:

> A fully erased ordinary record does not by itself count as evidence for persistent SoCT memory. SoCT-specific evidence would require a later residual after the relevant ordinary record-bearing degrees of freedom have been independently shown to be reset or bounded.

Whether even perfectly reversible transient record production can source `M` remains an open model choice and must not be decided retrospectively from a desired result.

### Observer emergence / Recursive Coupling

Observer emergence is a **partitioned downstream research track**, not a prerequisite for the gravity, cosmology, or lower-level observation work.

The current Recursive Coupling & Observer Formation (RCOF) hypothesis asks whether observer-like organization can be operationally characterized when records of previous internal-external coupling become causal inputs to future coupling.

```text
interaction
-> accessible relational record
-> coupling-history memory
-> recursive access
-> modification of future coupling
-> operational observer formation
```

This does not imply that recursive systems are conscious.

Canonical files:

```text
docs/research/recursive-coupling-observer-formation.md
papers/math/soc-observer-emergence-first-tuning-fork.md
papers/math/soc-observer-emergence-crossfeed-map.md
```

## Nested hypotheses

The observation/memory program uses the following separation:

```text
H0 — complete ordinary quantum/open-system dynamics
H1 — useful operational observation/record summary, no new physical state
H2 — additional persistent state M with fixed source/evolution/coupling laws
H3 — independently operationalized conscious-access contribution
```

Failure of H3 does not falsify H0-H2. Failure of H2 does not erase any standalone value of H1. The galaxy/cosmology branches must likewise be assessed on their own quantitative predictions.

## Current status of the observation simulation program

The README previously described the simulation ladder as if record erasure and memory feedback were still future work. That is now stale.

Current foundations work includes:

```text
qubit + pointer baselines
pointer + environment separation
record creation / exact erasure
redundancy / irreversibility tests
observation-derived source comparisons
explicit unitary record/decoherence benchmarks
complete reset-and-probe H0/H1/H2 benchmark (SIM-04H)
incomplete-reset / hidden-reservoir adversary (SIM-04I)
recursive-coupling / observer-formation path (new research branch)
```

The strongest present conclusion is methodological:

> Standard quantum/open-system dynamics explains interaction, decoherence, record formation, erasure, and redundancy. An additional persistent state is mathematically testable, but is neither empirically required nor uniquely identifiable until conventional hidden-state explanations are bounded.

## Falsification structure

SoCT should become more constrained as the program develops.

Examples:

- **Operational observation functional:** revise or abandon a proposed functional if it is coordinate/partition arbitrary, unstable under coarse-graining, or adds no useful compression beyond established measurement/information formalisms.
- **Persistent memory state:** reject it as necessary when ordinary hidden-state models of equal or lower complexity explain held-out history-dependent data.
- **Spatial memory propagation:** a fitted `D_M\to0` favors a simpler local reservoir over a propagating field.
- **Conscious-access channel:** a controlled null result constrains that channel without being treated as a falsification of unrelated gravity/cosmology branches.
- **Empirical unification:** if no shared quantitative structure, parameter relation, or cross-domain prediction can be derived, "collapse leaves memory" remains an organizing hypothesis rather than a demonstrated physical unification.

## Publication roadmap

The historical seven-paper roadmap remains useful as a project map, but paper claims must follow the evidence actually achieved in each branch:

1. P1 — age-dependent galactic rotation curves / SPARC
2. P2 — high-redshift disk galaxies / time-dependent gravity
3. P3 — SoCT concept-to-equation
4. P4 — controlled observer/conscious-access quantum test
5. P5 — memory-field variation / Hubble-tension track
6. P6 — black-hole memory-compression hypothesis
7. P7 — unified-framework synthesis

P7 is conditional: a strong unified-framework claim requires quantitative bridges rather than thematic similarity alone.

Canonical roadmap:

```text
docs/publication-roadmap-march-2026.md
```

## Repository map and audit

Current audit/reconciliation documents:

```text
docs/repo-audit-current-state.md
docs/repo-reconciliation-current-state.md
```

Prediction tracker:

```text
PREDICTIONS.md
```

Theory overview:

```text
docs/theory-overview.md
```

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
