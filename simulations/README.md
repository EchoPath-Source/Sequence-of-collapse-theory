# Simulations Hub

This folder is reserved for computational, modeling, and validation materials.

## Operational observation program

Active sequence:

```text
simulations/observation-qubit-pointer/
simulations/observation-qubit-pointer-environment/
simulations/observation-record-erasure/
simulations/observation-redundancy-irreversibility/
simulations/observation-history-memory-feedback/
simulations/observation-history-controls/
simulations/observation-history-randomized-crossover/
simulations/observation-history-preparation-carryover/
simulations/observation-history-covariate-error/
```

Simulation 1 establishes the standard-quantum qubit-pointer baseline. Simulation 2 separates designated pointer record formation from total system decoherence. Simulation 3 shows that an ideal reversible record can be erased even though record creation occurred earlier. Simulation 3b shows that distributed records survive partial reversal and motivates persistence/redundancy/irreversibility weighting in the candidate record-production source.

Simulation 4 introduces the speculative SoCT memory-feedback term and defines a matched-standard-state/different-history discriminator. Simulation 4b shows that its simple smooth phase trajectory is not unique under ordinary nuisance drift. Simulation 4c redesigns the test using randomized history-dose crossover. Simulation 4d shows that preparation-induced ordinary carryover can create a large false history effect even under randomized assignment.

Simulation 4e attacks the next assumption: measured covariates are incomplete and noisy. With true `lambda_M=0`, measurement error and omitted history-correlated ordinary variables can regenerate statistically strong apparent history coefficients. Therefore a residual cannot be interpreted as SoCT memory merely because known carryover covariates were included in a regression.

## Observation simulation ladder

```text
Simulation 1:  qubit + pointer                          COMPLETE baseline
Simulation 2:  qubit + pointer + environment            COMPLETE baseline
Simulation 3:  record creation + exact erasure          COMPLETE baseline
Simulation 3b: redundant/distributed record             COMPLETE baseline
Source v0.1:   durable record-production source         DEFINED candidate
Simulation 4:  SoCT history-dependent memory feedback  COMPLETE toy discriminator
Simulation 4b: nuisance/drift adversarial controls      COMPLETE; simple trajectory NOT UNIQUE
Simulation 4c: randomized history-dose crossover        COMPLETE identifiability redesign
Simulation 4d: preparation carryover controls           COMPLETE; naive false positive demonstrated
Simulation 4e: covariate error + omitted carryover      COMPLETE; residual can reappear under null
Simulation 4f: sham + negative-control sensitivity      NEXT
Simulation 5:  conscious-access layer                   DEFERRED until lower layers stabilize
```

## Current experimental-design requirement

A credible history-memory test now requires all of the following before a SoCT-specific interpretation is allowed:

```text
randomized history dose
+ crossed physical hardware
+ matched ordinary present state
+ sham preparation histories
+ measured carryover covariates
+ calibrated covariate measurement error
+ negative-control observables
+ omitted-variable sensitivity analysis
+ preregistered rejection/exclusion rules
```

The central discriminator is no longer simply `different history -> different phase`. It is whether a residual follows randomized record-history dose **after** ordinary present-state differences and plausible hidden carryover have been independently bounded.

## Related derivation files

```text
papers/math/soc-operational-observation-model.md
papers/math/soc-observation-to-spacetime-derivation-ladder.md
papers/math/soc-observer-emergence-first-tuning-fork.md
papers/math/soc-record-production-source-v0-1.md
papers/math/soc-localization-memory-hamiltonian.md
```

## Other active simulation directions

- SPARC memory-fit output tables and parameter logs.
- PM void-filament H-split parameter logs.
- Effective-G / memory-kernel toy models.
- CMB / gravitational-wave / black-hole comparison models.
- Parent-child directional-memory toy simulations.
- Observer-emergence / first-tuning-fork modeling after the lower observation layer stabilizes.

## Import and claim boundary

Every simulation asset should record its parameters, source, whether it is exploratory/illustrative/validation-grade, and whether it uses real or synthetic data.

Simulation outputs are mechanism and design checks unless directly tied to observed data with reproducible analysis. Synthetic signal injection must never be presented as an empirical detection of SoCT, memory fields, observer effects, or consciousness-dependent physics.
