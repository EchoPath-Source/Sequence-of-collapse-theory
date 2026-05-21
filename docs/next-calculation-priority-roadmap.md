# Next Calculation Priority Roadmap

**Status:** Active calculation queue  
**Purpose:** Track the next calculations needed to move SoCT/PNT from documented architecture toward reproducible, submission-ready work.

---

## Current Priority Order

### 1. Kerr ring quantization -> l_E -> E_E -> neutrino check

**Status:** Pending / high leverage  
**Why it matters:** Unlocks multiple CIH / Engramon / parent-universe downstream claims.

Required work:

1. Resolve `M_parent` discrepancy across source documents.
2. Recompute from a single Kerr / Bekenstein-Hawking entropy convention.
3. Derive ring length scale `l_E`.
4. Convert to energy scale `E_E`.
5. Check whether the neutrino-coincidence survives.
6. Document failure conditions.

Suggested notebook:

```text
notebooks/kerr_ring_quantization_check.ipynb
```

Related source warning:

> Existing notes indicate possible inconsistent use of entropy formula or assumptions. The calculation must recompute all values from the same convention before any claim is made.

---

### 2. SPARC radial decomposition

**Status:** Candidate result documented / needs reproducible notebook  
**Why it matters:** Most important P1 publication discriminator.

Current artifacts:

```text
observations/sparc/results/inner_outer_radial_decomposition_summary.md
observations/sparc/results/inner_outer_correlation_summary.csv
```

Still required:

```text
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
notebooks/sparc_inner_outer_radial_decomposition.ipynb
```

Core result to reproduce:

> In the clean Disk+Q=1 subset, WISE-color / formation-history proxy correlations are stronger in outer fDM than inner fDM.

---

### 3. f0 from rho_DE cross-constraint

**Status:** Pending / one-calculation consistency test  
**Why it matters:** Connects SPARC/PNT memory normalization to observed dark-energy density.

Required work:

1. Define `f0` consistently across SPARC memory model and PNT dark-energy model.
2. Use observed `rho_DE` to constrain the allowed baseline/exhaust fraction.
3. Check whether the same normalization is compatible with SPARC outer fDM baseline.
4. Report whether the cross-constraint is consistent, strained, or impossible.

Suggested notebook:

```text
notebooks/f0_rho_de_cross_constraint.ipynb
```

Failure condition:

> If the `f0` required by observed dark energy is incompatible with the SPARC-inferred memory baseline by orders of magnitude, the shared-normalization version of the model is weakened.

---

### 4. Memory-field H0 correction

**Status:** Pending  
**Why it matters:** Completes the Hubble-tension picture beyond prompt EDE and void-filament dark-energy differential.

Current known contributions:

| Mechanism | Current status |
|---|---|
| PNT prompt EDE | toy model, partial shift |
| PNT void-filament differential | toy model, ~1-3 km/s/Mpc contribution |
| Direct memory-field gravity correction | uncalculated |
| Parent-universe contribution | uncalculated |

Required work:

1. Start from effective-G memory form:

```text
G_eff(x,t) = G0 [1 + alpha M(x,t)]
```

2. Estimate `Delta M` between recombination and today.
3. Derive sign and magnitude of:

```text
H_local = H_CMB * (1 + lambda * Delta M)
```

or a more defensible equivalent.

4. Check whether magnitude is small, relevant, or excluded.

Suggested notebook:

```text
notebooks/memory_field_h0_correction.ipynb
```

---

### 5. Thermalization tau_ex from plasma physics

**Status:** Pending / decisive for prompt EDE branch  
**Why it matters:** Validates or kills the PNT prompt-exhaust EDE mechanism.

Current toy requirement:

```text
tau_ex ~ 0.001 - 0.03 Myr
```

Required work:

1. Estimate early-universe scattering/thermalization times around `z ~ 3000-8000`.
2. Include or bound:
   - Thomson scattering;
   - Comptonization;
   - double Compton scattering;
   - bremsstrahlung;
   - pair processes where relevant;
   - spectral-distortion constraints.
3. Compare derived or bounded `tau_ex` to required range.
4. Decide whether prompt EDE remains viable.

Suggested notebook:

```text
notebooks/tau_ex_plasma_thermalization.ipynb
```

Failure condition:

> If physically defensible plasma timescales cannot approach the required prompt-exhaust decay/thermalization window, the PNT-EDE branch is strongly constrained.

---

## Additional Repo Hygiene Tasks

Already present or recently added:

```text
docs/empirical-exploration-thread-summary-v0-1.md
data/README.md
data/sparc/README.md
data/pantheon/README.md
data/pantheon/covariance-notes.md
data/pantheon/environment-labels-schema.md
notebooks/README.md
```

Still needed:

```text
observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv
notebooks/sparc_inner_outer_radial_decomposition.ipynb
visualizations/pnt_hubble_void.jsx
```

---

## Publication Priority

1. P1: SPARC age/fDM + radial decomposition.
2. P2: PNT two-timescale dark energy + void-filament H0 mechanism.
3. P3: CIH / Kerr-to-Cosmos directional memory, only after Kerr ring and axis derivations are clean.
4. P4: full SoCT synthesis.

---

## Research Integrity Rule

A calculation moves from `candidate` to `supporting evidence` only when:

1. assumptions are stated;
2. equations are fixed;
3. code/notebook is committed;
4. outputs regenerate;
5. failure condition is listed;
6. conventional alternatives are addressed.
