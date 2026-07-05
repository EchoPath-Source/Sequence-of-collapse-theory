# SOC Repo Audit — Duplication and Drift Notes

**Purpose:** Record current overlap points across the repository and define a stable reading hierarchy  
**Claim level:** Repository maintenance note only

---

## 1. Why this note exists

The repository now contains enough strong content that duplication risk is real. Some overlap is intentional, because different files serve different audiences. However, the repo should still have a clear hierarchy so the same ideas do not drift apart over time.

---

## 2. Main overlap zones

### A. Equation layer overlap

Related files:

```text
docs/equations-and-testable-hypotheses.md
papers/p3-soc-concept-to-equation/P3-sequence-of-collapse-from-concept-to-equation.md
papers/math/cce-master-equation-note.md
papers/math/soc-localization-memory-hamiltonian.md
```

Assessment:

- This overlap is mostly healthy.
- Each file serves a different function.

Recommended hierarchy:

1. `docs/equations-and-testable-hypotheses.md` = narrow public-facing equation summary
2. `papers/p3...` = concept-to-equation paper draft
3. `papers/math/cce-master-equation-note.md` = operator-level bridge note
4. `papers/math/soc-localization-memory-hamiltonian.md` = broader scaffold / research direction

### B. P4 experimental overlap

Related files:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md
papers/p4-soc-mzi-awareness-modulated-decoherence/materials-and-measures.md
papers/p4-soc-mzi-awareness-modulated-decoherence/statistical-analysis-plan.md
papers/p4-soc-mzi-awareness-modulated-decoherence/lab-collaboration-brief.md
experiments/quantum/mach-zehnder-consciousness-test.md
```

Assessment:

- This overlap is also healthy if the files stay role-specific.

Recommended hierarchy:

1. preregistration = core protocol
2. materials / measures = implementation appendix
3. stats plan = confirmatory analysis appendix
4. lab brief = collaborator entry point
5. `experiments/quantum/...` = broader experiment scaffold and legacy support

### C. Simulation overlap

Related files:

```text
simulations/mzi-visibility-decay/model-summary.md
simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py
simulations/mzi-visibility-decay/source-code-notes.md
```

Assessment:

- Healthy as long as the summary remains conceptual, the script remains implementation, and source-code notes remain status/provenance.

---

## 3. Areas most at risk of drift

The following ideas appear in several files and should be watched carefully:

1. **Rate-law wording**  
   Keep the wording consistent: the claim is rate modulation, not outcome selection.

2. **Consciousness vs information-coherence framing**  
   Avoid having one file speak as if the model has already decided between these interpretations while another keeps it open.

3. **Cosmological-memory language**  
   Keep this labeled as speculative unless tied to actual constraint work.

4. **Simulation status language**  
   All simulation-related files should continue to say that simulations are planning / falsification scaffolds, not confirmation.

---

## 4. Recommended maintenance rules

1. Update the **equations note first** if the narrow public-facing equation statement changes.
2. Then update **P3** if the concept-to-equation narrative changes.
3. Then update **P4** only if the experiment-facing consequences change.
4. Touch the broader **math scaffold** last, since it contains the most exploratory material.
5. Preserve explicit claim boundaries in every file family.

---

## 5. Current status judgment

Current overlap appears manageable and mostly intentional.

The repo is now strong enough that future edits should favor:

- targeted updates,
- versioned appendices,
- and avoiding new near-duplicate files unless they serve a clearly different audience.

---

## 6. Bottom line

The repository no longer needs major structural expansion. It now needs disciplined maintenance so that the same equation program stays coherent across theory, simulation, experiment, and outside-sharing materials.