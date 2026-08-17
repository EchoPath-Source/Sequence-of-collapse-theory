# Simulation 1 — Qubit + Pointer Observation Benchmark

**Status:** Baseline complete  
**Physics level:** Standard quantum dynamics + benchmark pointer-memory channel only  
**SoCT-specific feedback:** None  
**Consciousness term:** None

## Purpose

This is the first simulation in the SoCT operational observation program.

It tests whether candidate observation metrics behave sensibly before any SoCT memory feedback is introduced.

The simulation asks whether increasing measurement interaction strength produces increasing:

- pointer-state distinguishability;
- quantum system-pointer correlation;
- accessible record information;
- provisional observation strength;

and whether degrading the pointer record causes the persistent observation metric to decay.

## Model

The system qubit begins in

```math
|+\rangle = (|0\rangle+|1\rangle)/\sqrt{2}
```

and the two-state pointer begins in `|0>`.

The measurement interaction is parameterized by `theta`:

```math
|0\rangle|0\rangle \rightarrow |0\rangle|0\rangle
```

```math
|1\rangle|0\rangle \rightarrow |1\rangle|\phi(\theta)\rangle
```

with

```math
|\phi(\theta)\rangle
=\cos\theta|0\rangle+\sin\theta|1\rangle.
```

Therefore:

```text
theta = 0      -> no pointer record
theta = pi/2   -> orthogonal / perfectly distinguishable pointer records
```

After the interaction, pointer persistence is benchmarked with

```math
\rho(t)=r(t)\rho+[1-r(t)]I/2
```

where

```math
r(t)=e^{-\gamma t}.
```

This depolarizing channel is only a toy record-retention model. It is not the SoCT memory field `M`.

## Metrics

The script calculates:

```text
measurement_strength       = sin^2(theta)
pointer_trace_distance     = distinguishability of conditioned pointer states
quantum_mutual_info_bits   = total S:O quantum correlation immediately after interaction
holevo_bits                = upper bound on accessible binary record information
persistence_ratio          = retained Holevo information / initial Holevo information
omega_event                = measurement_strength * initial trace distance
omega_persistent           = omega_event * persistence_ratio
```

`omega_event` and `omega_persistent` are provisional diagnostics, not proposed physical laws.

## Baseline result

The sanity tests pass.

At `theta=0`:

```text
trace distance = 0
Holevo record information = 0
Omega_event = 0
```

At `theta=pi/2`:

```text
trace distance = 1
Holevo record information = 1 bit
quantum mutual information = 2 bits
Omega_event = 1
```

Across the interaction sweep, initial distinguishability, accessible record information, and `Omega_event` increase monotonically.

For every nonzero interaction condition, the benchmark depolarizing memory channel causes `Omega_persistent` to decrease monotonically with elapsed time.

This is the expected behavior for a useful first observation metric.

## Interpretation

Simulation 1 does **not** provide evidence for SoCT-specific physics.

It establishes a clean null baseline:

```text
ordinary quantum interaction
  -> correlation
  -> distinguishable pointer record
  -> accessible information
  -> record decay
```

This gives the observation project a calibrated lower layer before introducing either:

```text
SoCT memory feedback H_M = lambda_M M O_M
```

or

```text
conscious-access coupling H_c = lambda_c Phi_c O_c.
```

An important result is that total quantum correlation and readable record information are not identical. At perfect measurement coupling the pure entangled pair carries 2 bits of quantum mutual information while the binary pointer carries at most 1 bit of accessible record information. The observation model should therefore avoid treating generic correlation alone as equivalent to an observational record.

## Run

```bash
python simulations/observation-qubit-pointer/simulate_qubit_pointer.py
```

Default output:

```text
simulations/observation-qubit-pointer/results.csv
```

Expected terminal summary:

```text
wrote 45 rows
perfect-record limit: D=1.000000, chi=1.000000 bit, QMI=2.000000 bits, Omega_event=1.000000
sanity checks: PASS
```

## Next simulation

Simulation 2 should add an explicit environment `E` and separately track:

```text
S-O record formation
S-E decoherence
record persistence
redundant environmental information
```

The goal is to determine whether the operational observation metric adds anything beyond ordinary decoherence strength, or simply reparameterizes it.

## Claim boundary

Use:

> Simulation 1 validates the behavior of provisional observation metrics under a controlled standard-quantum benchmark.

Avoid:

> Simulation 1 demonstrates physical collapse memory or conscious observation effects.
