# Simulations Hub

This folder is reserved for computational, modeling, and validation materials.

## What belongs here

- symbolic derivations translated into code
- parameter sweeps
- simulation screenshots
- validation summaries
- numerical experiments for memory kernels
- SPARC fitting outputs
- CMB / GW / BH modeling notes
- notebooks converted to stable markdown summaries
- effective-G / memory-kernel toy models
- PM void-filament H-split notes and parameter logs

## Current status

The repo now contains runnable simulation material alongside imported and exploratory scaffolds.

### Operational observation program

The active observation simulation sequence is:

```text
simulations/observation-qubit-pointer/
simulations/observation-qubit-pointer-environment/
simulations/observation-record-erasure/
simulations/observation-redundancy-irreversibility/
simulations/observation-history-memory-feedback/
simulations/observation-history-controls/
simulations/observation-history-randomized-crossover/
simulations/observation-history-preparation-carryover/
```

Simulation 1 is a standard-quantum qubit + two-state pointer benchmark. It sweeps measurement interaction strength and computes pointer trace distance, quantum mutual information, Holevo record information, persistence, and provisional observation-strength diagnostics.

Simulation 2 adds explicit environment fragments and independently varies pointer-record strength and environmental-record strength. It demonstrates that system decoherence can occur while a designated pointer has zero record, so the operational observation metric is not merely a relabeling of total decoherence.

Simulation 3 creates a pointer record and then applies the exact inverse unitary. Present record metrics return to zero while an explicitly defined cumulative positive record-production bookkeeping functional remains nonzero. This exposes the SoCT source-choice problem: should `M` track current records, durable records, integrated persistence, or historical record production?

Simulation 3b distributes the record across multiple environment fragments and then erases only a subset. Distributed record structure survives partial reversal and vanishes only after every record-bearing fragment is reversed in the toy model. This motivates weighting a candidate source by accessible information, persistence, redundancy, and resistance to reversal.

Simulation 4 is the first explicitly SoCT-specific toy discriminator. Two systems start with the same ordinary quantum state, Hamiltonian, and environment, but different speculative memory values inherited from different prior record histories. With `lambda_M=0`, their trajectories are identical. With `lambda_M != 0`, the added term `lambda_M M O_M` produces a calculable history-dependent phase residual.

Simulation 4b is an adversarial control layer. It shows that, over a finite observation window, the simple exponential-memory phase basis can be absorbed extremely well by ordinary constant, linear-frequency, and quadratic-drift nuisance terms, especially for slow memory decay. Therefore a single smooth phase trajectory is not a robust unique signature of SoCT memory.

Simulation 4c changes the design rather than overfitting the same trajectory. Prior history dose is randomized and crossed between physical arms, while hardware offsets and slow drift remain apparatus-tied. In synthetic injected-signal tests, the randomized history coefficient is recoverable while the null stays consistent with zero. This establishes an identifiability strategy, not evidence for SoCT.

Simulation 4d attacks the randomized design with a deeper confound: history preparation itself can leave ordinary present-state differences such as heating, coherence loss, and pulse exposure. In the synthetic null, a naive history-only model produces a very strong false positive, while explicit carryover adjustment removes it. This establishes that randomized history labels are not sufficient unless ordinary preparation carryover is matched, measured, randomized, or bounded.

Simulations 1-3b include:

```text
no SoCT memory feedback
no consciousness term
```

Simulation 4 introduces only the speculative memory-feedback term. Simulations 4b-4d progressively attack that discriminator with ordinary nuisance and carryover structure. Consciousness remains excluded.

Related derivation files:

```text
papers/math/soc-operational-observation-model.md
papers/math/soc-observation-to-spacetime-derivation-ladder.md
papers/math/soc-observer-emergence-first-tuning-fork.md
papers/math/soc-record-production-source-v0-1.md
papers/math/soc-localization-memory-hamiltonian.md
```

The current empirical exploration summary is preserved at:

```text
docs/empirical-exploration-thread-summary-v0-1.md
```

This summary frames the strongest near-term gravitational simulation route as a low-energy effective-G / memory-kernel model rather than a Planck-scale rewrite.

Working phenomenological form:

```math
G_eff(x,t) = G_0 [1 + alpha M(x,t)]
```

Minimal exponential memory form:

```math
M(t) = 1 - exp(-t/tau)
```

## Active simulation directions

1. Operational observation: qubit -> pointer -> environment -> erasure -> redundancy/irreversibility -> history-matched memory feedback.
2. Measurement-error and unmeasured-carryover sensitivity for history protocols.
3. Observer-emergence / first-tuning-fork modeling after the lower observation layer stabilizes.
4. SPARC memory-fit output tables and parameter logs.
5. PM void-filament H-split parameter logs.
6. Effective-G / memory-kernel toy-model scripts.
7. CMB / gravitational-wave / black-hole comparison models.
8. Parent-child directional-memory toy simulations.

## Observation simulation ladder

```text
Simulation 1:  qubit + pointer                         COMPLETE baseline
Simulation 2:  qubit + pointer + environment           COMPLETE baseline
Simulation 3:  record creation + exact erasure         COMPLETE baseline
Simulation 3b: redundant/distributed record            COMPLETE baseline
Source v0.1:   durable record-production source        DEFINED candidate
Simulation 4:  SoCT history-dependent memory feedback COMPLETE toy discriminator
Simulation 4b: nuisance/drift adversarial controls     COMPLETE; simple trajectory NOT UNIQUE
Simulation 4c: randomized history-dose crossover       COMPLETE identifiability redesign
Simulation 4d: preparation carryover controls          COMPLETE; naive false positive demonstrated
Simulation 4e: unmeasured carryover / covariate error  NEXT
Simulation 5:  conscious-access layer                  deferred until lower layers stabilize
```

## Import rule

For every simulation asset added later, include:

- filename
- date
- source thread or source file
- parameter summary
- whether it is exploratory, illustrative, or validation-grade
- whether it is real-data, synthetic, or toy-model output

## Claim boundary

Simulation outputs should be treated as mechanism checks unless directly tied to observed data and reproducible scripts.

Synthetic signal-injection demonstrations must not be presented as real observational detections.
