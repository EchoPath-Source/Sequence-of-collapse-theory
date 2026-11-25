# P6 continuous-density prediction and null-model contract

2026-11-25. PR39 merged at 043035143be295195d1a6149b901c7b21e6ff725. Theory-only audit; no observational distance outcomes or H0 fits. Original P6 remains unchanged. Reviewed PREDICTIONS.md, this folder's void-filament-h0-mechanism.md, visualizations/pnt_hubble_void.jsx, papers/p5-hubble-tension-memory-gradient/README.md, docs/dark-sector-taxonomy.md and papers/math/pnt-soct-covariance-conservation-and-timescale-audit.md. Canonical toy parameters retained without fitting.

## Recoverable prediction

Let s=.15, n=1.5, H*=67.4 km/s/Mpc, Om=.315, Ode=.685, A=Ode*s/(1-s)=.12088235294. Within the stated domain -.9<=delta<=.5, clipping of the failed fraction is inactive.

    f_fail(delta)=1-s*(1+delta)^n
    q(delta)=f_fail(delta)/(1-s)
    Htoy(delta)=H*sqrt(1+A*(1-(1+delta)^n))
    dHtoy/ddelta=-H* A*n*(1+delta)^(n-1)/(2*sqrt(1+A*(1-(1+delta)^n)))

Negative derivative throughout domain; derivative at zero -6.110603 km/s/Mpc per unit delta. This is the existing toy expansion estimate, not an additional theory parameter or a derivation from Einstein equations. Matter term held fixed in original formula. Htoy(0)=H*. Normalization at delta=0 is not a volume-averaged exhaust normalization; nonlinear averaging would require a specified density distribution. No time dependence, smoothing scale or propagation rule is supplied. Do not add a matter density term, choose a saturation function, or sum a GR flow term with Htoy and call it the original model.

| delta | q | Htoy | Htoy-H* | conditional mu shift | linear GR local expansion shift |
|---:|---:|---:|---:|---:|---:|
| -.8 | 1.160687 | 71.012555 | 3.612555 | -.113376 | 9.521370 |
| -.35 | 1.083992 | 69.311794 | 1.911794 | -.060736 | 4.165599 |
| -.2 | 1.050199 | 68.549014 | 1.149014 | -.036707 | 2.380342 |
| 0 | 1 | 67.4 | 0 | 0 | 0 |
| .2 | .944494 | 66.106254 | -1.293746 | .042087 | -2.380342 |
| .3 | .914901 | 65.406036 | -1.993964 | .065210 | -3.570514 |
| .5 | .852273 | 63.898872 | -3.501128 | .115834 | -5.950856 |

GR values at large |delta| merely extrapolate the linear reference, not validated nonlinear void calculations. The fiducial -.35 reproduces 34.139% of the assumed 5.6 km/s/Mpc difference *arithmetically*, not evidence that the local matter contrast is -.35 or that PNT explains a measured share of the tension. Within entire domain q spans .852273–1.170890 (ratio 1.374), not 2–4x as stated in visualization prose; -.8 versus .3 ratio ~1.269. Flag legacy visualization statement for correction; unchanged in this PR. The visualization's illustrative total mechanism range is not a joint fit.

## Conditional distance template and bridge to observed predictor

If, and only if, distances at fixed redshift rescale inversely with Htoy, g(delta)=-5 log10(Htoy(delta)/H*). dg/ddelta at zero=+.196870 mag per unit delta. Example fixed matter contrasts -.2 versus +.2: H(low)-H(high)=2.442759, g(high)-g(low)=.0787933 mag. Not a light-cone derivation and not a measured result. A local environment at a remote source cannot simply be substituted for the expansion rate along the observer-source path. Need metric/velocity/light propagation and stress-energy conservation to derive actual distance residuals. The two-timescale bridge and covariant conservation gates remain open.

PR39 uses log weighted tracer density ratio ln rho_g rather than real-space total matter delta_R. A possible *conditional* bridge on suitable scales is delta_g= b_R(z)*delta_m plus stochasticity/RSD/selection corrections, with delta_g=rho_g-1 only after validating mean normalization. This is not established for current BGS estimator. b_R, redshift-space mapping, density smoothing and stochastic errors must be independently calibrated (selection-matched mocks or independent matter reconstruction), not chosen to yield the anticipated effect. IQR of log tracer ratio alone is insufficient to give matter endpoint values. No quantitative R or z dependence follows from toy. No transfer of original 1–3 target to sample IQR. Do not clip out-of-domain matter estimates to force agreement. If the mapping/propagation is unavailable, classify continuous-density extension as exploratory phenomenology, not a preregistered test of a fixed PNT amplitude.

## Conventional null: analytical gate

Linear continuity: div_x v = -a H f delta_m. Thus local isotropic volume expansion perturbation delta H = div_x v/(3a) = -H f delta_m/3. For spherical perturbations v_r(r)= -a H f r * mean_delta(<r)/3 (comoving r). At z=0, f approx Om^.55=.52975, slope -11.901712 km/s/Mpc per unit delta. Same negative sign as PNT; a free linear density-flow slope is degenerate with leading PNT term. This reference is NOT a source-observer distance modulus prediction or an additive correction; do not subtract it from observations or sum it with the toy. Nonlinear density profiles, observer position, anisotropy, other structures and RSD matter. Curvature of toy function is not uniquely distinguishing without conventional nonlinear controls.

Refs: Cai et al. https://doi.org/10.1093/mnras/stw1809 ; Nadathur et al. https://doi.org/10.1093/mnras/sty2799 ; CF4 mock/velocity covariance https://doi.org/10.1093/mnras/stad2764 ; CF4 selection/distance prior https://doi.org/10.1093/mnras/stag1144 ; CF4 distance catalog https://arxiv.org/abs/2209.11238 .

## Forward-model comparison contract (proposed, not implemented)

M0: flat LCDM background plus FP distance/zero-point calibration, selection/truncation, population dependence, measurement and calibration covariance, with full conventional velocity field and relativistic redshift/distance projection. Fit in the distance-modulus or native log-distance likelihood, not inverse noisy distances. For a source at observed z, low-z leading term mu residual approx -5/ln(10) * v_parallel/(cz), positive v away from observer; use full redshift and distance mapping in final model including observer motion and appropriate distance convention. Positive v shifts observed z upward for fixed distance; local divergence is not v_parallel. Group selection and multiple survey calibrations, FP population dependence, redshift-dependent selection, Malmquist effects, self-counts, overlapping neighborhoods, shared random block uncertainty and density/RSD errors must be modeled consistently.

M1: M0 plus fixed conditional PNT template with amplitude A_PNT (distinct from A above). A_PNT=0 is nested conventional null; =1 is fiducial toy template only under independently justified matter and distance mapping. If free linear/curved density trend allowed for conventional confounds, calculate weighted design projection of template and residual information; report rank deficiency or degeneracy rather than claiming identifiability. An unconstrained amplitude or generic slope is exploratory, not uniquely evidence for PNT. Do not fit a CF4 velocity field from the same distance residuals and reuse it as independent flow control. Use selection-matched LCDM mock light cones or external reconstructions with overlap/cross-covariance tracked. Velocity covariance must use physical line-of-sight projections and calibrated cosmology, not the illustrative PR39 exponential alone.

Next implementation: outcome-blind mock/null forward-model design and synthetic signal injection, quantify false positives/coverage and recovered amplitude under selection, density measurement uncertainty, coherent flows and calibration offsets. Revisit 20/30 Mpc/h only on outcome-blind precision and power criteria. Freeze scale, mapping, nuisance, comparison, uncertainty and rejection criteria before data outcomes. If fiducial template cannot be mapped or is unidentifiable, stop confirmatory extension and document why. Original strict P6 remains underpowered and untested; preserve as a separate track. No new data acquisition needed for synthetic tests; representative mocks or independent density/flow calibration will be needed before a physical null can be validated.

## Reproduction

    python notebooks/desi/pnt_density_prediction.py
    python -m unittest discover -s notebooks/desi -p test_pnt_density_prediction.py -v

Executed exact new standalone Python code and 5 tests locally; no astronomy files loaded. Analytical comparator only, no physical covariance, mock forward model, or observational likelihood implemented.
