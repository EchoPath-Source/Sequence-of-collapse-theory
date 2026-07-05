# SOC Outside Sharing Map

**Purpose:** Identify which repository files are best suited for different audiences  
**Claim level:** Communication guide only

---

## 1. For experimental physicists and lab collaborators

Start here:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md
papers/p4-soc-mzi-awareness-modulated-decoherence/materials-and-measures.md
papers/p4-soc-mzi-awareness-modulated-decoherence/statistical-analysis-plan.md
papers/p4-soc-mzi-awareness-modulated-decoherence/lab-collaboration-brief.md
```

Why:

- these files define the actual experimental question,
- clarify what success and failure look like,
- and keep the claim bounded to a rate-law test.

---

## 2. For theoretical physicists or mathematically inclined reviewers

Start here:

```text
docs/equations-and-testable-hypotheses.md
papers/p3-soc-concept-to-equation/P3-sequence-of-collapse-from-concept-to-equation.md
papers/math/soc-localization-memory-hamiltonian.md
papers/math/cce-master-equation-note.md
papers/p3-soc-concept-to-equation/derivation-note.md
```

Why:

- these files isolate the equation layer,
- show the distinction between phenomenology and derivation,
- and connect the minimal rate law to broader operator-level framing.

---

## 3. For general scientific readers

Start here:

```text
docs/scientist-brief-one-page.md
docs/equations-and-testable-hypotheses.md
papers/p3-soc-concept-to-equation/P3-sequence-of-collapse-from-concept-to-equation.md
```

Why:

- these files give a readable overview without requiring the full lab packet,
- and they avoid heavy metaphysical overhead.

---

## 4. For technically curious public readers

Start here:

```text
docs/scientist-brief-one-page.md
papers/p3-soc-concept-to-equation/P3-sequence-of-collapse-from-concept-to-equation.md
simulations/mzi-visibility-decay/model-summary.md
```

Why:

- these files explain the idea and the proposed tests at a digestible level,
- while still keeping the simulation and experiment boundaries explicit.

Do **not** start public readers with dense math scaffolds unless they ask for them.

---

## 5. Files to avoid sending as first contact

Avoid using these as the first thing you send unless the audience specifically wants them:

```text
papers/math/soc-localization-memory-hamiltonian.md
simulations/mzi-visibility-decay/SOC MZI Visibility Decay Simulation.py
papers/p3-soc-concept-to-equation/bibliography-notes.md
```

Reason:

- they are useful support files,
- but they are not the cleanest first impression.

---

## 6. Default outside-sharing packets

### Packet A — Scientist quick brief

```text
docs/scientist-brief-one-page.md
docs/equations-and-testable-hypotheses.md
papers/p4-soc-mzi-awareness-modulated-decoherence/lab-collaboration-brief.md
```

### Packet B — Theory review packet

```text
docs/equations-and-testable-hypotheses.md
papers/p3-soc-concept-to-equation/P3-sequence-of-collapse-from-concept-to-equation.md
papers/p3-soc-concept-to-equation/derivation-note.md
papers/math/cce-master-equation-note.md
```

### Packet C — Experiment packet

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md
papers/p4-soc-mzi-awareness-modulated-decoherence/materials-and-measures.md
papers/p4-soc-mzi-awareness-modulated-decoherence/statistical-analysis-plan.md
papers/p4-soc-mzi-awareness-modulated-decoherence/lab-collaboration-brief.md
```

---

## 7. Claim boundary reminder

For all outside sharing, the safest baseline phrasing is:

> The repository presents a testable observer-linked rate-law program and associated falsification paths.

Avoid sending the repo with language implying that the theory has already been confirmed.