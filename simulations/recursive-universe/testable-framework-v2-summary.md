# Recursive Universe Model v2.0 — Testable Framework Summary

**Status:** Refined toy framework / falsifiability scaffold  
**Source:** `recursive_universe_v2_testable-3.py`  
**Claim level:** Speculative; designed to identify constraints, not to claim detection.

---

## Purpose

The v2 recursive universe model attempts to make the parent-memory / child-universe idea more falsifiable by replacing the arbitrary v1 transfer function with a bounce-inspired form and checking observability against non-Gaussianity constraints.

---

## Key Improvements Over v1

v2 adds:

1. bounce-inspired transfer function;
2. standard inflation plus memory power-spectrum decomposition;
3. toy CMB angular-power approximation;
4. rough Planck `f_NL` constraint check;
5. parameter-space scan for falsifiability.

---

## Bounce-Inspired Transfer Function

Working form:

```text
T(k) = eta * exp[-(k / k_horizon)^2] * [1 + 0.3 * sin(omega * log(k / k_bounce) + phase)]
```

Where:

- `eta` is parent-memory coupling strength;
- `k_horizon` controls small-scale suppression;
- `k_bounce` sets the bounce scale;
- `omega` sets log-periodic oscillation frequency;
- `phase` may encode parent anisotropy.

This form is still not derived from quantum gravity, but it is more physically structured than the v1 arbitrary transfer.

---

## Power Spectrum Decomposition

The model defines:

```text
P_total(k) = P_inflation(k) + P_memory(k)
P_memory(k) = T(k)^2 * P_parent(k)
```

Standard inflation parameters in the script:

```text
A_s = 2.1e-9
n_s = 0.965
k_pivot = 0.05 Mpc^-1
```

---

## Falsifiability Scan

The v2 script scans coupling values:

```text
eta = [0.001, 0.003, 0.01, 0.03, 0.1]
```

For each eta, it estimates:

- predicted `f_NL`;
- fractional quadrupole deviation `Delta C2 / C2`;
- whether it satisfies a Planck-like non-Gaussianity limit;
- whether the signal is observable above a 1% threshold.

---

## Important Constraint

The model identifies a tension:

```text
strong coupling -> observable signal but too much non-Gaussianity
weak coupling -> allowed by f_NL but too small to observe
```

This is the central useful result.

Repo-safe statement:

> The recursive-universe memory-transfer idea is constrained by a narrow window: the signal must be weak enough to satisfy non-Gaussianity limits but strong enough to produce a measurable low-ell deviation. The toy model suggests this window may be small or absent without a more precise physical transfer function.

---

## Figure Outputs Referenced

The v2 script generates:

```text
falsifiability_analysis.png
cmb_power_spectrum_comparison.png
```

The uploaded images correspond to:

1. non-Gaussianity constraint vs coupling eta;
2. observability vs coupling eta;
3. CMB power spectrum comparison between standard inflation and memory-modified inflation.

---

## Required Before Scientific Use

1. Replace `ToyCMBCalculator` with CLASS/CAMB.
2. Use exact Planck non-Gaussianity likelihoods or published constraints.
3. Define a physical transfer function from an explicit bounce/horizon model.
4. Avoid fitting transfer parameters after inspecting real CMB anomalies.
5. Pre-register low-ell statistics before comparing to Planck maps.

---

## Relationship to CIH Paper Track

This simulation should inform the CIH package, not replace it.

CIH still requires:

- predicted preferred axis;
- expected amplitude;
- parity behavior;
- polarization signature;
- comparison against systematics;
- look-elsewhere correction.

Related file:

```text
papers/cosmology/cih/cih-package-index.md
```

---

## Conclusion

The v2 framework is useful because it turns the parent-universe memory idea into a constrained question:

> Is there any physically allowed parent-memory transfer function that produces an observable low-ell CMB signal without violating non-Gaussianity constraints?

The current answer is not established. The next valid step is a Boltzmann-code and bispectrum-aware implementation, not further toy tuning.
