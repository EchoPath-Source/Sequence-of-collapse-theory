# PNT Void–Filament Hubble Test

**Status:** toy-model scaffold  
**Related paper package:** `papers/pnt-dark-energy-hubble-window/`  
**Visualization source:** `pnt_hubble_void.jsx` pending import / conversion

## Purpose

This simulation track tests the Planck Nucleation Theory prediction that voids and filaments should carry different effective dark-energy density because their failed-nucleation fractions differ.

Core prediction:

```text
rho_DE,void > rho_DE,filament
H0,void > H0,filament
```

## Physical mechanism

In PNT:

- Planck-scale nucleation attempts occur throughout the vacuum substrate.
- In dense environments, a larger fraction of attempts are converted into bound structures or black-hole-like causal separations.
- In voids, fewer nucleation attempts convert into stable structures.
- Failed attempts return exhaust to the accessible low-energy sector.
- Therefore voids retain a larger effective dark-energy contribution.

## Toy model equations

Failed-nucleation fraction:

```text
f_fail(delta) = 1 - f_succ,mean * max(0, 1 + delta)^n
```

with physical cap:

```text
0 <= f_fail(delta) <= 1
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
H0_CMB = 67.4 km/s/Mpc
H0_local,obs = 73.0 km/s/Mpc
Omega_m = 0.315
Omega_DE = 0.685
f_succ,mean = 0.15
n = 1.5
local delta ≈ -0.35
```

## Current toy result

For `delta ≈ -0.35` and `n = 1.5`:

```text
H0_PNT,local ≈ 69.3 km/s/Mpc
Delta H0 ≈ +1.9 km/s/Mpc
Observed tension = 73.0 - 67.4 = 5.6 km/s/Mpc
Fraction explained ≈ 34%
```

Interpretation:

> The void–filament dark-energy differential can explain a meaningful fraction of the local-CMB Hubble tension in the toy model, but it does not solve the full tension by itself.

## Validity domain

The Schmidt–Kennicutt-inspired scaling breaks down at high overdensity if extrapolated naively. The current toy model should be treated as valid only across a bounded phenomenological range:

```text
-0.9 <= delta <= +0.5
```

Cluster cores and highly nonlinear environments require a different transfer function.

## Known issue

Raw high-density extrapolation can drive `f_fail` negative. This is unphysical. All implementations must cap:

```text
f_fail in [0, 1]
f_succ in [0, 1]
```

Future versions should replace the power-law mapping with a bounded saturating function.

## Observational tests

### Test 1: H0 residual vs environment

Prediction:

```text
H0(void hosts / void-dominated lines of sight) > H0(filament or cluster environments)
```

after controls.

### Test 2: Type Ia supernova residuals

Prediction:

```text
SN Ia residuals should correlate weakly with void/filament environment beyond standard peculiar-velocity corrections.
```

### Test 3: Separate matter and dark-energy signatures

Standard void models predict a matter-density effect. PNT predicts an added dark-energy-like term. Compare Hubble residuals against both density maps and dark-energy proxy reconstructions.

## Required controls

- peculiar velocity corrections
- host galaxy properties
- calibration ladder
- Malmquist bias
- survey selection
- redshift binning
- local density reconstruction
- large-scale flow model
- BAO / SN / CMB consistency

## Next steps

1. Import or convert the JSX visualization into a reproducible Python notebook.
2. Export fiducial tables for `delta`, `rho_DE_ratio`, and `H0(delta)`.
3. Replace raw power-law with saturating environmental transfer function.
4. Add comparison against standard matter-only void effect.
5. Identify public datasets for environment-binned H0 or SN residual testing.
