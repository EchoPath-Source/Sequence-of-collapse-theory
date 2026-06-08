# PNT Void–Filament H0 Mechanism

**Status:** calculated toy model / P2 support artifact  
**Related paper:** P2 — Planck Nucleation Exhaust and Dark Energy / Hubble Tension  
**Visualization:** `visualizations/pnt_hubble_void.jsx`  
**Claim level:** candidate mechanism; not a full cosmological fit

## Summary

This note preserves the Planck Nucleation Theory (PNT) void–filament Hubble mechanism. The model proposes that underdense regions retain a higher failed-nucleation exhaust fraction than dense filaments, producing a higher local effective dark-energy density and therefore a higher locally inferred expansion rate.

The key result of the current toy model is:

> A representative local underdensity around `delta ≈ -0.35` produces `H0 ≈ 69.3 km/s/Mpc`, explaining about `34%` of the nominal local–CMB Hubble tension.

This is a meaningful partial contribution, not a full solution.

## Core mechanism

```text
voids -> fewer successful structure-forming nucleations
      -> more failed nucleation exhaust
      -> higher effective rho_DE
      -> faster local expansion
      -> higher locally inferred H0
```

Dense filaments and cluster-forming regions convert more nucleation attempts into bound structures, stars, or black-hole-like causal separations. Voids convert fewer attempts, leaving more failed-exhaust contribution in the effective vacuum sector.

## Toy model equations

Failed-nucleation fraction:

```text
f_fail(delta) = 1 - f_succ,mean * max(0, 1 + delta)^n
```

with cap:

```text
0 <= f_fail <= 1
```

Dark-energy ratio:

```text
rho_DE(delta) / rho_DE,mean = f_fail(delta) / f_fail(0)
```

Local expansion estimate:

```text
H0(delta) = H0_CMB * sqrt[(Omega_m + Omega_DE * rho_DE(delta)/rho_DE,mean) / (Omega_m + Omega_DE)]
```

## Fiducial parameters

```text
H0_CMB       = 67.4 km/s/Mpc
H0_local_obs = 73.0 km/s/Mpc
Omega_m      = 0.315
Omega_DE     = 0.685
f_succ,mean  = 0.15
n            = 1.5
local delta  ≈ -0.35
```

## Fiducial result

```text
H0_PNT_local ≈ 69.3 km/s/Mpc
Delta H0     ≈ +1.9 km/s/Mpc
Observed nominal tension = 73.0 - 67.4 = 5.6 km/s/Mpc
Fraction explained ≈ 34%
```

## Interpretation

The PNT void–filament mechanism gives a concrete, testable, environment-dependent contribution to the Hubble tension.

Conservative framing:

> The PNT void–filament mechanism is a calculated toy model showing that environment-dependent dark-energy density could contribute approximately 1–3 km/s/Mpc toward the local–CMB H0 discrepancy. It is not yet a full cosmological fit.

## Model caveat

The Schmidt–Kennicutt-style scaling breaks down at high density if extrapolated naively. Raw high-density extrapolation can drive `f_fail` negative, which is unphysical.

Required boundary condition:

```text
0 <= f_fail <= 1
0 <= f_succ <= 1
```

Recommended physical range for the current toy model:

```text
-0.9 <= delta <= +0.5
```

Cluster cores and strongly nonlinear environments require a bounded saturating transfer function rather than the current simple power-law mapping.

## Prediction table

| Prediction | Status | Test |
|---|---|---|
| `rho_DE,void > rho_DE,filament` | toy-model prediction | environment-binned dark-energy or expansion residuals |
| `H0,void > H0,filament` | toy-model prediction | H0 residual vs void/filament classification |
| Void contribution explains a nonzero fraction of Hubble tension | calculated toy result | compare against distance-ladder residuals |
| PNT adds dark-energy-like environmental contribution beyond matter-only void effects | key discriminant | compare density maps against SN/BAO residuals |
| Full Hubble tension can be resolved by PNT alone | not established | requires combined cosmological fit |

## Observational discriminants

Standard matter-only void models predict a local expansion effect from density/flow structure. PNT predicts an additional effective dark-energy contribution with a different environmental scaling.

Testable discriminants:

1. H0 residuals versus cosmic-web environment.
2. Type Ia supernova residuals versus void/filament classification.
3. BAO scale or distance residuals versus environment.
4. Comparison of matter-density maps with dark-energy proxy residuals.
5. Redshift dependence of the environmental signal.

## Status boundary

This artifact strengthens the P2 track because it gives a concrete, testable environment-dependent `H0` mechanism. It remains a toy model until implemented in a controlled cosmological analysis.
