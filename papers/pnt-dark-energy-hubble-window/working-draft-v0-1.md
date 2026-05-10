# Planck Nucleation Exhaust as a Two-Timescale Dark Energy Model

**Working Draft v0.1**  
**Project:** Sequence of Collapse Theory / Planck Nucleation Theory  
**Author:** Antoine L. Shephard / Echo Mirrowen  
**Status:** Internal working draft, not yet submitted, not yet peer reviewed  
**Purpose:** Convert the PNT dark-energy and Hubble-window discussion into a publishable, physics-first manuscript skeleton.

---

## Candidate Title

**Planck Nucleation Exhaust as a Two-Timescale Dark Energy Model: Memory-Field Residue, Void-Filament Differentials, and an Early-Exhaust Feasibility Window**

---

## Abstract Draft

Planck Nucleation Theory (PNT) proposes that failed Planck-scale nucleation events contribute to an effective vacuum-energy sector, while longer-lived entanglement residue from successful and failed nucleation attempts contributes to the Sequence of Collapse Theory memory field. This working paper studies the dark-energy implications of that proposal using a two-timescale decomposition. The prompt exhaust channel, with an effective decay or thermalization timescale of approximately 10^3 to 3 x 10^4 years, can generate an Early-Dark-Energy-like transient around the matter-radiation transition, reducing the sound horizon in the correct direction for Hubble-tension relief. In minimal sourced-decay toy models, however, the reduction remains partial, approximately 1-3%, below the likely 4-6% required for full Hubble-tension resolution. The long-memory residue channel, with a gigayear-scale persistence time, is therefore treated as the core late-time dark-energy component, predicting mild w(z) evolution and a void-versus-filament dark-energy differential. The prompt-channel Hubble extension is framed as a constrained feasibility window requiring Boltzmann-code and spectral-distortion follow-up rather than as a demonstrated solution.

---

## 1. Scope and Research Boundary

This paper is intentionally narrower than the full Sequence of Collapse Theory synthesis.

It does **not** attempt to prove consciousness-collapse coupling, observer finalization, science-religion unification, or the full SoCT metaphysical framework.

It focuses only on the physics-facing PNT question:

> Can Planck-scale nucleation exhaust and memory residue be modeled as a two-timescale dark-energy sector with observationally testable consequences?

The consciousness and meaning layers remain downstream synthesis topics and should not be foregrounded in this paper.

---

## 2. Core PNT Claim Relevant to Dark Energy

PNT proposes that the vacuum contains continuous Planck-scale nucleation attempts. Most fail and return energy to the accessible low-energy regime. Some succeed as gravitationally stable structures or black-hole-like causal separations.

The dark-energy sector is decomposed as:

```text
rho_DE^PNT(z) = rho_prompt(z) + rho_memory(z)
```

Where:

- `rho_prompt(z)` is a short-lived prompt exhaust channel that may couple to the early photon-baryon plasma.
- `rho_memory(z)` is a long-lived residue channel associated with accumulated entanglement/memory modifications in the Planck-scale substrate.

This decomposition emerged as necessary from repeated toy-model checks. A single monotonic accumulation channel cannot simultaneously behave like Early Dark Energy and late dark energy.

---

## 3. Two-Timescale Decomposition

### 3.1 Prompt Exhaust Channel

The prompt component is modeled as a sourced-decay integral:

```text
rho_prompt(t) = integral_0^t S_fail(t') exp[-(t - t') / tau_ex] dt'
```

Where:

- `S_fail(t)` is the failed-nucleation source rate.
- `tau_ex` is the prompt exhaust decay or thermalization timescale.

Toy calculations indicate that EDE-like viability requires:

```text
tau_ex ~ 0.001 - 0.03 Myr
       ~ 10^3 - 3 x 10^4 years
```

This channel decays to negligible levels by the present epoch and therefore does not explain today's dark-energy density on its own.

### 3.2 Long-Memory Residue Channel

The memory component is modeled as a long-persistence residue:

```text
rho_memory(t) = integral_0^t S_residue(t') K_memory(t - t') dt'
```

with a memory kernel such as:

```text
K_memory(Delta t) = exp[-Delta t / tau_memory]
```

A working target range from prior SoCT/SPARC framing is:

```text
tau_memory ~ 3.5 - 9 Gyr
```

The late memory component is the main P2 anchor because it can support:

- mild late-time w(z) evolution,
- environmental dark-energy differentials,
- void-versus-filament expansion differences,
- connection to collapse-memory gravity work.

---

## 4. Late Memory Component: Core Publishable Track

### 4.1 Equation-of-State Direction

If `rho_memory` accumulates slowly but is not a strict cosmological constant, it should produce an effective equation of state near but not exactly equal to -1.

Working qualitative prediction:

```text
w_eff(z) ≈ -1 at higher redshift
w_eff(z=0) mildly above -1, roughly -0.95 to -0.98 in exploratory framing
```

This must be derived quantitatively before submission.

### 4.2 Void-Filament Differential

PNT predicts that failed nucleation exhaust should be environment-dependent.

In dense filaments and galaxy-rich environments, a larger fraction of nucleation attempts are converted into stable structures or bound collapse products. In cosmic voids, fewer attempts are converted, leaving a larger failed-exhaust contribution.

Working prediction:

> Effective dark-energy density should be higher in cosmic voids than in galaxy filaments at comparable redshift, beyond standard Lambda-CDM environmental expectations.

Candidate observational target:

- DESI BAO void statistics
- void-versus-filament expansion-rate comparisons
- environment-dependent w(z) reconstructions

This is the high-confidence near-term test track for P2.

---

## 5. Prompt EDE Feasibility Window

### 5.1 Why a Simple Accumulation Model Fails

A monotonic accumulated dark-energy component grows toward the present. That is the wrong shape for Early Dark Energy, which requires a component that is relevant near the pre-recombination / equality era and then rapidly dilutes or shuts off.

Therefore:

```text
rho_DE(t) proportional to t
```

is not an EDE model.

### 5.2 Gaussian Source Toy Model

The initial feasibility model used an early source bump centered around `z_c ~ 3500-10000` with short `tau_ex`.

Findings:

- EDE-like transients are possible.
- `z_c ~ 5000-8000` places the fractional bump in a more useful range.
- Sound-horizon reduction is directionally correct but typically only ~1-3%.

### 5.3 Radiation-Coupled Source Toy Model

A more physically motivated source uses early plasma coupling:

```text
S_fail,prompt(z) proportional to (1 + z)^4
```

with a transition cutoff near matter-radiation equality:

```text
z_transition ~ 3400
```

Findings:

- The source is better motivated than a Gaussian.
- It still produces only partial sound-horizon reduction in the minimal toy model.
- Best toy-model outcomes remain approximately ~1.8-2.8%, below the likely ~4-6% needed for full Hubble-tension resolution.

### 5.4 Status of Hubble-Tension Claim

The correct claim is:

> The PNT prompt channel opens a constrained EDE feasibility window but does not yet demonstrate a full Hubble-tension resolution in minimal toy models.

The paper must not claim that PNT solves the Hubble tension unless a Boltzmann-code implementation confirms sufficient sound-horizon reduction under physical transfer functions.

---

## 6. Microphysical Transfer Function

The missing object is a plasma transfer function:

```text
T_plasma(z, k, E)
```

This should encode:

- Comptonization,
- photon injection,
- baryon momentum transfer,
- spectral distortion constraints,
- perturbation response,
- CMB anisotropy and damping-tail limits,
- BAO consistency.

The factor-of-two shortfall in the toy model should be framed not as a failure, but as a concrete follow-up target:

> Does a physically correct Boltzmann/spectral-distortion treatment amplify, suppress, or rule out the prompt-channel effect?

Candidate tools:

- CLASS
- CAMB
- CosmoTherm / spectral-distortion-style analysis
- Full CMB + BAO likelihood comparison

---

## 7. Falsification Criteria

PNT-P2 is weakened or falsified if:

1. The late memory component cannot produce a viable w(z) trajectory within observational bounds.
2. DESI-like void-versus-filament analyses show no environment-dependent dark-energy differential, or show the opposite sign after controls.
3. The prompt channel violates CMB spectral-distortion or anisotropy constraints.
4. Boltzmann-code implementation shows `Delta r_s / r_s` remains below ~2% across all physically allowed prompt-channel transfer functions.
5. The model requires more free parameters than standard EDE or dark-sector alternatives to achieve the same fit quality.

---

## 8. Prediction Table

| Prediction | Confidence | Dataset / Tool | Status |
|---|---:|---|---|
| Void dark-energy density exceeds filament dark-energy density at matched redshift | High | DESI BAO / void statistics | Needs derivation |
| Late-time w(z) mildly evolves away from -1 | Medium | DESI DR2+ / SN / BAO | Needs fit |
| Prompt exhaust produces EDE-like transient | Medium | Toy model + Boltzmann code | Toy supported |
| Prompt channel reduces sound horizon enough to relieve Hubble tension | Speculative | CLASS/CAMB + CMB likelihood | Not demonstrated |
| Spectral distortions constrain or detect prompt exhaust | Speculative | FIRAS / PIXIE-like future constraints | Needs modeling |

---

## 9. Publication Strategy

Recommended sequence:

1. **P1: SPARC collapse-memory gravity paper**  
   Empirical anchor. Strengthen with radial decomposition and age/dark-fraction analysis.

2. **P2: PNT two-timescale dark-energy paper**  
   Lead with late memory and void/filament predictions. Treat Hubble tension as a feasibility window.

3. **P3: CIH / CMB directional-memory paper**  
   Requires stronger derivation of directional geometry and axis prediction.

4. **P4: Full SoCT synthesis**  
   Only after P1/P2/P3 establish physics-facing credibility.

---

## 10. Immediate Next Work

- Derive the late-memory `w(z)` expression.
- Derive a first quantitative void-filament differential.
- Write a reproducible notebook for the toy prompt-channel calculations.
- Define the Boltzmann-code source term required for CLASS/CAMB.
- Keep consciousness-collapse and metaphysical implications out of this paper except as background to the broader SoCT program.

---

## Working Summary

The toy phase has completed its job. It established that PNT naturally decomposes into two dark-energy-like channels, that a prompt EDE-like transient is possible but insufficient in minimal form, and that the late memory component is the strongest near-term publishable target. The next bottleneck is not further toy tuning; it is formal derivation, observational mapping, and paper drafting.
