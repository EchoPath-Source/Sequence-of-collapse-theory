# SIM-04G — Qubit + Detector + Environment Record-Persistence Results

**Status:** explicit open-system/unitary toy benchmark complete  
**Claim level:** standard quantum-mechanical methodology result only; this is **not evidence for SoCT-specific physics**.

## Question

Are peak decoherence, detector correlation, persistent records, reversible correlation, record erasure, and redundant environmental records operationally distinct quantities?

This is the first observation-foundations benchmark in this track that replaces the analytic binary-channel proxy with an explicit state-vector model.

## Model

Five qubits are used:

```text
S  = observed system
D  = detector / pointer
E1,E2,E3 = environment fragments.
```

The system begins in

```math
|+>_S,
```

while the detector and environment begin in `|0>`.

A partial measurement-like interaction is

```math
U_SD(theta)
= |0><0|_S \otimes I_D
+ |1><1|_S \otimes R_y(2 theta)_D.
```

At `theta = 0` the detector states are indistinguishable; as `theta` approaches `pi/2`, the detector becomes an orthogonal which-alternative record.

Environment records are created by controlled copies from `D` into selected environment fragments.

The local measurement interaction can then be reversed by applying

```math
U_SD(theta)^\dagger.
```

For the erasure case, the environment-copy operations are also reversed before the local unmeasurement.

No SoCT memory term is present anywhere in this benchmark.

## Scenarios

For the same initial `S-D` interaction strength, four cases are compared:

```text
reversible    = correlate S and D, then immediately undo U_SD
persistent_1  = copy D into E1, then undo U_SD only
redundant_3   = copy D into E1,E2,E3, then undo U_SD only
erased_3      = copy into E1,E2,E3, reverse those copies, then undo U_SD.
```

Metrics include

```text
system coherence
peak decoherence loss
quantum mutual information I(S:D)
fragment mutual information I(S:E_k)
coherence recovered after local unmeasurement.
```

## Representative result at theta = 1.0

All four cases have the **same initial measurement interaction**, and therefore the same peak values immediately after `U_SD`:

```text
peak system decoherence loss = 0.45970
peak I(S:D)                  = 1.55550 bits.
```

They diverge only after the fate of the record differs:

| Scenario | Sum I(S:E) after copy | Final recovered coherence | Final recovery deficit | Final sum I(S:E) |
|---|---:|---:|---:|---:|
| reversible | 0.000 | **1.000** | 0.000 | 0.000 |
| persistent_1 | 0.778 | 0.292 | **0.708** | 1.170 |
| redundant_3 | 2.333 | 0.292 | **0.708** | 1.656 |
| erased_3 | 2.333 | **1.000** | 0.000 | 0.000 |

The same qualitative ordering holds throughout the tested interaction sweep `theta = 0.4, 0.8, 1.0, 1.2`.

## Interaction-strength sweep

Final recovery deficit after attempting to undo the local measurement:

| theta | reversible | persistent_1 | redundant_3 | erased_3 |
|---:|---:|---:|---:|---:|
| 0.4 | ~0.000 | 0.152 | 0.152 | ~0.000 |
| 0.8 | ~0.000 | 0.515 | 0.515 | ~0.000 |
| 1.0 | 0.000 | 0.708 | 0.708 | 0.000 |
| 1.2 | ~0.000 | 0.869 | 0.869 | ~0.000 |

## Interpretation

### 1. Peak decoherence does not identify a persistent record

For fixed `theta`, all four scenarios have identical peak system decoherence and identical initial system-detector correlation.

Yet the reversible case returns to unit coherence after `U_SD^dagger`, while the persistent-record cases do not.

Therefore

```text
peak decoherence != durable record formation.
```

A transient entangling interaction can temporarily suppress subsystem coherence while remaining fully reversible.

### 2. Environmental record formation blocks local recoherence

Once detector information is transferred to an environment fragment, locally reversing only the `S-D` interaction no longer restores the original system coherence.

At `theta = 1.0`:

```text
reversible final coherence   = 1.000
persistent final coherence   = 0.292.
```

This provides a concrete operational distinction between

```text
correlation that can be locally uncomputed
```

and

```text
correlation whose information has escaped into additional degrees of freedom.
```

### 3. Record erasure matters

The `erased_3` scenario temporarily creates exactly the same large environmental record-information sum as `redundant_3`:

```text
sum I(S:E) after copy = 2.333 bits at theta=1.0.
```

But when the environment-copy operations are reversed before unmeasurement,

```text
final coherence = 1.000
final environmental record information = 0.
```

Thus

```text
transient information acquisition != persistent record.
```

This is direct support for keeping a persistence / irreversibility factor in any operational `Gamma_rec` definition rather than identifying record production with the instantaneous growth of correlation alone.

### 4. Redundancy and decoherence are not the same scalar

Copying the detector record into three environment fragments rather than one raises the sum of fragment-accessible information substantially:

```text
persistent_1 I(S:E) sum after copy = 0.778
redundant_3  I(S:E) sum after copy = 2.333
```

but the final system recovery deficit is the same in this toy model:

```text
0.708.
```

So after the first environment record already prevents full local recoherence, additional redundancy can continue increasing without producing a corresponding increase in this particular decoherence metric.

Therefore

```text
decoherence strength
```

and

```text
environmental record redundancy
```

should be tracked separately.

This is consistent with the literature-informed decision to benchmark later work directly against Quantum Darwinism / Spectrum Broadcast Structure concepts rather than treating ordinary decoherence as synonymous with objectivity.

### 5. The observation model is partly standard open-system physics

Nothing in SIM-04G requires the SoCT field `M`.

The distinctions

```text
interaction
correlation
decoherence
record escape
record erasure
redundancy
```

already arise within ordinary unitary quantum mechanics when different subsystems are tracked explicitly.

This is scientifically important for SoCT: `Omega` or `Gamma_rec` may be useful operational summaries even if they introduce **no new physics at all**.

The burden on SoCT is therefore higher:

> after these standard record/decoherence processes are modeled, does an additional `M` state improve held-out prediction through the predeclared source-decay-diffusion and feedback law?

## Consequence for the source functional

SIM-04F showed that a persistence-aware source can be discriminated from raw interaction/information in a synthetic record model.

SIM-04G now supplies a quantum-mechanical reason to retain that distinction:

```text
same peak decoherence
+ same initial S-D correlation
can lead to
full recoherence
or persistent residual decoherence
according to whether records escaped and remained available.
```

A stronger future `Gamma_rec` should therefore be formulated in terms of **information that becomes robustly distributed / inaccessible to simple local reversal**, not merely positive instantaneous mutual-information growth.

## What SIM-04G does not establish

It does not establish

- objective wavefunction collapse;
- a SoCT memory field;
- a new source of gravity or spacetime curvature;
- consciousness dependence;
- that environmental redundancy is sufficient for phenomenal observation;
- that the present five-qubit model captures realistic macroscopic measurement.

## Next gate

The next high-value integration test is to connect the quantum record diagnostic back to the SoCT memory source without double-counting standard environmental memory.

A suitable next simulation should compare

```text
H0: standard unitary/open-system evolution only
H1: standard evolution summarized by Gamma_rec, but no extra M feedback
H2: standard evolution + Gamma_rec -> M -> predeclared feedback
```

on held-out measurement / erasure / redundancy protocols.

The decisive question is no longer whether records exist. Standard quantum mechanics already provides them in the toy model.

The question is whether adding `M` predicts anything **beyond** the complete open-system state.

## Reproduction

Run

```bash
python experiments/observation-foundations/sim04g_open_system_record_persistence.py
```

Machine-readable output

```bash
python experiments/observation-foundations/sim04g_open_system_record_persistence.py --json
```
