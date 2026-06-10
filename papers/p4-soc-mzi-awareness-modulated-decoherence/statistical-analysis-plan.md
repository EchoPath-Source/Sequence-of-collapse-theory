# P4 Appendix — Statistical Analysis Plan

**Canonical track:** P4 — SOC-MZI awareness-modulated decoherence  
**Status:** Repo publication appendix draft  
**Purpose:** Provide a dedicated statistical analysis appendix for the current P4 preregistration draft

---

## 1. Role of this appendix

This appendix isolates the confirmatory and robustness analysis logic for the SOC-MZI protocol.

It is intended to make the P4 experiment easier to review from a methodological perspective and to reduce ambiguity about which tests are confirmatory, which are robustness checks, and which remain exploratory.

This appendix should be read together with:

- `papers/p4-soc-mzi-awareness-modulated-decoherence/SOC-MZI-01-preregistration.md`
- `papers/p4-soc-mzi-awareness-modulated-decoherence/materials-and-measures.md`
- `experiments/quantum/mach-zehnder-consciousness-test.md`

---

## 2. Core statistical claim

The analysis is designed to test whether an operational observer-coherence variable explains residual visibility variation beyond ordinary environment and apparatus effects.

The key scientific distinction is:

- **supported**: evidence for a bounded rate-law effect under preregistered conditions,
- **not supported**: no reproducible separation beyond controlled uncertainty,
- **not allowed**: post hoc reinterpretation of noise as theory support.

---

## 3. Primary confirmatory tests

### Test 1 — Main condition effect

Model form:

```text
V ~ condition + (1|subject) + covariates
```

Directional expectation:

```text
beta_condition > 0
```

Interpretation:

- low-`A` visibility exceeds high-`A` visibility if the model is correct

### Test 2 — Timing asymmetry

Model form:

```text
V ~ condition × timing + (1|subject) + covariates
```

Directional expectation:

```text
beta_interaction > 0
```

Interpretation:

- early windows show stronger effective suppression than late windows

### Test 3 — Continuous dose response

Model form:

```text
V ~ A_continuous + (1|subject) + covariates
```

Directional expectation:

```text
beta_A < 0
```

Interpretation:

- larger measured `A(t)` corresponds to lower residual visibility under the rate-law hypothesis

### Multiplicity control

Current preregistration draft target:

```text
Sidak-corrected alpha = 0.017
```

This should remain the confirmatory threshold unless the preregistration is formally revised.

---

## 4. Covariate handling

Current planned covariates include:

- pupil diameter
- micro-motion / head translation
- temperature drift
- trial position / fatigue terms
- other apparatus-specific quality terms once finalized

Analysis principle:

- covariates are included to reduce trivial artifact explanations,
- not to tune the model until a preferred outcome appears.

If covariate handling changes, the change must be documented and versioned before unblinding where possible.

---

## 5. Random effects and repeated measures

The present design is within-subject and repeated-measures.

Minimum random-effects structure in the current draft:

- random intercept by subject

Potential extensions, if justified by final data density and convergence behavior:

- random slopes for condition,
- random slopes for delay,
- random slopes for timing window.

Any simplification from a richer preplanned structure should be documented explicitly.

---

## 6. Robustness checks

Planned robustness checks include:

1. **Permutation testing**  
   Shuffle condition labels to generate a null distribution for the observed separation.

2. **Bayesian sensitivity analysis**  
   Evaluate whether the result survives skeptical priors on the coupling term.

3. **Adversarial pipeline replication**  
   Independent analyst applies different but pre-allowed artifact handling choices.

4. **Tail robustness**  
   Winsorized or trimmed-tail re-analysis to check whether a small number of extreme trials drive the apparent effect.

These checks are meant to pressure-test the result, not rescue it.

---

## 7. Exploratory analyses

The following remain exploratory unless moved into a revised preregistration:

- EEG band-specific decomposition
- nonlinear fits for `f(A)`
- classifier-based validation of `A(t)`
- cross-delay extrapolation
- subgroup analyses by physiology quality or behavioral performance

Exploratory outputs may be useful for follow-up experiments, but should not be reported as primary support.

---

## 8. Effect-size framing

Current planning assumptions use a visibility difference on the order of:

```text
Delta V ≈ 0.03 ± 0.01
```

These values should be treated as design assumptions informed by the current simulation layer, not as empirical findings.

Recommended reporting:

- estimated effect size,
- confidence interval or compatible interval,
- uncertainty floor,
- and comparison against a practical null threshold.

---

## 9. Null and falsification logic

The analysis should count strongly against the current rate-law hypothesis if the data show:

1. no reproducible separation between high- and low-`A` conditions,
2. no early/late asymmetry,
3. no monotonic `A(t)` relation,
4. reversal or collapse under sham/null-information conditions inconsistent with the model,
5. or repeated cross-lab null outcomes under comparable designs.

Current practical null guide from the protocol draft:

```text
|Delta V| < 0.005
```

This should remain explicitly labeled as a protocol threshold, not a universal law.

---

## 10. Blinding and analysis integrity

Statistical integrity depends on preserving:

- scrambled condition labels for the primary analyst,
- locked analysis scripts prior to unblinding,
- independent or adversarial re-analysis,
- and documentation of any deviations from the preregistered plan.

Best practice:

- hash analysis code before unblinding,
- archive all model versions,
- preserve both successful and null outputs.

---

## 11. Reporting recommendations

A scientist-facing report should include:

- descriptive summaries by condition, delay, and timing window,
- model coefficients with uncertainty,
- sham vs non-sham comparisons,
- robustness-check outputs,
- data-quality and exclusion summaries,
- and a plain-language statement of whether the preregistered signatures appeared.

Recommended wording if supported:

> The observed pattern is consistent with the preregistered rate-law extension under the present operational definition of `A(t)`.

Recommended wording if not supported:

> The present data do not support the preregistered rate-law extension beyond controlled uncertainty.

Avoid stronger wording unless replication exists.

---

## 12. Claim boundary

This appendix specifies how the P4 protocol should be analyzed.

It does not convert simulation assumptions into empirical evidence. Its purpose is to ensure that a positive result would survive skeptical review and that a null result would remain scientifically meaningful.