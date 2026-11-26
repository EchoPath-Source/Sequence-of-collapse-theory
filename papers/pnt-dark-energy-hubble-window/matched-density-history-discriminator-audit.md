# P6 matched-density history discriminator: synthetic audit and conventional simulation pilot

2026-11-26 UTC. PR42 merged at 67cbf71c47ec62cab3f8b059d955f69108651444. No astronomical inputs, measured moduli, velocity residuals or H0 outcomes loaded. This extends the conditional homogeneous finite-exhaust closure in finite-memory-exhaust-response-audit.md, not a new physical prediction. Original P6 unchanged.

## Matched-history design

768 pairs, 64 blocks, 320 equal midpoint-constant source intervals over 8 Gyr, seeds 20261125 and 20261126. Pair members have analytic trajectories delta_+(t), delta_-(t)=d*exp((t-8)/8) +/- A*sin^2(pi*t/8), d uniform [-.3,.25], A uniform [.05,.25]. Identical endpoint density and time derivative at both endpoints. Within canonical toy domain, no clipping. This is a single prescribed trajectory family with no dynamical growth or gravity solution. Hold E(t=0)=1 and D_E=0. For interval [t_j,t_{j+1}], weight exp(-(t_end-t_{j+1})/tau)*(1-exp(-(t_{j+1}-t_j)/tau)); E_end=1+sum w_j*(q(delta_j)-1). Exact for the discretized source. Conditional g=mu(E_plus)-mu(E_minus), mu=-2.5 log10(.315+.685 E); not light-cone physics. Positive g means the previously denser member has smaller conditional expansion proxy. Each pair is ordered by its known synthetic history, not its distance outcome.

Pair-difference covariance: sum of two independent FP-like measurement variances, each sigma uniformly .43-.60 mag, plus illustrative shared block variance .03^2 mag^2. No claim of calibrated CF4 covariance. Use a free pair-difference intercept (conservative possible systematic offset between history classes), current density and its square as baseline nuisance columns. The assembly variable B=2A represents true difference in peak history bump; noisy proxy adds independent .08 and shared block .04 Gaussian noise. Stress systematic c=.08 B+.04 B*d mag chosen illustratively, not measured astrophysical bias. Nuisance models: baseline only; add B; add B and B*d; add noisy B and its interaction instead. Thus matching density alone does not eliminate an unknown conventional history response. Matching actual galaxy populations, velocities, tidal fields and calibrations not implemented.

For fixed covariance C=L L^T, whiten g and X, use SVD projection onto orthogonal complement of nuisance design; information I=||g_perp||^2. If numerically degenerate, no finite amplitude estimate or power assigned. Otherwise SE=1/sqrt(I), minimum detectable amplitude (MDA80) approximately 2.801585*SE, analytic two-sided Gaussian rejection probability under injected amplitude 1 and confounded amplitude 0. Intercept removes ability to identify the mean ordered-pair difference independently of a history-class offset; this is not the power of an ideal paired test with a known zero offset. No Monte Carlo outcomes needed; conditional power calculated analytically. The systematic produces bias (g_perp^T L^-1 c)/I. Fixed known nuisance design and covariance, no selection model, no fitted data.

## Executed synthetic results

Seed 20261125, conditional median paired modulus difference (mag) and baseline-nuisance clean power.

| tau Gyr | Median difference | 10th–90th percentile | MDA80 | Clean power |
|---:|---:|---:|---:|---:|
| .1 | .0001802 | .0000852–.0002798 | 1058.23 | .050001 |
| 1 | .0111832 | .0052717–.0173545 | 17.05 | .053099 |
| 2 | .0204582 | .0096818–.0317268 | 9.31 | .060446 |
| 5 | .0221097 | .0103829–.0339932 | 8.67 | .062036 |
| 10 | .0159815 | .0075161–.0245839 | 12.00 | .056267 |
| 20 | .0096775 | .0045714–.0148842 | 19.81 | .052294 |

Illustrative tau=5 Gyr (not selected for observational use):

| Nuisance | MDA80 | Clean injected power | Confounded null rejection | Confounded amplitude bias |
|---|---:|---:|---:|---:|
| current density | 8.673 | .062036 | .064162 | 1.084103 |
| exact assembly B | 125.218 | .050057 | .050091 | 1.259349 |
| exact B and interaction | 20632.811 | .050000 | .050000 | approximately 0 |
| noisy assembly and interaction | 13.725 | .054786 | .055644 | 1.085587 |

Exact assembly B retains (8.673/125.218)^2=0.004798 (~0.48%) of baseline amplitude information. Exact interaction absorbs even more. Noisy proxy can leave apparent information because the true confound is not controlled. A small false-positive rate here reflects low power, not absence of confounding: expected amplitude bias exceeds unity in baseline and noisy cases. Seed 20261126 at tau=5 gives median .0223266 mag, MDA80 8.824/128.427/19647.648/14.649 in same nuisance order and baseline power .061626. Both seeds reproduce qualitative conclusion. Tau grid preselected as in PR42; do not select tau by best apparent power. This artificial trajectory family tightly ties memory to the assembly variable by construction; results are not a no-go theorem for more complex histories. No validated observational amplitude, actual CF4 power or physical null simulation.

## Conventional simulation pilot contract (not executed)

Candidate source: Quijote standard fiducial suite (real-space 3D cubes), https://quijote-simulations.readthedocs.io/en/latest/df.html ; standard snapshots z=0,.5,1,2,3 per https://quijote-simulations.readthedocs.io/en/latest/features.html . Big Sobol Sequence (BSQ) documents 11 redshift outputs z=6,5,4,3,2,1.5,1,.7,.5,.2,0, 256^3 CIC matter fields and Rockstar merger trees: https://quijote-simulations.readthedocs.io/en/latest/bsq.html . BSQ cosmologies vary across simulations; do not pool as fixed cosmology, use explicit parameter metadata and a preselected near-fiducial subset for higher-cadence sensitivity. Standard Quijote preferred for matched cosmology and independent realizations, BSQ for time-resolution sensitivity. Actual file paths/availability, permissions and checksums not checked. No simulation data downloaded. Reference Villaescusa-Navarro et al. https://arxiv.org/abs/1909.05273 .

First bounded pilot: 3 distinct fixed-cosmology fiducial realizations, matching grids at z=3,2,1,.5,0, 256^3 if available; confirm axes, real-space field, periodic box 1000 h^-1 Mpc, density conventions and mean (BSQ HDF5 df is CIC particle counts, not overdensity), cosmology, snapshot times and phase identity. Compute delta=df/mean(df)-1 for verified mass/count fields, with appropriate handling for already normalized overdensity. At fixed Eulerian comoving coordinates, use periodic spherical top-hat smoothing R=20,30 h^-1 Mpc (not k=1/R); use actual cosmology to convert redshift to cosmic time. Extract the same grid coordinates at every epoch; do not follow halos in this Eulerian test. Separate Lagrangian histories require tracked particles/merger trees, different modeling. Do not identify galaxy stellar age with Eulerian matter history. Apply q domain at all times, report out-of-domain attrition, no clipping. Smoothing before q is a coarse-grained modeling choice, not equivalent to smoothing nonlinear q. Compare grid/time resolution and interpolation (piecewise-constant vs linear interpolation); sparse snapshot cadence cannot establish short tau convergence, report unresolvable tau. Source initial state and starting redshift sensitivity, no fitted tau/ell. Zero diffusion first, nonzero D requires spatial mode evolution, not per-cell independent relaxation.

Use reproducible coordinate sampling (e.g. seed and fixed stride) with train/holdout by entire independent realization, spatial blocking for within-box dependence. Summarize variance of conditional history response after present density, current growth proxy, smoothed tidal invariants/multiscale density and standard assembly proxies; history-matched pairs selected without distance outcomes. Validate that residual history variation persists in held-out boxes, not merely present-density or linear growth proxy. Compare a shuffled-history adversary conditioned on present environment and conventional covariates. Do not claim FP population calibration from dark-matter-only data; selection-matched galaxy/velocity mocks and independent calibration are separate gates. Fixed external physical source and light-cone mapping remain open. If conventional assembly absorbs response or signal too weak, close candidate as blocked rather than optimize cuts. This is an information/identifiability audit, not a cosmological fit.

Prefer remote computation or compact derived trajectory exports (coordinates, smoothing radii, snapshot redshifts/times, delta, tidal/growth/assembly metadata, seed/realization IDs and provenance manifest); no full particle snapshot or large catalog transfer required for the first pilot. No acquisition initiated this pass.

## Reproduction and decision

    OPENBLAS_NUM_THREADS=1 python -m unittest discover -s notebooks/desi -p test_history_discriminator.py -v
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/history_discriminator.py
    OPENBLAS_NUM_THREADS=1 python notebooks/desi/history_discriminator.py --seed 20261126

Exact new local files executed, 5/5 tests passed, both seeds completed (NumPy 2.3.5, SciPy 1.17.0). Code SHA256 a06e1c032811c99bde829e14812a92cd8ca6355df097bb1cd57c79ffc5a9e388; tests SHA256 94b17a48e35bd59b7450d5f6e8c4442c59984de5ce7391e3f0412775df621781. CI pending. History ordering can distinguish equal endpoint density in the candidate equation, but this synthetic paired design fails the power and assembly-identifiability gates. Real simulation history pilot remains pending. No promotion to confirmatory P6, no unblinding or H0 fit. Protected source, parameters, causality, energy conservation and observable mapping unresolved.
