# RM-01B — Cross-Family Persistent-Record Geometry Stress Test

**Status:** complete first cross-family benchmark  
**Track:** observation foundations / representational novelty mining  
**Claim level:** toy-model methodology only; not evidence for SoCT or emergent spacetime.

## Question

Does the RM-01 support-overlap reconstruction survive qualitatively different hidden geometries without changing the reconstruction metric?

RM-01B fixes Jaccard distance as the primary candidate and tests:

```text
cycle
periodic torus
irregular geometric graph
bottleneck graph
nonlocal-shortcut graph
variable-speed graph
```

The reconstruction algorithm receives only persistent record supports. It is not given node coordinates, family labels, or hidden distances.

## Record generation

For every family, record probability is generated from the family's effective propagation distance:

```math
p_{if} = b \exp[-d_eff(i,f)/\ell].
```

The strong regime is fixed at:

```text
broadcast b   = 1.0
persistence q = 0.95
8 record fragments per hidden node
30 independent seeds
```

The record-spread scale is `1.6` times the median nearest-neighbor effective distance of the generated substrate. This rescales the *generator* to each graph's natural unit; it does not tune the reconstruction metric.

## Controls

Each family is tested in three modes:

1. **local** — record support follows effective propagation distance;
2. **scrambled** — each source retains the same probability multiset, but fragment assignments are shuffled;
3. **global** — the same mean record density is broadcast homogeneously.

Therefore a positive result must depend on structured relational support, not merely the number of records.

## Results

Primary Jaccard recovery against effective hidden distance:

| family | local rho | scrambled rho | global rho | local 4-NN |
|---|---:|---:|---:|---:|
| cycle | **0.779 +/- 0.009** | -0.010 | 0.003 | **0.873** |
| torus | **0.823 +/- 0.010** | -0.002 | -0.003 | **0.635** |
| irregular | **0.774 +/- 0.041** | 0.071 | 0.065 | **0.776** |
| bottleneck | **0.916 +/- 0.004** | 0.022 | 0.035 | **0.673** |
| shortcut | **0.752 +/- 0.011** | 0.099 | 0.089 | **0.577** |
| variable speed | **0.761 +/- 0.057** | 0.084 | 0.081 | **0.778** |

Across the six local families:

```text
mean Jaccard rho ~= 0.801
mean 4-NN recovery ~= 0.719
```

Across the same families:

```text
mean scrambled Jaccard rho ~= 0.044
mean global Jaccard rho    ~= 0.045
```

The cross-family result therefore survives the first generalization gate.

## Effective versus background geometry

Two adversarial families separate the effective propagation metric from a simpler background geometry.

### Nonlocal shortcuts

Records are generated using real low-cost shortcut edges.

```text
Jaccard vs effective geometry   rho = 0.752
Jaccard vs background geometry  rho = 0.590
```

The record structure follows the effective propagation geometry more closely than the background geometry.

### Variable propagation speed

The same geometric graph is given heterogeneous edge speeds.

```text
Jaccard vs effective geometry   rho = 0.761
Jaccard vs background geometry  rho = 0.724
```

The separation is smaller, but again the record-support relation tracks the effective path metric more closely.

This suggests the reconstruction is not necessarily recovering an externally privileged embedding. It is recovering the geometry of the process that actually propagates records.

## Metric comparison

Jaccard remains the strongest general simple candidate.

Hamming works well on some regular/high-density families but degrades sharply on irregular and variable-speed families.

Binary variation of information remains unreliable:

```text
cycle          VI rho =  0.158
torus          VI rho =  0.016
irregular      VI rho = -0.186
bottleneck     VI rho = -0.097
shortcut       VI rho = -0.220
variable speed VI rho = -0.188
```

RM-01's rejection of binary VI therefore survives the cross-family test.

## What RM-01B establishes

Only the following limited statement is supported:

> A fixed support-overlap metric can recover substantial information about several different effective propagation geometries when persistent records are produced locally with respect to those geometries.

It also supports:

> Matched record abundance without structured locality is insufficient.

## What RM-01B does not establish

There is a major remaining limitation:

```text
the record generator still explicitly uses hidden effective distance
```

Therefore a successful reconstruction is still, at some level, recovering the locality kernel that generated the data.

RM-01B shows that this is not peculiar to one square lattice, but it does **not** yet show geometry emerging from dynamics that lack an explicitly supplied distance-decay rule.

That becomes the next gate.

## RM-01C — dynamic propagation gate

Replace

```math
p(record) = exp[-d/ell]
```

with actual local dynamics, for example:

```text
random-walk diffusion
finite-speed stochastic propagation
local copying with loss
graph-wave / epidemic-style spread
```

The simulation should supply only local transition rules. Distance should never appear in the record-generation probability.

Then ask whether record-support relations recover:

```text
effective distance
topology
dimension
bottlenecks
nonlocal shortcuts
```

If they do, the claim becomes stronger:

```text
local dynamics
-> persistent records
-> relational support structure
-> recoverable effective geometry
```

If they do not, RM-01/B should be interpreted only as kernel inversion rather than an emergent-geometry mechanism.

## Reproduction

```bash
python experiments/observation-foundations/rm01-record-geometry/rm01b_heldout_geometries.py \
  --seeds 30
```
