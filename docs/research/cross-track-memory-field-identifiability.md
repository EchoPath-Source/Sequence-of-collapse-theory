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

## 6. Stronger held-out architecture

The preferred test is not initially a three-domain discovery fit.

### Stage A — derive the bridge

Use theory, dimensions, and simulations to specify which parameters/invariants are transferable.

No observational track may determine its own post-hoc transformation law.

### Stage B — two-track development

Use quantum-methodology constraints plus SPARC to test whether a shared parameterization is mathematically coherent.

This stage may refine the model but is not a confirmatory unification test.

### Stage C — freeze

Freeze:

- source law,
- universal/scaling parameter definitions,
- priors,
- observable maps,
- nuisance treatment,
- success/failure criteria.

### Stage D — held-out Pantheon+ test

After the Pantheon+ pipeline is complete, use the frozen quantum+SPARC-constrained model to predict an allowed Pantheon+ region.

Schematically,

```math
D_Q,D_S
\rightarrow
p(\theta_U,\theta_S|D_Q,D_S)
\rightarrow
p(D_P|D_Q,D_S,H_{SoCT}).
```

Then compare the held-out Pantheon+ result against that posterior predictive distribution.

This is stronger than fitting all three tracks and reporting goodness of fit.

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

### CTI-03 — track likelihood interfaces

Specify the minimal outputs each track must expose to a joint fitter.

### CTI-04 — quantum + SPARC prototype

Build a synthetic/two-track hierarchical fit before Pantheon+ is admitted.

Purpose: expose structural incompatibilities early.

### CTI-05 — Pantheon readiness audit

Complete the raw-input/covariance pipeline and assess whether the environment-H0 dataset has enough power for a held-out prediction.

### CTI-06 — freeze document

Pre-register the bridge, priors, mappings, and failure criteria before revealing/using the held-out Pantheon+ result for cross-track tuning.

### CTI-07 — held-out third-track test

Run the frozen posterior-predictive Pantheon+ test.

### CTI-08 — joint all-track diagnostic

Only after the held-out test, run the full joint fit for parameter estimation and residual diagnosis.

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
quantum + SPARC prototype
   |
   +-- incompatible ----> revise theory before Pantheon
   |
 compatible
   |
   v
freeze cross-track model
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

The immediate next gate is **CTI-01: canonical parameter inventory**, followed by **CTI-02: dimensional bridge**.
