# RM-01E — Pre-geometric relational dynamics and model competition

**Status:** completed first-pass toy benchmark  
**Claim level:** methodology / toy-model result only  
**Not evidence for:** SoCT, physical spacetime emergence, or a gravity-as-memory mechanism.

## Question

Can a coordinate-free relational system evolve under local rules so that its persistent records are well described by a stable low-dimensional geometry, without inserting coordinates or a geometric distance into the generator?

RM-01A-D began from a supplied substrate graph. RM-01E removes the familiar substrate-family assumption and instead begins from a random regular relation network.

## Generator

All runs use 64 nodes with degree 4. No coordinates are assigned.

Three degree-preserving local update rules are compared:

1. **memory** — repeated local random-walk pulses create an accumulated co-exposure matrix; double-edge swaps are accepted when they increase remembered co-exposure while keeping the graph connected;
2. **triadic** — common-neighbor closure guides the same degree-preserving swaps;
3. **random** — random symmetric swap preferences provide the topology null.

After evolution, persistent binary records are generated only from local diffusion on the final graph. Jaccard record distance is used to test whether those records recover direct relations.

## Model competition

The evolved graph has no family label or coordinates. Fifteen percent of non-bridge edges are held out together with a matched number of nonedges. Candidate descriptions are fit on the remaining relation graph and scored by held-out ROC AUC.

Candidates:

```text
Euclidean latent: 1D, 2D, 3D, 8D
Poincare / hyperbolic: 2D
generic low-rank latent: rank 8
block/community: k = 2, 4, 8
common-neighbor / small-world proxy
tree/path-distance proxy
degree-only baseline
```

The model competition is a structural diagnostic, not a formal Bayesian model-evidence calculation. Higher-dimensional models have more flexibility; therefore the strongest geometric result is when low-dimensional Euclidean models are competitive or win without a complexity advantage being granted to them.

## 30-seed result

### Record reconstruction

Persistent records continue to encode the evolved relation graph strongly:

```text
memory   record-edge ROC AUC = 0.970 +/- 0.012
triadic  record-edge ROC AUC = 0.994 +/- 0.004
random   record-edge ROC AUC = 0.961 +/- 0.012
```

This is expected to some degree: diffusion records local interaction topology. The emergence question is therefore not whether records can recover a graph, but what structural class the graph evolves toward.

### Held-out model prediction

Mean held-out ROC AUC:

| Model | memory | triadic | random |
|---|---:|---:|---:|
| Euclidean 1D | 0.563 | 0.885 | 0.442 |
| Euclidean 2D | 0.558 | 0.905 | 0.409 |
| Euclidean 3D | 0.585 | 0.925 | 0.375 |
| Euclidean 8D | 0.591 | 0.930 | 0.334 |
| Hyperbolic 2D | 0.557 | 0.908 | 0.346 |
| Generic low-rank 8 | 0.612 | 0.911 | 0.488 |
| Block 8 | **0.647** | 0.916 | 0.481 |
| Small-world CN | 0.586 | 0.896 | 0.481 |
| Tree/path | 0.591 | 0.912 | 0.368 |

The random rule remains near chance for most structural models.

The naive memory-reinforcement rule does **not** produce a clear low-dimensional geometric winner. Its strongest mean model is the block/community family.

The triadic-closure rule is qualitatively different. Euclidean latent models are highly predictive, with 3D AUC `0.925 +/- 0.045` and 8D AUC `0.930 +/- 0.042`. Low-dimensional Euclidean models (1D/2D/3D) are the best raw-AUC model in `18/30` seeds; including Euclidean 8D raises Euclidean-family wins to `21/30`.

### Topological diagnostics

```text
                    clustering     mean path     diameter     growth exponent
memory                 0.156          3.447          6.2          1.634
triadic                0.610          6.967         15.7          1.041
random                 0.041          3.167          5.4          1.742
```

The triadic system develops high local closure, long mesoscale paths, and near-linear ball-volume growth. This is consistent with an emergent low-dimensional, chain/filament-like relational organization rather than a random-regular small-world topology.

## Main result

RM-01E does **not** support the claim

```text
memory alone -> geometry
```

The stronger surviving statement is:

```text
persistent records faithfully encode relational topology,
but low-dimensional geometric organization requires additional structural constraints.
```

In this benchmark, a local consistency/closure rule is sufficient to produce a coordinate-free relational network that is strongly compressible by low-dimensional Euclidean latent models.

This suggests a more specific candidate mechanism:

```text
local interaction
-> persistent record / memory
-> transitive relational closure or consistency
-> stable neighborhoods
-> low-dimensional effective geometry
```

rather than

```text
memory magnitude -> geometry.
```

## Relation to gravity-as-memory

The result is relevant to the SoCT gravity-as-memory program only at the level of mechanism design.

If memory is to participate in geometry, the fundamental object may need to include relational consistency or closure, for example a memory kernel

```math
K_M(i,j,t)
```

rather than only a scalar memory amplitude `M(x,t)`.

A future geometry map would then schematically take the form

```math
g^{eff} = G[K_M]
```

with the crucial additional requirement that `K_M` evolve under local consistency rules capable of producing metric structure.

RM-01E does not yet provide a relativistic metric, curvature tensor, Lorentzian signature, Einstein dynamics, or a physical source law.

## Failure / caution

1. Triadic closure is itself a strong structural prior. The result shows that geometry-like organization can emerge without coordinates, not that geometry emerges from arbitrary local dynamics.
2. Euclidean 8D slightly exceeds 3D in mean AUC, so continuum 3+1-dimensional spacetime is not derived.
3. The graph is fixed-size and degree-preserving.
4. The model competition is predictive but not a formal minimum-description-length or Bayesian evidence calculation.
5. No Lorentzian causal structure is present.
6. No SoCT-specific memory-field feedback into geometry is used.

## Next gate — RM-01F

The next simulation should combine the two ingredients that RM-01E separated:

```text
persistent accumulated memory
+
local relational closure
```

and test whether a memory-dependent closure law can produce and then **dynamically deform** an effective geometry.

The critical comparison should be:

```text
ordinary triadic closure
vs
memory-weighted closure
vs
instantaneous-state closure
vs
random rewiring
```

A gravity-as-memory toy signature would require the memory-weighted system to show a reproducible history-dependent geometric residual after present-state observables are matched.

That would finally test the causal direction needed by the theory:

```text
past history -> persistent memory -> changed future relational geometry.
```
