# SIM-04C — Candidate Causal-Distance Comparison Results

**Status:** initial cross-family benchmark complete  
**Claim level:** toy-model methodology result only; not evidence for SoCT or emergent spacetime.

## Question

Which candidate causal-distance construction, if any, generalizes across geometry families without confusing background embedding distance with effective causal/path distance?

This benchmark explicitly scores against two different targets:

```text
background embedding geometry
    = Euclidean separation in the hidden coordinate layout

effective causal/path geometry
    = shortest path through the actual transmission network
      using hidden physical transit cost
```

These targets coincide closely in simple local networks but can diverge under bottlenecks, shortcuts, or variable propagation speed.

## Candidate metrics

Each candidate is computed on the observed network and then converted to an all-pairs shortest-path metric.

```text
D1 = inverse calibrated transmission / causal capacity
D2 = -log calibrated transmission
D3 = calibrated propagation delay
D4 = unweighted hop count
D5 = learned combination of D1-D4
```

`D5` is trained **only** on the `chain` and `grid` families, with per-graph median normalization, then evaluated on all families without retraining.

Direct transmission is generated as an exponentially decaying function of hidden edge transit cost plus modest multiplicative noise. Delay is generated from the same hidden transit cost with smaller multiplicative noise. These assumptions make D2 and D3 intentionally favorable sanity-check estimators; the point is to test how their shortest-path reconstructions behave under withheld network families.

All reported values are mean Spearman rank correlations across 25 deterministic seeds.

## Effective causal/path geometry

| Family | D1 inverse capacity | D2 -log transmission | D3 calibrated delay | D4 hop count | D5 learned combination |
|---|---:|---:|---:|---:|---:|
| chain | 0.999 | 0.998 | 0.999 | 1.000 | 0.999 |
| grid | 0.988 | 0.985 | 0.989 | 1.000 | 0.989 |
| irregular | 0.991 | 0.989 | **0.997** | 0.941 | 0.967 |
| bottleneck | 0.996 | 0.995 | **0.996** | 0.983 | 0.987 |
| shortcut | 0.981 | 0.971 | 0.985 | 0.984 | **0.990** |
| variable speed | 0.985 | 0.987 | **0.998** | 0.914 | 0.942 |

## Background embedding geometry

| Family | D1 inverse capacity | D2 -log transmission | D3 calibrated delay | D4 hop count | D5 learned combination |
|---|---:|---:|---:|---:|---:|
| chain | 0.999 | 0.998 | 0.999 | 1.000 | 0.999 |
| grid | 0.974 | 0.973 | 0.974 | 0.974 | 0.975 |
| irregular | 0.925 | 0.923 | 0.932 | 0.874 | 0.902 |
| bottleneck | 0.948 | 0.948 | 0.947 | 0.927 | 0.933 |
| shortcut | 0.806 | 0.820 | 0.806 | 0.711 | 0.792 |
| variable speed | 0.877 | 0.866 | 0.877 | 0.874 | 0.883 |

## Interpretation

### 1. No universal scalar distance rule emerged

All four hand-built metrics work extremely well on the regular training-style families. That is precisely why those families are insufficient to choose among them.

The withheld families expose meaningful differences.

### 2. Calibrated delay is the strongest simple generalizer in this toy model

`D3` gives the best or essentially tied performance on effective causal/path geometry for:

- irregular networks;
- bottleneck networks;
- variable-speed networks.

Its performance is especially strong in the variable-speed family:

```text
D3 effective rho = 0.998
D4 hop-count rho = 0.914
D5 learned rho   = 0.942
```

This illustrates why topological hop count alone cannot represent metric scale when edge transit costs differ strongly.

### 3. Negative-log transmission behaves as expected but is not uniquely privileged

Because direct transmission was generated approximately as

```math
T_e ~ exp(-alpha c_e),
```

`-log(T_e)` is approximately linear in hidden edge cost. Its strong performance is therefore a sanity check, not a discovery.

Noise, clipping, and shortest-path composition still prevent it from being exactly equivalent to hidden transit cost.

### 4. Inverse capacity is surprisingly robust in rank but has weaker physical justification as a metric

`D1` often preserves effective-distance ordering very well, including on irregular and bottleneck networks. But unlike `-log(T)`, inverse capacity does not turn multiplicative transmission into an additive path law in a principled way.

Therefore high rank performance alone is not enough to select it as a fundamental distance construction.

### 5. Hop count is a strong topology baseline and a poor universal metric

On a regular chain or grid, all edges have comparable hidden cost, so hop count is excellent and even reaches perfect rank correlation in the benchmark.

That advantage disappears as soon as edge costs vary:

```text
irregular:      0.941
effective rho
variable speed: 0.914
```

This reinforces the separation

```text
topological adjacency != metric distance.
```

### 6. The learned combination does not universally beat simpler physics-informed estimators

`D5` was trained on chain + grid data. It generalizes reasonably well but underperforms calibrated delay on unseen irregular and variable-speed systems:

```text
irregular:      D5 0.967 vs D3 0.997
variable speed: D5 0.942 vs D3 0.998
```

It performs best on the shortcut family (`0.990`), showing that combination can help in some mixed regimes.

The broader lesson is important:

```text
better fit on familiar geometry families
    does not imply better causal metric generalization.
```

This is an explicit anti-overfitting result for the observation-foundations program.

### 7. Shortcut networks force the background/effective distinction

The shortcut family is the clearest example.

For effective causal/path geometry, candidate metrics remain strong:

```text
D1 0.981
D2 0.971
D3 0.985
D4 0.984
D5 0.990
```

But agreement with the original Euclidean embedding falls sharply:

```text
D1 0.806
D2 0.820
D3 0.806
D4 0.711
D5 0.792
```

The estimator is not necessarily failing. The shortcut creates a real low-cost causal route that the background embedding does not represent.

Therefore every future geometry test must ask:

> Are we trying to reconstruct an assumed background manifold, or the geometry actually experienced by causal propagation?

Those are not always the same problem.

### 8. Variable propagation speed creates the same distinction without explicit nonlocal edges

In the variable-speed family, all nodes still live in an ordinary Euclidean embedding, but heterogeneous edge speeds make effective travel distance differ from coordinate separation.

The causal metrics track effective path geometry much better than Euclidean background geometry.

This suggests a general principle for the track:

```text
causal geometry is operationally closer to travel/influence cost
than to coordinate separation unless additional assumptions identify the two.
```

## What survives from SIM-04A/B/C

The geometry program now has a more disciplined hierarchy:

```text
1. causal order / reachability
   -> robust qualitative causal structure

2. local timing + calibrated transmission
   -> edge-scale dynamical information

3. interval number / density
   -> scale information in causal-order models

4. path composition
   -> effective causal geometry

5. comparison with independent background geometry
   -> determines whether effective and embedding geometries agree
```

No single response amplitude or learned scalar should be promoted to fundamental distance without additional physical derivation.

## Implication for the recursive SoCT track

The recursive loop can now be stated more carefully:

```text
observation / intervention
    -> inferred causal order and local channel properties
    -> effective causal geometry
    -> constraints on future interaction pathways
    -> new observations
```

The next SoCT-specific question is **not** whether causal data can be turned into some geometry; the toy simulations show several ways to do that.

The sharper question is:

> If an SoCT memory variable `M` changes future transition laws, does it alter effective causal geometry in a distinctive way that cannot be absorbed into ordinary changes of local transmission, speed, hidden state, or environmental memory?

That is the proper bridge to a future memory-perturbation simulation.

## Next step

Before injecting SoCT memory, the safest next move is a small **SIM-04D identifiability gate** or equivalent analysis:

```text
Can changes in geometry be distinguished from changes in local medium/speed,
receiver susceptibility, hidden nodes, or ordinary dynamical memory?
```

If not, an `M`-driven geometry shift would be observationally non-identifiable.

Only after that gate should the program proceed to a SoCT-specific perturbation of the causal/geometry layer.

## Reproduction

Run:

```bash
python experiments/observation-foundations/sim04c_candidate_distance_comparison.py --seeds 25
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim04c_candidate_distance_comparison.py --seeds 25 --json
```
