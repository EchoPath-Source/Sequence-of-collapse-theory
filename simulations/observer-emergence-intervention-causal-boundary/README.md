# O-1D3g — Intervention-Defined Causal Boundary

## Question
If spatial location is not a sufficient self-boundary, can a more useful boundary be defined by intervention sensitivity and recoverability?

O-1D3f showed that a perfectly connected external controller is functionally equivalent to the internal controller, while latency and disruption of the loop sharply reduce continuation. O-1D3g therefore intervenes on the components of the temporally extended regulation loop itself.

## Model
The regulated system has:

- true health `h`;
- a noisy diagnostic stream;
- a persistent estimated self-state `h_hat`;
- a short diagnostic ledger;
- a continuation-value controller;
- WORK and MAINTAIN actions;
- a failure threshold that terminates future task access.

The estimator updates recursively:

`h_hat(t+1) = (1-alpha) h_hat(t) + alpha diagnostic(t)`

with `alpha = 0.20`.

The intervention occurs at step 200 of a 500-step episode.

## Conditions
1. `intact_internal` — intact loop.
2. `external_zero_latency` — computationally matched external replica; same information and immediate action authority.
3. `estimator_reset` — the self-state estimate is reset once to a healthy default, then normal online updating resumes.
4. `reset_with_reconstruction` — the reset estimate is reconstructed from the recent 20-entry diagnostic ledger.
5. `reset_with_stale_reconstruction` — control reconstruction from the first 20 diagnostics of the episode rather than the recent ledger.
6. `state_estimator_replacement` — for 20 steps after intervention, the operative self-state is replaced by a fixed healthy-state surrogate.
7. `action_channel_intervention` — for 20 steps after intervention, the controller's chosen action is inverted.

## Frozen results
The internal and matched zero-latency external implementations are exactly identical in all tested regimes.

At degradation `0.08`:

| condition | reward / episode | post-intervention reward | mean lifetime | failure rate |
|---|---:|---:|---:|---:|
| intact internal | 350.77 | 205.88 | 472.93 | 0.100 |
| external zero latency | 350.77 | 205.88 | 472.93 | 0.100 |
| estimator reset | 347.49 | 202.56 | 467.30 | 0.120 |
| recent-ledger reconstruction | 354.04 | 207.65 | 475.87 | 0.093 |
| stale reconstruction | 355.98 | 208.96 | 479.32 | 0.080 |
| state-estimator replacement | 246.64 | 99.87 | 334.06 | 0.573 |
| action-channel intervention | 329.56 | 183.06 | 459.36 | 0.147 |

At degradation `0.12`, sustained state-estimator replacement is especially destructive:

- intact reward / episode: `283.95`
- intact failure rate: `0.000`
- estimator replacement reward / episode: `167.82`
- estimator replacement failure rate: `0.733`

Action-channel intervention is also harmful but less destructive than sustained self-state replacement in this implementation.

## Interpretation
The strongest supported result is not that any single internal variable defines a self.

A one-time estimator reset is only mildly damaging because the loop can quickly rebuild the estimate from continuing observations. In contrast, sustained replacement of the operative self-state or sustained intervention on the action channel strongly degrades continuation.

This supports the more useful engineering statement:

`functional identity depends on an intervention-sensitive, recoverable causal loop rather than on the inviolability of any one stored variable.`

The emerging candidate boundary is therefore temporal and organizational:

```text
records
  -> self-state estimate
  -> continuation-sensitive decision
  -> action
  -> future sensing capacity
  -> new records
```

A component belongs to the operational loop insofar as intervening on it predictably changes the system's future capacity to continue sensing and acting.

## Important negative result
`external_zero_latency == intact_internal`

again. Internal physical location remains insufficient as an observer criterion.

## Reconstruction result — do not oversell
Recent-ledger reconstruction did not uniquely outperform the stale-ledger control across this small frozen grid. In some regimes the stale reconstruction scored slightly better.

Therefore O-1D3g does **not** establish that autobiographical reconstruction has a privileged functional role. The correct conclusion is narrower: the architecture can recover from a point disruption, but this implementation does not yet isolate a uniquely valuable reconstruction source.

There is also a Monte Carlo limitation: after interventions cause different actions, the arms consume different random draws and are not paired counterfactual trajectories. Large effects such as sustained estimator replacement are robust enough to be informative here; small differences between reconstruction arms should not be treated as causal evidence.

## Observer-emergence claim boundary
O-1D3g supports ordinary control-theoretic properties only:

- causal dependence,
- persistence,
- intervention sensitivity,
- recoverability,
- continuation-sensitive regulation.

It does not establish consciousness, phenomenology, intrinsic agency, a metaphysical self, or novel SoCT physics.

## EchoForm implication
For persistent NPCs / EchoForms, this suggests identity should not be implemented as a single sacred state object. A more robust architecture is a reconstructible causal history:

`ledger -> memory -> self-state -> policy -> action -> new ledger entries`

If one cached self-state is lost, a persistent agent should be able to rebuild enough of it from durable records to continue coherently.

See:

`docs/engineering/echoform-persistent-agent-architecture.md`

## Next gate — O-1D3h: paired reconstruction and endogenous repair
Before recursive self-model depth, the reconstruction question needs a stronger test.

Required improvements:

1. common-random-number / paired counterfactual event streams across arms;
2. recent-ledger reconstruction versus stale, shuffled, donor, and zero-memory controls;
3. reconstruction from durable records after self-state corruption;
4. a recovery objective defined before intervention;
5. matched external reconstruction;
6. explicit measurement of whether the system detects its own model/state corruption before repair;
7. an endogenous repair arm in which recovery is triggered by detected prediction error rather than by experimenter instruction.

The stronger candidate observer-like step is therefore not merely `recover after reset`, but:

`detect self-model failure -> use retained history to reconstruct -> restore future regulation`.
