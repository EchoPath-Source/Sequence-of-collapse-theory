# SIM-03B — Susceptibility and Criticality Adversary Results

**Status:** adversarial toy-model benchmark complete  
**Claim level:** methodology result only; not evidence for SoCT or emergent spacetime.

## Question

Can raw intervention amplitude safely stand in for transmission strength, object membership, or effective distance when different receivers have different susceptibilities and when recurrent dynamics approach a critical/resonant regime?

The target confound is

```text
large response != strong transmission != small distance != same object
```

## Setup

A hidden 18-node directed transmission network contains three dynamical modules. Node order is permuted. The estimator is not given the labels.

For the susceptibility benchmark, the immediate observed response is

```math
K_{ij} = g_i W_{ij} + \epsilon_{ij},
```

where

- `W_ij` is direct source-to-target transmission;
- `g_i` is receiver susceptibility/local gain;
- `epsilon_ij` is measurement noise.

An independent local calibration probe estimates `g_i`, producing

```math
\hat T_{ij}=K_{ij}/\hat g_i.
```

For the criticality benchmark, recurrent dynamics are

```math
A=c\,\mathrm{diag}(g)W,
```

with `c` chosen to set a requested spectral radius. Long-time integrated response is

```math
R=A+A^2+A^3+\cdots=(I-A)^{-1}A.
```

This deliberately mixes direct transmission with all longer recurrent paths.

All reported values are means over 50 deterministic random seeds.

## Part 1 — Receiver susceptibility

| Case | Object ARI raw / normalized | Module-edge AUC raw / normalized | Transmission rank rho raw / normalized | Gain-to-hub correlation raw / normalized |
|---|---:|---:|---:|---:|
| uniform | 1.000 / 1.000 | 1.000 / 1.000 | 0.980 / 0.979 | n/a |
| heterogeneous | 1.000 / 1.000 | 0.969 / 1.000 | 0.772 / 0.916 | 0.841 / 0.333 |
| extreme | 1.000 / 1.000 | 0.922 / 1.000 | 0.692 / 0.866 | 0.829 / 0.440 |
| noisy calibration | 1.000 / 1.000 | 0.951 / 1.000 | 0.738 / 0.859 | 0.832 / 0.231 |

### Interpretation

The coarse module partition remains easy in this deliberately modular test bed, so ARI stays perfect. That should **not** be overinterpreted.

The more diagnostic quantities show the confound clearly:

1. heterogeneous gain degrades the ordering of inferred transmission strengths;
2. raw inferred node strength becomes strongly correlated with receiver gain (`rho ~ 0.83-0.84`);
3. local susceptibility normalization substantially improves direct-transmission recovery and reduces gain-driven false hubness;
4. even a deliberately noisy susceptibility calibration remains useful in this parameter range.

Therefore raw response amplitude is unsafe as a distance or causal-strength proxy even when coarse object clustering appears robust.

## Part 2 — Recurrent criticality

| Spectral radius | Direct transmission rho raw / normalized | Integrated-response rho raw / normalized | Integrated object ARI raw / normalized |
|---:|---:|---:|---:|
| 0.70 | 0.754 / 1.000 | 0.522 / 0.751 | 1.000 / 1.000 |
| 0.90 | 0.754 / 1.000 | 0.295 / 0.506 | 1.000 / 1.000 |
| 0.97 | 0.754 / 1.000 | 0.116 / 0.149 | 0.993 / 1.000 |
| 0.99 | 0.754 / 1.000 | 0.046 / 0.053 | 0.509 / 0.590 |

### Critical result

For the **direct one-step response**, dividing out receiver susceptibility reconstructs the direct transmission ranking exactly in this noiseless criticality subtest:

```text
rho = 1.000.
```

But the same normalization cannot undo recurrent path mixing in the long-time response.

As the spectral radius approaches `1`, integrated response becomes dominated by repeated amplification and indirect paths. At radius `0.99`:

```text
integrated transmission rank agreement:
raw        rho = 0.046
normalized rho = 0.053
```

and even the coarse hidden-module partition degrades to

```text
raw ARI        = 0.509
normalized ARI = 0.590.
```

So the failure is not merely receiver susceptibility. Near criticality, long-time response ceases to be a faithful local transmission map.

## Falsification outcome

The naive hypothesis

```text
large intervention response -> strong causal edge -> short effective distance
```

**fails** under the adversarial benchmark.

A weaker statement survives:

> Small-lag intervention response can estimate direct transmission if local susceptibility is separately calibrated and if recurrent/indirect path contamination is controlled.

This is the quantity that may be used as an input to later causal-geometry reconstruction.

## Consequence for SIM-04

SIM-04 must not derive geometry from raw or long-time response amplitude.

The revised input hierarchy should be:

1. **earliest detectable causal order / reachability**;
2. **first-response delay**;
3. **small-lag/direct response**, with receiver susceptibility calibrated separately;
4. **event/count or effective-volume information** where relevant;
5. long-time integrated response only as an auxiliary dynamical observable, never as the distance metric by itself.

Adversarial SIM-04 cases must include:

- heterogeneous susceptibility;
- near-critical recurrence;
- hidden/common-cause nodes;
- long-range shortcut edges;
- variable propagation speed/coupling strength;
- noise and finite intervention counts.

## What this does not establish

- No universal definition of objecthood has been derived.
- No spacetime geometry has been reconstructed yet.
- No quantum system is simulated here.
- No SoCT memory field is tested here.
- The exact susceptibility division used here assumes a simple multiplicative small-signal gain model; nonlinear systems may require state-dependent local response calibration.

## Reproduction

```bash
python experiments/observation-foundations/sim03b_susceptibility_criticality_adversary.py --seeds 50
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim03b_susceptibility_criticality_adversary.py --seeds 50 --json
```

## Decision

**SIM-03B passes as an adversarial-methodology result and falsifies the raw-response distance heuristic.**

Proceed to SIM-04A using causal order, earliest response, and explicitly separated susceptibility rather than integrated response magnitude.
