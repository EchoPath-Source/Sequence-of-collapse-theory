# Collapse / Decoherence / Observer-State Discriminants — SoCT

**Status:** Research-comparison scaffold  
**Purpose:** Define observations that can distinguish standard environmental decoherence, objective-collapse models, and the current Sequence of Collapse Theory (SoCT) observer-state hypothesis.

## Scope

This file converts literature adjacency into discriminating tests. It does **not** assume that any nonstandard collapse model is correct, and it does not treat observer-state correlations as evidence unless apparatus, environmental, statistical, and physiological alternatives are controlled.

The current SoCT P4 scaffold is deliberately narrow:

```text
lambda_eff = lambda_env + lambda_c A(t)
V(tau, A) = V0 exp[-lambda_eff tau]
```

where `A(t)` is an operational observer-state variable and `lambda_c = 0` recovers the no-observer-coupling case.

A valid SoCT test must therefore discriminate an observer-linked contribution from ordinary decoherence, drift, selection effects, and objective-collapse dynamics that do not depend on conscious access.

## Claim Boundary

- A visibility change is not automatically collapse.
- A correlation with physiology is not automatically causal observer coupling.
- Objective-collapse models do not imply consciousness-driven collapse.
- Decoherence is the default comparison baseline and must be modeled before adding a new channel.
- SoCT is weakened if its proposed observer-state signature is reproducibly absent under adequately powered, preregistered conditions.

## Primary Discriminant Matrix

| Feature / observable | Standard QM + decoherence | GRW / CSL-like objective collapse | Diósi-Penrose-like gravity collapse | Current SoCT observer-state channel | Discriminating value |
|---|---|---|---|---|---|
| Environmental sensitivity | Visibility/coherence changes with temperature, vibration, scattering, phase noise, detector effects, and other couplings | Environmental effects remain, plus intrinsic stochastic localization | Environmental effects remain, plus proposed gravity-related instability | Environmental effects remain, plus hypothesized `A(t)`-linked contribution | Essential baseline; any SoCT signal must survive matched environment controls |
| System mass / size scaling | No new intrinsic collapse term; decoherence often increases strongly with system complexity and coupling | Characteristic deviations grow toward larger/more massive systems depending on model parameters | Expected reduction timescale depends on gravitational self-energy / mass-distribution separation | No current repo prediction that observer coupling must scale like CSL or DP mass scaling | Mass scaling can distinguish established collapse-model parameterizations from an observer-state term |
| Observer presence with no task-relevant access | No special physical role expected beyond ordinary apparatus/environment changes | No special consciousness role | No special consciousness role in the basic proposal | Sham/null-information condition should approach baseline if structured observer access is required | High-value SoCT-specific control |
| High- vs low-`A(t)` observer state | No fundamental dependence after physical covariates are controlled | No fundamental dependence on `A(t)` | No fundamental dependence on `A(t)` | Preregistered visibility/dephasing difference predicted if `lambda_c != 0` | Core P4 discriminator |
| Recorded-but-unaccessed vs consciously accessed information | Standard theory predicts physical evolution from interaction/measurement structure, not later human access as a new law | No special access dependence | No special access dependence | Current P14 branch predicts a possible difference under controlled delayed-access conditions | Strong discriminator if protocol prevents physical-path differences between conditions |
| Timing dependence relative to observer-access window | Determined by ordinary interaction and decoherence timescales | Determined by model collapse rate and system parameters | Determined by gravitational collapse timescale | Current protocol predicts possible early/late or delay dependence tied to `A(t)` exposure | Useful only if timing is preregistered and apparatus timing is stable |
| Spontaneous heating / radiation / diffusion | No collapse-specific excess | Some CSL parameterizations predict non-interferometric signatures such as heating, diffusion, or radiation | Specific DP implementations can be constrained by non-interferometric observables | Not a primary SoCT observer-state prediction | Positive non-interferometric signal without observer dependence would favor objective-collapse physics over P4 |
| Trial-history hysteresis | Ordinary apparatus memory/drift possible and must be modeled | Not a generic defining prediction, though stochastic dynamics can have model-specific correlations | Not a generic defining prediction | SoCT P13/P15 proposes possible residual history or post-observation effects through memory persistence | Potentially distinctive but currently secondary and highly artifact-sensitive |
| Intention-selected outcome bias | Standard Born statistics | Standard collapse models preserve statistical rules in their own parameterized way | Basic DP does not provide arbitrary intention control | Not a current core SoCT claim; P8 is explicitly speculative | Should not be used as a primary validation target |

## Minimal Experimental Logic

A serious P4 experiment should be capable of testing the following nested models:

### M0 — Apparatus / environmental model

```text
V = f(phase drift, temperature, vibration, detector state, timing, trial order, source stability, ...)
```

### M1 — Environmental dephasing model

```text
lambda_eff = lambda_env
```

### M2 — Observer-extended SoCT model

```text
lambda_eff = lambda_env + lambda_c A(t)
```

The scientifically relevant question is not whether `M2` can fit the data. It is whether adding `lambda_c A(t)` produces preregistered out-of-sample or likelihood-level improvement that survives nuisance controls, multiple-testing discipline, and independent analysis.

## High-Value Control Conditions

| Control | Purpose | Interpretation if it removes the effect |
|---|---|---|
| Participant absent | Measures pure apparatus/environment baseline | Supports ordinary physical explanation |
| Participant present, null information | Separates presence from task-relevant access | Weakens an access-specific SoCT interpretation if effect remains unchanged |
| High-A vs low-A matched optical trials | Tests graded observer-state hypothesis | Null separation constrains `lambda_c` |
| Sham target / irrelevant target | Tests whether generic attention/arousal is sufficient | If effect follows arousal rather than relevant access, current SoCT interpretation requires revision |
| Delayed access with identical prior physical logging | Tests P14 access dependence | Equality constrains conscious-access branch |
| Blinded analysis labels | Prevents analyst-expectancy leakage | Mandatory for credibility |
| Apparatus-only replay / synthetic timing control | Tests whether timing structure alone recreates effect | Positive replay effect favors artifact/timing explanation |

## What Would Favor Each Research Lane?

### Standard decoherence favored

A result favors the standard baseline if apparent condition differences are explained by measured phase noise, detector/source drift, thermal/mechanical variation, trial order, behavioral movement, or other ordinary couplings, and no stable residual remains after correction.

### Objective-collapse model favored

A result would be more naturally aligned with an objective-collapse lane if deviations track mass, spatial separation, or model-specific non-interferometric signatures while remaining independent of observer access and `A(t)`.

That would **not** validate SoCT's observer channel.

### SoCT observer-state channel remains viable

The current P4 observer-state hypothesis remains viable only if a preregistered effect:

1. tracks the defined `A(t)` variable or access condition;
2. survives environmental and apparatus covariates;
3. is not reproduced by sham/null-information conditions;
4. shows the prespecified timing structure if timing is part of the prediction;
5. replicates independently; and
6. cannot be reduced to generic arousal, movement, expectation, or analysis flexibility.

## Falsification / Constraint Conditions

The P4 observer-state channel should be considered constrained if an adequately powered, blinded, preregistered experiment finds:

- `lambda_c` statistically consistent with zero within a useful sensitivity bound;
- no high-A / low-A visibility or coherence difference;
- no conscious-access / machine-only difference;
- no prespecified timing relation;
- or all apparent effects disappear under ordinary apparatus/environment/physiology controls.

Repeated null results should narrow or retire the observer-coupling parameter space rather than be reinterpreted as hidden support.

## Repo Mapping

Primary SoCT predictions:

```text
PREDICTIONS.md: P7, P13, P14, P15, P16
```

Protocol and measures:

```text
papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md
papers/p4-soc-mzi-awareness-modulated-decoherence/materials-and-measures.md
papers/p4-soc-mzi-awareness-modulated-decoherence/statistical-analysis-plan.md
papers/p4-soc-mzi-awareness-modulated-decoherence/lab-collaboration-brief.md
```

Math scaffold:

```text
papers/math/soc-localization-memory-hamiltonian.md
```

## Next Quantitative Work

1. Define the exact null and alternative statistical models for `lambda_c`.
2. Freeze a primary `A(t)` estimator before data collection.
3. Produce a power curve for the smallest observer-linked dephasing effect worth detecting.
4. Add sensitivity bounds that translate a null result into an upper limit on `|lambda_c|`.
5. Separate the primary observer-state test from secondary hysteresis/post-observation tests.
6. Predefine what outcome would cause P7/P14/P16 to be marked `falsified / constrained` in `PREDICTIONS.md`.

## Source Notes

- G. C. Ghirardi, A. Rimini, T. Weber, *Physical Review D* **34**, 470 (1986), DOI `10.1103/PhysRevD.34.470` — original GRW framework.
- P. Pearle, *Physical Review A* **39**, 2277 (1989), DOI `10.1103/PhysRevA.39.2277` — continuous stochastic localization development.
- A. Bassi et al., *Reviews of Modern Physics* **85**, 471 (2013), DOI `10.1103/RevModPhys.85.471`, arXiv:`1204.4325` — collapse-model foundations and experimental tests.
- M. Carlesso et al., *Nature Physics* **18**, 243–250 (2022), DOI `10.1038/s41567-021-01489-5` — non-interferometric constraints on collapse models.
- W. H. Zurek, *Reviews of Modern Physics* **75**, 715 (2003), DOI `10.1103/RevModPhys.75.715`, arXiv:`quant-ph/0105127` — decoherence and einselection.
- W. H. Zurek, *Nature Physics* **5**, 181–188 (2009), DOI `10.1038/nphys1202` — quantum Darwinism.
- R. Penrose, *General Relativity and Gravitation* **28**, 581–600 (1996), DOI `10.1007/BF02105068` — gravity-related objective reduction motivation.

## Reference-Use Boundary

These sources establish neighboring models and known experimental discriminants. They do not establish the SoCT term `lambda_c A(t)`. That term must stand or fall on its own preregistered empirical performance.