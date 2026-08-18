# SIM-04B — Geometry From Order + Count + Delay Results

**Status:** initial literature-informed benchmark complete  
**Claim level:** toy-model methodology result only; not evidence for emergent spacetime or SoCT.

## Question

Given causal order among events, event-count information, and an independently measured propagation/clock delay, how much of a hidden flat spacetime geometry can be reconstructed without exposing coordinates to the estimator?

This simulation follows the causal-set-inspired distinction identified in the literature review:

```text
causal order -> who can influence whom
number / density -> effective interval scale
operational delay -> additional temporal scale information
```

The benchmark does **not** claim that real spacetime is generated this way.

## Model

Events are sprinkled in finite flat Minkowski boxes in:

- `1+1` dimensions (`d = 2` spacetime dimensions);
- `2+1` dimensions (`d = 3` spacetime dimensions).

For a true timelike pair `i < j`, hidden coordinates define

```math
tau_ij = sqrt(Delta t_ij^2 - r_ij^2)
```

with `c = 1`.

The estimator is not given `r_ij` or `tau_ij`.

From causal order it counts the number of observed events in the causal interval:

```math
N_ij = |{k : i < k < j}|.
```

For homogeneous event density `rho`, the flat-spacetime interval volume obeys

```math
V_d(tau) = zeta_d tau^d,
```

so the order+number estimator is

```math
tau_hat_ij = [N_ij / (rho zeta_d)]^(1/d).
```

When an operational coordinate/propagation delay `Delta t` is also available, a candidate spatial separation is reconstructed as

```math
r_hat_ij = sqrt(max(Delta t_ij^2 - tau_hat_ij^2, 0)).
```

The purpose is to test this mechanism and expose where it fails.

## Adversaries

Five scenarios are evaluated across 25 deterministic random seeds:

1. **uniform** — homogeneous event sprinkling and calibrated delay;
2. **random thinning** — roughly 45% of events are removed, then density is recalibrated from the surviving sample;
3. **density gradient** — event sampling is intentionally nonuniform while the estimator still uses one global density;
4. **shortcuts** — a small number of forward-in-time relations are added between pairs that were spacelike in the hidden Minkowski geometry, then transitive closure is restored;
5. **variable delay** — node-specific clock/propagation factors distort the raw delay; a separate calibration is also evaluated.

Interior-pair filtering reduces simple finite-box boundary bias. At most 8,000 timelike pairs per seed are scored.

Primary metrics are Spearman rank correlation with hidden proper-time or spatial separation and proper-time RMSE.

## Results — 1+1 dimensions

| Scenario | Proper-time rho: count | Proper-time rho: raw delay | Proper-time RMSE: count | Spatial rho: raw delay + count | Spatial rho: calibrated delay + count | False-causal fraction |
|---|---:|---:|---:|---:|---:|---:|
| uniform | 0.973 | 0.819 | 0.423 | 0.860 | 0.860 | 0.000 |
| random thinning | 0.950 | 0.813 | 0.557 | 0.811 | 0.811 | 0.000 |
| density gradient | 0.940 | 0.882 | 1.010 | 0.632 | 0.632 | 0.000 |
| shortcuts | 0.859 | 0.786 | 1.425 | 0.483 | 0.483 | 0.156 |
| variable delay | 0.973 | 0.712 | 0.422 | 0.529 | 0.860 | 0.000 |

Typical standard deviations across seeds were small for the uniform case (`~0.006` for count-derived proper-time rho) and larger when shortcut topology was injected (`~0.025` for proper-time rho and `~0.088` for reconstructed spatial rho).

## Results — 2+1 dimensions

| Scenario | Proper-time rho: count | Proper-time rho: raw delay | Proper-time RMSE: count | Spatial rho: raw delay + count | Spatial rho: calibrated delay + count | False-causal fraction |
|---|---:|---:|---:|---:|---:|---:|
| uniform | 0.909 | 0.688 | 0.542 | 0.906 | 0.906 | 0.000 |
| random thinning | 0.848 | 0.683 | 0.697 | 0.845 | 0.845 | 0.000 |
| density gradient | 0.848 | 0.801 | 1.339 | 0.725 | 0.725 | 0.000 |
| shortcuts | 0.746 | 0.530 | 1.300 | 0.787 | 0.787 | 0.185 |
| variable delay | 0.909 | 0.510 | 0.542 | 0.533 | 0.906 | 0.000 |

## Interpretation

### 1. Order + number carries nontrivial metric information in the clean toy model

Under homogeneous sprinkling, interval count transformed with the correct spacetime dimension and global event density tracks hidden proper time substantially better than raw coordinate delay alone:

```text
1+1: rho 0.973 versus 0.819
2+1: rho 0.909 versus 0.688
```

This is a toy demonstration of the causal-set-style `order + number` idea, not a novel spacetime-reconstruction theorem.

### 2. Delay adds a different kind of information

Count estimates timelike interval scale. Delay then helps separate temporal and spatial contributions. In the clean cases the combined reconstruction achieves spatial-distance rank correlations of approximately

```text
1+1: 0.860
2+1: 0.906.
```

Therefore causal order/count and delay are not simply interchangeable observables in this benchmark.

### 3. Random missing events are damaging but not catastrophic if density is recalibrated

After random thinning, count-derived proper-time rank correlation remains

```text
1+1: 0.950
2+1: 0.848.
```

This is consistent with the fact that random thinning changes sampling density more than the underlying causal ordering. It does **not** imply arbitrary missingness is safe.

### 4. Nonuniform density exposes a required assumption

A global-density count estimator becomes biased when event density varies over the hidden spacetime.

Although rank correlation remains moderately high, proper-time RMSE increases sharply and combined spatial reconstruction degrades, especially in `1+1`.

Therefore:

```text
interval count is not a pure distance observable;
it is a distance-times-density observable until density has been calibrated.
```

Any later geometry claim must either assume homogeneous sprinkling or estimate local/effective density independently.

### 5. Nonlocal shortcuts do not behave like ordinary noise

Injected shortcut relations change the causal order itself. After transitive closure, roughly

```text
1+1: 15.6%
2+1: 18.5%
```

of observed causal relations are absent from the original hidden Minkowski order.

Count-derived reconstruction then moves away from the original Minkowski geometry.

This should not automatically be labeled estimator failure: if shortcut relations are physically real, they define a different **effective causal geometry**. The benchmark therefore distinguishes

```text
reconstructing the geometry encoded by causal relations
from
recovering a background geometry that those relations no longer obey.
```

That distinction is important for any later SoCT interpretation.

### 6. Operational delay requires its own calibration

The variable-delay adversary leaves causal order and interval count unchanged, so count-derived proper time remains at the clean baseline.

But raw combined spatial reconstruction falls to approximately

```text
1+1: 0.529
2+1: 0.533.
```

After the imposed local clock/propagation factors are calibrated separately, spatial reconstruction returns to approximately

```text
1+1: 0.860
2+1: 0.906.
```

This mirrors the lesson from SIM-03B:

```text
measured response/delay = geometry-dependent transmission
                         x local instrument/medium properties.
```

Those factors must not be conflated.

## What survives

The strongest surviving hierarchy is now:

```text
causal order
    -> causal comparability / topology
order + calibrated event number/density
    -> timelike interval scale
+ calibrated delay / clock information
    -> additional spatial-separation information
```

No single scalar response amplitude is sufficient.

## New recursive implication

The benchmark makes the observation-resolution issue more precise.

The geometry reconstructed by an observer is conditional on which events and relations enter the record:

```math
G_hat = G_hat(O_epsilon, N_obs, rho_hat, Delta t_hat, T_obs),
```

where detection threshold, observed event count, density estimate, delay calibration, and observation horizon all affect the inferred structure.

This creates a scale/observer-resolution recursion:

```text
geometry constrains accessible causal records
    -> records determine reconstructed geometry
    -> reconstructed geometry determines which coarse causal relations are treated as local
    -> new observations refine the reconstruction.
```

This is methodological, not a claim that physical geometry literally depends on human observation.

## Failure boundaries established by SIM-04B

A causal-geometry estimator should be rejected or explicitly qualified if it:

- uses interval count without controlling event density;
- treats nonlocal shortcuts as mere measurement noise;
- uses raw propagation delay without local clock/medium calibration;
- assumes missing events are random when the missingness mechanism is structured;
- interprets reconstruction of effective causal geometry as proof of a specific underlying background geometry.

## Next step — SIM-04C

SIM-04C should compare candidate distance constructions on withheld geometry families rather than privileging the count estimator used here.

At minimum compare:

```text
D1 = inverse calibrated direct causal capacity
D2 = -log calibrated transmission
D3 = calibrated propagation delay
D4 = order + interval count / density
D5 = combined estimator trained on some geometry families and tested on unseen families
```

The required question is not "which estimator fits this simulator best?" but:

> Which causal-distance construction, if any, generalizes across dimensionality, missingness, density variation, shortcuts, and heterogeneous local dynamics?

Only after that comparison should a SoCT-specific memory field be injected into the causal/geometry layer.

## Reproduction

Run:

```bash
python experiments/observation-foundations/sim04b_order_count_delay_geometry.py --seeds 25
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim04b_order_count_delay_geometry.py --seeds 25 --json
```
