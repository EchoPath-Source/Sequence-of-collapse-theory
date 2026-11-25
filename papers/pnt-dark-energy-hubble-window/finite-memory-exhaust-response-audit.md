# P6 finite-memory exhaust response: conditional derivation and numerical audit

2026-11-25. PR41 merged at 6ee0ee5bf1a7adf0d4a48c69b6866bd0df3b482a. Theory-only calculation, no astronomical inputs or measured distance outcomes. Original P6 remains intact. Motivated by the failed instantaneous-template identifiability test in data/desi/P6_SYNTHETIC_IDENTIFIABILITY_AUDIT.md.

## Source lineage and claim boundary

- papers/math/soc-localization-memory-hamiltonian.md: dM/dt = alpha C - beta M + D_M laplacian M.
- papers/math/pnt-soct-covariance-conservation-and-timescale-audit.md: protected M_p driven by Q[C], beta_p << beta_f; Q[C] and covariant conservation unresolved. Causal damped second-order completion discussed there, with effective alpha=g/gamma, beta=omega_M^2/gamma, D_M=c_M^2/gamma.
- papers/p5-hubble-tension-memory-gradient/README.md: rho_eff=rho_Lambda+rho_Mp is candidate bridge, not a derived stress tensor.
- papers/pnt-dark-energy-hubble-window/continuous-density-prediction-audit.md: q(delta)=[1-.15*(1+delta)^1.5]/.85 on [-.9,.5], Htoy=67.4*sqrt(.315+.685*q).

These sources do NOT identify the protected memory field with failed exhaust, specify its relaxation/diffusion parameters or establish a matter-history source law. The following is a **new conditional closure**, inspired by the existing equation and normalized to recover the static PNT toy. No claim of derivation from a microscopic action.

## Candidate closure

Define E dimensionless exhaust ratio, tau>0 in Gyr, physical D_E>=0 in (Mpc/h)^2/Gyr, comoving x in Mpc/h, and ell=sqrt(D_E*tau). On a prescribed flat FLRW background in a fixed comoving coordinate frame (no advection, dilution or backreaction included):

    partial_t E = (q(delta)-E)/tau + (D_E/a^2) laplacian_x E.

The source normalization is a modeling decision: uniform constant delta gives E=q in equilibrium. It requires alpha times source = q/tau; varying tau therefore changes the source strength at fixed static normalization, not just persistence. Do not interpret it as the original M dynamics with independent alpha held fixed. Initial E=1 is a choice, not a measured initial condition. At nonzero k, steady response is smoothed; static PNT recovered exactly only in homogeneous limit (or negligible diffusion). E=1 refers to the uniform mean-density source, not necessarily ensemble mean of nonlinear q.

For u=E-1 and s=q-1 Fourier mode:

    du_k/dt + lambda_k(t) u_k = s_k/tau
    lambda_k=(1+(k ell/a)^2)/tau
    u_k(t)=u_k(t_i) exp[-integral_i^t lambda] 
            + (1/tau) integral_i^t s_k(t') exp[-integral_t'^t lambda] dt'.

In linear perturbation theory s_k=q'(0) delta_k with q'(0)=-.225/.85=-.264705882. Nonlinear q couples modes; k>0 pulse exercises below are prescribed source-mode amplitudes, not nonlinear density fields or physical void sizes. k is angular wavenumber in h/Mpc; 2pi/k wavelength is not an aperture radius.

## Matched-history result

Fixed a=1, uniform mode k=0, same initial E=1. Two 2 Gyr blocks at delta=+.2 and -.2 (reverse order), followed by 1 Gyr identical delta=0 probe. Equal time-integrated source; neither order changes final density. Let q_L=q(-.2), q_H=q(.2), T=2, P=1. Exact difference between dense-first/void-last and reverse:

    Delta E = (q_L-q_H)/(tau*lambda) * (1-exp(-lambda*T))^2 * exp(-lambda*P).

For k=0 lambda=1/tau. Positive difference for finite positive tau and T. Both limits vanish: short tau loses history during nonzero common probe; long tau with fixed equilibrium normalization and finite blocks responds too weakly. This is history ordering, not simply total collapse accumulation. Conditional toy H=67.4 sqrt(1+.685*u) is used ONLY as a local expansion proxy; no line-of-sight distance prediction.

| tau Gyr | Delta E | Conditional Delta H km/s/Mpc |
|---:|---:|---:|
| .1 | .00000480 | .000111 |
| 1 | .02907332 | .671372 |
| 2 | .02561806 | .591668 |
| 5 | .00940632 | .217230 |
| 10 | .00314277 | .072569 |
| 20 | .00091057 | .021023 |

These selected durations and tau values are illustrative, not calibrated to astrophysical histories. Sub-km/s/Mpc in this scan is not a bound on other histories. Do not select tau to maximize detectable contrast. The instantaneous PR40 density model predicts zero matched-history difference. Ordinary assembly bias, nonlinear flow and population history can also produce matched-current-density differences: not a unique PNT discriminator.

Diffusion changes effective relaxation in addition to amplitude. At tau=5, ell=10, k=.1, prescribed mode Delta E=.0107431 vs .0094063 at k=0; faster effective relaxation can enhance an order contrast in some slow-response regimes. It is incorrect to claim diffusion always suppresses this transient. Strong damping does suppress the growing-mode transfer and can erase history at high k.

## Cosmological growing-mode degeneracy

For linear growing matter perturbations delta_k(a)=G(a) delta_k(a_end)/G(a_end), the forced solution with fixed initial prescription gives u_k(a_end)=q'(0)*F(k,a_end)*delta_k(a_end). At a fixed k and z it remains proportional to instantaneous density. A memory convolution of a separable, common growth history is not a new independent history regressor. Multi-k and multi-z transfer can be distinct in this closure but conventional bias, redshift-space distortions, scale-dependent response and growth/selection uncertainties must be independently constrained. Do not fit an arbitrary function of k and z and attribute it to memory.

Numerically integrate normalized linear response using H(a)=H0 sqrt(Om/a^3+Ode), G(a) proportional to H(a)*integral_0^a da'/(a'^3 H(a')^3), a_start=.25, zero initial perturbation, constant physical D_E. Flat dust+Lambda growing mode, neglect radiation, no self-consistent modification to growth. F is a dimensionless linear coefficient relative to current unsmoothed q'(0)*delta. Initial normalization delta(a_end)=1 is unit linear response, NOT a nonlinear delta=1 input. The initial equilibrium alternative is u_k(a_start)=q'(0)*delta_k(a_start)/(1+(ell*k/a_start)^2).

Selected computed transfer values, same k=.05 h/Mpc:

| tau Gyr | ell Mpc/h | F at z=0 | F at z=.5 |
|---:|---:|---:|---:|
| 1 | 0 | .960723 | .924524 |
| 1 | 10 | .758202 | .586185 |
| 1 | 30 | .295740 | .159159 |
| 5 | 0 | .745839 | .575024 |
| 5 | 10 | .596874 | .417836 |
| 5 | 30 | .256516 | .139902 |
| 10 | 0 | .532025 | .363165 |
| 10 | 10 | .452028 | .296330 |
| 10 | 30 | .220770 | .121931 |

At tau=10, ell=0, z=0, equilibrium initialization yields F=.630365 vs .532025 for zero initial perturbation. Redshift/scale behavior is conditional on tau, ell, physical-vs-comoving transport choice, and initial state. None is predicted or calibrated by the current source theory. The growing-mode transfer is not itself an observed H0 difference.

## Conservation and causality gates

A dimensionless relaxational E is not automatically a dark-energy stress tensor. If one provisionally sets rho_E=rho_E,ref E with constant reference, a homogeneous perfect-fluid equation would require dot(rho_E)+3H(rho_E+p_E)=Q (c=1). For p_E=-rho_E, time variation needs Q=dot(rho_E), and spatial variation requires compatible momentum exchange; total matter+exhaust+interaction stress tensor must be conserved. No such exchange law or perturbation pressure/sound speed is supplied here. Diffusion in first-order form is parabolic and cannot be fundamental causal propagation; require a derived covariant causal completion (e.g. the existing damped second-order scaffold with speed constrained <=c, if actually justified). No identification of E with M_p or protected source Q[C], no microphysical energy budget, no gravitational backreaction or photon propagation. No sum with GR local-divergence proxy permitted.

## Decision and next gate

Structural history sensitivity demonstrated for the conditional closure; unique observable prediction NOT established. Retain as theoretical exploratory extension rather than modify PREDICTIONS.md or preregister. To attempt a discriminator, define source and protected exhaust mapping, independently constrain tau/ell, specify an actual matter-history proxy using simulation histories (e.g. formation time, past density trajectory in an explicitly chosen Eulerian or Lagrangian frame), and compare matched current density with different history while controlling conventional assembly and FP population/selection. Need histories along the modeled field coordinates, not equate stellar age with past matter density. Test on conventional selection-matched mocks with assembly effects, independently constrained velocity/light-cone model and held-out history residual; if history is fully predictable from density or absorbed by nuisance, stop. Assess power after calibration, including joint history/density proxy errors. No additional raw observational acquisition needed now.

## Reproduction

    python notebooks/desi/memory_exhaust_response.py
    python -m unittest discover -s notebooks/desi -p test_memory_exhaust_response.py -v

Exact two new Python files executed locally; 6/6 tests passed (including independent ODE comparison, exact pair contrast, limits and growth initialization). Full 27-row transfer grid printed by script. No data files, outcome fits or physical validation.
