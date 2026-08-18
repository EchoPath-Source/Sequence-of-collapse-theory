# SIM-04I — Incomplete Reset / Hidden Reservoir Adversary Results

**Status:** conventional-adversary benchmark complete  
**Claim level:** synthetic methodology/identifiability result only; this is **not empirical evidence for or against a physical SoCT memory field**.

## Central question

> **How complete must independent reset verification be before a post-reset history residual can be distinguished from an ordinary leftover reservoir?**

SIM-04H showed that an extra state `M` can produce a post-reset residual after all explicitly modeled ordinary degrees of freedom are reset. SIM-04I now strengthens the conventional null instead of making H2 more flexible.

The conventional adversary is deliberately allowed to have the same source, decay, and diffusion family as `M`.

Therefore probe-only observations are structurally non-identifying.

The only additional information comes from an independently calibrated reset diagnostic that couples to ordinary reservoir state but is assumed not to couple to the proposed H2 state.

---

## Models

### H2

A persistent state survives the ordinary reset and produces a fresh-probe phase residual.

The reset diagnostic has zero mean under H2.

### Conventional incomplete-reset reservoir

An ordinary reservoir survives reset by a fraction

```text
q = 0.35
```

in the primary benchmark.

It is allowed to evolve with the same

```text
beta = 0.08
D    = 0.15
```

used by the H2 benchmark.

The probe sees one effective phase scale, while an independent diagnostic sees

```math
Z_diag = kappa_diag q R + noise.
```

`kappa_diag` represents how strongly the reset diagnostic couples to the ordinary reservoir.

The diagnostic-noise scale `sigma_diag` is then varied.

This setup is intentionally adversarial: if the diagnostic is blind, the ordinary reservoir is allowed to be observationally identical to `M`.

---

## Primary result — conventional diffusive reservoir generator

Values below are means over 80 deterministic shot/noise realizations.

`Delta BIC = BIC(conventional) - BIC(H2)`, so negative values favor the conventional reservoir.

| Diagnostic coupling `kappa_diag` | `sigma_diag` | Fraction selecting conventional reservoir | Mean Delta BIC |
|---:|---:|---:|---:|
| 1.00 | 0.100 | 0.575 | -2.16 |
| 1.00 | 0.050 | **1.000** | -18.87 |
| 1.00 | 0.020 | **1.000** | -134.03 |
| 1.00 | 0.010 | **1.000** | -542.67 |
| 1.00 | 0.005 | **1.000** | -2172.68 |
| 0.20 | 0.100 | 0.038 | +3.70 |
| 0.20 | 0.050 | 0.150 | +2.74 |
| 0.20 | 0.020 | 0.575 | -2.16 |
| 0.20 | 0.010 | **1.000** | -18.87 |
| 0.20 | 0.005 | **1.000** | -84.80 |
| 0.05 | 0.100 | 0.000 | +4.43 |
| 0.05 | 0.050 | 0.000 | +4.18 |
| 0.05 | 0.020 | 0.050 | +3.48 |
| 0.05 | 0.010 | 0.188 | +2.17 |
| 0.05 | 0.005 | 0.575 | -2.16 |
| **0.00** | any tested | **unresolved** | **0.00** |

## Interpretation

### 1. Independent reset diagnostics can defeat a conventional mimic

When the ordinary leftover reservoir is strongly visible to the reset diagnostic (`kappa_diag = 1`), only moderate diagnostic precision is needed before the conventional explanation is consistently selected.

At

```text
sigma_diag = 0.05
```

the conventional model is selected in all 80 runs.

The post-reset probe by itself does not provide this discrimination. The independent diagnostic does.

### 2. Weakly observable reservoirs can masquerade as H2

At

```text
kappa_diag = 0.20,
sigma_diag = 0.05,
```

the conventional reservoir is selected in only about 15% of runs even though it generated the data.

Improving the diagnostic to

```text
sigma_diag = 0.01
```

raises conventional-model selection to 100% in this benchmark.

Thus

```text
apparent H2 preference can be a reset-diagnostic sensitivity problem.
```

### 3. Very weakly coupled conventional reservoirs remain dangerous

For

```text
kappa_diag = 0.05,
```

even `sigma_diag = 0.005` identifies the conventional generator in only about 57.5% of runs.

This is a direct warning against interpreting a null reset diagnostic as proof of environmental closure.

A diagnostic can report "nothing detected" simply because it couples weakly to the relevant hidden mode.

### 4. A completely blind conventional reservoir is exactly degenerate

For

```text
kappa_diag = 0,
```

the maximum probe-prediction difference between H2 and the matched conventional reservoir is

```text
0.0.
```

The models also have the same effective parameter dimensionality in the restricted observation set, so the benchmark reports an unresolved tie rather than allowing a complexity penalty to manufacture an H2 preference.

Therefore

```text
probe-only precision cannot break a truly hidden-state degeneracy.
```

No number of additional fresh-probe shots solves this structural problem.

---

## Reset-completeness sweep

At fixed diagnostic quality

```text
kappa_diag = 0.20
sigma_diag = 0.02
```

the fraction of the ordinary reservoir that survives reset is varied.

| True surviving fraction `q` | Fraction selecting conventional reservoir | Mean Delta BIC |
|---:|---:|---:|
| 0.10 | 0.075 | +3.24 |
| 0.20 | 0.263 | +1.70 |
| 0.35 | 0.575 | -2.16 |
| 0.50 | 0.925 | -8.00 |
| 0.70 | **1.000** | -18.81 |

Large reset failures are easy to diagnose. Small residual ordinary states are much harder to exclude.

This gives the experimental requirement a quantitative form:

> The smaller the conventional state left after reset, the stronger the independent closure diagnostic must be before an H2-like residual becomes interpretable.

---

## H2-generator sanity check

When the synthetic data are actually generated by H2 and the reset diagnostic has nonzero coupling to conventional reservoirs, H2 is selected in approximately

```text
97.5%
```

of the representative 80-run conditions tested.

The conventional fit drives its inferred surviving ordinary fraction close to zero.

For a completely blind diagnostic (`kappa_diag = 0`), H2 and the matched conventional hidden reservoir again become exactly unresolved.

This is appropriate: the simulation does not allow model selection to infer ontology from observationally identical predictions.

---

## What SIM-04I changes about the memory-field assessment

The current simulation sequence does **not** show that an SoCT memory field is necessary.

The more conservative reading is:

```text
standard quantum record dynamics explain interaction, decoherence,
record persistence, erasure, and redundancy;

ordinary hidden/local reservoirs can explain some post-reset history effects;

a conventional diffusive reservoir can reproduce the complete H2 probe
signature if it is not independently observed;

M becomes a useful additional state only when simpler ordinary state
completions are excluded and its fixed cross-history law adds predictive value.
```

Thus the present status is

```text
M is mathematically viable and falsifiable,
but not empirically necessary or uniquely identified.
```

---

## Strongest surviving possible novelty of H2

The candidate new-physics signature is no longer simply

```text
history dependence
```

or

```text
post-reset residual.
```

It would need to be something closer to

```text
verified matched ordinary state
+ different retained-record histories
+ nonzero transferable relaxation
+ nonzero transferable spatial propagation
+ fixed probe coupling
+ held-out prediction
+ independent failure to detect any ordinary reservoir capable of carrying it.
```

Even then, a completely hidden conventional degree of freedom with identical dynamics remains an ontology ambiguity until some additional discriminating prediction is found.

---

## Next gate

SIM-04I suggests two parallel next steps rather than immediately increasing H2 complexity.

### Track A — derive a discriminator beyond state naming

Search for a prediction that follows from the proposed SoCT origin of `M` but not from an arbitrary conventional reservoir with the same phenomenological decay/diffusion law.

Candidates include constraints tying the source specifically to record-production structure, universal parameter relations, conservation/backreaction requirements, or coupling to another independently measured observable.

### Track B — laboratory-feasibility reset audit

Translate the synthetic reset fraction and diagnostic sensitivity into an experiment-design question:

```text
what ordinary environmental modes would need to be measured or bounded,
and to what precision,
for a real reset-and-probe test to be informative?
```

A laboratory proposal should not be advanced until this closure budget is explicit.

---

## Reproduction

Run:

```bash
python experiments/observation-foundations/sim04i_incomplete_reset_hidden_reservoir.py
```

Machine-readable output:

```bash
python experiments/observation-foundations/sim04i_incomplete_reset_hidden_reservoir.py --json
```
