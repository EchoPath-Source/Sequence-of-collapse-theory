# Sequence of Collapse Theory — Project Status

**Purpose:** provide a grounded snapshot of what exists, what is being tested, what remains speculative, and what should happen next.

This file should be updated whenever a major artifact, notebook, paper draft, simulation, or preregistration is added.

## Current position

SoCT/PNT is a broad theoretical and metaphysical research program exploring collapse, memory, gravity, consciousness, and cosmology. The repo now contains a documentation-first scaffold, formal notes, preregistration scaffolds, candidate empirical summaries, and toy-model cosmology artifacts.

The next credibility threshold remains reproducible empirical work, especially the SPARC age / missing-mass package and its new inner/outer radial-decomposition follow-up.

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
| SPARC reproducibility package scaffold | `observations/sparc/` | Present, needs runnable notebook and derived data |
| SPARC outer mass discrepancy analysis | `observations/sparc/results/outer_mass_discrepancy_analysis.md` | Candidate result note |
| SPARC inner/outer radial decomposition | `observations/sparc/results/inner_outer_radial_decomposition_summary.md` | Candidate radial-discriminator result |
| SPARC inner/outer correlation summary | `observations/sparc/results/inner_outer_correlation_summary.csv` | Machine-readable summary committed |
| PNT void-filament H0 mechanism | `papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md` | Calculated toy-model note |

## Highest-priority missing artifact

### SPARC reproducibility package completion

Target path:

```text
observations/sparc/
```

Required files:

```text
observations/sparc/
├─ sparc_age_dark_matter_analysis.ipynb
├─ data/
│  ├─ sparc_age_fdm_data.csv
│  └─ sparc_wise_inner_outer_fdm_split.csv
├─ results/
│  ├─ summary.json
│  ├─ correlation_table.csv
│  ├─ inner_outer_correlation_summary.csv
│  └─ bootstrap_results.csv
└─ figures/
   ├─ age_dm_full_sample.png
   ├─ age_dm_mass_bins.png
   └─ inner_outer_radial_decomposition.png
```

Goal:

> A visiting physicist should be able to run the notebook and reproduce the claimed age / dark-matter or missing-mass correlation and the inner/outer radial-decomposition result from documented inputs.

## Active workstreams

| Workstream | Current state | Next step |
|---|---|---|
| SPARC age / missing-mass analysis | Candidate empirical signal documented; reproducibility package scaffolded | Add derived CSV, notebook, results tables, controls, preregistration link |
| SPARC radial decomposition | Candidate radial-discriminator summary committed | Add full split dataset and notebook reproduction |
| SPARC environment/cosmic-web test | Motivated by weak central-brightness dependence | Cross-match with cosmic web / local density catalogs |
| Planck Memory Substrate | Formal doc added | Derive continuity equation or conservation-like relation for Engramon density |
| PNT dark-energy / Hubble tension | P2 package and void-filament toy model added | Add calculation scripts, Pantheon test, and working-paper integration |
| Observer-coupled decoherence | MZI protocol and simulation summary exist | Add preregistration-style protocol and simulation notebook |
| CMB directional memory / CIH | Conceptual and toy simulation packages identified | Derive specific axis/amplitude prediction before empirical claim |
| Gravitational-wave memory residuals | Long-term test identified | Define measurable residual signature and dataset |
| Philosophical foundations | Docs added | Keep separate from empirical claims; cite only as interpretive scaffolding |

## Scientific vs metaphysical status

### Scientific / empirical claims

These require datasets, equations, notebooks, and falsification conditions:

- galaxy age / missing-mass correlation,
- radial decomposition of memory-field-like effects,
- PNT dark-energy profile,
- Hubble tension / sound-horizon impact,
- void/filament H0 and dark-energy differential predictions,
- MZI observer-state decoherence test,
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
| SPARC radial result is color/proxy driven | Validate against alternate age/formation-history proxies and reproduce from code. |
| PNT/EDE toy models cannot reach required amplitude | Document honest constraints and use them to prune the model. |
| PNT void-filament H0 model is phenomenological | Derive `f_fail(delta)` physically and test against Pantheon/DESI rather than overclaiming. |
| Metaphysical claims overrun scientific framing | Keep metaphysical docs in `docs/` with status labels and avoid using them as empirical evidence. |

## Immediate next actions

1. Add the full derived SPARC inner/outer split CSV under `observations/sparc/data/`.
2. Add runnable `sparc_age_dark_matter_analysis.ipynb` when data and code are ready.
3. Add a notebook or script that regenerates `inner_outer_correlation_summary.csv`.
4. Add PNT void-filament H0 calculation script or notebook.
5. Add Pantheon+ environment-H0 implementation using full covariance.
6. Add PNT working paper draft under `papers/pnt-working-paper/` or continue integrating into `papers/pnt-dark-energy-hubble-window/`.
7. Add simulation scripts under `simulations/` with README files explaining assumptions and failures.

## Collaboration posture

Preferred public stance:

> This is an independent research program with speculative theory, explicit falsifiable predictions, candidate empirical artifacts, and a commitment to adversarial collaboration. The metaphysical architecture is documented separately from empirical claims.

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
