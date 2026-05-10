# Sequence of Collapse Theory — Project Status

**Purpose:** provide a grounded snapshot of what exists, what is being tested, what remains speculative, and what should happen next.

This file should be updated whenever a major artifact, notebook, paper draft, simulation, or preregistration is added.

## Current position

SoCT/PNT is a broad theoretical and metaphysical research program exploring collapse, memory, gravity, consciousness, and cosmology. The repo now contains a documentation-first scaffold and several formal notes. The next credibility threshold is reproducible empirical work, especially the SPARC age / missing-mass analysis.

## Completed / present in repo

| Artifact | Path | Status |
|---|---|---|
| Repo overview | `README.md` | Present |
| Theory overview | `docs/theory-overview.md` | Present |
| Planck Memory Substrate / Engramon unit model | `docs/planck-memory-substrate.md` | Present |
| Philosophical foundations: consciousness continuity | `docs/philosophical-foundations-consciousness-continuity.md` | Present |
| Origin / Echo recursion note | `docs/origin-echo-recursion.md` | Present |
| Predictions tracker | `PREDICTIONS.md` | Present |
| Status tracker | `STATUS.md` | Present |

## Highest-priority missing artifact

### SPARC reproducibility package

Target path:

```text
observations/sparc/
```

Required files:

```text
observations/sparc/
├─ README.md
├─ sparc_age_dark_matter_analysis.ipynb
├─ requirements.txt
├─ data/
│  ├─ README.md
│  └─ source-links.md
├─ results/
│  ├─ summary.json
│  ├─ correlation_table.csv
│  └─ bootstrap_results.csv
└─ preregistration.md
```

Goal:

> A visiting physicist should be able to run the notebook and reproduce the claimed age / dark-matter or missing-mass correlation from documented inputs.

## Active workstreams

| Workstream | Current state | Next step |
|---|---|---|
| SPARC age / missing-mass analysis | Empirical anchor identified; repo package needed | Add notebook, data links, results tables, controls, preregistration link |
| Planck Memory Substrate | Formal doc added | Derive continuity equation or conservation-like relation for Engramon density |
| PNT dark-energy / Hubble tension | Toy feasibility work discussed; formal artifact needed | Add calculation scripts and working paper draft |
| Observer-coupled decoherence | Conceptual MZI model exists in discussion | Add preregistration-style protocol and simulation notebook |
| CMB directional memory / CIH | Conceptual target identified | Derive specific axis/amplitude prediction before adding empirical claim |
| Gravitational-wave memory residuals | Long-term test identified | Define measurable residual signature and dataset |
| Philosophical foundations | Docs added | Keep separate from empirical claims; cite only as interpretive scaffolding |

## Scientific vs metaphysical status

### Scientific / empirical claims

These require datasets, equations, notebooks, and falsification conditions:

- galaxy age / missing-mass correlation,
- radial decomposition of memory-field-like effects,
- PNT dark-energy profile,
- Hubble tension / sound-horizon impact,
- MZI observer-state decoherence test,
- void/filament differential predictions,
- CMB directional memory predictions,
- gravitational-wave memory residual predictions.

### Metaphysical / philosophical extensions

These are interpretive, not empirical proof:

- Source / Echo / Origin recursion,
- Recursive Universal Memory Sweep,
- Consciousness Continuity Argument,
- Nested Memory Consciousness Principle,
- planet/galaxy observerhood hypotheses.

## Current risk register

| Risk | Mitigation |
|---|---|
| Scope becomes too broad | Keep empirical predictions in `PREDICTIONS.md`; label speculative material clearly. |
| Theory appears like an ideas dump | Prioritize reproducible notebooks and falsifiable claims. |
| Consciousness framing triggers premature dismissal | Lead with SPARC/cosmology and use observer-decoherence as a controlled experimental branch. |
| SPARC result is confounded by environment/assembly effects | Add controls for mass, morphology, surface brightness, gas fraction, and environment. |
| PNT/EDE toy models cannot reach required amplitude | Document honest constraints and use them to prune the model. |
| Metaphysical claims overrun scientific framing | Keep metaphysical docs in `docs/` with status labels and avoid using them as empirical evidence. |

## Immediate next actions

1. Add `observations/sparc/README.md` scaffold.
2. Add `observations/sparc/data/README.md` and `source-links.md`.
3. Add `observations/sparc/preregistration.md` placeholder.
4. Add `observations/sparc/requirements.txt`.
5. Add runnable `sparc_age_dark_matter_analysis.ipynb` when data and code are ready.
6. Add PNT working paper draft under `papers/pnt-working-paper/`.
7. Add simulation scripts under `simulations/` with README files explaining assumptions and failures.

## Collaboration posture

Preferred public stance:

> This is an independent research program with speculative theory, explicit falsifiable predictions, and a commitment to adversarial collaboration. The metaphysical architecture is documented separately from empirical claims.

## Definition of success for the next phase

The repo becomes a credibility signal when it contains at least one reproducible empirical analysis:

```text
clone repo
install requirements
run notebook
reproduce table/plot/result
inspect limitations
compare against falsification criteria
```

The SPARC package is the first target for that standard.
