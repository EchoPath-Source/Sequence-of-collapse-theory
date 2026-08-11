# SoCT / PNT Dark-Sector Taxonomy

**Status:** Taxonomy scaffold  
**Claim level:** Interpretive scientific framing, not established cosmology  
**Purpose:** Keep dark matter, dark energy, and ordinary matter branches distinct.

---

## Purpose

This document defines a clean taxonomy for the dark-sector branch of SoCT/PNT so the framework does not over-broaden or conflate different mechanisms.

The taxonomy is provisional and should be revised as calculations and observations constrain the model.

---

## Three-Sector Framing

| Sector | SoCT/PNT interpretation | Scientific status |
|---|---|---|
| Ordinary matter | Rendered/localized collapse in the luminous/photonic sector | Established matter exists; SoCT interpretation speculative |
| Dark matter | Hidden gravitational memory / cross-dimensional collapse residue / non-luminous scaffolding | Candidate interpretation of missing-mass phenomenology |
| Dark energy | Post-bounce expansive curvature / unresolved pressure / two-timescale PNT exhaust | Candidate interpretation of accelerated expansion |

---

## Ordinary Matter

Working interpretation:

> Ordinary matter is rendered collapse: stable, luminous, locally accessible structure coupled strongly to the photonic sector.

Ordinary matter includes:

- baryons;
- stars;
- gas;
- luminous structures;
- directly observable mass-energy.

SoCT does not deny ordinary matter or standard gravitational effects. It asks whether ordinary matter is only the visible/localized portion of a broader collapse-memory process.

---

## Dark Matter Branch

Working interpretation:

> Dark-matter-like effects may arise from hidden gravitational memory: accumulated collapse-history or non-luminous scaffolding that affects motion gravitationally without emitting light.

Possible subcomponents:

1. collapse-memory accumulation;
2. cross-dimensional or parent-child residue;
3. unrendered gravitational scaffolding;
4. conventional particle dark matter, if present, as one component rather than full explanation;
5. baryonic feedback and assembly effects as conventional confounds.

Primary SoCT observables:

- galaxy age / missing-mass correlation;
- outer-halo preference;
- radial decomposition;
- environment/cosmic-web dependence;
- high-redshift baryon dominance or declining rotation curves;
- SPARC residual structure.

Main conventional alternatives:

- CDM halo concentration;
- assembly bias;
- feedback history;
- stellar mass coupling;
- gas fraction and morphology;
- MOND-like acceleration scaling;
- selection effects.

### Cosmic-web memory interpretation

Dark matter should not be described as simply absent from voids or as already replaced by SoCT. The safer research framing is:

> Voids are dark-matter underdensities and low-collapse-history regions, while filaments and halos are high-collapse-history regions where the gravitational scaffold has accumulated.

In SoCT/PNT language, the cosmic web may be interpreted as a candidate memory-density map:

```text
voids      -> low collapse history / low memory density / dark-matter underdensity
filaments  -> high collapse history / accumulated memory density / strong dark-sector scaffolding
halos      -> localized collapse-history wells around galaxies and clusters
```

This is a research interpretation, not proof. It motivates tests of whether history-weighted gravity or memory-density proxies can explain dark-sector observables better than current-matter-only proxies under controlled comparison.

Related P6 motivation note:

```text
papers/p6-black-holes-memory-compression-nodes/gravitational-memory-motivation.md
```

---

## Dark Energy Branch

Working interpretation:

> Dark energy may reflect unresolved expansion pressure, Planck nucleation exhaust, or post-bounce curvature residue rather than a strict cosmological constant.

PNT two-timescale split:

```text
rho_DE^PNT(z) = rho_prompt(z) + rho_memory(z)
```

Where:

| Component | Role | Status |
|---|---|---|
| `rho_prompt` | short-lived radiation/plasma-coupled exhaust; possible EDE-like transient | toy model constrained |
| `rho_memory` | long-lived residue / late-time dark-energy-like component | stronger current PNT track |

Primary observables:

- DESI `w(z)` evolution;
- Pantheon+ environment-dependent H0;
- void/filament dark-energy differential;
- BAO consistency;
- CMB sound-horizon constraints;
- spectral-distortion constraints for prompt channel.

---

## Void-Filament Differential

PNT predicts:

```text
rho_DE_void > rho_DE_filament
```

because voids convert fewer nucleation attempts into bound structures, leaving more failed-nucleation exhaust.

Observable:

```text
H0_void > H0_filament
```

Related file:

```text
papers/pnt-dark-energy-hubble-window/void-filament-h0-mechanism.md
```

Pantheon import status:

```text
data/PANTHEON_IMPORT_STATUS.md
```

---

## Black-Hole Information / Gravity-Memory Motivation

Black-hole information preservation and evaporation questions provide a useful motivation for the gravity-as-memory branch, but not direct evidence for it.

Repo-safe phrasing:

> Black-hole information preservation, dark-matter cosmic-web structure, and void/filament contrast are compatible with a gravity-as-memory interpretation, but they do not prove SoCT/PNT. They motivate formal models and reproducible tests of whether gravitational anomalies can be organized as accumulated collapse history.

This motivation belongs primarily in P6:

```text
papers/p6-black-holes-memory-compression-nodes/gravitational-memory-motivation.md
```

---

## What Must Not Be Conflated

Do not treat these as identical:

```text
dark matter ≠ dark energy
collapse memory ≠ prompt exhaust
late memory residue ≠ EDE transient
parent-child inheritance ≠ local SPARC signal
metaphysical Source/Echo/Origin ≠ empirical cosmology
research taxonomy ≠ product claim
```

Each branch requires its own equations, datasets, and falsification conditions.

---

## Falsification Conditions

### Dark matter / memory branch weakens if:

- age/fDM and radial signals disappear under controls;
- environment fully explains results conventionally;
- outer residuals behave exactly as standard halo models predict;
- no high-redshift evolution pattern survives literature review.

### Dark energy / PNT branch weakens if:

- two-timescale model cannot fit expansion history;
- void/filament H0 sign is absent or reversed;
- prompt component violates CMB or spectral-distortion constraints;
- `rho_DE` normalization conflicts with SPARC/PNT cross-constraints.

### Parent-child / CIH branch weakens if:

- no quantitative axis/amplitude prediction can be derived;
- predicted CMB signatures violate non-Gaussianity constraints;
- observed alignments vanish after systematics/look-elsewhere corrections.

### Black-hole / memory-compression branch weakens if:

- no formal memory-compression operator can be defined without violating known constraints;
- the information-preservation analogy cannot be connected to falsifiable observables;
- P6 remains metaphorical rather than mathematically bounded;
- CMB/large-scale directional tests fail after systematics and look-elsewhere corrections.

---

## Product Boundary

Product repositories may use engineering language such as adaptive memory, field-inspired routing, topology-aware diagnostics, or persistence only after the relevant concept is translated through:

```text
docs/research_to_product_handoff.md
docs/claim_boundaries_for_products.md
```

Do not translate this taxonomy into product claims that say dark matter is replaced, dark energy is solved, physical memory fields are verified, or SoCT has been experimentally confirmed.

---

## Repo-Safe Summary

Use:

> SoCT/PNT treats the dark sector as potentially composite: missing-mass behavior may involve collapse-memory structure, while accelerated expansion may involve Planck-scale exhaust or long-lived memory residue. These branches are related but not interchangeable.

Avoid:

> Dark matter and dark energy are the same thing.

---

## Next Work

1. Add equations for each branch.
2. Link each branch to a primary dataset.
3. Define a parameter ledger for shared quantities.
4. Add a falsifiability table to `PREDICTIONS.md`.
5. Keep metaphysical claims out of empirical taxonomy unless clearly labeled.
6. Keep product translations routed through the claim-boundary docs.
7. Add literature references on black-hole information preservation, gravitational memory, cosmic-web dark matter, and void/filament underdensities.
