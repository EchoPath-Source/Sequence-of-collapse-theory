# Representational Novelty Mining

**Status:** exploratory hypothesis-generation method  
**Claim level:** research heuristic only  
**Epistemic rule:** source analogy is never treated as physical evidence.

## Purpose

This track tests whether deliberately distant representational domains — mythology, ancient cosmology, metaphysics, philosophy, mathematics, biology, computation, and modern physics — can generate scientifically useful structural questions that survive ordinary mathematical and empirical scrutiny.

The method does **not** assume that ancient or esoteric sources encode modern physics.

The workflow is:

```text
source structure
-> abstract relation
-> candidate scientific question
-> remove the source
-> mathematical model
-> nulls / adversaries
-> simulation or derivation
-> prior-art search
-> empirical test
```

A candidate is retained only if it remains scientifically meaningful after the originating source is deleted.

## Safeguards

1. Structural rather than lexical matching.
2. Reverse mapping: ask whether ordinary experience could naturally generate the metaphor.
3. Negative controls against unrelated source material.
4. Mathematical compression before scientific interpretation.
5. Falsification before interpretation.
6. Prior art after independently recording the generated structure.
7. No source privilege: scientific success does not validate the originating metaphysical source.

## RM-01 — surviving abstraction

The first full run progressively stripped away creation/order/observation language until the surviving scientific question was:

> Can effective geometry be reconstructed from relationships among persistent, redundantly accessible physical records?

The originating source is no longer required by the hypothesis and is not used as evidence.

The benchmark series is stored at:

```text
experiments/observation-foundations/rm01-record-geometry/
```

## Simulation ladder

### RM-01 — metric gate

```text
structured local persistent record overlap -> recoverable hidden geometry
scrambled/global record controls            -> no recovery
binary variation-of-information             -> fails
Jaccard support distance                     -> survives
```

### RM-01B — geometry-family transfer

The same Jaccard reconstruction generalizes across cycle, torus, irregular, bottleneck, shortcut, and variable-speed substrates.

Record relations track effective propagation geometry more strongly than background embedding when genuine low-cost shortcuts are introduced.

### RM-01C — remove global distance from record generation

Records arise only from repeated local transition dynamics:

```text
local edge rules
-> propagated influence
-> persistent records
-> recoverable relational geometry
```

No all-pairs distance or coordinate is used to generate record probability.

### RM-01D — higher structure

A reconstruction supplied only with persistent record supports recovers:

```text
mean local direct-edge ROC AUC  = 0.978
scrambled/global edge ROC AUC   = ~0.505
bottleneck partition ARI        = 1.000
shortcut closeness percentile   = 0.996
```

An equal-size / fixed-record-density suite preserves:

```text
cycle < 2-D < 3-D
```

in `30/30` local seeds, compared with `6/30` scrambled and `0/30` global controls.

### RM-01E — pre-geometric model competition

Every run begins from a coordinate-free 64-node degree-4 random regular relation graph.

Memory-only, triadic-closure, and random update rules compete.

Persistent records continue to encode the evolved graph strongly, but naive accumulated-memory reinforcement does **not** select low-dimensional geometry; block/community structure wins on average.

Coordinate-free triadic closure behaves differently:

```text
Euclidean 1D AUC = 0.885
Euclidean 2D AUC = 0.905
Euclidean 3D AUC = 0.925
Euclidean 8D AUC = 0.930
```

The surviving lesson is:

```text
persistent memory encodes relational topology
+
local relational consistency / closure can organize topology into a geometry-like regime
```

rather than:

```text
memory magnitude -> geometry
```

### RM-01F — matched present / different history

Two branches begin from the exact same present graph and the same event multiset, but the past temporal order is reversed.

History-insensitive controls remain identical.

A memory-sensitive update produces future divergence, but a node-permuted hidden kernel can produce even larger raw divergence. Therefore raw hysteresis is rejected as a memory-specific signature.

The accepted statistic is history-aligned geometry:

```text
true H_geo     = 0.0297 hops
permuted null  = 0.0108 hops
paired p       = 0.02197
```

This provides the first toy demonstration of the causal direction:

```text
same present
+ different temporal history
-> different persistent relational memory
-> history-specific future geometry
```

### RM-01G — local action principle

RM-01G replaces the hand-designed memory-weighted closure score with one scalar objective:

```math
S[G,K_M]
=
-\alpha N_\triangle(G)
-\beta\sum_{(i,j)\in E(G)}\widehat K_M(i,j),
```

subject to fixed degree, fixed edge count, and connectivity.

Local double-edge swaps are accepted only when they lower `S`.

After exploratory selection on seeds `0-99`, `beta=0.10` was frozen and tested on 300 fresh seeds `2000-2299`.

All history-insensitive controls remain exactly zero-divergence:

```text
ordinary triangle action        = 0.000
instantaneous-state action      = 0.000
scalar-memory-amplitude action  = 0.000
paired random action            = 0.000
```

The scalar control is particularly important: equal total memory magnitude cannot distinguish the futures.

Held-out history-specific response:

```text
H_geo true       = 0.20095 +/- 0.20042 hops
H_geo permuted   = 0.00527 +/- 0.12824 hops
paired p         = 4.70e-35
```

A triangle/Forman-style graph-curvature proxy also shows a localized history-aligned redistribution:

```text
memory/curvature alignment      = -0.11015
permuted-memory null            = -0.00988
paired p                        = 4.34e-13
```

The sign is model-specific and is **not** interpreted as physical Ricci curvature.

The surviving RM-01G chain is:

```text
past temporal ordering
-> persistent relational memory K_M
-> local scalar action S[G,K_M]
-> action-lowering relational dynamics
-> history-specific metric deformation
-> localized curvature-like graph response
```

### RM-01H — transferability gate

RM-01H asks whether the RM-01G action defines one transferable coarse-grained response across changing size, degree, memory persistence, and network topology.

The raw coupling `beta` fails immediately as an intensive parameter because the triangle term changes in discrete units whose leverage depends strongly on degree and topology.

A proposal-level dimensionless coupling was therefore defined:

```math
\lambda_{eff}
= \beta\,
\frac{\sigma(\Delta K_M)}
{\alpha\,\sigma(\Delta N_\triangle)}.
```

RM-01H also corrected two explicit finite-size artifacts:

```text
history events scale with source-group size
accepted-improvement update budget scales with edge count
```

A two-parameter threshold response fitted only on `n=48/64` regular graphs achieved:

```text
training R^2 = 0.8024
training MAE = 0.01594
```

but failed on fresh `n=80/96` systems with frozen parameters:

```text
holdout R^2 = -0.8784
holdout MAE = 0.03876
```

A focused topology holdout at the frozen baseline coupling also fails:

```text
random regular: H_geo = 0.1687 +/- 0.1751, p = 0.00224
small-world:    H_geo = 0.0698 +/- 0.3090, p = 0.396
ring lattice:   H_geo = 0.0000 in 15/15 seeds
```

Therefore RM-01H is intentionally recorded as a **failed transfer gate**.

The current action is a genuine finite-network history-dependent geometry mechanism, but it is not yet a transferable constitutive law.

The most likely failure is structural: a raw global triangle-count term and a normalized continuous memory term do not define one common local intensive energy density across graph families/discretizations.

## Relationship to SoCT

Representational Novelty Mining remains upstream of SoCT interpretation.

The relevant existing SoCT ladder is:

```text
quantum interaction
-> distinguishable record
-> persistent accessible record
-> observation / record-production functional
-> candidate SoCT memory source
-> memory dynamics
-> open spacetime bridge
```

RM-01A-H do **not** establish the SoCT-specific gravity step.

What they motivate is a relational memory object such as:

```math
K_M(i,j,t),
```

rather than relying only on a scalar `M(x,t)`.

The most defensible current inference is:

```text
structured relational memory
+ local consistency dynamics
can produce history-specific effective-geometry response in toy networks,
but the first finite-network action does not transfer as a continuum law.
```

## Current claim boundary

Do not claim that RM-01 derives:

- spacetime;
- 3+1 dimensions;
- Lorentzian signature;
- physical curvature;
- Einstein equations;
- stress-energy conservation;
- lensing/geodesic dynamics;
- or evidence for a real SoCT memory field.

RM-01H specifically blocks promotion of RM-01G to a weak-field continuum/gravity analogy.

## Next gate — RM-01I

Repair the **action**, not the failed response curve.

The next candidate should use genuinely local/intensive quantities, schematically:

```math
S = \sum_i s_i,
```

with a normalized local density such as

```math
s_i
= -\alpha C_i
- \beta\frac{1}{d_i}\sum_{j\in N(i)}\widehat K_M(i,j),
```

where `C_i` is a local closure or curvature-like density rather than raw global triangle count.

RM-01I must repeat the matched-present/reversed-history test and require positive held-out transfer across size, degree, memory scale, and topology before any continuum analogy is reconsidered.
