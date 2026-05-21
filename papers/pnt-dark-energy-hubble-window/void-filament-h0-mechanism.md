# PNT Void-Filament H0 Mechanism

**Status:** Calculated toy-model mechanism / not a full cosmological fit  
**Source artifact:** `pnt_hubble_void.jsx` dashboard and thread calculation notes  
**Related tests:** Pantheon+ environment-dependent H0, DESI void/filament BAO statistics  
**Claim level:** Candidate PNT mechanism explaining part of the Hubble tension.

---

## Core Idea

Planck Nucleation Theory predicts that effective dark-energy density may vary by cosmic environment.

In this model:

- cosmic voids convert fewer nucleation attempts into bound structures;
- therefore more attempts fail and return as effective exhaust;
- failed nucleation exhaust contributes to local dark-energy density;
- voids therefore have higher effective dark-energy density;
- higher local dark-energy density produces faster local expansion;
- faster local expansion raises locally measured H0 relative to CMB-inferred H0.

This gives a physical mechanism for an environment-dependent component of the Hubble tension.

---

## Toy Model

The dashboard uses the following failure-fraction model:

```text
f_fail(delta) = 1 - f_succ_mean * max(0, 1 + delta)^n
```

with physical cap:

```text
0 <= f_fail <= 1
```

and local dark-energy ratio:

```text
rho_DE(delta) / rho_DE(mean) = f_fail(delta) / f_fail(0)
```

Fiducial values:

```text
f_succ_mean = 0.15
Omega_m     = 0.315
Omega_DE    = 0.685
H0_CMB      = 67.4 km/s/Mpc
H0_local    = 73.0 km/s/Mpc
n           = 1.5
```

Local H0 estimate:

```text
H0_local(delta) = H0_CMB * sqrt[(Omega_m + Omega_DE * rho_DE_ratio(delta)) / (Omega_m + Omega_DE)]
```

---

## Key Result

For a local underdensity roughly associated with the Laniakea / local environment:

```text
delta ≈ -0.35
```

The toy model gives:

```text
H0_PNT ≈ 69.3 km/s/Mpc
```

This accounts for approximately:

```text
~34% of the 67.4 -> 73.0 km/s/Mpc Hubble tension
```

Interpretation:

> The void-filament dark-energy differential does not fully resolve the Hubble tension, but it provides a concrete, testable contribution of approximately 1-3 km/s/Mpc in the toy model.

---

## Combined Hubble-Tension Picture

Current internal estimate:

| Mechanism | Contribution | Status |
|---|---:|---|
| Void dark-energy differential | ~1-3 km/s/Mpc | calculated toy model |
| Prompt EDE component | ~1-2 km/s/Mpc | toy model only |
| Memory-field gravity correction | unknown | uncalculated |
| Parent-universe dark-energy contribution | unknown | uncalculated |

Conservative combined statement:

> PNT is not yet a demonstrated Hubble-tension solution, but its void-filament mechanism gives a concrete environment-dependent contribution that can be tested with existing supernova and large-scale-structure data.

---

## Important Caveat

The Schmidt-Kennicutt-style scaling breaks down at very high overdensity.

The raw model can produce unphysical behavior in cluster cores unless capped. The dashboard therefore caps:

```text
f_fail in [0, 1]
```

and treats the reliable range as approximately:

```text
-0.9 <= delta <= +0.5
```

High-density cluster-core interpretations should not be used until the source model is replaced by a physically derived failure/success fraction.

---

## Why This Is Novel

Standard local-void models explain part of the Hubble tension through matter underdensity alone.

PNT adds a second term:

```text
matter underdensity + dark-energy enhancement
```

This matters because the two effects should have different observational signatures.

Discriminating test:

> Compare H0 residuals against matter-density maps and independent dark-energy/environment proxies. If PNT is correct, the void contribution should not be reducible to matter-density underdensity alone.

---

## Primary Observable Prediction

Void environments should yield higher best-fit local H0 than filament environments:

```text
Delta_H0 = H0_void - H0_filament > 0
```

The locked Pantheon+ test is documented at:

```text
experiments/cosmology/pantheon-environment-h0-test.md
```

---

## Additional Predictions

1. H0 varies with cosmic environment.
2. H0 anisotropy correlates with large-scale underdense directions.
3. Type Ia supernova brightness residuals encode environment-dependent dark-energy contribution.
4. Void effect plus prompt EDE may explain a larger fraction of the tension than either alone.
5. Filament-rich regions should show lower inferred dark-energy contribution after controlling for matter density.

---

## Required Next Work

1. Derive `f_fail(delta)` from a physical PNT source model rather than a phenomenological scaling.
2. Run the Pantheon+ void/filament H0 test with full covariance.
3. Compare against standard matter-only local-void models.
4. Test sensitivity to local underdensity value and catalog choice.
5. Add DESI BAO void/filament comparison.
6. Convert the JSX dashboard into a reproducible notebook or static figure set.

---

## Related Files

```text
papers/pnt-dark-energy-hubble-window/working-draft-v0-1.md
papers/pnt-dark-energy-hubble-window/toy-model-results-v0-1.md
experiments/cosmology/pantheon-environment-h0-test.md
papers/cosmology/pnt/planck-nucleation-theory-master-note.md
```

Optional visualization artifact:

```text
visualizations/pnt_hubble_void.jsx
```

---

## Paper-Safe Language

Use:

> The PNT void-filament mechanism predicts an environment-dependent dark-energy contribution that can shift local H0 upward in underdense regions by approximately 1-3 km/s/Mpc in a fiducial toy model.

Avoid:

> PNT solves the Hubble tension.
