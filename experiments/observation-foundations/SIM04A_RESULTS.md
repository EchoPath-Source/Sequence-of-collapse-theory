# SIM-04A — Causal Order / Earliest Response Results

**Status:** initial finite-intervention benchmark complete  
**Claim level:** toy-model methodology result only; not evidence for emergent spacetime or SoCT.

## Question

Can directed causal reachability and earliest influence be recovered from finite noisy interventions when coordinates, the edge list, and the true topological order are hidden?

This simulation deliberately does **not** infer distance from response magnitude.

## Model

Each run creates a 20-node weighted directed acyclic graph (DAG) with:

- a concealed random topological order;
- a hidden causal backbone;
- random forward shortcut edges;
- positive edge weights;
- Gaussian measurement noise;
- either uniform or strongly heterogeneous receiver susceptibility.

An intervention at source `j` produces lagged responses through powers of the hidden transition matrix:

```math
A, A^2, A^3, \ldots
```

The estimator receives noisy response estimates only. It marks a source-target pair as causally related when the response first exceeds a conservative `4 sigma` significance threshold.

The estimator attempts to recover:

1. direct one-lag edges;
2. finite-horizon causal reachability;
3. earliest causal lag.

The maximum observation horizon is 8 discrete lags.

All values below are means over 100 deterministic random seeds.

## Results — Uniform susceptibility

| Trials per intervention | Reach precision | Reach recall | Direct-edge precision | Direct-edge recall | Earliest-lag MAE |
|---:|---:|---:|---:|---:|---:|
| 25 | 0.99955 | 0.96701 | 0.99946 | 1.00000 | 0.02607 |
| 50 | 0.99957 | 0.98644 | 0.99946 | 1.00000 | 0.01275 |
| 100 | 0.99957 | 0.99475 | 0.99946 | 1.00000 | 0.00549 |
| 200 | 0.99958 | 0.99846 | 0.99946 | 1.00000 | 0.00195 |
| 500 | 0.99958 | 0.99963 | 0.99946 | 1.00000 | 0.00069 |

## Results — Heterogeneous susceptibility

| Trials per intervention | Reach precision | Reach recall | Direct-edge precision | Direct-edge recall | Earliest-lag MAE |
|---:|---:|---:|---:|---:|---:|
| 25 | 0.99966 | 0.89055 | 0.99927 | 0.98872 | 0.04545 |
| 50 | 0.99967 | 0.94016 | 0.99927 | 0.99948 | 0.03283 |
| 100 | 0.99968 | 0.96943 | 0.99927 | 1.00000 | 0.02283 |
| 200 | 0.99968 | 0.98569 | 0.99927 | 1.00000 | 0.01252 |
| 500 | 0.99969 | 0.99482 | 0.99927 | 1.00000 | 0.00575 |

## Interpretation

### 1. Causal order is substantially more robust than amplitude-derived distance

Across the tested regimes, the conservative significance detector keeps causal-reachability precision above `0.9995` on average.

The estimator is therefore much less tempted by the susceptibility confound exposed in SIM-03B because it asks primarily:

```text
did an intervention produce a statistically detectable downstream effect,
and at what earliest lag?
```

rather than:

```text
how large was the eventual response?
```

### 2. Heterogeneous susceptibility mainly creates false negatives, not false proximity

At only 25 trials, heterogeneous receiver gain reduces reachability recall from

```text
0.967 -> 0.891,
```

while precision remains approximately

```text
0.9997.
```

This is the expected finite-data failure mode: low-susceptibility receivers can hide weak causal paths.

Increasing repeated interventions restores those paths monotonically:

```text
heterogeneous reach recall
25 trials  -> 0.891
50 trials  -> 0.940
100 trials -> 0.969
200 trials -> 0.986
500 trials -> 0.995
```

### 3. Direct edges are easier than full reachability

Direct-edge recall reaches approximately `1.0` by 100 trials even with heterogeneous gain. Longer indirect paths are harder because transmitted effects decay along paths and can fall below the detection threshold.

### 4. Earliest-response timing is recoverable when a path is detected

The mean absolute earliest-lag error is already far below one discrete time step and decreases with additional trials.

This supports using earliest causal response / delay as a separate observable in SIM-04B rather than replacing it with response magnitude.

## Important limitation

The benchmark is deliberately favorable in several ways:

- the true graph is acyclic;
- all edge weights are positive, avoiding path cancellation;
- intervention targets are known exactly;
- no hidden intermediate nodes are included yet;
- noise is Gaussian and stationary;
- the observation clock is synchronized;
- propagation occurs in discrete unit lags;
- the simulator does not yet include memory-dependent transition laws.

Therefore this is a **sanity gate**, not a demonstration that real spacetime causal order is straightforward to infer.

## Decision

SIM-04A passes the initial causal-order gate.

The result supports the hierarchy

```text
causal order / reachability
    -> earliest response / delay
    -> susceptibility-normalized direct strength
    -> only then attempt effective geometry.
```

It also provides a clear failure mode to preserve in later tests:

> finite interventions can omit weak causal relations without generating many false ones, so apparent causal disconnection must not automatically be interpreted as infinite geometric separation.

## Next step — SIM-04B

Attempt hidden-geometry reconstruction using causal order plus timing/scale information, with explicit adversarial cases:

1. 1D hidden chain/ring geometry;
2. 2D lattice;
3. long-range shortcut edges;
4. heterogeneous propagation speed;
5. hidden intermediate nodes;
6. heterogeneous susceptibility;
7. recurrent/near-critical contamination kept separate from earliest-response inference.

The principal comparison should be among:

```text
order only
order + delay
order + count/density
order + delay + calibrated direct transmission
```

rather than a single raw-response distance formula.

## Reproduction

```bash
python experiments/observation-foundations/sim04a_causal_order_earliest_response.py --seeds 100
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim04a_causal_order_earliest_response.py --seeds 100 --json
```
