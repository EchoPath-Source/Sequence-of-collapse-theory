# Sequence of Collapse Theory — Project Status

**Purpose:** provide a grounded snapshot of what exists, what is being tested, what remains speculative, and what should happen next.

This file should be updated whenever a major artifact, notebook, paper draft, simulation, or preregistration is added.

## Current position

SoCT/PNT is a broad theoretical and metaphysical research program exploring collapse, memory, gravity, consciousness, and cosmology. The repo now contains roadmap documents, formal notes, preregistration scaffolds, candidate empirical summaries, runnable analysis support, paper-local result tables, toy-model cosmology artifacts, and clear audit/reconciliation documents.

The next credibility threshold remains reproducible empirical work, especially the SPARC age / missing-mass package and its inner/outer radial-decomposition follow-up.

## Completed / present in repo

| Artifact | Path | Status |
|---|---|---|
| Repo overview | `README.md` | Present |
| Current reconciliation | `docs/repo-reconciliation-current-state.md` | Present / newest repo-state map |
| Current audit | `docs/repo-audit-current-state.md` | Present |
| Theory overview | `docs/theory-overview.md` | Present |
| Planck Memory Substrate / Engramon unit model | `docs/planck-memory-substrate.md` | Present |
| Philosophical foundations: consciousness continuity | `docs/philosophical-foundations-consciousness-continuity.md` | Present |
| Origin / Echo recursion note | `docs/origin-echo-recursion.md` | Present |
| Predictions tracker | `PREDICTIONS.md` | Present |
| Status tracker | `STATUS.md` | Present |
| SPARC reproducibility package | `observations/sparc/` | Present; derived data, manifests, result summaries, and runnable script support are present; `.ipynb` notebook remains optional/missing by exact filename |
| SPARC runnable script | `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py` | Present / paper-local reproducibility artifact |
| SPARC notebook-path wrapper | `notebooks/sparc/sparc_age_fdm_analysis.py` | Present / compatibility wrapper |
| SPARC older script path | `notebooks/sparc/sparc_age_dm_analysis.py` | Present / retained for compatibility |
| SPARC outer mass discrepancy analysis | `observations/sparc/results/outer_mass_discrepancy_analysis.md` | Candidate result note |
| SPARC inner/outer radial decomposition | `observations/sparc/results/inner_outer_radial_decomposition_summary.md` | Candidate radial-discriminator result |
| SPARC inner/outer correlation summary | `observations/sparc/results/inner_outer_correlation_summary.csv` | Machine-readable summary committed |
| SPARC reproducibility manifest | `observations/sparc/results/reproducibility-manifest.md` | Present / maps inputs, scripts, outputs, and remaining gaps |
| P1 SPARC imported result CSVs | `papers/p1-age-dependent-rotation-curves-sparc/results/` | Candidate correlation, partial-correlation, regression, mass-proxy, and bootstrap CSVs committed |
| SPARC figure provenance | `figures/sparc/figure-provenance.md` | Present / updated with imported and script-generated figure paths |
| PNT void-filament H0 mechanism | `papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md` | Calculated toy-model note |
| PNT void-filament visualization | `simulations/pnt_hubble_void/pnt_hubble_void.jsx`; `visualizations/pnt_hubble_void.jsx` | Present / simulation and visualization copy |
| SOC-MZI visibility-decay simulation | `simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py`; `papers/p4-soc-mzi-awareness-modulated-decoherence/simulations/soc_mzi_visibility_decay_simulation.py` | Present / runnable simulation support |
| Pantheon+ source-input documentation | `data/pantheon/README.md`; `data/pantheon/covariance-notes.md`; `data/pantheon/environment-labels-schema.md` | Present / environment-label table still missing |

## Highest-priority remaining artifact

### Pantheon+ environment-label table

Current highest-priority missing derived artifact:

```text
data/pantheon/environment_labels.csv
```

Purpose:

> Enable the Pantheon+ environment-H0 test to move from scaffold/source-input documentation to a real covariance-aware void/filament analysis.

Required before any Pantheon+ environment-H0 claim:

1. locked environment-label methodology;
2. source/provenance for void/filament catalog;
3. row alignment to Pantheon+SH0ES table;
4. validation counts for void / filament / unclassified;
5. no threshold tuning after inspecting `Delta_H0`.

## SPARC package status

The SPARC/P1 package is no longer merely scaffolded.

Present:

```text
observations/sparc/data/sparc_age_fdm_data.csv
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
observations/sparc/results/inner_outer_correlation_summary.csv
observations/sparc/results/outer_mass_discrepancy_analysis.md
observations/sparc/results/inner_outer_radial_decomposition_summary.md
observations/sparc/results/reproducibility-manifest.md
papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_partial_correlations.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_regression_models.csv
papers/p1-age-dependent-rotation-curves-sparc/results/mass_proxy_comparison.csv
papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_binned_bootstrap.csv
figures/sparc/figure-provenance.md
```

Still useful but not blocking:

```text
observations/sparc/sparc_age_dark_matter_analysis.ipynb  [missing by exact notebook filename]
figures/sparc/SPARC_age_vs_fdm_scatter.png              [missing by exact filename; current mapping points to script-generated sparc_age_fdm_scatter.png]
```

Interpretation:

> The script-driven SPARC workflow and P1 result tables are present. A full `.ipynb` notebook remains optional/missing by exact filename, but the status should no longer imply that the P1 tables or runnable script are absent.

## Active workstreams

| Workstream | Current state | Next step |
|---|---|---|
| SPARC age / missing-mass analysis | Candidate empirical signal documented; derived CSVs, paper-local P1 result CSVs, runnable script support, and provenance manifests present | Run/verify script outputs against committed result tables; add optional `.ipynb` if desired |
| SPARC radial decomposition | Candidate radial-discriminator summary and full split dataset committed | Add/verify reproduction script for inner/outer correlation summary and outlier/leverage diagnostics |
| SPARC environment/cosmic-web test | Motivated by weak central-brightness dependence | Cross-match with cosmic web / local density catalogs |
| Pantheon+ environment-H0 | Source-input documentation and schema present; environment labels missing | Create/import `data/pantheon/environment_labels.csv` with locked methodology |
| Planck Memory Substrate | Formal doc added | Derive continuity equation or conservation-like relation for Engramon density |
| PNT dark-energy / Hubble tension | P5 package and void-filament toy model added | Add calculation scripts/notebook and integrate into working-paper text |
| Observer-coupled decoherence | MZI protocol and runnable visibility-decay simulation exist | Add protocol index and generated simulation outputs/figures |
| CMB directional memory / CIH | Conceptual and toy simulation packages identified | Derive specific axis/amplitude prediction before empirical claim |
| Gravitational-wave memory residuals | Long-term test identified | Define measurable residual signature and dataset |
| Philosophical foundations | Docs added | Keep separate from empirical claims; cite only as interpretive scaffolding |

## Scientific vs metaphysical status

### Scientific / empirical claims

These require datasets, equations, notebooks/scripts, and falsification conditions:

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
| Theory appears like an ideas dump | Prioritize reproducible scripts/notebooks and falsifiable claims. |
| Consciousness framing triggers premature dismissal | Lead with SPARC/cosmology and use observer-decoherence as a controlled experimental branch. |
| SPARC result is confounded by environment/assembly effects | Add controls for mass, morphology, surface brightness, gas fraction, and environment. |
| SPARC radial result is color/proxy driven | Validate against alternate age/formation-history proxies and reproduce from code. |
| PNT/EDE toy models cannot reach required amplitude | Document honest constraints and use them to prune the model. |
| PNT void-filament H0 model is phenomenological | Derive `f_fail(delta)` physically and test against Pantheon/DESI rather than overclaiming. |
| Static figures are mistaken for evidence | Use `figures/sparc/figure-provenance.md`; cite data + code, not screenshots alone. |
| Metaphysical claims overrun scientific framing | Keep metaphysical docs in `docs/` with status labels and avoid using them as empirical evidence. |

## Immediate next actions

1. Create or import `data/pantheon/environment_labels.csv` with locked provenance and validation rules.
2. Run/verify `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py` and compare generated outputs to paper-local P1 tables.
3. Add optional `observations/sparc/sparc_age_dark_matter_analysis.ipynb` if a notebook interface is needed for outside reviewers.
4. Add/verify a radial-decomposition reproduction script for `inner_outer_correlation_summary.csv`.
5. Add PNT void-filament H0 calculation script or notebook.
6. Add generated SOC-MZI simulation outputs/figures and a P4 protocol index.
7. Keep all output labels conservative: source, candidate result, reproducibility artifact, preregistration, simulation, or speculative/theory.

## Collaboration posture

Preferred public stance:

> This is an independent research program with speculative theory, explicit falsifiable predictions, candidate empirical artifacts, runnable analysis support, and a commitment to adversarial collaboration. The metaphysical architecture is documented separately from empirical claims.

## Definition of success for the next phase

The repo becomes a credibility signal when at least one empirical analysis can be reproduced by an outside reviewer:

```text
clone repo
install requirements
run script or notebook
reproduce table/plot/result
inspect limitations
compare against falsification criteria
```

The SPARC package is the first target for that standard, and it is now close enough that the priority is verification, not initial scaffolding.
