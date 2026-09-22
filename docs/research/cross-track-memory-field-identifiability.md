# Cross-Track Memory-Field Identifiability Program

**Status:** canonical research roadmap / pre-fit specification  
**Claim level:** methodology and falsification architecture; no cross-track unification result is claimed  
**Motivation:** SIM-04I establishes that a hidden conventional reservoir can be structurally degenerate with the proposed SoCT memory state in a single reset-and-probe experiment.

## 1. Central problem

Within one experimental domain, a conventional hidden reservoir can be assigned the same source, decay, diffusion, and probe-coupling law as the proposed memory state `M`. If so, probe data alone cannot identify the ontology.

The program therefore asks a stronger question:

> Can one quantitatively specified memory framework make transferable predictions across independent quantum, galactic, and cosmological datasets with fewer freedoms than separate domain-specific alternatives?

The goal is not to use cross-domain agreement as proof that `M` exists. The goal is to turn the SoCT unification claim into an additional falsifiable constraint.

## 2. Candidate common dynamics

The current observation-sourced memory equation is

```math
\partial_t M
= \alpha_{rec}\Gamma_{rec}
- \beta M
+ D_M\nabla^2 M,
```

with

```math
C_{obs}=\kappa_{rec}\Gamma_{rec},
\qquad
\alpha_{rec}=\alpha\kappa_{rec}.
```

A quantum probe may couple through

```math
H_M=\lambda_M M O_M.
```

A gravity phenomenology may use a mapping such as

```math
G_{eff}=G_0[1+\alpha_G M],
```

while a cosmological track may require a separate observable map from `M` or its gradients/history to the fitted expansion observable.

The source/evolution law and the observable couplings must not be conflated.

## 3. Parameter classes

Before any joint fit, every parameter must be assigned to one of four classes.

### U — candidate universal parameters

Parameters claimed to describe the same physical memory dynamics across domains.

Candidate examples:

```text
beta
D_M
source-law shape / exponents
dimensionless invariants derived from alpha_rec, beta, D_M
```

No parameter is universal merely because the same symbol has been used in multiple papers.

### S — scale-transformed parameters

Quantities related across domains by a derived dimensional or renormalization/scaling relation.

Example structure:

```math
\Pi_M =
f(\alpha_{rec},\beta,D_M,L,T,...)
```

where `\Pi_M` is dimensionless and is the actual universal quantity.

### C — domain coupling parameters

Parameters describing how a common `M` state couples to a domain-specific observable.

Examples:

```text
lambda_M     quantum probe coupling
alpha_G      gravitational response coupling
g_H          cosmological observable coupling
```

These need not be numerically equal.

### N — nuisance / apparatus parameters

Detector efficiency, stellar mass-to-light nuisance terms, supernova calibration quantities, environment-label uncertainty, reset fidelity, and other domain-specific terms.

These must not be silently promoted into SoCT degrees of freedom.

## 4. Parameter ledger requirement

Create a machine-readable ledger before joint fitting with columns:

```text
parameter
symbol
units
class [U/S/C/N]
domain
definition
prior/range
source file
transformation law
currently constrained?
identifiability notes
```

The ledger must expose when two tracks use the same symbol for physically different quantities.

## 5. Joint likelihood architecture

Let the common SoCT parameter block be `theta_U`, scale-law parameters be `theta_S`, domain couplings be `theta_C^d`, and nuisance parameters be `eta_d`.

A future simultaneous fit can be written

```math
\mathcal L_{joint}
=
\mathcal L_Q(D_Q|\theta_U,\theta_S,\theta_C^Q,\eta_Q)
\,
\mathcal L_S(D_S|\theta_U,\theta_S,\theta_C^S,\eta_S)
\,
\mathcal L_P(D_P|\theta_U,\theta_S,\theta_C^P,\eta_P).
```

Here:

- `Q` = quantum reset/probe or future laboratory data,
- `S` = SPARC / galaxy track,
- `P` = Pantheon+ / cosmology track.

The scientific value comes from **shared constrained structure**, not merely multiplying likelihoods.

If every domain receives an independent copy of all memory parameters, the exercise does not test unification.



## 5A. Pre-fit admissibility rule for cross-track bridges

The phrase **physically justified** is not permitted to be assigned retrospectively after inspecting cross-track fits.

Before a target track is examined, every proposed universal parameter, invariant, or scale transformation must be registered with an explicit derivational basis.

An admissible bridge must satisfy at least one predeclared category:

1. **Dimensional necessity** — the combination follows from units and the assumed governing variables, with no data-selected exponents or coefficients.
2. **Common dynamical derivation** — the relation follows from the same underlying equation, action, Hamiltonian, field equation, or other specified dynamical structure used across the tracks.
3. **Symmetry / conservation constraint** — the relation follows from a stated symmetry, invariance, conservation law, or covariance requirement.
4. **Predeclared scale transformation** — the scale dependence is derived or specified before examining the target track and contains a fixed, auditable parameter count.
5. **Independent prior derivation** — the relation was derived from independent theory or data not subsequently used as the target test.

The following do **not** qualify:

- numerical similarity discovered after fitting;
- choosing a convenient dimensionless combination after inspecting target results;
- adding exponents or scale factors because they align the tracks;
- relabeling unrelated fitted quantities with the same symbol;
- selecting among many candidate transformations based on which one best matches the held-out track.

Each bridge must therefore carry a provenance record:

```text
bridge_id
mathematical_form
derivation_category
derivation_source
free_parameters
units / dimensionless status
calibration data allowed
target data forbidden before freeze
date frozen
revision identifier
```

If a bridge is changed after target-data inspection, the modified bridge is a **new hypothesis** and requires new held-out evidence.

## 5B. Primary unification test: predict, do not jointly fit

The principal empirical unification test is **not** a simultaneous three-track fit.

The primary protocol is:

```text
derive bridge
-> fit calibration track
-> freeze universal/scaling block
-> predict independent tracks
-> score predictions without refitting shared parameters
```

For the current program, SPARC is the preferred calibration track because it is the most mature empirical branch.

Let the admissible shared/scaling parameter block be

```math
\theta_M=(\theta_U,\theta_S).
```

Calibration gives

```math
p(\theta_M|D_S).
```

The frozen model then generates posterior-predictive distributions

```math
p(D_P|D_S,H_{SoCT})
=
\int
p(D_P|\theta_M,\eta_P,H_{SoCT})
p(\theta_M|D_S)
p(\eta_P)
\,d\theta_M\,d\eta_P
```

and, when real laboratory data exist,

```math
p(D_Q|D_S,H_{SoCT})
=
\int
p(D_Q|\theta_M,\eta_Q,H_{SoCT})
p(\theta_M|D_S)
p(\eta_Q)
\,d\theta_M\,d\eta_Q.
```

Domain nuisance parameters may be marginalized only when their definitions and priors were specified independently of the target residual.

They may not alter the frozen universal/scaling memory dynamics.

A failed cold prediction cannot be converted into a successful unification result by subsequently allowing `\theta_M` to float.

A post-failure refit may motivate a revised model, but that model begins a new hypothesis cycle.

## 5C. Role of the eventual joint fit

The all-track joint likelihood remains useful, but it is **secondary**.

After the cold tests it may be used for:

- parameter estimation;
- residual diagnosis;
- tension localization;
- sensitivity analysis;
- comparison with separate-domain models;
- designing the next experiment.

It must not replace or overwrite the result of the frozen out-of-sample test.

A model that fails the cold prediction but fits after joint retuning has demonstrated flexibility, not the originally claimed cross-track prediction.

## 5D. Small-N protection

With only a small number of substantially independent physical tracks, apparent agreement among best-fit parameters is vulnerable to coincidence and researcher degrees of freedom.

Therefore:

- cross-track success is not defined by overlap of three fitted confidence regions alone;
- the number of candidate bridges considered must be recorded;
- target-track results must not be used to select the bridge;
- at least one empirical track must remain untouched after the final bridge freeze;
- whenever possible, leave-one-domain-out posterior prediction should be reported;
- a later independent laboratory experiment is especially valuable because current SIM-04H/I results are synthetic methodology tests.

This structure is intended to prevent a small number of flexible tracks from manufacturing apparent unification.


## 5E. SPARC provenance and calibration freeze gate

SPARC is the preferred development/calibration track because it is currently the most mature empirical branch, **not because it is an untouched preregistered dataset**.

Prior SPARC development has already consumed researcher degrees of freedom through choices and checks involving mass/age proxies, binning, resampling, robustness analyses, and related pipeline decisions. Those choices must be disclosed rather than erased by relabeling SPARC as a calibration dataset.

Before CTI extracts the cross-track calibration posterior, create a frozen SPARC calibration manifest containing at minimum:

```text
dataset/version
sample inclusion/exclusion rules
distance/inclination quality rules
stellar mass-to-light assumptions
age / formation-history proxy set
primary proxy designated for calibration
bin definitions, if used
regression / likelihood form
covariates and control variables
bootstrap/resampling procedure
robustness variants already explored
multiple-testing / model-selection history
nuisance parameters and priors
canonical output statistic
code commit / data hashes
known prior exploratory decisions
freeze date
```

The manifest must distinguish historically explored choices, canonical calibration choices, and sensitivity-only analyses that cannot replace the canonical result after freeze.

If the canonical calibration fails, a robustness variant may diagnose why, but it cannot silently become the new calibration analysis. Promoting a different variant starts a new hypothesis/version cycle.

## 5F. Decision-rule freeze gate

A cold prediction must have a numerical decision rule before the target result is inspected.

For each held-out track, freeze the likelihood/error model, target observables, approved nuisance parameters and priors, test/model-comparison statistic, numerical compatibility/rejection criterion, expected power or sensitivity, quality-control rules, systematic treatment, and definition of an inconclusive result.

The protocol does **not** choose arbitrary universal cutoffs before a justified statistical model exists. The numerical rule and its justification must instead be frozen after the track's likelihood/error/power model is established but before the held-out target result is revealed to the cross-track analysis.

Possible frameworks include posterior-predictive criteria, calibrated chi-square or likelihood-ratio tests, Bayes-factor thresholds with justified priors, frequentist confidence criteria with calibrated coverage, or equivalence regions where scientifically appropriate.

The rule should be simulation-calibrated when feasible. Three outcomes must remain available:

```text
compatible
incompatible
inconclusive / underpowered
```

**Inconclusive does not count as successful prediction.**

A result that misses a frozen criterion cannot be reclassified as success because it is close. It may motivate a revised hypothesis requiring new held-out evidence.

### Nuisance-parameter firewall

Every target track must have a pre-approved nuisance ledger.

A quantity qualifies as nuisance only if it represents a known measurement, calibration, selection, foreground/background, or domain-specific systematic with an independently motivated role in the standard analysis.

A nuisance parameter must not alter the frozen universal/scaling memory law, implement a new cross-scale transformation, absorb arbitrary target residual structure, acquire a flexible functional form only after target inspection, or act as a disguised domain-specific copy of a supposedly universal SoCT parameter.

If acceptable target fit requires a new flexible nuisance term after unblinding, the original frozen prediction has failed or become inconclusive; the modified model is a new hypothesis.

## 5G. Cross-scale bridge gate

A shared symbol `M` does not establish that galactic, cosmological, and microscopic memory variables are quantitatively interchangeable.

Before SPARC-derived parameters can predict another scale, CTI must derive an admissible transformation.

For the laboratory branch:

```math
\mathcal T_{G\to Q}:
(\theta_M,L_G,T_G,\mathcal B_G)
\mapsto
(\theta_M^Q,L_Q,T_Q,\mathcal B_Q).
```

For cosmology:

```math
\mathcal T_{G\to P}:
(\theta_M,L_G,T_G,\mathcal B_G)
\mapsto
(\theta_M^P,L_P,T_P,\mathcal B_P).
```

Here `\mathcal B` denotes relevant physical background/boundary conditions rather than an extra unconstrained fitting function.

Each transformation is itself a cross-track bridge and must independently satisfy Section 5A.

If no admissible `\mathcal T_{G\to Q}` exists, SPARC is **not entitled to make a quantitative laboratory prediction**. If no admissible `\mathcal T_{G\to P}` exists, SPARC is **not entitled to make a quantitative Pantheon+ prediction**.

That outcome is scientifically informative: the framework has not yet earned quantitative cross-scale unification.

A transformation introduced after examining the target is a new hypothesis and cannot be tested on that same target as if it were held out.

## 5H. Revised pre-unblinding chain

```text
common theory
-> admissible bridge derivation
-> SPARC provenance audit
-> canonical SPARC pipeline freeze
-> SPARC calibration posterior
-> admissible cross-scale transformation
-> target nuisance ledger
-> target likelihood / power model
-> numerical decision-rule freeze
-> target unblinding / cold prediction score
-> only afterward: diagnosis or joint refit
```

Every arrow must be auditable by version/commit.


## 6. Stronger held-out architecture

The preferred test is not initially a three-domain discovery fit.

### Stage A — derive the bridge

Use theory, dimensions, and simulations to specify which parameters/invariants are transferable.

No observational track may determine its own post-hoc transformation law.

### Stage B — SPARC calibration and synthetic-methodology validation

Use SPARC as the initial empirical calibration track for the admissible shared/scaling block.

SIM-04H/I remain methodology and identifiability benchmarks. Because they are synthetic, they are not counted as independent empirical evidence for nature's value of the shared parameters.

### Stage C — freeze

Before examining the held-out target result, freeze:

- source law;
- admissible universal/scaling parameter definitions;
- the derivation/provenance of every cross-track bridge;
- priors;
- observable maps;
- nuisance treatment;
- success/failure criteria;
- the list of bridge variants considered.

### Stage D — held-out Pantheon+ test

After the Pantheon+ pipeline is complete, use the frozen SPARC-calibrated model to predict an allowed Pantheon+ region.

Schematically,

```math
D_S
\rightarrow
p(\theta_U,\theta_S|D_S)
\rightarrow
p(D_P|D_S,H_{SoCT}).
```

Then compare the held-out Pantheon+ result against that posterior predictive distribution without refitting the shared/scaling block.

### Stage E — prospective laboratory prediction

Use the frozen model to state the quantitative laboratory signature and required sensitivity before a real experiment is analyzed.

When independent laboratory data become available,

```math
D_S
\rightarrow
p(\theta_U,\theta_S|D_S)
\rightarrow
p(D_Q|D_S,H_{SoCT}).
```

The real laboratory result then becomes a second cold empirical test.

### Stage F — post-test joint fit

Only after the cold tests may all tracks be jointly fit for parameter estimation and diagnosis.

The joint fit cannot retroactively turn a failed frozen prediction into a successful unification test.

## 7. Pantheon+ gate

The Pantheon+ environment-H0 branch is not yet ready to serve as the held-out third track.

Before Stage D:

1. required raw SN inputs must be staged with provenance;
2. covariance handling must pass validation;
3. environment labels must pass row/order/provenance checks;
4. predeclared redshift and grouping rules must be frozen;
5. the baseline environment-H0 analysis must run successfully;
6. statistical power must be assessed;
7. no SoCT cross-track tuning may use the held-out result before the freeze.

If Pantheon+ is underpowered for the proposed discriminator, that fact must be reported rather than compensated for by relaxing the model.

## 8. Competing models

At minimum compare:

### H_sep — separate-domain phenomenology

Each domain receives independent effective memory-like parameters.

This may fit well but makes no strong unification claim.

### H_shared — shared SoCT dynamics

One universal/scaling parameter block is shared across domains, with only justified domain couplings and nuisance terms.

### H_null — domain-standard models

Each domain uses its appropriate conventional model without a shared SoCT memory state.

### H_res,Q — quantum hidden-reservoir model

The quantum experiment includes a conventional hidden reservoir. It may mimic `M` locally but receives no automatic access to galaxy/cosmology parameter constraints.

The relevant question is not whether `H_shared` can fit. It is whether its cross-domain constraints produce predictive value relative to these alternatives.

## 9. Degeneracy-breaking logic

A local hidden reservoir remains a viable explanation of a quantum residual whenever it can reproduce the laboratory observables.

Cross-track consistency adds a different requirement:

```text
local quantum residual
+ galaxy-scale memory phenomenology
+ cosmological environment signature
-> one predeclared shared/scaled parameter structure
```

A laboratory reservoir has no generic reason to satisfy constraints derived independently from galaxies and supernova cosmology.

However, cross-track agreement still would not logically prove that the underlying ontology is a fundamental field `M`. A sufficiently flexible deeper conventional theory could reproduce the same shared law.

Therefore cross-track consistency is an **identifiability gain and unification test**, not an ontology proof.

## 10. Unification falsification criterion

The empirical SoCT unification claim is weakened or rejected if no physically justified shared parameter, invariant combination, or scaling law can describe independent tracks without introducing enough domain-specific freedom to remove cross-track predictive constraint.

Operational warning signs include:

- each track requires unrelated values of a supposedly universal parameter;
- scale transformations are introduced only after seeing the target data;
- every mismatch is absorbed by a new domain coupling;
- the joint model has no stronger held-out predictions than independent fits;
- common parameters are practically unconstrained after marginalizing nuisances;
- apparent agreement depends on incompatible units or definitions of `M`;
- removing one track does not narrow predictions for any other track.

If this occurs, `collapse leaves memory` may remain an organizing hypothesis, but the stronger empirical unification claim has failed.

## 11. Positive criterion

A meaningful cross-track result requires more than overlapping best-fit points.

At minimum:

1. the shared/scaling law is specified before the held-out test;
2. at least one parameter or invariant is genuinely constrained by more than one independent track;
3. conditioning on one track measurably narrows predictions for another;
4. the held-out track lands within the predeclared predictive region;
5. the shared model competes successfully after complexity penalties;
6. posterior predictive checks show no systematic domain failure;
7. alternative conventional explanations are compared rather than omitted.

## 12. Metrics

Candidate diagnostics include:

```text
posterior predictive coverage
Bayes factors where priors are defensible
WAIC / LOO-CV
BIC/AIC for controlled benchmark comparisons
parameter tension metrics
KL information gain across tracks
leave-one-domain-out prediction
prior-to-posterior contraction
shared-vs-separate parameter model comparison
```

No single metric should be treated as a discovery criterion.

## 13. Cross-track information gain

A useful operational measure is whether one domain teaches us something testable about another.

For example,

```math
IG_{S\to P}
=
D_{KL}
[
p(\theta_U|D_S)
\,||\,
p(\theta_U)
].
```

More directly, compare the Pantheon predictive width before and after conditioning on SPARC/quantum information:

```math
R_{pred}
=
\frac{
Width[p(D_P|H)]
}{
Width[p(D_P|D_Q,D_S,H)]
}.
```

If `R_pred\approx1`, the supposedly shared model may have little practical cross-track constraint.

## 14. Relationship to SIM-04I

SIM-04I should be treated as the motivation for this program.

It established in synthetic benchmarks that:

- a conventional hidden reservoir can mimic the complete probe signature;
- probe precision alone cannot break an exact structural degeneracy;
- independent diagnostics help only when they actually couple to the hidden reservoir;
- ontology cannot be inferred from an observationally identical phenomenological state.

The cross-track program asks whether SoCT can make additional commitments that the local mimic does not inherit for free.

## 15. Relationship to RCOF / consciousness

Recursive Coupling & Observer Formation is not part of the initial joint fit.

The first cross-track identifiability program should use:

```text
quantum record / memory discriminator
SPARC
Pantheon+
```

without requiring a consciousness variable.

RCOF may later consume the operational record framework, but a failure of observer-emergence or conscious-access hypotheses must not invalidate an otherwise successful lower-level memory test.

## 16. Immediate work packages

### CTI-00 — SPARC provenance audit

Before treating SPARC as calibration data, inventory the analysis choices already explored and produce the canonical calibration manifest required by Section 5E.

### CTI-01 — canonical parameter inventory

Audit all uses of:

```text
M
alpha
alpha_rec
beta
D_M
kappa_rec
lambda_M
alpha_G
C_obs
Gamma_rec
```

and classify each as U/S/C/N.

### CTI-02 — dimensional bridge

Derive units and candidate dimensionless groups. Determine whether `beta` and `D_M` can meaningfully be universal across laboratory, galactic, and cosmological scales or require a scale law.

### CTI-02B — cross-scale transformation derivation

Derive or reject admissible `T_G->Q` and `T_G->P` mappings before either target is used for cross-track validation. A missing bridge blocks the corresponding quantitative prediction.

### CTI-03 — track likelihood interfaces

Specify the minimal outputs each track must expose to prediction and later joint fitting. Include nuisance ledgers, likelihood/error models, and the information needed to calibrate a numerical decision rule.

### CTI-04 — SPARC calibration + cross-track prediction prototype

Use SPARC to calibrate the admissible shared/scaling block and use the synthetic quantum benchmarks to validate the prediction machinery and expose structural incompatibilities. Do not count synthetic recovery as empirical cross-track confirmation.

### CTI-05 — Pantheon readiness audit

Complete the raw-input/covariance pipeline and assess whether the environment-H0 dataset has enough power for a held-out prediction.

### CTI-05B — target decision-rule calibration

Using target-track methodology without revealing the held-out result to the cross-track analysis, establish the likelihood/error model, power/sensitivity, nuisance firewall, and justified numerical compatible/incompatible/inconclusive rule.

### CTI-06 — freeze document

Pre-register each bridge's admissibility basis, the full candidate-bridge list, priors, mappings, nuisance treatment, and failure criteria before revealing/using the held-out Pantheon+ result for cross-track tuning.

### CTI-07 — held-out third-track test

Run the frozen SPARC-derived posterior-predictive Pantheon+ test without refitting the universal/scaling block.

### CTI-08 — prospective laboratory prediction and post-test joint diagnostic

State the laboratory prediction before real probe data are analyzed. After the cold Pantheon+ and eventual laboratory tests, run the full joint fit only for parameter estimation, residual diagnosis, and next-generation model development.

## 17. Decision tree

```text
SIM-04I local degeneracy
        |
        v
CTI-01 parameter audit
        |
        v
Can a physically justified shared/scaled parameter block be defined?
   | no ----------------> unification claim reduced/rejected
   |
  yes
   |
   v
SPARC calibration + prediction prototype
   |
   +-- incompatible ----> revise theory before Pantheon
   |
 compatible
   |
   v
freeze admissible bridge + cross-track model
   |
   v
held-out Pantheon+ prediction
   |
   +-- fails -----------> shared unification model falsified/constrained
   |
 survives
   |
   v
full joint fit + stronger conventional alternatives
   |
   v
laboratory design / external validation
```

## 18. Claim language

Use:

> SoCT is testing whether a common memory-dynamics structure can make transferable predictions across independent physical domains.

Use:

> Cross-track consistency would strengthen identifiability relative to a domain-local hidden reservoir.

Avoid:

> Agreement across tracks proves a new fundamental field.

Avoid:

> A quantum residual confirms the galaxy/cosmology model.

## 19. Current status

```text
SIM-04I structural degeneracy: identified
cross-track parameter ledger: not yet completed
dimensional bridge: not yet derived
quantum+SPARC hierarchical prototype: not yet built
Pantheon+ baseline result: not yet complete
held-out three-track test: not yet run
empirical unification: not established
```

The immediate next gates are **CTI-00: SPARC provenance audit**, **CTI-01: canonical parameter inventory**, and **CTI-02: dimensional bridge**. No cold cross-track prediction is authorized until the relevant cross-scale bridge and decision rule are frozen.
