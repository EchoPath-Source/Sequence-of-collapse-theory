# RM-01F — Matched-present / different-history memory-geometry evolution

**Status:** completed first-pass + held-out toy benchmark  
**Claim level:** methodology / toy-model result only  
**Not evidence for:** SoCT, physical spacetime curvature, Einstein dynamics, or a physical gravity-as-memory mechanism.

## Question

Can two systems with the **same observable present relational state** but different persistent histories evolve into measurably different future relational geometries when the update law is memory-sensitive?

The target causal pattern is:

```text
same present graph
+ different past temporal ordering
-> different persistent memory kernel
-> different future relational geometry
```

A positive result is meaningful only if ordinary present-state controls do not diverge and if the future deformation retains some directional relationship to the actual remembered history rather than merely responding chaotically to any hidden perturbation.

## Matched-present construction

Each seed begins from the same 64-node degree-4 random regular present graph `G0`.

Two past histories are built from the **same multiset of source events** but in opposite temporal order:

```text
history A: source-group A old -> source-group B recent
history B: source-group B old -> source-group A recent
```

The source histories are compressed into exponentially decayed co-exposure kernels `M_A` and `M_B`.

At the forward-test boundary:

```text
G_A(t0) = G_B(t0) exactly
active source_A(t0) = active source_B(t0) = none
||M_A||_F = ||M_B||_F = 1
```

Thus degree sequence, edge set, clustering, path structure, and all graph observables are identical at `t0`. Only the persistent history kernel differs.

## Forward rules

Paired branches use common random numbers.

Controls:

```text
ordinary triadic closure
instantaneous-state closure
paired random rewiring
```

Test rule:

```text
memory-weighted closure
```

The memory term acts only on candidate missing relations; existing present links are zeroed inside the memory bias so the current graph itself is not double-counted.

A specificity null uses a node-permuted version of each memory kernel. This preserves the kernel's value distribution, Frobenius norm, symmetry, and matrix structure under relabeling while destroying alignment with the actual source history.

## Primary metrics

### Edge divergence

```text
1 - Jaccard(E_A, E_B)
```

### Metric divergence

```text
1 - Spearman(d_A, d_B)
```

using all-pairs graph shortest-path distances.

### History-aligned geometric residual

For each pair `(i,j)` define

```text
Delta M_ij = M_A(i,j) - M_B(i,j)
Delta d_ij = d_B(i,j) - d_A(i,j)
```

so positive `Delta d` means the pair ends closer in future A.

The primary history-direction statistic compares the top and bottom 10% of `Delta M`:

```text
H_geo =
  0.5 * [
      mean(Delta d | top 10% Delta M)
    - mean(Delta d | bottom 10% Delta M)
  ]
```

Positive `H_geo` means pairs preferentially remembered by one history become relatively closer in that history's future geometry.

## Exploratory tuning and held-out validation

The memory coupling was explored on seeds below 300.

After fixing the forward parameters (`memory_beta = 2`, 10 epochs, 4 attempted accepted-improvement swaps per epoch), the primary validation was run on **300 fresh seeds: 300-599**.

The reported inferential statistics below refer only to that held-out seed range.

## Held-out result — 300 seeds

### Present-state controls

Under paired common randomness:

```text
ordinary triadic closure edge divergence      = 0.000
instantaneous-state closure edge divergence   = 0.000
paired random rewiring edge divergence        = 0.000
```

This is the required matched-present sanity check: when the hidden history is not used, opposite past order alone cannot change the future.

### Memory-weighted future divergence

```text
edge Jaccard divergence
= 0.480 +/- 0.210

metric divergence (1 - shortest-path Spearman)
= 0.572 +/- 0.229

mean absolute shortest-path difference
= 0.703 +/- 0.269 graph hops
```

Thus the same present graph develops substantially different future relation and distance structure when the persistent history kernel participates in the update law.

### Generic hidden-kernel null

The node-permuted-memory null diverges even more strongly:

```text
edge divergence
= 0.734 +/- 0.057

metric divergence
= 0.842 +/- 0.063
```

This is an important caution.

It means that **raw future divergence is not a memory-specific signature**. A sufficiently structured arbitrary hidden perturbation can also drive strong path-dependent rewiring.

Therefore the benchmark does not accept:

```text
different hidden state -> different geometry
```

as evidence for a meaningful memory-geometry map.

### History-specific directional residual

The more selective statistic is `H_geo`.

True remembered history:

```text
H_geo = 0.0297 +/- 0.0910 graph hops
95% CI = [0.0194, 0.0401]
```

Node-permuted memory evaluated against the actual history:

```text
H_geo,null = 0.0108 +/- 0.1064 graph hops
95% CI = [-0.0012, 0.0229]
```

Tests on the held-out 300 seeds:

```text
true H_geo vs zero:
t(299) = 5.655
p = 3.63e-08

paired true H_geo vs permuted-memory null:
mean difference = 0.0189 graph hops
95% CI = [0.00275, 0.0350]
t(299) = 2.303
p = 0.02197
```

The effect is therefore **small but reproducible in this toy system**.

The appropriate statement is:

> After matching the entire present graph and using the same event multiset in reversed temporal order, a memory-sensitive closure law produces future geometric differences that retain a weak but statistically reproducible directional signature of the actual past ordering. A relabeled hidden-memory kernel produces larger generic divergence but a weaker history-aligned residual.

## What survived

RM-01F supports the toy causal chain:

```text
past temporal order
-> persistent relational memory
-> memory-sensitive relation update
-> future effective-geometry deformation
```

It does **not** support:

```text
memory alone automatically creates geometry
```

and it does not show that arbitrary hidden-state-driven divergence is physically meaningful.

The important progress over RM-01E is that the causal arrow has now been tested in the required direction:

```text
same present + different history -> different future geometry
```

with an explicit history-specific statistic.

## Relation to gravity-as-memory

This is the first RM-01 benchmark that resembles the logical structure required by a gravity-as-memory mechanism.

A candidate relational memory object is

```math
K_M(i,j,t).
```

A future theory would require something schematically like

```math
G_{t+1} = F(G_t, K_M(t))
```

or, in a continuum limit,

```math
g_eff = G[K_M].
```

RM-01F demonstrates only that such a map can generate a detectable history-dependent geometric residual in a controlled graph model.

It does not derive:

- Lorentzian spacetime;
- curvature tensors;
- Einstein field equations;
- stress-energy conservation;
- gravitational lensing or geodesic motion;
- a physical SoCT source law;
- or evidence that nature contains the proposed memory variable.

## Important failure boundary

The permuted-memory null is crucial.

Because it causes even larger raw graph divergence, **future divergence itself is not diagnostic**.

Any future SoCT memory-geometry claim must therefore predict a structured residual tied to the real history, not merely hysteresis or sensitivity to an unobserved state.

That becomes a methodological requirement for later galaxy/cosmology tests as well:

```text
history-specific geometry residual
>
matched arbitrary-hidden-state residual
```

using a predeclared statistic.

## Validation provenance

The forward rule and coupling were explored on seeds `< 300`.

A fresh held-out run used seeds `300-599` with the fixed parameter set described above. The 300 held-out trials were completed in the analysis environment and archived as CSV.

The packaged script was additionally:

```bash
python -m py_compile rm01f_matched_present_history_geometry.py
python rm01f_matched_present_history_geometry.py --seed-start 300 --seeds 3
```

The full standalone 300-seed packaging rerun exceeded the execution-window limit; it is not the source of the reported values. The reported values come from the completed held-out batch before packaging.

## Next gate — RM-01G

RM-01F establishes a weak history-specific deformation, but the update law still explicitly inserts the memory kernel into the closure score.

RM-01G should ask whether a **local action/energy principle** can generate the same memory-dependent geometry without directly prescribing the desired rewiring score.

Candidate direction:

```text
relational state G
+ persistent kernel K_M
-> local cost/action functional S[G, K_M]
-> gradient/stochastic local updates
-> emergent metric response
```

Required tests:

1. derive the update from a scalar/local objective rather than a hand-designed closure score;
2. keep matched-present / reversed-history construction;
3. recover the RM-01F history-specific residual on held-out seeds;
4. test whether the deformation has a curvature-like localized signature;
5. compare against ordinary hysteresis, hidden-medium change, and arbitrary latent-state controls;
6. determine whether a coarse-grained continuum constitutive law can be fitted without using history labels.

Only after that should the program attempt a weak-field gravity analogy.
