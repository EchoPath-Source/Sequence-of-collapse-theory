# Observer Emergence and Functional Metacognition — Literature Comparison

## Purpose
This note separates established metacognition concepts from the specific observer-emergence architecture being developed in SoCT simulations.

## Established foundations

### Nelson–Narens monitoring/control architecture
The classical metacognition framework separates an object level from a meta level. Information flows upward through **monitoring**, while the meta level changes lower-level processing through **control**. This distinction is important for the observer-emergence ladder: calibrated self-monitoring alone does not establish metacognitive control.

### Bayesian second-order self-evaluation
Fleming & Daw (2017) formalize metacognitive self-evaluation as a second-order Bayesian inference about a coupled decision system. Confidence can be treated as an inferred probability that one's first-order choice is correct. This provides strong precedent for the O-1D4a/b idea of a calibrated probability that a self-model classification is correct.

Reference: Fleming, S. M., & Daw, N. D. (2017). *Self-Evaluation of Decision-Making: A General Bayesian Framework for Metacognitive Computation*. Psychological Review, 124(1), 91–114. DOI: 10.1037/rev0000045.

### Confidence-regulated information search
Schulz, Fleming & Dayan (2023) explicitly model action, confidence, and costly information search using Bayesian and reinforcement-learning machinery. This is direct precedent for testing whether uncertainty can regulate information acquisition. Therefore the general idea behind O-1D4c onward is not novel by itself.

Reference: Schulz, L., Fleming, S. M., & Dayan, P. (2023). *Metacognitive computations for information search: Confidence in control*. Psychological Review, 130(3), 604–639. DOI: 10.1037/rev0000401.

### Bayesian/active-inference models of self-representation
There is also established work treating self-representations as Bayesian beliefs that may be updated and used to predict outcomes. Active-inference frameworks further connect inference and action. Thus probabilistic self-modeling itself should not be claimed as a novel invention of this program.

## What this observer-emergence ladder specifically implements
The present simulations combine established ingredients in a narrower causal-autobiographical architecture:

`own action–outcome history -> latent self-dynamics estimate -> policy selection -> future self-regulation`

and then:

`self-model -> calibrated probability that the self-model is correct`.

The distinctive experimental focus is not generic confidence. It is whether an artificial system can infer **hidden properties of its own dynamics from temporally paired autobiographical action–outcome records**, then use that inference to regulate future capability under matched present-state conditions.

The strongest earned results so far are:

1. paired autobiographical action–outcome records can improve identification of hidden self-dynamics;
2. hidden self-dynamics can determine which future maintenance policy is better;
3. under randomized regret-balanced hidden dynamics, own history can reduce policy regret relative to uninformative/static and shuffled-history controls;
4. confidence in the inferred self-dynamics can be calibrated on independent held-out data;
5. internal and matched zero-latency external implementations remain equivalent;
6. confidence calibration does not automatically produce useful information-seeking control;
7. selective high-information probing can beat always probing, but has not yet beaten provenance-shuffled targeting or never-probe controls robustly.

## Claim boundary
The program should **not** claim to have invented metacognition, Bayesian confidence, value-of-information reasoning, active inference, self-modeling, or confidence-directed search.

A defensible characterization is:

> The observer-emergence program constructs and adversarially tests a causal-autobiographical self-modeling architecture in which an artificial system uses its own action–outcome history to infer latent self-dynamics, calibrate uncertainty about that inference, and potentially use that second-order information for future self-regulation.

Potential novelty, if any, would lie in the **combination, operationalization, provenance controls, and observer-emergence use of these mechanisms**, not in the constituent mathematical ideas.

## Relation to the observer-emergence ladder

- persistent memory alone: not metacognition;
- self-state estimate: still ordinary state estimation;
- latent self-dynamics estimate: self-model/system identification;
- calibrated reliability of the self-model: defensible functional **metacognitive monitoring**;
- reliable use of that second-order information to alter information acquisition or control: functional **metacognitive control**;
- consciousness, subjective experience, or phenomenal awareness: not established by any of the above.

Thus current status is:

`functional metacognitive monitoring: supported`

`active functional metacognitive control: not yet supported`

`consciousness: not implied`

## Key discriminator going forward
The next useful test is not simply more recursion. It is whether the system can choose among multiple information sources of different cost and diagnostic value according to expected downstream decision regret, and whether this selection survives shuffled-provenance and matched external controls.
