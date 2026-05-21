# Empirical Exploration Thread Summary v0.1

**Author:** Antoine L. Shephard / Echo Mirrowen  
**Status:** Internal / pre-publication synthesis  
**Scope:** SoCT empirical exploration phase: SPARC, effective-G memory model, PM simulation alignment, and Pantheon+ environment-H0 pipeline.

---

## 1. Purpose

This document preserves the first major empirical transition of the Sequence of Collapse Theory from conceptual cosmology into a structured, testable research program.

The thread moved from broad theory into four measurable channels:

1. SPARC age versus outer dark-matter-fraction correlation.
2. Effective-G / memory-kernel formulation of gravity.
3. PM simulation interpretation of void-filament expansion differentials.
4. Pantheon+ covariance-aware environment-dependent H0 pipeline.

The goal is not to claim confirmation. The goal is to preserve a disciplined record of what has been proposed, what has been provisionally supported, and what remains unverified.

---

## 2. Core Empirical Hypothesis

If gravity includes an accumulated collapse-history or memory-field component, then older and/or more structurally evolved systems should show stronger apparent gravitational excess than younger systems with comparable baryonic content.

Galaxy-scale phrasing:

```text
older stellar population -> greater accumulated memory -> stronger outer velocity excess -> higher inferred f_DM
```

Cosmological-environment phrasing:

```text
void regions -> lower collapse memory -> faster local expansion
filament regions -> higher collapse memory -> slower local expansion
```

Primary predicted sign:

```text
H0_void > H0_filament
```

---

## 3. SPARC Empirical Anchor

The SPARC analysis is currently the strongest empirical anchor in this phase.

Thread-level working result:

```text
Pearson/Spearman age-f_DM correlation: r ~ +0.20
p-value: ~0.005 to 0.008 depending on cuts
```

Interpretation:

- The signal is modest.
- The signal is not decisive.
- The signal is directionally consistent with memory-field gravity.
- The signal reportedly survives basic mass-proxy robustness and train/test splitting.
- The signal weakens under richer multivariate control, suggesting possible mediation through structure rather than a direct independent force term.

Important caution:

The D4000 spectral-age proxy and environment-split results are promising but require full re-validation from raw ingestion and reproducible cross-matching.

---

## 4. Effective-G Memory Model

The cleanest formal framing developed in the thread is not a Planck-scale rewrite, but an effective gravitational coupling model:

```math
G_eff(x,t) = G_0 [1 + alpha M(x,t)]
```

where:

- `G_0` is the locally measured Newtonian gravitational constant.
- `alpha` is a small memory-coupling amplitude.
- `M(x,t)` is an accumulated memory field.

A minimal exponential memory form is:

```math
M(t) = 1 - exp(-t/tau)
```

This preserves the usual Planck-unit definitions at the fundamental level because it does not modify `c`, `hbar`, or the local definition of `G_0`. The modification is treated as a low-energy, large-scale effective coupling.

---

## 5. Velocity-Shift Bridge

Circular velocity satisfies:

```math
V^2(r) = r g(r)
```

With memory amplification:

```math
V_obs^2(r,t) = V_bar^2(r) [1 + alpha M(t)]
```

Using the exponential memory form:

```math
V_obs^2(r,t) = V_bar^2(r) [1 + alpha(1 - exp(-t/tau))]
```

For small `alpha`:

```math
Delta V / V_bar ~ 0.5 alpha (1 - exp(-t/tau))
```

The SPARC outer dark-matter fraction is:

```math
f_DM = 1 - (V_bar / V_obs)^2
```

Substitution gives:

```math
f_DM(t) = 1 - 1/[1 + alpha(1 - exp(-t/tau))]
```

Weak-coupling approximation:

```math
f_DM(t) ~ alpha(1 - exp(-t/tau))
```

For observational fitting, use a baseline term:

```math
f_DM(t) = f_0 + A_mem(1 - exp(-t/tau))
```

Thread-level visual extraction suggested approximately:

```text
f_0 ~ 0.60
A_mem ~ 0.20
tau ~ 7-8 Gyr
```

This is preliminary and must be replaced by a raw-data nonlinear fit.

---

## 6. PM Simulation Alignment

The PM simulation track is interpreted as a meso-scale testbed for the same memory-field hypothesis.

Thread-level result:

```text
Delta H / H ~ 0.5% in the expected direction
void expansion bias positive
filament memory/collapse drag negative relative to voids
```

This is not a claim of real cosmological detection. It is a controlled internal simulation result showing that the sign and scale of the proposed mechanism can remain subdominant rather than catastrophic.

---

## 7. Pantheon+ Environment-H0 Pipeline

The Pantheon+ track is the next major observational test.

Locked primary hypothesis:

```math
Delta H0 = H0_void - H0_filament > 0
```

Pipeline requirements:

1. Use Pantheon+ SN table with redshift, distance modulus, sky position, and IDs.
2. Use the covariance matrix for all primary fits.
3. Cross-match supernovae to void/filament environment labels.
4. Fit H0 separately for void and filament subsets under fixed flat LCDM background.
5. Compute `Delta H0` and covariance-aware uncertainty.
6. Run redshift-matched bootstrap, permutation test, sky jackknife, diagonal-only diagnostic, alternate catalog check, and redshift-cut sensitivity.

Primary statistic:

```math
Delta H0 = H0_void - H0_filament
```

Interpretation bands:

```text
Delta H0 > 0, <1 sigma: correct sign, not significant
Delta H0 > 0, 1-2 sigma: suggestive
Delta H0 > 0, 2-3 sigma: interesting, needs replication
Delta H0 > 0, >3 sigma: strong candidate signal
Delta H0 < 0: tension with the SoCT prediction
```

---

## 8. Current Status

Established at thread level:

- SPARC contains a modest positive age-f_DM signal.
- A minimal exponential memory model maps cleanly into both effective-G language and f_DM fitting.
- Approximate tau extraction from visual SPARC trend lands in the broader 3.5-9 Gyr working band.
- PM simulations have produced sign-consistent, subdominant void-filament expansion behavior.
- Pantheon+ covariance-aware pipeline has been defined but not yet finalized with real-data verdict.

Not yet established:

- A fully audited raw-data nonlinear SPARC tau fit.
- Independent D4000 validation.
- Reproducible isolated/group environment split.
- Real-data Pantheon+ environment H0 detection.
- A demonstrated need for the deeper Planck Nucleation Theory substrate.

---

## 9. Research Integrity Note

This phase explicitly separates:

- measured signals,
- simulated behavior,
- preregistered pipeline intent,
- and speculative substrate interpretation.

Synthetic signal-injection demonstrations must not be represented as real detections. LLM-generated or visually extracted parameters must be replaced by reproducible raw-data analysis before publication claims.

---

## 10. Recommended Next Additions

1. Add raw SPARC analysis CSV and/or notebook.
2. Add Pantheon+ SN table and environment-label cross-match output.
3. Add covariance-aware H0 fitting script.
4. Add nonlinear SPARC memory-fit notebook.
5. Add `data/README.md` with dataset provenance and licensing notes.
6. Add `notebooks/README.md` describing reproducibility standards.

---

## 11. Working Summary

The strongest near-term SoCT research route is:

```text
history-dependent effective gravity -> exponential memory accumulation -> age-dependent outer velocity excess -> environment-dependent expansion residuals
```

The PNT substrate remains interesting, but the empirical program should proceed first through the effective-G / memory-kernel layer because it is simpler, testable, and does not require modifying Planck-scale physics.
