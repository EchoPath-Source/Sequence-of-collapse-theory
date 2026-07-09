# Papers Index — Sequence of Collapse Theory

This folder follows the canonical seven-paper publication sequence from the March 2026 SOC Publication Roadmap.

## Purpose

Use this area for manuscripts that are moving beyond exploratory notes into:

- structured paper drafts;
- submission-ready outlines;
- journal-targeted versions;
- appendices and supplementary methods;
- calculation notes tied to specific manuscripts;
- OSF-ready preregistration and supporting files.

Each paper folder should eventually include:

```text
README.md
working-draft.md or working-draft-vX-Y.md
figures/ or figure-notes.md
results/ or calculation-notes.md
references.md
status.md
REPRODUCIBILITY.md or EXPERIMENT_STATUS.md where applicable
```

## Repository-wide reproducibility and claim-boundary docs

```text
docs/reproducibility_checklist.md
docs/research_to_product_handoff.md
docs/claim_boundaries_for_products.md
```

Use these before translating any paper output into EchoGenesis, EchoPath, Vision Codex, or product-facing language.

## Canonical paper sequence

### P1 — Age-Dependent Galactic Rotation Curves as Evidence for a Spacetime Memory Field

Folder:

```text
papers/p1-age-dependent-rotation-curves-sparc/
```

Status: data in hand / write now.

Reproducibility/status:

```text
papers/p1-age-dependent-rotation-curves-sparc/REPRODUCIBILITY.md
data/SPARC_IMPORT_STATUS.md
```

Target: MNRAS or PRL.

### P2 — High-Redshift Disk Galaxies Do Not Require Dark Matter

Folder:

```text
papers/p2-high-redshift-time-dependent-gravity/
```

Status: published on Medium / import full text or PDF.

Target: astro-ph.GA -> MNRAS.

### P3 — Sequence of Collapse: From Concept to Equation

Folder:

```text
papers/p3-soc-concept-to-equation/
```

Status: published on Medium / import full text or PDF.

Target: quant-ph / Foundations of Physics.

### P4 — SOC-MZI-01: Awareness-Modulated Decoherence in Mach-Zehnder Interferometry

Folder:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/
```

Status: preregistered on OSF / needs full protocol import and lab collaboration.

Experiment status:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/EXPERIMENT_STATUS.md
```

Target: Nature Physics / PRL Registered Report path.

### P5 — Memory Field Density Variation and the Hubble Tension

Folder:

```text
papers/p5-hubble-tension-memory-gradient/
```

Status: outlined / write after P1.

Pantheon import status:

```text
data/PANTHEON_IMPORT_STATUS.md
```

Target: Astrophysical Journal Letters.

### P6 — Black Holes as Memory Compression Nodes

Folder:

```text
papers/p6-black-holes-memory-compression-nodes/
```

Status: outlined / write after P1 + P2 land.

Target: PRL / General Relativity and Gravitation.

### P7 — Sequence of Collapse: A Unified Framework for Quantum Mechanics, General Relativity, and Consciousness

Folder:

```text
papers/p7-unified-framework/
```

Status: foundation built / write last.

Target: Physical Review D / Reviews of Modern Physics.

## Support packages created before roadmap realignment

The following folders are preserved as supporting material rather than deleted:

```text
papers/p1-memory-field-gravity-sparc/
papers/pnt-dark-energy-hubble-window/
papers/p3-causal-inversion-directional-memory/
papers/p4-observer-dependent-decoherence-cgds/
papers/p5-soct-synthesis/
papers/math/
```

Mapping:

- `p1-memory-field-gravity-sparc/` supports canonical P1.
- `pnt-dark-energy-hubble-window/` supports canonical P5.
- `p3-causal-inversion-directional-memory/` supports canonical P6.
- `p4-observer-dependent-decoherence-cgds/` supports canonical P4.
- `p5-soct-synthesis/` is superseded by canonical P7 but preserved as earlier synthesis scaffold.
- `math/` supports canonical P3 and P7.

## Immediate import needs

1. P2 Medium article export / full text.
2. P3 Medium article export / full text.
3. P4 full SOC-MZI-01 preregistration protocol and appendices.
4. P1 SPARC analysis outputs, tables, plots, code, and confidence intervals.
5. SOC Research Agenda export if OSF agenda project is preserved.
6. P5 Pantheon+ SN table, covariance, environment labels, row-order validation, and derived diagnostic outputs.

## Current import principle

Only move material into canonical paper folders when it is:

- clearly sourced;
- separated from product/vision language;
- labeled as exploratory, draft, preregistered, or submission-facing;
- paired with methods/results where empirical claims are made.

## Grounding rule

Each paper draft should separate:

```text
Established references
Internal toy calculations
Preliminary results
Speculative mechanisms
Metaphysical interpretation
```

This separation is essential for external scientific credibility.

## Product boundary

Do not place EchoPath Memory Layer product claims, private kernel internals, or product roadmaps in the paper folders. Product impact can be mentioned only as bounded research impact notes and should pass through `docs/research_to_product_handoff.md` and `docs/claim_boundaries_for_products.md` first.
