# CNN-O1 Stage 2 — Record-Conditioned Write Hypothesis (v0.1)

**Status:** Research specification / implementation handoff. Not a completed preregistration, validated result, or claim about physical memory fields.

**Canonical home:** Sequence-of-collapse-theory (SoCT), under the observation-foundations and SoCT-memory discriminator program.

**Runtime implementation:** https://github.com/EchoPath-Source/EchoPath-Memory-Layer-/pull/77 (PR #77; draft; tests have not yet been run).

## 1. Purpose and scope

CNN-O1 Stage 2 examines a narrow software-level question: can a configurable record-conditioned write gate change the memory update produced by a simulated event while preserving the event/firing decision itself?

This is an implementation and model-discrimination question. A positive software test would establish only that the configured gate behaves as specified in the simulation. It would not establish that a new physical memory field exists, that observation causes objective collapse, or that the implementation is a faithful physical model of Gamma_rec.

## 2. Research context

SoCT's broader candidate bridge is

\`\`\`math
C_{obs}(x,t)=\kappa_{rec}\Gamma_{rec}(x,t),
\qquad
\partial_t M=\alpha_{rec}\Gamma_{rec}-\beta M+D_M\nabla^2M.
\`\`\`

Here, Gamma_rec is a proposed persistence-aware record-production rate. It remains a versioned research hypothesis, not established physics. CNN-O1 Stage 2 is **not** a derivation or empirical validation of this bridge. It is a bounded computational probe of one record-conditioned update mechanism.

## 3. Software-level hypothesis

Let p_i be the pre-reset potential for node i, theta_i its effective firing threshold, s_i the configured normalization scale, and f in [0,1] the configured observation-record floor. For a node that fires, define the suprathreshold margin

\`\`\`math
q_i=\operatorname{clip}\left(\frac{p_i-\theta_i}{s_i},0,1\right),
\qquad
g_i=f+(1-f)q_i.
\`\`\`

The Stage 2 gated update is

\`\`\`math
\Delta m_i = w_M g_i,
\`\`\`

where w_M is the configured memory-write magnitude. This form is intended to make the gate vary with suprathreshold margin, rather than saturating merely because a node crossed threshold. The implementation must use the same pre-reset potential that determines the firing event.

### Auto-stimulation events

Auto-stimulation is exogenous to the threshold-crossing event path, so it must not bypass the option. In the current implementation proposal, the configured event weight is used as an explicit bounded strength proxy:

\`\`\`math
q_{auto}=\operatorname{clip}(|w_{event}|,0,1),
\qquad
g_{auto}=f+(1-f)q_{auto}.
\`\`\`

This is a pragmatic software proxy, **not** a validated estimate of Gamma_rec. It should remain separately identifiable in logs/tests and should not be described as a physical record-production law.

## 4. Required comparisons

The minimum computational comparison is:

- **Control:** record-conditioned write disabled; baseline dynamics and write behavior unchanged.
- **Treatment:** record-conditioned write enabled with an explicitly configured floor.
- **Matched event check:** for matched inputs/configuration, the event/firing decision should remain unchanged where the gate is specified to affect only the write magnitude.
- **Strict gate-effect check:** at least one fired node must show a strictly larger memory update in the higher-gate condition; a non-strict inequality alone is insufficient to demonstrate a gate effect.
- **Auto-stimulation check:** when auto-stimulation is enabled, verify that the option gates those writes too, with expected results for floor and event-weight boundary cases.
- **Disabled-path regression:** disabling the option must preserve legacy behavior.
- **Integration regressions:** Stage 1 equivalence and the V9/V10/V11 regression suite must pass before the change is treated as validated.

Tests are currently recorded in the runtime repository, but their execution status is **not run / not yet verified**. Do not report a pass until CI or an equivalent reproducible local run supplies results.

## 5. Interpretation and falsification boundaries

A failed implementation test falsifies the relevant software behavior as implemented; it does not by itself falsify SoCT. A passing implementation test shows conformance to this specified computational rule; it does not support the existence of physical M or distinguish it from ordinary hidden-state mechanisms.

The broader SoCT discriminator remains:

> Matched, explicitly accounted ordinary present state + different prior durable-record histories + fresh probe → reproducible history-dependent residual.

The repository's prior simulation work highlights that an unobserved conventional reservoir can mimic an added-memory-state signal. Any future physical claim therefore requires independent reset/environment diagnostics and a comparison against ordinary hidden-state alternatives of equal or lower complexity.

## 6. Preregistration and provenance

Before treating CNN-O1 Stage 2 as a scientific test rather than a software test, record the following in a versioned preregistration or dated analysis plan:

1. Exact model version, equations, parameter values, seed policy, and event/write semantics.
2. Primary outcome and effect-size definition.
3. Null and alternative models, including ordinary hidden-reservoir alternatives.
4. Exclusion, reset-verification, and missing-run rules.
5. Planned sample size / simulation count, uncertainty method, and stopping rule.
6. Code commit, environment, dependency versions, test command, logs, and machine-readable outputs.
7. Clear separation between confirmatory tests and exploratory parameter sweeps.

No OSF registration identifier or completed preregistration is asserted by this document. If a formal OSF record is used, link its persistent identifier here only after verifying it.

## 7. Repository boundary

- **Sequence-of-collapse-theory:** owns the hypothesis, versioned equations, preregistration linkage, analysis plan, results, limitations, and scientific interpretation.
- **EchoPath-Memory-Layer:** owns the runtime implementation, unit/integration tests, API/configuration behavior, and software release notes.

The runtime implementation must link back to this SoCT record. Product or public-facing copy must not present this experimental construct as validated physics.

## Change log

- **v0.1:** Initial canonical research specification and implementation boundary. Captures the record-conditioned write gate and the separate auto-stimulation proxy; validation remains pending.
