# SOC-HISTORY-01 — Quantum Platform Comparison

**Status:** Current design memo, September 2026  
**Purpose:** Rank candidate quantum platforms against the actual requirements of the SOC-HISTORY-01 history-memory protocol.

## Required capabilities

The experiment needs more than generic qubit quality. Priority capabilities are:

1. controlled record creation with an ancilla/environment;
2. selective mid-circuit measurement and reset;
3. preservation of a protected data qubit while record-bearing subsystems are measured/reset;
4. high-quality present-state tomography or equivalent diagnostics;
5. repeatable sham preparation with matched control burden;
6. tunable history dose;
7. independent nuisance monitoring;
8. enough coherence time for prepare -> history -> reset/match -> probe;
9. strong control over hardware crossing/randomization;
10. access to low-level pulse/measurement logs.

## Provisional ranking

### 1. Trapped ions — strongest first-platform candidate

**Why it fits:**

- naturally long coherence relative to control times;
- high-fidelity state preparation/readout;
- explicit ancilla/data separation;
- selective shelving/hiding makes it possible to protect data qubits while measuring/resetting record-bearing ions;
- recent systems demonstrate in-situ mid-circuit measurement and reset;
- architecture is unusually well suited to measuring whether a preparation protocol leaves ordinary residual state differences.

**Primary concern:** measurement/reset operations can still disturb neighboring data qubits through scattering, laser noise, motional effects, or magnetic sensitivity, so SOC-HISTORY-01 would require direct calibration of those channels rather than assuming isolation.

**Assessment:** best conceptual match for a first clean test.

### 2. Superconducting qubits — strongest high-throughput candidate

**Why it fits:**

- fast gates, measurement, and reset;
- mature dynamic-circuit and feed-forward tooling;
- recent demonstrations of rapid unconditional reset and flexible readout;
- excellent experimental throughput for randomized crossover and large trial counts;
- pulse-level observables make systematic studies practical in capable labs.

**Primary concern:** shorter coherence and stronger susceptibility to frequency drift, residual photons, crosstalk, heating, and calibration drift directly overlap the confound family exposed by Simulations 4b-4f.

**Assessment:** very attractive, but the nuisance-control burden may be substantially harder than in trapped ions.

### 3. Neutral atoms — promising and improving rapidly

**Why it fits:**

- natural separation of data and ancilla atoms;
- demonstrated mid-circuit measurement, shelving, reset, recooling, and recent high-fidelity repetitive operations;
- spatial structure may permit elegant distributed-record and redundancy variants later.

**Primary concern:** atom motion/loss, recooling, optical scattering, and state-preservation during imaging create additional ordinary-history channels that must be characterized.

**Assessment:** strong second-generation platform, especially for distributed-record tests.

### 4. Photonic systems — conceptually clean record propagation, weaker first choice for history reset/matching

**Why it fits:**

- natural measurement/record carriers;
- excellent for studying information propagation, redundancy, and environment fragments;
- potentially very clean tests of record accessibility and distributed observation.

**Primary concern:** deterministic storage, reversal, and preparation of the *same physical system* after distinct histories is less natural than in matter-qubit platforms. Native memory remains a practical challenge in many photonic architectures.

**Assessment:** excellent for Simulations 2/3b-style record-distribution experiments, less ideal for the first SOC-HISTORY-01 matched-present-state history test.

## Provisional decision

For SOC-HISTORY-01 v1, prioritize:

```text
1. trapped ions
2. superconducting qubits
3. neutral atoms
4. photonic implementation
```

This ranking is protocol-specific, not a claim about which platform is generally superior.

## Why trapped ions currently lead

The key problem is not merely detecting a phase shift. It is constructing two preparations with different record histories and then making the strongest credible claim that their ordinary present states are matched.

Trapped-ion shelving, long coherence, selective measurement/reset, and rich state diagnostics make that particular burden comparatively tractable.

## Required next amendment

Before external preregistration, produce a platform-specific protocol:

```text
SOC-HISTORY-01-TI
```

with:

- ion species / qubit encoding;
- target and ancilla roles;
- target-history pulse sequence;
- sham sequence;
- reset/hiding sequence;
- tomography/state-matching vector;
- motional-state diagnostics;
- photon-scattering and heating monitors;
- probe observable;
- calibration schedule;
- noise estimates and equivalence margins;
- power calculation.

## Claim boundary

Current experimental literature establishes that the needed classes of measurement/reset/protection operations exist on several platforms. It does not establish that SOC-HISTORY-01 will observe a history-dependent residual or that SoCT memory exists.
