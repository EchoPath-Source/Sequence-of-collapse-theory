# CTI-00 — SPARC Provenance and Specification-Robustness Gate

**Status:** implementation specification / calibration governance  
**Track:** Cross-Track Identifiability (CTI)  
**Role:** required before SPARC is allowed to anchor a frozen cross-track calibration posterior

## 1. Why this gate exists

SPARC is the most mature empirical SoCT branch, but it is not untouched confirmatory data.

The repository already contains multiple SPARC formulations and checks: age/fDM correlations, partial correlations, regression variants, Vmax-based bins, bootstrap summaries, mass-proxy comparisons, inner/outer decompositions, WISE/color formation-history proxies, and a draft preregistration with a different primary rotation-curve formulation.

That history is scientifically useful, but it creates researcher degrees of freedom.

CTI therefore treats SPARC as a **development/calibration track with disclosed analysis history**, not as a pristine preregistered test.

## 2. Existing analysis history that must remain visible

At minimum the calibration record must retain these existing branches/artifacts:

- `experiments/cosmology/sparc-memory-field-preregistration-v0-1.md`
  - proposed primary flatness ratio `F=v_out/v_in`;
  - proposed exponential age-timescale fit;
  - proposed controls and sample cuts;
  - draft preregistered significance rules.
- `data/sparc/sparc_age_fdm_data.csv`
  - current 175-row derived age/fDM table.
- `papers/p1-age-dependent-rotation-curves-sparc/analysis/sparc_age_fdm_analysis.py`
  - current reproducible age/fDM analysis.
- `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_correlations.csv`
- `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_partial_correlations.csv`
- `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_regression_models.csv`
- `papers/p1-age-dependent-rotation-curves-sparc/results/SPARC_age_fdm_binned_bootstrap.csv`
- `papers/p1-age-dependent-rotation-curves-sparc/results/mass_proxy_comparison.csv`
- `observations/sparc/data/sparc_wise_inner_outer_fdm_split.csv`
- `observations/sparc/results/inner_outer_radial_decomposition_summary.md`
- `observations/sparc/results/reproducibility-manifest.md`

The purpose is not to label all variants equally valid. It is to prevent the final calibration specification from being presented without its development history.

## 3. Important provenance discrepancy

The March draft preregistration and the current age/fDM pipeline are not identical analyses.

The preregistration proposed, among other items:

```text
F = v_out / v_in
F(t_age) = F0 + Delta_F [1 - exp(-t_age/tau_decay)]
inclination > 30 deg
distance < 100 Mpc
age correlation plus specified controls
target tau_decay extraction
```

The current reproducible paper script instead centers `fdm_outer_mean` versus `age_best`, with Pearson/Spearman correlations, residual partial correlations, OLS control models, Vmax tertile bins, and bootstrap old-young contrasts.

Therefore CTI must not describe the present `age_best -> fdm_outer_mean` analysis as though it were simply the untouched execution of the earlier preregistration.

This difference must be carried into the calibration manifest as development history.

## 4. Canonical specification cannot be selected by significance

The canonical SPARC calibration pipeline must be chosen on methodological grounds.

Forbidden selection rule:

> choose whichever defensible SPARC specification gives the smallest p-value, largest effect, or best agreement with SoCT.

Acceptable grounds include:

- closest match to a genuinely prior specification;
- strongest measurement provenance;
- least proxy ambiguity;
- best justified control structure;
- highest reproducibility;
- lowest known sensitivity to leverage/outliers;
- physically motivated observable definition;
- independent data-quality criteria.

The rationale must be written before the calibration posterior is promoted to cross-track use.

## 5. CTI-00A — provenance manifest

Create a machine-readable manifest with one row per materially distinct SPARC specification.

Required fields:

```text
spec_id
status [historical/candidate/canonical/sensitivity/rejected]
data_file
data_hash
code_path
code_commit
outcome_variable
primary_predictor
proxy_definition
sample_n
inclusion_rules
exclusion_rules
binning
controls
model_family
resampling
seed
primary_statistic
nuisance_terms
prior_status [predeclared/exploratory/post-hoc]
first_known_date
selection_rationale
notes
```

A specification is materially distinct if it changes the scientific observable, proxy construction, sample, control set, binning, model family, or other choice capable of meaningfully changing the inferred memory calibration.

## 6. CTI-00B — specification-curve robustness

Disclosure alone is insufficient.

For every **defensible** specification, estimate the calibration quantity or the nearest common effect representation that can be compared across specifications.

Let

```math
\hat\theta_M^{(s)}
```

be the inferred calibration quantity under specification `s`.

Where specifications do not estimate the same physical parameter directly, first report a common standardized observable/effect and do **not** pretend unlike parameters are interchangeable.

The specification analysis should report:

- point estimate;
- uncertainty interval;
- sample size;
- sign;
- model/proxy family;
- standardized effect where meaningful;
- whether the result survives the specification's own diagnostics.

## 7. Defensible-specification rule

The specification curve must not be diluted with arbitrary bad analyses.

A variant is included only if its methodological choice can be defended without reference to whether it helps SoCT.

Examples of potentially defensible variation:

- documented alternative age / formation-history proxies;
- pre-existing mass proxies;
- scientifically motivated quality cuts;
- documented control sets;
- reasonable binning alternatives when binning is required;
- unbinned model where appropriate;
- robust regression / leverage treatment specified for statistical reasons;
- bootstrap/resampling variants that preserve the estimand.

Examples that are not automatically defensible:

- searching arbitrary cut points for maximum significance;
- dropping galaxies because they weaken the effect;
- trying many transformations solely to maximize fit;
- target-informed proxy weighting;
- post-hoc combinations chosen for agreement with Pantheon+ or laboratory expectations.

Every included/excluded specification must have a recorded rationale.

## 8. Robustness quantities

Do not reduce robustness to a single p-value.

For a comparable parameter/effect across `K` defensible specifications, report at least:

```math
\text{median}(\hat\theta)
```

```math
\text{range}(\hat\theta)
```

```math
f_{sign}
=
\frac{1}{K}
\sum_s
\mathbf 1[
\operatorname{sign}(\hat\theta_s)
=
\operatorname{sign}(\hat\theta_{canonical})
]
```

and a normalized specification spread such as

```math
S_{spec}
=
\frac{
Q_{0.95}(\hat\theta_s)-Q_{0.05}(\hat\theta_s)
}{
\max(|\operatorname{median}(\hat\theta_s)|,\epsilon)
}.
```

The exact final robustness statistic and any numerical gate must be frozen only after the common estimand and uncertainty model are established.

No arbitrary stability cutoff is declared in this document.

## 9. Interpretation states

CTI-00B must end in one of three states:

### Stable enough to calibrate

Defensible specifications preserve the scientifically relevant direction/magnitude closely enough under the predeclared robustness rule to justify a canonical calibration posterior.

### Specification-sensitive

Reasonable analysis choices materially alter the inferred calibration.

This does not automatically falsify the SPARC association, but SPARC is not yet authorized to act as the sole cross-track parameter anchor.

### Inconclusive

The existing specifications do not estimate a sufficiently common quantity, provenance is incomplete, or uncertainty is too large to assess stability.

Inconclusive does not authorize cross-track calibration.

## 10. Separation of discovery and calibration

The existing SPARC result may remain a candidate empirical result.

CTI asks a different question:

> Is the parameter/effect stable enough across defensible specifications to carry quantitative predictive weight into another physical domain?

A statistically significant association can fail this calibration gate.

Conversely, a stable but weak association may be scientifically informative while lacking enough precision to generate a useful cold prediction.

## 11. Bridge sequencing

After CTI-00/01/02, cross-scale bridge work must proceed in this order:

```text
SPARC / galactic calibration
        |
        v
derive T_G->P
        |
        v
admissible?
   | no ----------------------> STOP G->P quantitative unification claim
   |
  yes
   |
   v
freeze Pantheon+ prediction protocol
        |
        v
cold Pantheon+ test
        |
        v
only then attempt T_G->Q
        |
        v
admissible?
   | no ----------------------> STOP G->Q quantitative unification claim
   |
  yes
   |
   v
prospective laboratory prediction
```

The order is deliberate.

`T_G->P` connects galactic and cosmological/astrophysical regimes and is the nearer bridge. `T_G->Q` spans many more orders of magnitude and must not be treated as equally cheap or automatic.

Failure to derive the nearer admissible bridge is evidence that the current formulation is not ready to claim the harder microscopic bridge.

## 12. Hard exit rule

**No admissible bridge exists** is a completed scientific outcome, not a task left open until a convenient mapping is invented.

If the admissibility criteria fail:

```text
NO ADMISSIBLE BRIDGE
        |
        v
do not unblind target as a SoCT cold prediction
        |
        v
record quantitative-unification claim as unsupported for this bridge
        |
        v
any later bridge = new hypothesis/version
        |
        v
requires new held-out evidence
```

This rule applies independently to `T_G->P` and `T_G->Q`.

## 13. Immediate implementation checklist

- [ ] inventory all existing SPARC specifications;
- [ ] identify which are materially distinct;
- [ ] record historical versus prior/predeclared status;
- [ ] identify a common estimand where scientifically legitimate;
- [ ] build the machine-readable specification manifest;
- [ ] implement a specification-curve runner;
- [ ] produce parameter/effect stability tables and figures;
- [ ] define the justified numerical robustness rule after the estimand/error model exists;
- [ ] freeze the canonical calibration pipeline;
- [ ] only then allow CTI-01/02 outputs to feed cross-track calibration.

## 14. Claim boundary

Use:

> SPARC is the development/calibration track, and its suitability as a cross-track anchor is conditional on provenance and specification robustness.

Avoid:

> SPARC is an untouched preregistered confirmation of the SoCT memory field.

Use:

> Failure to derive an admissible cross-scale bridge blocks the corresponding quantitative unification claim.

Avoid:

> Similar mathematical forms across scales establish a common field.
