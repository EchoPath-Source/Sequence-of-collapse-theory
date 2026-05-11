# Mach-Zehnder Consciousness-Coupled Decoherence Test

**Status:** Protocol scaffold / preregistration target  
**Source basis:** SOC-MZI visibility decay simulation and broader SoCT consciousness-collapse experiment discussions.

---

## Core Question

Does an operationally defined awareness / conscious-access variable explain residual Mach-Zehnder interferometer visibility variance after known physical decoherence channels are controlled?

---

## Minimal Hypothesis

The test begins from the SOC-MZI ansatz:

```text
lambda_eff = lambda_env + lambda_c * A(t)
V(tau, A) = V0 * exp[-lambda_eff * tau]
```

Where `A(t)` is not assumed to be mystical or subjective-only. It must be operationalized using measurable variables.

---

## Hypotheses

### H1a — Main Effect

At fixed delay `tau`, high operational awareness states produce lower visibility than low awareness states, after environmental controls.

```text
V(A_low) > V(A_high)
```

### H1b — Timing Asymmetry

Early awareness pulses produce stronger suppression than late pulses if exposure duration matters.

### H1c — Dose Response

Visibility suppression scales monotonically with `A(t)`.

---

## Operational Definition of A(t)

Required before preregistration:

```text
A(t) = w1 * E(t) + w2 * P(t) + w3 * B(t) + w4 * S(t)
```

Candidate terms:

- `E(t)` — EEG / neural engagement index.
- `P(t)` — physiological phase-locking or coherence measure.
- `B(t)` — behavioral task accuracy / response consistency.
- `S(t)` — normalized subjective attention rating.

Important: weights must be preregistered or learned in a separate training dataset before confirmatory testing.

---

## Required Controls

- thermal drift monitoring;
- phase stability monitoring;
- detector imbalance checks;
- beam splitter symmetry checks;
- randomized trial order;
- blinded condition labels;
- independent analysis scripts;
- environmental logging;
- exclusion criteria for apparatus instability.

---

## Visibility Is a Proxy, Not Proof

Visibility is treated as a first-order observable proxy for coherence modulation under controlled interferometric symmetry assumptions.

It is not treated as direct proof of consciousness-induced collapse.

Biased or asymmetric interferometers can decouple visibility from true quantum coherence. Any experimental implementation must therefore include bias-aware analysis and independent apparatus diagnostics.

---

## Preregistration Requirements

Before any confirmatory run:

1. define the interferometer configuration;
2. specify trial groups;
3. define `A(t)`;
4. define primary and secondary endpoints;
5. set exclusion criteria;
6. define SESOI or minimum effect size of interest;
7. define sample size / power target;
8. publish analysis code hash or locked version;
9. specify all environmental covariates;
10. specify null interpretation.

---

## Falsification Criteria

The hypothesis is weakened if:

- `A(t)` has no relationship to residual visibility after controls;
- visibility shifts are fully explained by apparatus drift or bias;
- effects vanish under blinding;
- high/low awareness conditions differ only after exploratory post-hoc filtering;
- the result fails independent replication.

---

## Next Work

- Convert OSF preregistration excerpts into this protocol.
- Extract source simulation into a notebook.
- Add bias-aware visibility model.
- Add nonmonotonic/noise-lobe model.
- Prepare a prereg-ready statistical analysis plan.
