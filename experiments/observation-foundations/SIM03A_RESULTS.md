# SIM-03A — Emergent Object Benchmark Results

**Status:** initial baseline complete  
**Claim level:** toy-model methodology result only; not evidence for SoCT or emergent spacetime.

## Question

Can hidden dynamical modules be recovered without coordinates or supplied object labels, and how do intervention-based estimators compare with ordinary correlation under a latent common-cause confound?

## Setup

Each run uses a 12-node stochastic nonlinear dynamical system with 3 withheld dynamical modules. Node order is randomly permuted so index position does not reveal group membership.

Three estimators are compared:

1. **intervention affinity** — spectral clustering of symmetric one-step intervention response;
2. **natural correlation** — spectral clustering of absolute observational correlation;
3. **response profile** — k-means on each node's incoming/outgoing intervention-response profile.

Three scenarios are tested across 20 deterministic random seeds:

- `clean_modular`;
- `weak_separation` with smaller within/between coupling contrast;
- `latent_common_cause`, in which strong hidden drivers impose an observational correlation partition unrelated to the true dynamical modules while leaving the intervention structure unchanged.

Primary metric: adjusted Rand index (ARI) against the withheld module labels.

## Results

| Scenario | Intervention ARI mean | Correlation ARI mean | Response-profile ARI mean |
|---|---:|---:|---:|
| clean modular | 1.000 | 1.000 | 1.000 |
| weak separation | 1.000 | 1.000 | 1.000 |
| latent common cause | 1.000 | 0.373 | 1.000 |

For the latent-common-cause case, correlation clustering had standard deviation approximately `0.224` across seeds and reached ARI `0.0` in at least one run, while both intervention-based estimators remained at ARI `1.0` in this deliberately simple benchmark.

## Interpretation

The baseline demonstrates a narrow but important point:

```text
observational correlation can recover the same modules as intervention dynamics
when the data-generating process is benign,
but a strong common-cause confound can redirect correlation structure
without changing the true intervention-defined coupling.
```

Therefore SIM-03/04 should preserve the distinction

```text
correlation != controllable causal influence.
```

This supports the revised plan to infer object boundaries and later geometry primarily from intervention/reachability structure, while using ordinary correlations only as auxiliary information.

## What this does NOT show

- It does not define a universal notion of objecthood.
- It does not show that intervention communities correspond to physical objects in general.
- It does not test criticality, nonlinear susceptibility, hidden nodes, or delayed memory yet.
- It does not reconstruct spatial geometry.
- It does not test quantum systems.
- It does not support a SoCT memory field.

The systems were deliberately constructed with clear modular ground truth, so perfect ARI for intervention methods is a sanity check rather than a surprising discovery.

## Next falsification step — SIM-03B

The next test must deliberately break the easiest intervention heuristic by varying receiver susceptibility/gain while holding topology fixed.

Target confound:

```text
large intervention response
    may mean strong transmission,
    or may mean highly susceptible receiver.
```

SIM-03B should therefore compare raw intervention amplitude with susceptibility-normalized estimates and test whether object partitions remain stable near resonant/critical response regimes.

## Reproduction

Run:

```bash
python experiments/observation-foundations/sim03a_emergent_object_benchmark.py --seeds 20
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim03a_emergent_object_benchmark.py --seeds 20 --json
```
