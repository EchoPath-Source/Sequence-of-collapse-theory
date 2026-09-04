# Observation Simulation 2 — Qubit + Pointer + Environment

**Status:** Baseline benchmark  
**Novel-physics content:** None  
**Purpose:** Test whether the operational observation metrics can distinguish explicit record formation from ordinary environmental decoherence and redundant environmental records.

## Model

The system qubit begins in

```math
|+\rangle_S = (|0\rangle + |1\rangle)/\sqrt{2}.
```

A pointer `P` and four environment fragments `E_k` begin in `|0>`.

Conditioned on the system being in `|1>`, the pointer and environment fragments rotate to

```math
|p(\theta)\rangle = \cos\theta |0\rangle + \sin\theta |1\rangle
```

and

```math
|e(\phi)\rangle = \cos\phi |0\rangle + \sin\phi |1\rangle.
```

The resulting pure state is

```math
|\Psi\rangle = \frac{1}{\sqrt{2}}
\left[
|0\rangle|0\rangle_P|0\cdots0\rangle_E
+
|1\rangle|p(\theta)\rangle_P\prod_k|e(\phi)\rangle_{E_k}
\right].
```

`theta` therefore controls explicit pointer-record strength while `phi` independently controls environmental recording/decoherence.

## Metrics

The sweep records:

- reduced system coherence;
- pointer trace distance;
- pointer Holevo-accessible information;
- pointer/system quantum mutual information;
- exploratory pointer observation proxy `Omega_pointer`;
- single-environment-fragment trace distance and Holevo information;
- system/environment-fragment mutual information;
- a simple redundancy count for fragments carrying at least 0.5 bits of accessible record information.

The exploratory pointer proxy is

```math
\Omega_P = D_P \chi_P.
```

This is not a final SoCT law. It is a diagnostic designed to test whether an observation metric can remain zero when a designated pointer stores no record even while the environment decoheres the system.

## Key benchmark cases

### A. No record anywhere

```text
theta = 0
phi   = 0
```

Expected:

```text
system coherence = 1
pointer record = 0
environment record = 0
Omega_pointer = 0
```

### B. Environmental decoherence without pointer record

```text
theta = 0
phi > 0
```

Expected:

- system coherence falls as environment fragments acquire state information;
- pointer trace distance and pointer Holevo information remain zero;
- `Omega_pointer` remains zero.

This is the decisive conceptual benchmark: **decoherence can increase while the designated pointer observation metric remains zero.** Therefore a record-specific observation metric need not be merely another name for total decoherence strength.

### C. Pointer record without redundant environment

```text
theta > 0
phi = 0
```

Expected:

- pointer record measures become nonzero;
- `Omega_pointer > 0`;
- there are no redundant environment records.

### D. Pointer plus redundant environment records

```text
theta > 0
phi > 0
```

Expected:

- explicit pointer record exists;
- system coherence is further suppressed by environmental records;
- multiple environment fragments can independently carry accessible information about the system.

## Analytic coherence check

The off-diagonal system coherence should obey

```math
C_S = |\cos\theta|\,|\cos\phi|^{N_E}.
```

The numerical reduced-density-matrix calculation should reproduce this relation.

## Interpretation boundary

This simulation tests only standard quantum correlations and open-system-style record proliferation in a finite unitary toy model.

It does **not** show:

- objective collapse;
- a SoCT memory field;
- consciousness effects;
- gravity emerging from information;
- a departure from standard quantum mechanics.

A positive result here means only that the proposed observation variables are operationally distinguishable from a single aggregate decoherence measure in this controlled model.

## Next gate

Simulation 3 should create and then erase/render inaccessible a record to determine whether the candidate SoCT source should track:

```text
temporary correlation,
durable record formation,
irreversible record production,
or downstream accessibility.
```

That distinction is necessary before identifying any record-production quantity with the SoCT memory source `C_obs(x,t)`.