# SIM-04J — Memory-Origin Constraint / Causal-Completion Results

**Status:** synthetic cross-regime benchmark complete  
**Claim level:** methodology only; not evidence for a physical SoCT memory field.

## Question

Can the current reaction-diffusion memory law be the slow limit of a more constrained causal field, so that late-time parameters predict short-time/high-spatial-frequency behavior without new high-frequency fit parameters?

Candidate completion:

```math
\partial_t^2 M + \gamma\partial_t M - c_M^2\nabla^2 M + \omega_M^2M = gC_{obs}.
```

Overdamped mapping:

```math
\alpha=g/\gamma,\qquad \beta=\omega_M^2/\gamma,\qquad D_M=c_M^2/\gamma.
```

Therefore

```math
c_M=\sqrt{\gamma D_M},
\qquad
k_c^2=(\gamma/4-\beta)/D_M.
```

## Design

Synthetic causal generator:

```text
gamma=5.0, beta=0.08, D_M=0.18, noise sigma=0.006.
```

Fit only late/low-k data:

```text
k=0.0,0.4,0.8,1.2; t=4..12.
```

Test on held-out early/high-k data:

```text
k=3.0,4.0,5.0; t=0..3.
```

Fifty noise realizations are evaluated. The causal completion and the pure diffusion model receive the same fitting privileges. `gamma` is treated as independently calibrated.

## Results

### Causal-field generator

| Model | fitted beta | fitted D_M | train RMSE | held-out RMSE |
|---|---:|---:|---:|---:|
| causal completion | 0.080 | 0.180 | 0.00602 | **0.00596** |
| pure diffusion | 0.080 | 0.185 | 0.00741 | **0.08880** |

Derived predictions:

```text
c_M = 0.94868
k_c = 2.54951
```

All held-out modes lie beyond the predicted crossover.

### Pure-diffusion null generator

| Model | fitted beta | fitted D_M | train RMSE | held-out RMSE |
|---|---:|---:|---:|---:|
| causal completion | 0.080 | 0.175 | 0.00742 | **0.08791** |
| pure diffusion | 0.080 | 0.180 | 0.00602 | **0.00596** |

Thus the benchmark does not automatically prefer the causal completion.

## Spectral identity

For an overdamped Fourier mode with slow pole `r_-(k)`, the completion predicts

```math
\frac{r_-(k)[\gamma-r_-(k)]}{\gamma}=\beta+D_Mk^2.
```

The transformed decay rate must therefore be affine in `k^2` with one shared intercept and slope.

## Interpretation

The current first-order memory equation is best treated as an effective low-frequency law unless a more complete derivation says otherwise. If `gamma` is independently calibrated, the causal completion links late-time decay, spatial diffusion, finite propagation speed, mode crossover, and high-k response with one parameter set.

A conventional hidden reservoir constructed with the same complete dynamical law remains observationally degenerate, so SIM-04J does not make `M` necessary. It does make the hypothesis more constrained and therefore more falsifiable.

## Reproduction

```bash
python experiments/observation-foundations/sim04j_memory_origin_constraints.py
```
