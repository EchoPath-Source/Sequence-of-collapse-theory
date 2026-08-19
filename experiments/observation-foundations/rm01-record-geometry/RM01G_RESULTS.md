# RM-01G — Local-action memory/geometry response

**Status:** completed first-pass + held-out toy benchmark  
**Claim level:** methodology / toy-model result only  
**Not evidence for:** SoCT, physical spacetime curvature, Einstein dynamics, or a physical gravity-as-memory mechanism.

## Question

Can the RM-01F matched-present / different-history geometric residual be reproduced when the forward update is not a hand-designed memory-weighted closure score, but instead follows one scalar local action / energy objective?

The target chain is:

```text
same present relational state
+ different persistent histories
-> different K_M
-> local action S[G,K_M]
-> action-lowering local updates
-> history-specific effective-geometry response
```

## Matched-present construction

RM-01G retains the RM-01F construction. For every seed:

```text
G_A(t0) = G_B(t0) exactly
same 64 nodes
same degree-4 edge set
same event multiset
opposite temporal ordering
no active source at t0
||K_A||_F = ||K_B||_F = 1
```

Thus the observable present graph and scalar memory norm are matched. Only the relational organization of persistent memory differs.

## Local action

The forward law is derived from

```math
S[G,K_M]
=
-\alpha N_\triangle(G)
-\beta \sum_{(i,j)\in E(G)} \widehat K_M(i,j),
```

subject to:

```text
fixed node count
fixed degree sequence
fixed edge count
graph connectivity
```

where `N_triangle(G)` is the number of local triangles / closed relational triples and `Khat_M` is the z-scored off-diagonal persistent memory kernel.

Frozen parameters:

```text
alpha = 1.0
beta  = 0.10
10 epochs
4 accepted-improvement attempts per epoch
```

`beta` was explored only on seeds below 100 and then frozen.

A degree-preserving double-edge swap is accepted only when it lowers `S`. The code evaluates the exact local action change from destroyed/created triangles plus removed/added memory-alignment terms. A direct audit on seed 2000 verified that the accumulated accepted local gains equal the total action drop to floating-point precision.

## Controls

The same paired common-random-number update machinery is used for:

```text
ordinary triangle action
instantaneous-state kernel action
scalar-memory-amplitude action
paired random action
```

The scalar-memory control is important. Because the two histories are normalized to the same total memory strength and the graph has fixed edge count, a uniform scalar memory amplitude adds only a constant to the action and cannot select one geometry over another.

A node-permuted memory kernel provides the arbitrary latent-state / hidden-structure null. It preserves the memory matrix value structure under relabeling while destroying alignment with the actual source history.

## Predeclared geometry statistic

RM-01G retains the RM-01F directional statistic:

```math
\Delta K_{ij}=K_A(i,j)-K_B(i,j),
```

```math
\Delta d_{ij}=d_B(i,j)-d_A(i,j).
```

For the upper and lower 10% of `Delta K`:

```math
H_{geo}=
\frac12[
\langle \Delta d \rangle_{top}
-
\langle \Delta d \rangle_{bottom}
].
```

Positive `H_geo` means relations preferentially remembered by a history become relatively closer in that history's future graph geometry.

## Curvature-like localization diagnostic

RM-01G adds a triangle-augmented Forman-style graph diagnostic:

```math
\kappa_{uv}=4-d_u-d_v+3T_{uv},
```

where `T_uv` is the number of shared neighbors of edge `(u,v)`. Node curvature is the mean incident edge value.

The localization statistic is:

```text
Spearman(
    node memory contrast,
    future node-curvature contrast
)
```

This is only a graph curvature proxy. Its sign has no direct interpretation as physical Ricci curvature.

## Exploratory freeze

On seeds `0-99`, after selecting `beta = 0.10`:

```text
H_geo                         =  0.214 hops
permuted-memory H_geo         = -0.012 hops

curvature alignment           = -0.156
permuted curvature alignment  =  0.001
```

The parameter was then frozen.

## Held-out validation

A fresh **300-seed holdout** used seeds `2000-2299`.

### Present-state / scalar controls

All paired history-insensitive controls remain exactly identical:

```text
ordinary triangle action edge divergence        = 0.000
instantaneous-state action edge divergence      = 0.000
scalar-memory-amplitude edge divergence         = 0.000
paired random action edge divergence            = 0.000
```

This confirms that reversed history alone does not alter the future unless relational persistent memory enters the action.

### Memory-action future divergence

```text
edge Jaccard divergence
= 0.7070 +/- 0.0574

metric divergence (1 - path-distance rho)
= 0.8245 +/- 0.0664

mean absolute shortest-path difference
= 1.2649 +/- 0.1047 graph hops
```

The memory-action branches therefore develop substantially different future relation and metric structure from the same present graph.

The accepted action-lowering updates accumulate a positive mean decrease in `S`:

```text
branch A accepted action gain = 28.47 +/- 3.08
branch B accepted action gain = 28.17 +/- 2.94
```

### History-specific geometric residual

True remembered history:

```text
H_geo
= 0.20095 +/- 0.20042 graph hops

95% CI
= [0.17817, 0.22372]
```

Node-permuted memory evaluated against the actual history:

```text
H_geo,null
= 0.00527 +/- 0.12824 graph hops

95% CI
= [-0.00930, 0.01984]
```

Held-out tests:

```text
true H_geo vs zero:
t(299) = 17.366
p = 3.38e-47

paired true vs permuted-memory:
t(299) = 14.124
p = 4.70e-35
```

### Localized curvature-like response

True history:

```text
memory / curvature alignment
= -0.11015 +/- 0.16737

95% CI
= [-0.12917, -0.09114]
```

Permuted-memory null:

```text
alignment_null
= -0.00988 +/- 0.15258

95% CI
= [-0.02722, 0.00745]
```

Held-out tests:

```text
true alignment vs zero:
t(299) = -11.399
p = 3.08e-25

paired true vs permuted-memory:
t(299) = -7.581
p = 4.34e-13
```

The sign is model-specific. The accepted statement is only that the actual remembered history predicts a reproducible localized redistribution in a curvature-like graph diagnostic that is absent under memory relabeling.

## Main result

RM-01G survives the key gate:

```text
past temporal ordering
-> persistent relational memory K_M
-> one scalar local action S[G,K_M]
-> local action-lowering updates
-> history-specific future metric deformation
-> localized curvature-like graph response
```

This is stronger than RM-01F because the future rule is no longer a directly constructed memory-weighted closure score. Triangle closure and memory alignment enter as terms in a scalar objective, and local graph evolution follows only the sign of the action variation.

## What the scalar control tells us

The result explicitly rejects:

```text
memory magnitude alone -> geometry
```

Equal-norm scalar memory cannot distinguish the two futures.

The surviving candidate is relational:

```text
structured K_M(i,j)
+ local consistency dynamics
-> geometry-sensitive response
```

This strengthens the motivation for treating the SoCT memory variable as potentially containing a relational kernel component rather than only a scalar `M(x,t)`.

## Claim boundary

RM-01G does **not** derive:

- physical spacetime;
- Lorentzian signature;
- a metric tensor `g_mu_nu`;
- Einstein field equations;
- stress-energy conservation;
- physical Ricci curvature;
- gravitational acceleration, lensing, or geodesics;
- a microscopic SoCT source law;
- or evidence that nature contains `K_M`.

The action itself is still phenomenological. The memory coupling term has been posited, not derived from a quantum or covariant theory. The triangle term is also a structural prior favoring relational closure.

## Methodological lesson

Raw path dependence is still insufficient. The important signature is:

```text
history-specific structured residual
>
arbitrary latent-state / memory-permutation residual
```

with matched present observables and frozen parameters.

This should remain a requirement for later SoCT galaxy/cosmology tests.

## Validation provenance

```text
exploratory parameter selection:
seeds 0-99

frozen beta:
0.10

held-out validation:
seeds 2000-2299

three packaged 100-seed runs:
2000-2099
2100-2199
2200-2299

script:
python -m py_compile rm01g_local_action_memory_geometry.py

smoke:
python rm01g_local_action_memory_geometry.py --seed-start 2000 --seeds 3
```

The three packaged held-out batches reproduce the combined 300-seed statistics reported here.

## Next gate — RM-01H

RM-01G now provides a scalar relational action but remains a finite graph model.

The next gate should ask whether its history-dependent response admits a stable coarse-grained constitutive description that generalizes across graph size and degree.

Candidate program:

```text
K_M
-> local action density
-> coarse-grained memory density / memory strain
-> fitted metric-response susceptibility
-> held-out size / topology transfer
```

Required tests:

1. train a response law on some graph sizes and test on unseen sizes;
2. vary degree and memory lengthscale without refitting the response coefficients;
3. compare scalar-memory, relational-memory, instantaneous-medium, and arbitrary latent-state nulls;
4. test whether the response is approximately local and additive at weak coupling;
5. identify the weak-coupling regime where `Delta geometry` is linear in memory contrast;
6. only if those gates pass, attempt a weak-field continuum analogy.

The key next question is whether RM-01G is merely a successful finite-network mechanism or the discrete limit of a transferable constitutive memory-to-geometry law.
