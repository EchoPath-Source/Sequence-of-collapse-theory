# RM-01H — Transferability gate for the local memory/geometry action

**Status:** completed first transfer gate  
**Claim level:** methodology / toy-model result only  
**Primary outcome:** **transfer gate failed**  
**Not evidence for:** SoCT, physical spacetime, curvature, Einstein gravity, or a continuum gravity-as-memory law.

## Question

RM-01G showed that a fixed finite graph can evolve under the scalar action

```math
S[G,K_M]
= -\alpha N_\triangle(G)
- \beta \sum_{(i,j)\in E(G)} \widehat K_M(i,j)
```

and produce a strong history-specific metric and curvature-like response.

RM-01H asks the harder question:

> Does one frozen coarse-grained memory-to-geometry response law transfer across unseen graph sizes, degrees, memory persistence scales, and present-network topologies without retuning?

A positive answer is required before any weak-field continuum analogy is justified.

---

## 1. First diagnostic: raw coupling is not intensive

The first sweep varied

```text
n = 48, 64, 80
mean degree = 4, 6
memory decay = 0.85, 0.90, 0.95
beta = 0, 0.025, 0.05, 0.075, 0.10, 0.125, 0.15
```

The raw response did **not** collapse as a function of `beta`.

At fixed `beta`, degree-4 and degree-6 systems responded very differently. This is expected from the discrete action: triangle changes occur in integer units while the memory contribution is continuous.

The first useful normalization was therefore defined from the distribution of valid local proposals in the present graph:

```math
\lambda_{eff}
= \beta
\frac{\sigma(\Delta K_M)}
{\alpha\,\sigma(\Delta N_\triangle)}.
```

This measures the typical proposal-level leverage of the memory term relative to the closure term.

It substantially improves collapse of the training curves, but does not by itself solve finite-size transfer.

---

## 2. Naive size-transfer failure

RM-01G used the same finite budget for every graph:

```text
40 history-source events
40 accepted-improvement swap attempts
```

independent of graph size.

That means larger graphs receive less history and less dynamical evolution per degree of freedom.

A first held-out size test therefore failed strongly:

```text
holdout R^2  = -1.3705
holdout MAE  =  0.04076
```

for the normalized response

```math
R_{geo}=H_{geo}/\langle d\rangle.
```

This failure is retained as an explicit finite-size boundary rather than ignored.

---

## 3. Intensive/extensive scaling repair

RM-01H then made only two physically motivated scaling changes:

### History exposure

The source-group size remains approximately `n/8`, and the number of source events is scaled so events per source-group member remain close to the RM-01G baseline.

### Evolution time

The number of attempted accepted-improvement swaps per epoch scales with edge count:

```math
N_{swap/epoch}
\approx 4\frac{|E|}{128}.
```

The RM-01G baseline (`n=64`, degree `4`) therefore remains exactly four swaps per epoch.

No response parameter was retuned for the held-out systems.

---

## 4. Frozen training law

Training systems used only:

```text
n = 48, 64
degree = 4, 6
memory decay = 0.85, 0.90
beta = 0.05, 0.10, 0.15
8 seeds per configuration
```

One two-parameter threshold law was fitted to configuration means:

```math
R_{geo}
= A\max(0,\lambda_{eff}-\lambda_c).
```

Training fit:

```text
A          = 0.18364957
lambda_c   = 0.26092832
training R^2 = 0.80239625
training MAE = 0.01593526
```

So, **within the training regime**, the normalized proposal-level coupling is a useful compression of size/degree/memory effects.

---

## 5. Fresh unseen-size holdout

The fitted parameters were frozen before testing:

```text
n = 80, 96
degree = 4, 6
memory decay = 0.95
beta = 0.05, 0.10, 0.15
10 fresh seeds per configuration
```

Result:

```text
holdout R^2 = -0.87842294
holdout MAE =  0.03876464
```

The training law systematically overpredicts the larger-system response in important parts of the sweep.

Therefore the proposed coarse-grained constitutive relation **fails unseen-size transfer**.

This remains true even after correcting the obvious history-exposure and update-budget scaling errors.

---

## 6. Focused topology holdout

A second frozen-coupling test used

```text
n = 64
degree = 4
memory decay = 0.90
beta = 0.10
15 fresh seeds per topology
```

with three coordinate-free present-network families.

### Random regular

```text
H_geo = 0.16866 +/- 0.17513
p = 0.00224 vs zero
```

The original regime continues to show a history-dependent response.

### Small-world

```text
H_geo = 0.06982 +/- 0.30904
p = 0.39635 vs zero
```

The mean sign is compatible with the original response but the global effect is noisy and non-significant.

A more local extreme-pair adjacency statistic gives

```text
edge contrast = 0.00514 +/- 0.00956
p = 0.05618
```

which is suggestive but does not pass the predeclared transfer standard.

### Ring lattice

```text
H_geo = 0.00000
edge contrast = 0.00000
```

for all `15/15` seeds at the frozen coupling.

The finite action is effectively locked by its strong local triangle structure in this regime; the memory term does not generate the history-specific deformation seen on random-regular graphs.

This is a direct topology-transfer failure.

---

## 7. Main result

RM-01H **does not support** the stronger statement

```text
RM-01G action -> transferable memory-to-geometry constitutive law.
```

The accepted statement is narrower:

```text
RM-01G defines a real finite-network history-dependent geometry mechanism,
but its response is strongly dependent on network size/topology and the
relative discrete leverage of closure versus memory.
```

The dimensionless proposal coupling

```math
\lambda_{eff}
= \beta\sigma(\Delta K_M)
/ [\alpha\sigma(\Delta N_\triangle)]
```

is useful inside the training family, but it is **not sufficient** to define a universal response law.

---

## 8. What this means for gravity-as-memory

This is an important negative result for the SoCT gravity-as-memory program.

RM-01F/G established the toy causal direction

```text
past history
-> persistent relational memory
-> future metric deformation.
```

RM-01H shows that this is **not yet enough** for a physics-style constitutive law.

A genuine continuum candidate must survive something like

```text
same local law
+ changing system size/topology/discretization
-> same coarse-grained response.
```

The current triangle-count action does not.

Therefore the program should **not** proceed to Einstein-equation or weak-field claims from RM-01G.

---

## 9. Likely source of failure

The current closure term is a raw discrete triangle count.

That makes its scale depend strongly on:

```text
degree
local clustering
graph family
available triangle-changing moves
finite graph size
```

while the memory term uses a normalized continuous kernel.

The two pieces therefore do not yet form a common intensive local energy density.

This likely explains both the coupling threshold and the ring-lattice lockout.

---

## 10. Next gate — RM-01I

RM-01I should **repair the action, not tune the failed response curve**.

The next candidate should be a genuinely local/intensive objective such as

```math
S = \sum_i s_i
```

with normalized local terms, for example

```math
s_i
= -\alpha\,C_i
- \beta\,\frac{1}{d_i}\sum_{j\in N(i)}\widehat K_M(i,j),
```

where `C_i` is a local closure or curvature-like density rather than a raw global triangle count.

Required RM-01I gates:

1. define the action entirely from local intensive quantities;
2. preserve the matched-present / reversed-history test;
3. fit coupling only on training sizes;
4. test unseen sizes, degrees, memory scales, and topologies;
5. require a positive transfer score before any continuum analogy;
6. retain scalar-memory, instantaneous-state, permuted-memory, and topology-lockout controls.

If RM-01I also fails transfer, the gravity-as-memory route should remain a finite relational toy mechanism rather than being promoted toward a continuum theory.

---

## Reproducibility

Files:

```text
rm01h_transferability_gate.py
rm01h_transfer_summary.csv
RM01H_RESULTS.md
```

Primary archived results:

```text
scaled training: 8 seeds/config
unseen size holdout: 10 seeds/config
topology holdout: 15 seeds/family
```

The result is intentionally classified as a **failed transfer gate**.
