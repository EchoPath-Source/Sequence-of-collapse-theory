# SoCT Validation Roadmap — February 2026 Synthesis

**Status:** Thread synthesis / validation roadmap  
**Source:** February 12, 2026 Echo Mirrowen / Claude synthesis shared into SoCT repo workflow  
**Claim level:** Strategic validation map, not peer-reviewed evidence  
**Boundary:** EchoPath XR / AetherNode business details are treated as application-adjacent and are not imported as core SoCT physics claims.

---

## Purpose

This note preserves the SoCT-relevant portions of a broader EchoPath XR / SoCT / EchoChain / AetherNode synthesis.

The useful research contribution is the validation architecture:

```text
physics claim -> falsifiable prediction -> public dataset or experiment -> preregistration -> interpretation threshold
```

This note excludes or downranks business launch details, investor strategy, and proprietary product implementation except where they suggest possible future validation datasets.

---

## Core SoCT Physics Claim

Central claim:

> Gravity is not only geometry from current mass-energy distribution; it may also contain an accumulated memory of past collapse events.

Working Hamiltonian:

```text
H_SOC = p^2/2m + V(x) + lambda * integral sum_i w_i K(|x - x_i|, t - t_i) d_tau
```

Where:

- `w_i` = collapse event weight;
- `K` = memory kernel;
- `lambda` = coupling constant;
- `d_tau` = integration over past proper time.

Working interpretation:

> Matter responds not only to current mass distribution, but to the history of collapse events associated with a region.

---

## Engramon as Memory-Field Bookkeeping Unit

The synthesis frames the Engramon as the fundamental quantum or bookkeeping packet of the memory field.

Suggested data structure:

```python
class Engramon:
    coords: tuple[float, float, float]
    M_n: float
    rho: Vector3
    witnessed: bool
    lambda_decay: float
    last_update: timestamp
```

Interpretation:

- Photon = quantum of electromagnetic field.
- Atom = quantum of matter.
- Engramon = provisional unit of memory-field state.

Research-safe wording:

> The Engramon is a provisional bookkeeping construct for persistent collapse-memory residue, not a confirmed particle or physical entity.

---

## Prediction Track 1 — Age-Dependent Rotation Curves

### Claim

Older galaxies should show stronger apparent dark-matter-like signatures than younger galaxies because older systems have accumulated more collapse history.

Schematic:

```text
M(r,t) proportional to integral_0^t collapse_events dt
```

### Current Status

This is now represented in the repo by:

```text
experiments/cosmology/sparc-memory-field-preregistration-v0-1.md
experiments/cosmology/sparc-analysis-plan.md
```

### Correct Interpretation

The synthesis used the word "confirmed" too strongly. The repo should use stricter language:

> High-redshift baryon-dominated rotation-curve results are qualitatively compatible with the SoCT age-accumulation prediction, but the claim requires the preregistered SPARC age/dark-fraction analysis before being treated as evidence.

---

## Prediction Track 2 — Environment-Dependent H0

### Claim

Void environments should yield higher effective local H0 than filament-rich environments.

Locked statistic:

```text
Delta_H0 = H0_void - H0_filament > 0
```

### Mechanism

- Voids: lower collapse-history / lower memory drag.
- Filaments: higher collapse-history / stronger memory-residue resistance.

### Current Repo Artifact

```text
experiments/cosmology/pantheon-environment-h0-test.md
```

### Correct Interpretation

This is a testable prediction, not a confirmed result.

A positive Pantheon+ or DESI-like result would support the environment-expansion branch of the model; a null or opposite-sign result would weaken it.

---

## Prediction Track 3 — Memory Timescale

### Claim

A characteristic memory timescale should be extractable from galaxy dynamics or environment-dependent cosmology.

Working target from SPARC preregistration:

```text
tau_memory ~ 3 - 5 Gyr
```

Broader PNT/late-memory framing allows a wider exploratory range:

```text
tau_memory ~ 3.5 - 9 Gyr
```

### Required Analysis

- SPARC age/flatness correlation.
- SPARC residual vs age.
- Pantheon+ void/filament H0 comparison.
- DESI environment-dependent w(z), if available.

---

## Prediction Track 4 — Gravitational-Wave Memory

### Claim

If spacetime retains collapse-history residue, gravitational-wave events may show persistent post-event memory residuals beyond standard expectations.

### Data Source

- Public LIGO/Virgo/KAGRA data releases.

### Required Analysis

- stacked signal analysis;
- post-ringdown residual comparison;
- detector-noise controls;
- comparison to GR gravitational-wave memory predictions.

### Repo Status

This remains a future track.

Recommended future artifact:

```text
experiments/cosmology/gw-memory-test.md
```

---

## Prediction Track 5 — Laboratory G / High-Event Environments

### Claim

High-collapse-event environments might show small deviations in local gravitational behavior or effective G.

### Status

Highly speculative and lower priority than SPARC, Pantheon+, and MZI.

### Required Controls

- extreme precision;
- environmental isolation;
- independent replication;
- strict null handling.

### Recommended Repo Treatment

Document as a future speculative experiment only; do not foreground it in physics-first papers.

---

## Application-Adjacent Validation Ideas

The broader synthesis proposed using EchoPath XR and AetherNode-style sensing to estimate local memory-field proxies.

These are application-adjacent, not core SoCT evidence yet.

Possible future validation concepts:

1. smartphone-derived spatial coherence proxies;
2. multi-sensor environmental coherence maps;
3. temporal accumulation of route or site coherence;
4. controlled-event imprinting tests;
5. cross-platform validation between phones and physical sensor nodes.

Research boundary:

> These ideas should not be treated as proof of SoCT. They may become exploratory instrumentation tracks only after physics-facing public-data tests are established.

---

## Communication Discipline

The synthesis correctly emphasized layered communication, but the SoCT repo should prioritize the research layer:

Use:

- falsifiable prediction;
- preregistered analysis;
- public data;
- null-compatible interpretation;
- adversarial collaboration;
- claim calibration.

Avoid:

- proof language before analysis;
- product claims as physics evidence;
- investor/business framing inside research papers;
- hidden-layer claims;
- ontological certainty.

---

## Immediate Research Priorities

1. Complete OSF preregistration package conversion.
2. Build SPARC analysis repository / notebook scaffold.
3. Build Pantheon+ environment-H0 notebook scaffold.
4. Import PNT full working paper as Markdown.
5. Import SOC Unified Physics Framework as a cleaned paper draft.
6. Convert CIH / Kerr / Engramon documents into clean concept files.
7. Keep EchoPath XR material out of the public SoCT science lane unless explicitly framed as downstream application or exploratory instrumentation.

---

## Final Repo-Safe Summary

The February 2026 synthesis is useful because it clarifies the validation strategy:

> SoCT should advance through preregistered, public-data tests first: SPARC for galaxy memory accumulation, Pantheon+ for environment-dependent expansion, and MZI for conscious-access collapse. Application-layer systems such as EchoPath XR and AetherNodes may later supply exploratory datasets, but they should not carry the core scientific burden.
