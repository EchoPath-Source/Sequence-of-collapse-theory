# Revised SIM-03 / SIM-04 Plan After Literature Confrontation

**Date:** 2026-08-17  
**Status:** ready for implementation  
**Reason for revision:** external literature shows that object discovery from microscopic dynamics and causal-order-based spacetime reconstruction already have substantial prior frameworks. The simulations are therefore reframed as adversarial benchmarks and integration tests rather than novelty demonstrations.

## SIM-03A — Emergent Object Benchmark

### Question

Can stable macroscopic subsystems be recovered from dynamics without using hidden geometry or supplied object labels, and do multiple independent criteria agree?

### Synthetic systems

1. two well-separated causal clusters;
2. spatial neighbors that are causally weakly coupled;
3. long-range functionally coupled components;
4. moving coherent subsystem exchanging components with a background;
5. nested multi-scale objects;
6. near-critical high-susceptibility region that should **not** automatically count as one stable object.

### Candidate estimators

- internal-vs-boundary intervention influence ratio;
- predictive sufficiency of a proposed macrostate;
- effective-information / causal-emergence proxy;
- dynamical graph community structure;
- simplified Markov-blanket-like conditional-independence boundary.

### Metrics

- adjusted Rand index against withheld ground truth where labels exist;
- normalized mutual information between recovered partitions;
- partition stability under noise and perturbation;
- held-out predictive log loss using recovered macrostates;
- sensitivity to thresholds/hyperparameters.

### Falsification / failure

SIM-03 fails as a general objecthood mechanism if:

- different reasonable criteria yield incompatible partitions;
- results collapse under small threshold changes;
- high local susceptibility is systematically mistaken for object membership;
- hidden spatial adjacency is required to recover labels;
- nested objects cannot be represented without ad-hoc tuning.

## SIM-03B — Susceptibility and Criticality Adversary

### Purpose

Directly test the confound discovered during the conceptual probe:

```text
large response != small distance != same object
```

### Construction

Use identical network topology while varying local gain/susceptibility. Include nodes near a critical or resonant response regime.

### Required result

A robust causal/object estimator should distinguish:

```text
transmission strength
from
receiver susceptibility / local amplification.
```

If it cannot, its output must not be used as geometry in SIM-04.

## SIM-04A — Causal Order Reconstruction

### Question

From finite intervention-response observations, can the algorithm recover which events/nodes can causally affect which others without access to coordinates?

### Inputs exposed to estimator

- intervention identity;
- response identity;
- temporal ordering / first detectable response;
- repeated trials under noise.

### Hidden from estimator

- coordinates;
- edge list;
- true path distance;
- ground-truth object labels.

### Output

A directed reachability / partial-order estimate.

### Metrics

- precision/recall of comparable causal pairs;
- transitive-consistency violations;
- false adjacency due to common causes;
- false reachability due to correlated noise.

## SIM-04B — Geometry From Order + Count/Density + Delay

### Motivation

Causal-set literature makes clear that order alone is not the full practical reconstruction problem. The revised benchmark should separate:

```text
causal order
scale / effective volume
propagation time
response amplitude.
```

### Candidate features

1. estimated causal order;
2. count of intermediate events/nodes in causal intervals;
3. propagation delay distributions;
4. susceptibility-normalized transmission as an auxiliary feature only.

### Ground-truth geometries

- 1D chain;
- 2D grid;
- anisotropic grid;
- bottleneck / corridor graph;
- irregular geometric graph;
- shortcut/nonlocal-edge graph;
- hidden-node graph;
- time-varying geometry analogue.

### Reconstruction targets

- ordinal neighborhood recovery;
- shortest-path rank correlation;
- embedding stress where a Euclidean/Lorentzian analogue is appropriate;
- topology recovery;
- robustness under node removal and missing interventions.

### Core adversaries

- receiver gain/susceptibility changes;
- resonance;
- critical slowing/amplification;
- common-cause correlations;
- nonlocal shortcut edges;
- memory-delayed responses;
- heterogeneous edge speeds.

## SIM-04C — Compare Candidate Distance Constructions

Do not privilege `-log(kappa)`.

Compare at least:

```text
D1 = shortest path on inverse normalized causal capacity
D2 = shortest path on negative log normalized transmission
D3 = propagation-delay metric
D4 = order + interval-count metric
D5 = learned combination trained on one geometry family and tested on another
```

A useful estimator must generalize across withheld geometry families rather than merely fit one simulator.

## Connection back to SoCT

These simulations are **not tests of SoCT by themselves**.

Their purpose is to create a validated inference layer that later allows the stronger question:

```text
Does adding a SoCT memory field M alter causal structure or effective geometry
in a distinctive, predeclared way that standard dynamical memory does not?
```

Only after SIM-03/04 have calibrated ordinary object and geometry inference should `M` be injected.

## Implementation order

1. implement SIM-03A on simple stochastic networks;
2. add SIM-03B critical/susceptibility adversary;
3. lock the causal estimator before geometry work;
4. implement SIM-04A reachability reconstruction;
5. implement SIM-04B order/count/delay geometry;
6. compare distance constructions in SIM-04C;
7. only then consider SoCT-specific memory perturbations.
