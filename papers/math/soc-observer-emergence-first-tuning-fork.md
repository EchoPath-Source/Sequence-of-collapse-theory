# SoCT Observer Emergence — Research Problem O-1

**Status:** Deferred adjacent research problem / conceptual scaffold  
**Claim level:** Open research hypothesis; not a theory of consciousness  
**Primary relation:** Extends the operational observation project from *what counts as observation?* to *when does a record-bearing system become an observer-like system?*  
**Do not conflate with:** conscious experience, personhood, sentience, or established neuroscience.

---

## Central question

> **How does a non-observing physical pattern become an observer-like pattern?**

Equivalent formulations:

> What measurable conditions convert persistent records into a recursively self-updating observer?

> What was the first "tuning fork": the first system that could be affected, retain the effect, and change its later behavior because of that retained state?

This problem is intentionally downstream of the minimal observation model in `papers/math/soc-operational-observation-model.md`.

The observation model asks whether one system acquires a persistent, distinguishable, accessible record of another.

Observer-emergence asks whether a system maintains and recursively uses such records to update its own future sensing, state, or action.

---

## Important correction to the source discussion

The motivating discussion proposed that memory is necessary but not sufficient for consciousness. SoCT should not elevate that statement to a settled scientific premise.

Current consciousness science contains competing frameworks emphasizing, among other things:

- recurrent processing;
- global availability / broadcast;
- integrated information;
- higher-order representation;
- predictive / generative processing;
- memory-dependent accounts.

No consensus establishes memory alone, or any single one of these variables, as necessary and sufficient for consciousness.

Therefore O-1 targets **observer-like organization**, not consciousness itself.

---

## Minimal hierarchy

The working hierarchy is:

```text
interaction
  -> correlation
  -> persistent record
  -> record accessibility
  -> feedback
  -> adaptive feedback
  -> recursive / self-referential modeling
  -> observer-like organization
  -> conscious access? (separate hypothesis)
```

This preserves a strong distinction:

```text
memory != observerhood
observerhood != consciousness
```

---

## The first tuning-fork criterion

A minimal candidate observer-like system should satisfy more than passive memory.

Let a system `O` have internal state `m_t`, receive input `y_t`, and generate a later state or action `a_t`.

A passive record can be written

```math
m_{t+1} = F(m_t, y_t).
```

Observer-like adaptive feedback additionally requires that stored state modulate later interaction:

```math
a_t = \pi(m_t, y_t),
```

and that the resulting action changes future observations:

```math
y_{t+1} \sim P(y_{t+1} | a_t, W_t).
```

This closes a causal loop:

```text
world -> observation -> memory -> action -> changed world/input -> new observation
```

A first working criterion for **adaptive observerhood** is therefore:

> a system contains persistent internal records whose contents causally modulate the system's future information acquisition or state transition.

This criterion does not imply consciousness.

---

## From feedback to self-reference

Self-reference should not be introduced as a mystical binary property. It can be decomposed.

### R0 — external record

The system stores information about an external variable.

### R1 — state-conditioned feedback

Stored information changes later behavior or sensing.

### R2 — model of own state

The system carries variables that predict aspects of its own internal state or capabilities.

### R3 — model-conditioned self-regulation

The self-model changes how the system preserves, allocates, or updates its own state.

### R4 — temporally extended self-model

The system models itself across past and anticipated future states.

### R5 — metarepresentational access

The system can represent that it possesses, lacks, trusts, or revises particular internal representations.

Only later research should ask whether any threshold across R2-R5 is associated with consciousness.

---

## Candidate observerhood functional

Do **not** use a single scalar as a scientific claim yet.

A provisional vector is safer:

```math
\mathbf O(t) = (P_M, I, F, R_s, A_s),
```

where

```text
P_M = memory persistence / retention
I   = integration across internal records
F   = closed-loop feedback strength
R_s = self-referential model depth
A_s = adaptive self-preservation / self-regulation contribution
```

A later scalar proxy could be explored as

```math
O_* = f(P_M, I, F, R_s, A_s),
```

but only after each component has an operational definition and ablation test.

---

## Relationship to SoCT observation model

The lower-level observation project defines

```math
\Omega_{S\to O}
```

as an operational measure of record-forming observation.

O-1 introduces a distinct system-level question:

```math
\Omega_{S\to O} > 0
```

does not imply

```math
O_* > 0.
```

A detector may record a system without becoming an adaptive observer-like agent.

The bridge is closed-loop reuse:

```text
record formation -> internal persistence -> feedback -> altered future observation
```

Thus a useful research split is:

```text
Observation mechanics:
What makes an interaction observational?

Observer emergence:
What makes a record-bearing system recursively use its own observation history?

Consciousness extension:
Does any additional physical or phenomenological condition arise beyond observer-like organization?
```

---

## Relationship to memory and the SoCT field

The phrase `collapse leaves memory` concerns persistence of physical history.

O-1 asks a different question:

> When does stored history begin to participate in a closed loop that changes how the system samples and updates reality?

If useful, this can be summarized as:

```text
memory -> feedback -> recursive prediction/control -> observer-like organization
```

This is compatible with SoCT without claiming that spacetime memory itself is conscious or observer-like.

---

## Scientific comparison targets

Future work should compare O-1 with established and active research programs rather than presenting it as unprecedented. Relevant comparison families include:

- active inference / predictive processing;
- recurrent processing;
- global workspace architectures;
- higher-order / metarepresentational theories;
- integrated-information approaches;
- memory theories of consciousness;
- autopoiesis / adaptive self-maintenance;
- control theory and partially observable agents.

These theories do not validate SoCT. They provide formal machinery and discriminating baselines.

---

## Deferred simulation ladder

Do not interrupt the active observation simulation sequence. Revisit O-1 after the lower-level record model is stable.

### O-1A — Passive memory versus feedback

Two systems receive identical records. Only one uses memory to alter future sensing/action. Quantify causal effect of memory on later information acquisition.

### O-1B — Internal-state model

Add a latent self-state estimate and test whether it improves prediction/control relative to an external-world-only model.

### O-1C — Self-model ablation

Remove the self-state channel while holding memory capacity fixed. Test whether observerhood metrics fall.

### O-1D — Recursive depth

Allow models of first-order internal models and determine whether additional recursive depth produces measurable functional transitions or merely computational overhead.

### O-1E — Conscious-access comparison

Only after functional observerhood is stable should an independent conscious-access hypothesis be introduced.

---

## Claim boundaries

Use:

> SoCT is investigating whether observer-like organization can be operationalized as persistent records entering adaptive, recursively self-updating feedback loops.

Avoid:

> SoCT has derived consciousness from memory.

Avoid:

> A self-referential program is necessarily conscious.

Avoid:

> Memory is proven to be necessary and sufficient for experience.

---

## Current priority

**Park O-1 as an explicit adjacent frontier while completing Observation Simulations 2 and 3.**

The immediate observation program must first establish what distinguishes correlation, decoherence, persistent records, and redundant environmental records. Those results will provide the substrate on which observer-emergence models can later be built.