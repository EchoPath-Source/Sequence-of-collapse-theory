# EchoForm Persistent-Agent Architecture

## Purpose
This document records an applied engineering bridge from the Observer Emergence research program to persistent NPC / EchoForm design. It does **not** claim that the resulting agents are conscious, sentient, or proof of observer emergence.

The practical hypothesis is narrower: mechanisms that make records causally active, temporally persistent, self-referential, predictive, and continuation-sensitive can be used to build characters whose identity and behavior develop across time rather than reset at each interaction.

## Core loop

`perception -> record -> persistent memory -> self-state -> prediction -> value -> action -> future self-state`

A persistent agent should distinguish at least two memory domains:

- `M_world`: what the agent has learned about the environment, places, actors, hazards, resources, and events.
- `M_self`: what the agent has learned about its own capabilities, commitments, injuries/resources, relationships, recent failures, confidence, goals, and prior decisions.

A stronger temporally extended representation is

`M_hat_self(t + dt | a)`

which represents the predicted future self-state conditional on taking action `a`.

## Mapping to EchoPath systems

### Q-RRG
Q-RRG can provide the dynamic pathing and option-selection substrate. Candidate actions or routes can be evaluated against world state, current goals, history-conditioned risk, and predicted future self-state.

### EchoPath Memory Layer
The Memory Layer can preserve world and self state across sessions. It should support both event-level memory and compressed persistent tendencies so that long history does not require replaying every event.

### Ledger
Ledger functions can provide provenance and a causal autobiography:

`event -> decision -> outcome -> self-state update`

The ledger should preserve enough information to reconstruct why a persistent tendency emerged and to distinguish current memory from historical evidence.

### Preconditioning
Preconditioning can bias candidate generation and path selection using accumulated experience, allowing repeated history to reshape the search landscape before full planning begins.

## Design principle: history-conditioned identity
Two agents with the same initial archetype should be allowed to diverge through different histories:

`same initial archetype + different history -> different persistent behavioral identity`

Examples include cautious behavior after repeated betrayal, increased exploration after repeated successful uncertainty, or larger resource reserves after repeated scarcity.

## Design principle: self-models must be causal
A `self_state` object is not sufficient. The state must change future decisions in a measurable way. Removing, shuffling, or delaying self-state information should alter behavior if the representation is functionally meaningful.

This follows directly from the observer-emergence control ladder, which repeatedly separates mere stored information from causally useful information.

## Instrumental self-preservation
O-1D3e provides a useful engineering principle: do not necessarily reward an NPC directly for 'survival' or 'health.' Instead, continued capability can have instrumental value because loss of capability removes future access to goals.

A character can therefore retreat because continuing would reduce expected future agency, not merely because `HP < threshold`.

Conceptually:

`expected future goal capacity if continue < expected future goal capacity if recover`

This can produce more natural maintenance, retreat, rest, resupply, or social-help behavior without hard-coding self-preservation as a terminal value.

## Restart-persistent identity criterion
A useful engineering criterion is:

**Persistent identity = history-dependent behavior that survives restart and causally affects future choices.**

This criterion is intentionally weaker than consciousness or observerhood. It is testable in software and suitable for EchoForm development.

## Suggested agent state layers
A future EchoForm implementation can separate:

1. world state / environment model
2. autobiographical event ledger
3. compressed long-term memory
4. self-state estimate
5. future self-state predictor
6. goals / commitments / value model
7. policy / planner
8. Q-RRG path and option search
9. preconditioning biases
10. persistence / restart recovery

## Evaluation tests
Useful ablations include:

- restart persistence: does identity survive process restart?
- memory shuffle: does temporal misalignment reduce coherent behavior?
- self-state ablation: does removing self-state change decisions?
- ledger provenance replay: can a major tendency be traced to prior events?
- counterfactual future-self test: does changing predicted future capability alter present action?
- matched external-controller control: can the same behavior be reproduced by an external policy given identical information?

The last control is important scientifically. Equivalent external control would not reduce engineering usefulness, but it prevents interpreting ordinary adaptive control as evidence of intrinsic observerhood.

## Research / product separation
Maintain two distinct tracks:

- **Observer Emergence Research**: asks what mechanisms are necessary or sufficient for increasingly observer-like causal organization.
- **EchoForm Persistent-Agent Engineering**: uses validated mechanisms to construct persistent, history-conditioned, self-modeling characters without making consciousness claims.

This separation allows the engineering program to benefit from negative and positive research results while keeping scientific claim boundaries intact.
