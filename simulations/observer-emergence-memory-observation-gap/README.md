# O-1D3i — Memory Indispensability Under an Observation Gap

## Question
When fresh self-observation is temporarily unavailable after a disruption, does retained history preserve action quality and continuation?

## Design
At step 200 the self-state estimate is reset/reconstructed and fresh diagnostics are withheld for 30 steps. The controller must propagate its reconstructed self-state through that gap. All arms use paired potential-outcome streams so diagnostic noise, damage opportunities, repair draws, and task-hit draws are matched by episode/time index.

Arms: own recent history, matched external use of the same history, shuffled history, stale history, donor history, zero-memory reset, and oracle current state.

## Frozen result
Memory is useful relative to zero-memory in the moderate regimes, but autobiographical ownership is not uniquely privileged.

At degradation 0.08:

- own history: reward 326.70, lifetime 441.07, failure 0.215, gap oracle-action match 0.662;
- zero memory: reward 316.13, lifetime 426.69, failure 0.265, gap match 0.629;
- stale history: reward 326.89, lifetime 441.55, failure 0.215;
- donor history: reward 333.21, lifetime 450.91, failure 0.184.

The donor control can outperform own history despite much worse immediate reconstruction error. This means the benchmark does not support a claim that autobiographical ownership itself is functionally privileged.

Internal and matched zero-latency external use of own history are identical.

## Interpretation
Supported:

`retained state information can improve continuation when fresh observation is unavailable`.

Not supported:

`my own history is uniquely privileged because it is mine`.

The result motivates decomposing memory representation itself. O-1D3j therefore asks whether ordered history contains useful information beyond compressed state summaries.

This is synthetic ordinary control theory only; no consciousness or novel-physics claim.
