# PNT-EDE Toy Model Results v0.1

**Status:** Internal calculation summary  
**Purpose:** Preserve the four-step toy-model feasibility discussion for the PNT prompt-exhaust / Early Dark Energy window.

---

## Executive Summary

The toy-model phase should be considered complete.

Multiple checks converged on the same result:

- A single monotonic accumulated dark-energy component cannot behave like Early Dark Energy.
- PNT requires a two-timescale structure.
- A short-lived prompt exhaust component can create an EDE-like transient.
- A long-lived memory residue component is required for late dark energy / SPARC / DESI-style behavior.
- The prompt component shifts the sound horizon in the correct direction but not enough in the minimal model.
- The remaining gap must be addressed with microphysical plasma transfer modeling, not more toy parameter tuning.

---

## Core Sourced-Decay Model

The prompt component was modeled as:

```text
rho_prompt(t) = integral_0^t S_fail(t') exp[-(t - t') / tau_ex] dt'
```

The corresponding EDE fraction is:

```text
f_EDE(z) = rho_prompt(z) / rho_total(z)
```

---

## Result 1: Monotonic Accumulation Fails EDE Shape

A simple accumulated component grows toward the present because the integration window at present is much longer than the integration window at high redshift.

At `z ~ 4000`, the universe is only tens of thousands of years old. At the present epoch, the universe is approximately 13.8 Gyr old. Any long-lived accumulated component is therefore dominated by later-time sources.

Conclusion:

```text
rho_DE proportional to accumulated exhaust alone is a late dark-energy model, not an EDE model.
```

---

## Result 2: Two-Timescale Structure Is Required

The calculations require two physically distinct components:

| Component | Role | Required timescale |
|---|---|---:|
| Prompt exhaust | EDE-like transient / Hubble-window feasibility | ~0.001 - 0.03 Myr |
| Memory residue | Late dark energy / SPARC / DESI / void-filament | ~Gyr |

Approximate separation:

```text
~5 orders of magnitude
```

This is not optional. A single channel cannot play both roles.

---

## Result 3: Gaussian Early-Source Toy Model

A Gaussian early source was used as the first placeholder:

```text
S_fail(z) = S0 [1 + alpha exp(-(ln(1+z)-ln(1+z_c))^2 / 2 sigma^2)]
```

Findings:

- EDE-like transients are achievable.
- Useful source centers are roughly `z_c ~ 5000 - 8000`.
- Short decay times are required: `tau_ex ~ 0.001 - 0.03 Myr`.
- Sound-horizon reduction is directionally correct but partial.

Approximate reduction:

```text
f_EDE ~ 5%   -> Delta r_s / r_s ~ 0.3 - 1%
f_EDE ~ 10%  -> Delta r_s / r_s ~ 1 - 2%
f_EDE ~ 15%  -> Delta r_s / r_s ~ 2 - 3%
```

---

## Result 4: Radiation-Coupled Source Toy Model

A more physically motivated source was tested:

```text
S_fail,prompt(z) proportional to (1 + z)^4
```

with a cutoff near matter-radiation equality:

```text
z_transition ~ 3400
```

This source is better motivated because the early hot plasma energy density scales like radiation.

However, a pure `(1+z)^4` source requires an upper activation boundary; otherwise, the integral is dominated by arbitrarily early times.

Representative result range:

```text
f_EDE peak ~ 10-15%
Delta r_s / r_s ~ 1.0 - 2.8%
```

Conclusion:

```text
Radiation-coupled sourcing improves physical motivation but does not close the full Hubble-tension gap in the minimal toy model.
```

---

## Thermalization Constraint

The prompt channel requires:

```text
tau_ex ~ 10^3 - 3 x 10^4 years
```

A rough Thomson-scattering sanity check using early-universe electron densities suggests that scattering times around `z ~ 3000-10000` are not obviously too slow. Order-of-magnitude estimates are years to hundreds of years depending on redshift.

Important caveat:

```text
Scattering time is not full thermalization time.
```

A real treatment must include:

- Comptonization,
- double Compton scattering,
- bremsstrahlung,
- pair equilibrium,
- spectral distortions,
- photon-baryon perturbation response.

---

## Sound-Horizon Status

Toy models achieved:

```text
Delta r_s / r_s ~ 1 - 3%
```

A full Hubble-tension resolution likely requires approximately:

```text
Delta r_s / r_s ~ 4 - 6%
```

Therefore:

```text
PNT prompt exhaust is directionally correct but insufficient in minimal toy form.
```

The missing factor is roughly 2, not an order of magnitude.

---

## Interpretation of the Gap

The gap should not be closed by more source-shape tuning.

The toy model lacks the microphysical transfer function that maps high-energy prompt exhaust into the photon-baryon fluid:

```text
T_plasma(z, k, E)
```

This transfer function must be calculated with Boltzmann-code or spectral-distortion methods.

Possible outcomes:

1. It amplifies the effect into the 4-6% range.
2. It leaves the effect near 1-3%.
3. It suppresses the effect or violates CMB constraints.

All three outcomes are scientifically useful.

---

## Final Toy-Phase Verdict

| Question | Toy-model result |
|---|---|
| Can PNT produce an EDE-shaped transient? | Yes |
| Is the prompt channel short-lived enough in principle? | Possibly; requires microphysical derivation |
| Does the prompt component survive to today? | No, and it should not |
| Does prompt exhaust explain present Omega_DE? | No |
| Is a late memory component required? | Yes |
| Does the sound horizon shift in the right direction? | Yes |
| Is the shift large enough? | Not yet |
| Should more toy tuning continue? | No |

---

## Next Required Calculation

The next calculation is not another toy source-function sweep.

Required next step:

```text
Implement PNT prompt source as an external energy-injection / perturbation source in CLASS or CAMB and evaluate CMB + BAO likelihood effects.
```

Secondary step:

```text
Derive the late-memory w(z) and void-filament differential quantitatively.
```

---

## Use in Paper

This file should feed Section 3 and Section 4 of the PNT-P2 working draft.

Recommended language:

> In minimal sourced-decay models, the PNT prompt channel generates a transient EDE-like component and reduces the sound horizon in the correct direction, but the reduction remains partial. We therefore identify the microphysical plasma transfer function as the decisive next calculation rather than claiming a resolved Hubble tension.
