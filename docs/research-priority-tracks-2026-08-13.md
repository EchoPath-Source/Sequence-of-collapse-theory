# SoCT Research Priority Tracks — 2026-08-13

**Status:** Active planning note  
**Purpose:** Preserve two newly identified research tracks before returning to the already-active DESI/Pantheon workflow.

## Context

Recent literature-positioning and discriminant work clarified two parallel tasks that should be preserved without displacing the existing empirical roadmap.

These are not replacements for the current DESI/Pantheon sequence. They are explicit follow-on tracks that strengthen SoCT's ability to distinguish itself from conventional and adjacent explanations.

---

## Track A — P1 Gravity Discrimination Sequence

### Goal

Move P1 beyond a simple age-versus-inferred-dark-fraction correlation and test whether formation history adds predictive information after strong conventional galaxy-dynamics baselines are already accounted for.

### Sequence

```text
derive/add g_bar
  -> fit the standard baryonic-acceleration baseline
  -> examine age/history residuals
  -> fit a fixed MOND-like benchmark
  -> fit a fixed halo benchmark
  -> cross-validation / out-of-sample comparison
  -> environment controls
```

### Scientific purpose

The key SoCT question is not merely:

> Do older galaxies show larger inferred mass discrepancies?

The stronger question is:

> Does independently measured formation history predict a stable residual after baryonic acceleration, structural variables, conventional halo behavior, MOND-like phenomenology, and environment are accounted for?

If the answer is no, the current P1 memory interpretation is weakened or constrained.

If the answer is yes and the residual survives preregistered controls and out-of-sample tests, SoCT gains a more distinctive empirical target.

### Required comparator ladder

1. **Baryons-only diagnostic** — useful but insufficient as a serious comparator.
2. **Baryonic / radial-acceleration baseline** — determine whether history adds information beyond the observed baryon-dynamics relation.
3. **Fixed MOND-like benchmark** — use a preregistered interpolation choice rather than per-galaxy tuning.
4. **Fixed halo benchmark** — use an explicit halo prescription and transparent priors.
5. **History-aware conventional model** — include assembly, surface brightness, morphology, gas fraction, stellar-population, and environment proxies where available.
6. **Candidate SoCT memory term** — evaluate only after the stronger baselines are established.

### Primary discriminant

The potentially distinctive SoCT signature is **history dependence at matched present-state conditions**.

A memory-field interpretation is more meaningful if two systems with similar present baryonic structure, acceleration scale, morphology, and environment retain a systematic difference associated with independently measured formation history.

### Repo support

```text
references/gravity-model-discriminants.md
papers/p1-age-dependent-rotation-curves-sparc/working-draft-v0-1.md
papers/p1-age-dependent-rotation-curves-sparc/REPRODUCIBILITY.md
observations/sparc/
PREDICTIONS.md
```

### Immediate next artifact when Track A resumes

Determine whether the current committed SPARC package already contains enough radial baryonic quantities to calculate `g_bar` consistently. If not, define the exact additional fields/source table needed before modifying the analysis pipeline.

---

## Track B — Theory Comparison & Failure Matrix

### Goal

Develop an academically conservative framework for comparing SoCT/PNT with major competing or adjacent research programs without converting literature adjacency into validation or promotional ranking.

### Core principle

The useful question is not:

> Which theory gets the highest subjective grade?

It is:

> What does each framework explain well, where does it stop, what distinctive predictions does it expose to failure, and what would SoCT have to demonstrate to outperform it in that domain?

### Proposed comparison dimensions

| Dimension | Evaluation question |
|---|---|
| Scope | How many major domains or open problems does the framework attempt to connect? |
| Novelty | Does it introduce a genuinely distinct mechanism or only reparameterize an existing one? |
| Formal maturity | Are governing equations, parameter meanings, conservation requirements, and limiting cases sufficiently defined? |
| Near-term testability | Can distinctive predictions be tested with existing datasets or laboratory technology? |
| Falsifiability / parameter economy | Can the framework fail cleanly without rescuing weak results through excessive parameter freedom? |
| Empirical support | How much independent observational or experimental evidence currently favors the framework? |

### Candidate comparison set

The matrix should eventually compare SoCT/PNT with at least:

- Lambda-CDM;
- particle dark matter / WIMP programs;
- MOND and relativistic MOND-like approaches;
- GRW / CSL objective-collapse models;
- Diósi-Penrose gravitational collapse;
- decoherence / quantum Darwinism;
- emergent / entropic gravity;
- holographic and emergent-spacetime programs;
- causal set theory;
- loop quantum gravity / loop quantum cosmology;
- string-theoretic quantum gravity;
- selected consciousness theories only where directly relevant to the observer-state channel.

Do not collapse distinct programs such as string theory and multiverse cosmology into one row merely for convenience.

### Required structure for each theory

Each comparison should include:

```text
Core mechanism:
Major empirical / conceptual successes:
Primary unresolved limitations:
Current testability:
Known falsification or constraint channels:
Where it overlaps SoCT:
Where it differs from SoCT:
What SoCT must outperform or explain better:
What evidence would favor the comparator over SoCT:
What evidence would favor SoCT over the comparator:
Current evidence status:
```

### Claim boundary

This matrix must not state that SoCT is already the "leading theory" on the basis of scope, novelty, or a composite grade.

The academically defensible positioning is:

> SoCT may be unusual among speculative unification programs in combining broad explanatory scope with several near-term falsification channels. Its current independent empirical support remains preliminary, so any claim of comparative leadership must be earned through successful discriminating tests against strong conventional and adjacent baselines.

### Why this matters

A scorecard becomes scientifically useful only when it separates:

```text
research architecture quality
from
empirical evidential standing
```

This prevents broad scope from being mistaken for confirmation and prevents mature but narrower theories from being downgraded simply because they do not attempt a total unification.

### Repo support

```text
references/adjacent-theories-map.md
references/collapse-decoherence-observer-discriminants.md
references/gravity-model-discriminants.md
references/consensus-pnt-soct-literature-positioning.md
```

### Immediate next artifact when Track B resumes

Create a first-pass `references/theory-comparison-failure-matrix.md` only after current empirical work is resumed and stabilized. The first version should prioritize comparison quality and failure criteria over letter grades.

---

## Relationship to the Existing Active Workflow

These two tracks are now preserved, but they do **not** supersede the current DESI/Pantheon sequence.

The active empirical workflow remains:

```text
DESI plan ✅
  -> data contract ✅
  -> notebook plan ✅
  -> DR1 resources verified ✅
  -> exact column semantics ✅
  -> smoke SQL ready ✅
  -> smoke execution
  -> estimator
  -> labels
  -> Pantheon+ crossmatch
  -> covariance-aware H0 test
```

Current gate:

> Execute the prepared DESI DR1 25-row smoke query against NOIRLab Data Lab and record the returned schema/provenance before scaling the query.

The two newly documented tracks should therefore be treated as preserved follow-ons rather than reasons to interrupt the smoke-query-to-H0 path.

---

## Priority Rule

Unless new evidence changes the ordering:

```text
1. Resume and complete the active DESI/Pantheon empirical workflow.
2. Return to Track A and strengthen P1 with g_bar + strong gravity baselines.
3. Build Track B Theory Comparison & Failure Matrix from the resulting empirical/discriminant state.
```

Track B should be informed by what SoCT can actually demonstrate, not only by what the architecture proposes.

---

## Claim-Discipline Rule

Across all three streams:

- adjacency is not validation;
- scope is not evidence;
- correlation is not mechanism;
- model fit is not uniquely identifying evidence;
- null results constrain parameter space and should not be reinterpreted as hidden support;
- competing theories must be represented at their strongest reasonable form;
- any eventual claim that SoCT is a leading framework should rest on comparative empirical performance, parameter economy, and successful out-of-sample predictions.
