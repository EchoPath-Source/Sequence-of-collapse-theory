# EchoForm Persistent-Agent Architecture

## Purpose

This note records an engineering application of the observer-emergence research program without converting the scientific work into a consciousness claim.

The observer-emergence simulations ask which functional ingredients distinguish passive records from persistent, recursively self-updating systems. Even if those benchmarks never establish observer emergence in a strong scientific sense, the same discriminators can inform the construction of persistent NPCs and EchoForms.

The engineering target is therefore deliberately narrower:

> Build history-conditioned artificial characters whose durable memories, self-state estimates, predictive models, and continuation-sensitive policies causally affect future behavior.

No claim of consciousness, phenomenology, intrinsic agency, or novel physics is required.

## Core loop

A useful EchoForm architecture can be expressed as:

```text
perception
  -> record
  -> persistent memory
  -> self-state estimate
  -> prediction
  -> value / continuation estimate
  -> action
  -> changed world + changed self
  -> new record
```

This extends ordinary world memory with an explicitly separate self-model.

### World memory

`M_world` can encode facts such as:

- places visited,
- environmental hazards,
- player relationships,
- territory and resource history,
- prior paths,
- observed failures and successes,
- social commitments and unresolved events.

### Self memory

`M_self` can encode operational variables such as:

- current capabilities,
- available resources,
- damage or fatigue state,
- confidence in sensors or beliefs,
- recent failures,
- commitments,
- role or goal state,
- learned tendencies,
- longer-term behavioral history.

A stronger predictive layer asks not merely `what state am I in?` but:

`M_self(t + dt | action)`

or operationally:

> What is my expected future capability if I take this action?

That is the engineering analogue of the predictive self-model benchmarks in the observer-emergence track.

## Mapping to EchoPath components

### EchoPath Memory Layer

The Memory Layer is the natural substrate for persistent world and agent state. It can preserve information across scene transitions, sessions, respawns, or server restarts rather than treating an NPC as a stateless policy invocation.

A useful split is:

```text
memory/world/*
memory/self/*
memory/relationships/*
memory/commitments/*
memory/skills/*
```

The research implication is that a stored field is not enough. A memory should count as functionally important only when ablation or shuffling measurably changes future decisions.

### Ledger

The ledger provides provenance and a durable causal autobiography:

```text
event
  -> perceived state
  -> active memories
  -> decision
  -> action
  -> outcome
  -> self-state update
```

This allows later inspection of *why* an EchoForm changed behavior, not merely what its current state happens to be.

A derived memory state can therefore be treated as a compression of ledger history rather than an opaque overwrite:

`ledger_t -> memory_t -> policy_(t+1)`

### Q-RRG

Q-RRG can operate as the dynamic pathing / possibility substrate. Candidate trajectories or actions can be conditioned on the EchoForm's world memory, self-state, goals, risks, commitments, and history.

Conceptually:

`Q-RRG state = f(world, M_world, M_self, goal, risk, history)`

The same physical environment can therefore induce different route choices for different EchoForms because their histories and self-models differ.

### Preconditioning

Preconditioning can bias candidate generation and evaluation before a full search. For a persistent agent this means accumulated experience can shape which plans are considered first rather than forcing every decision to begin from an unconditioned search space.

The provenance requirement should be retained: preconditioned choices should remain traceable to the memories or historical patterns that biased them.

## Lessons already supported by the observer-emergence benchmarks

The current simulations support several engineering design rules while remaining within ordinary information/control theory.

1. **Persistent memory alone is insufficient.** O-1A showed that memory becomes behaviorally important when it is causally reused.
2. **Self-information alone is insufficient.** O-1B and O-1C showed that possessing information about internal state does not guarantee utility.
3. **Resource matching matters.** O-1C2 showed that self-state information can improve action timing when resource budgets are fairly matched.
4. **State-informed regulation can preserve future capability.** O-1D-prep showed that timing maintenance from internal condition can preserve future sensing ability.
5. **Internal location is not automatically privileged.** O-1D2 and O-1D3 found matched zero-latency external controllers can reproduce internal control.
6. **Prediction is not automatically robust.** O-1D3 showed predictive control can over-maintain under distribution shift.
7. **Better self-models do not guarantee better policies.** O-1D3b/c separated dynamics identification from decision quality.
8. **Self-preservation should not be inserted as a hidden objective.** O-1D3d showed that explicitly valuing health can bake the desired behavior into the benchmark.
9. **Instrumental preservation can emerge from continuation value.** O-1D3e showed maintenance can emerge when failure removes future task access even with no direct reward for health.

These are useful constraints for designing believable persistent characters because they distinguish functional mechanisms from decorative state variables.

## Persistent identity criterion

For engineering purposes, a strong but non-consciousness-based definition is:

> Persistent identity is history-dependent behavior that survives restart and causally affects future choices.

This can be tested experimentally.

Given two otherwise identical EchoForms initialized from the same archetype, allow their histories to diverge. If the architecture is functioning, the later policies should diverge in interpretable ways tied to those histories.

For example:

```text
same archetype + hostile social history -> more cautious trust policy
same archetype + repeated exploration success -> greater uncertainty tolerance
same archetype + repeated scarcity -> larger resource reserve policy
```

The difference should remain after persistence/reload and should disappear or change predictably under relevant memory ablation.

## Suggested EchoForm state model

A future implementation could expose a versioned state contract such as:

```text
EchoFormState
  identity
  current_self_state
  world_model
  relationship_model
  commitments
  episodic_memory_refs
  compressed_tendencies
  predictive_self_model
  continuation_value
  active_goal
  policy_context
  provenance_refs
```

The ledger should remain the evidence layer; compressed tendencies and self-model variables should be reproducible from or at least attributable to ledger entries.

## Evaluation suite

Persistent-agent tests should inherit the adversarial style of the observer work:

- memory ablation,
- memory shuffling,
- stale-memory controls,
- matched information budgets,
- matched action budgets,
- external-controller equivalence,
- restart/persistence tests,
- history-divergence tests,
- provenance reconstruction,
- continuation-value ablation,
- false-memory / corrupted-ledger sensitivity.

A mechanism should be promoted only when removing or corrupting it produces a specific predicted behavioral change.

## Boundary with observer-emergence research

The engineering track and scientific track should cross-feed without being conflated.

```text
Observer Emergence Research
       | discriminators / failure modes
       v
EchoForm Persistent-Agent Architecture
       | implementation evidence
       v
better operational questions for Observer Emergence
```

EchoForms can therefore benefit from the observer work even if no experiment ever justifies the statement that an artificial observer or consciousness has emerged.

The practical claim is narrower and testable:

> Memory, causal reuse, self-state modeling, predictive control, continuation value, and durable provenance can be composed into persistent artificial characters whose histories become part of their future behavior.
