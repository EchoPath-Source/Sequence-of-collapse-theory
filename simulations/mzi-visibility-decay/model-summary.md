# SOC-MZI Visibility Decay Simulation — Model Summary

**Source:** `_Sequence_of_Collapse_SOC_-_MZI_Visibility_De.pdf`  
**Status:** Simulation / feasibility scaffold, not experimental evidence  
**Claim level:** Mathematically compatible minimal model; physically novel extension requiring operational mapping of `A(t)`.

---

## Core Purpose

This simulation models Mach-Zehnder interferometer visibility under an awareness-modulated decoherence term.

The working ansatz is:

```text
lambda_eff = lambda_env + lambda_c * A(t)
V(tau, A) = V0 * exp[-lambda_eff * tau]
```

Where:

- `lambda_env` is the environmental decoherence rate.
- `lambda_c` is a free awareness-coupling coefficient.
- `A(t)` is an abstract awareness / attention index.
- `tau` is the interferometer delay.
- `V0` is baseline visibility.

The uploaded simulation uses a simple exponential visibility decay, shot-noise perturbation, and a timing asymmetry between early and late attention pulses.

---

## Key Model Predictions

1. **Main effect:** visibility decreases faster for higher `A`.
2. **Timing asymmetry:** early pulses should produce stronger suppression than late pulses.
3. **Dose response:** visibility suppression should scale monotonically with `A`.

These are useful because they translate the broad SoCT consciousness-collapse claim into falsifiable MZI-style observables.

---

## Minimal Parameter Set From Source

```text
lambda_env = 0.02
lambda_c   = 0.015
V0         = 0.90
DELAYS     = [10, 20, 40, 80] microseconds
A_LOW      = 0.2
A_HIGH     = 0.8
N_PHOTONS  = 5000
```

Timing asymmetry in the toy model:

```text
early tau_eff = 1.15 * tau
late  tau_eff = 0.85 * tau
```

---

## Literature-Positioning Summary

The source file includes a Consensus-style comparison with existing MZI decoherence literature.

Main points:

- Real MZI visibility often decays with effective dephasing rates driven by physical knobs such as temperature, path length, bias, noise, phonons, and electron-electron interactions.
- Pure exponential decay is a useful simplification but not the full behavior of real interferometers.
- Visibility can equal a decoherence parameter in ideal symmetric cases, but in biased/asymmetric setups it can misrepresent underlying coherence.
- Real interferometers can show lobes, zeros, revivals, asymmetric decay, and non-Gaussian noise structures.
- `A(t)` is the novel element. It is not a known physical knob and must be operationalized.

---

## Critical Limitation

The model is not yet experimentally testable until `A(t)` is mapped onto measurable variables.

Candidate operational definition:

```text
A(t) = w1 * neural_engagement(t)
     + w2 * physiological_phase_locking(t)
     + w3 * behavioral_task_accuracy(t)
     + w4 * subjective_attention_rating(t)
```

The weights must be preregistered or learned only in a training dataset.

---

## Recommended Repo Split

This source should feed two repo tracks:

```text
simulations/mzi-visibility-decay/
  model-summary.md
  source-code-notes.md
  future-notebook.ipynb

experiments/quantum/
  mach-zehnder-consciousness-test.md
```

---

## Falsification Criteria

The SOC-MZI hypothesis is weakened if:

1. operational `A(t)` fails to predict residual visibility after environmental controls;
2. high-`A` and low-`A` conditions show no distinguishable visibility behavior in adequately powered blinded trials;
3. timing asymmetry disappears under preregistered analysis;
4. all observed deviations are explained by detector bias, phase drift, thermal noise, shot noise, or apparatus asymmetry.

---

## Next Work

1. Extract code into a standalone Python script or notebook.
2. Define `A(t)` using measurable physiological and behavioral variables.
3. Convert the MZI design into an OSF prereg-ready protocol.
4. Add bias-aware and nonmonotonic noise models before any experimental claim.

---

## Paper-Safe Summary

> SOC-MZI is a minimal simulation showing how an awareness-index term could be added to an effective dephasing model. It is structurally compatible with visibility-decay modeling in interferometry, but its novel variable `A(t)` requires operational definition and controlled experimental mapping before the hypothesis can be tested.
