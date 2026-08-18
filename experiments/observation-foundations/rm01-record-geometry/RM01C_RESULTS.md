# RM-01C — Dynamic Local-Propagation Record Geometry

**Status:** first dynamic-propagation gate complete  
**Track:** observation foundations / representational novelty mining  
**Claim level:** toy-model methodology only; not evidence for SoCT or emergent spacetime.

## Question

Can persistent record relationships recover useful geometry when the record generator never uses global distance?

RM-01 and RM-01B used:

```math
p(record) \propto \exp[-d/\ell].
```

That left an important loophole: successful reconstruction could be interpreted as inversion of the same distance kernel used to generate the records.

RM-01C removes that kernel.

## Dynamic generator

For each graph, local edge conductance is defined only from the local edge cost:

```math
w_{uv} = 1/c_{uv}.
```

A row-normalized lazy transition matrix is then constructed:

```math
P = (1-\lambda)D^{-1}W + \lambda I,
```

with `lambda = 0.25`.

Starting from a source-localized state:

```math
p_0 = delta_source,
```

the signal propagates only by repeated local transitions:

```math
p_{t+1} = p_t P.
```

Cumulative local exposure is:

```math
E = sum_t gamma^t p_t,
```

with 10 propagation steps and `gamma = 0.90`.

A fragment records according to:

```math
p_record = 1 - exp(-g E),
```

with `g = 1.5`, followed by persistence `q = 0.95`.

**No all-pairs distance or global coordinate enters record generation.**

Global distance is computed only afterward as an evaluation target.

## Families

The same six families from RM-01B are used:

```text
cycle
torus
irregular
bottleneck
shortcut
variable speed
```

Each is tested under:

```text
local dynamic propagation
scrambled-record null
homogeneous global-record null
```

with 30 independent seeds.

## Primary result

Jaccard record-support distance versus the supplied effective shortest-path geometry:

| family | local rho | scrambled rho | global rho | 4-NN recovery |
|---|---:|---:|---:|---:|
| cycle | **0.829** | -0.002 | -0.005 | **0.931** |
| torus | **0.835** | 0.000 | -0.001 | **0.672** |
| irregular | **0.875** | 0.033 | 0.045 | **0.748** |
| bottleneck | **0.932** | 0.008 | 0.011 | **0.661** |
| shortcut | **0.749** | 0.004 | -0.004 | **0.645** |
| variable speed | **0.854** | 0.026 | 0.038 | **0.734** |

Across local families:

```text
mean Jaccard rho ~= 0.846
```

Across controls:

```text
mean scrambled rho ~= 0.012
mean global rho    ~= 0.014
```

Thus the support-overlap signal survives removal of the explicit global distance-decay generator.

## A more natural dynamic geometry

Because records now arise from a random-walk-like process, ordinary weighted shortest-path distance is not necessarily the most natural target.

Define a local transition-path cost:

```math
c^{dyn}_{uv} = -\log P_{uv}.
```

The corresponding symmetrized most-probable-path distance is constructed only for evaluation.

For the local regime:

| family | Jaccard vs shortest-path | Jaccard vs dynamic-path |
|---|---:|---:|
| cycle | 0.829 | 0.829 |
| torus | 0.835 | 0.835 |
| irregular | 0.875 | **0.889** |
| bottleneck | **0.932** | 0.923 |
| shortcut | 0.749 | **0.776** |
| variable speed | 0.854 | **0.886** |

The dynamic-path target is particularly better for irregular, shortcut, and variable-speed substrates.

This suggests an important refinement:

> Persistent records appear to reconstruct the geometry of the process that propagates them, which need not be identical to a naive background or shortest-path geometry.

## Shortcut result

For the nonlocal-shortcut family:

```text
Jaccard vs background geometry      rho = 0.725
Jaccard vs effective shortest path  rho = 0.749
Jaccard vs dynamic path geometry    rho = 0.776
```

The ordering is consistent with record structure following the actual local transition process rather than the original background embedding.

## Variable-speed result

For heterogeneous local speeds:

```text
Jaccard vs effective shortest path  rho = 0.854
Jaccard vs background geometry      rho = 0.865
Jaccard vs dynamic path geometry    rho = 0.886
```

This is also a useful negative correction: the originally labeled `effective shortest-path` metric is not always the best description of the record dynamics.

The record geometry is more accurately tied to transition probabilities.

## What has changed from RM-01/B

The surviving chain has strengthened from:

```text
distance kernel
-> persistent records
-> recovered distance
```

to:

```text
local interaction rules
-> propagated influence
-> persistent records
-> relational support geometry
```

That is a materially stronger toy result because global distance is no longer required to create the records.

## What RM-01C still does not establish

The substrate graph and its local edge properties are still supplied.

Therefore RM-01C does **not** show:

```text
records create geometry from nothing
```

It shows:

```text
records can encode/reconstruct geometry implicit in local relational dynamics
```

This distinction is essential.

The current result is best understood as a candidate bridge:

```text
local causal dynamics
-> persistent record structure
-> recoverable effective geometry
```

not as a derivation of physical spacetime.

## Next gate: RM-01D

The next experiment should ask whether the record network can recover higher-level geometric properties without being told the substrate family:

```text
topological dimension / spectral dimension
local neighborhood structure
bottleneck locations
shortcut relations
curvature-like graph diagnostics
```

A stronger version should generate a pre-geometric interaction network using only local relational rules, then ask whether a low-dimensional effective geometry appears in its persistent-record structure.

That would begin addressing the harder question:

> Can geometry emerge as a useful compressed description of record-producing relational dynamics, rather than merely being reconstructed from an already geometric substrate?

## Reproduction

```bash
python experiments/observation-foundations/rm01-record-geometry/rm01c_dynamic_propagation.py \
  --seeds 30
```
