# SoCT Memory-Origin Constraints and Causal Completion

**Status:** analytical constraint program / candidate causal completion  
**Claim level:** derived consequences of the current scaffold; not established new physics  
**Related files:** `papers/math/soc-localization-memory-hamiltonian.md`, `papers/math/pnt-soct-covariance-conservation-and-timescale-audit.md`, `docs/operational-observation-current-formulation.md`

## 1. Why this derivation is needed

The current phenomenological memory law is

```math
\partial_t M = \alpha C_{obs} - \beta M + D_M \nabla^2 M.
```

This is a reaction-diffusion equation. It is useful as an effective low-frequency model, but if interpreted as a fundamental relativistic field equation it has the usual parabolic-equation problem: localized disturbances develop arbitrarily small nonzero tails at arbitrarily large distances for any `t>0`.

The repository's covariance/conservation audit already requires that a physical memory sector ultimately be embedded in a causal, conservation-compatible field description rather than treated as an unconstrained phenomenological term.

The aim here is therefore not to add flexibility. It is to ask what extra constraints appear if the existing diffusion law is only the slow/overdamped limit of a causal field.

## 2. Minimal causal completion

A minimal damped hyperbolic completion is

```math
\partial_t^2 M
+ \gamma\,\partial_t M
- c_M^2\nabla^2 M
+ \omega_M^2 M
= g\,C_{obs}.
```

Interpretation:

- `gamma` = damping / environmental relaxation rate of the memory sector;
- `c_M` = finite propagation speed of memory disturbances;
- `omega_M` = restoring / mass-like frequency scale;
- `g` = source coupling.

The conservative kinetic/spatial/mass part can arise from a scalar-field action. The damping term is effective/open-system structure and requires either an explicit bath, a physical preferred medium/rest frame, or a more complete covariant treatment. This file does **not** claim that this completion is unique.

## 3. Recovery of the current SoCT equation

In the overdamped slow regime

```math
|\partial_t^2 M| \ll \gamma |\partial_t M|,
```

the causal equation reduces to

```math
\partial_t M
\simeq
\frac{g}{\gamma} C_{obs}
- \frac{\omega_M^2}{\gamma}M
+ \frac{c_M^2}{\gamma}\nabla^2M.
```

Therefore the current parameters are not independent labels in this completion. They map to

```math
\alpha = g/\gamma,
```

```math
\beta = \omega_M^2/\gamma,
```

```math
D_M = c_M^2/\gamma.
```

Equivalently,

```math
g = \gamma\alpha,
\qquad
\omega_M^2 = \gamma\beta,
\qquad
c_M^2 = \gamma D_M.
```

This is the first useful origin constraint: once `gamma` is independently measured, the late-time diffusion parameters predict a finite propagation speed and restoring scale rather than leaving them free.

## 4. Spectral constraint

For a spatial Fourier mode `M_k` after the source is switched off,

```math
\ddot M_k + \gamma \dot M_k
+ (\omega_M^2+c_M^2k^2)M_k = 0.
```

Using the overdamped mapping,

```math
\omega_M^2+c_M^2k^2
= \gamma(\beta+D_Mk^2).
```

The two decay poles are

```math
r_\pm(k)
= \frac{\gamma \pm
\sqrt{\gamma^2-4\gamma(\beta+D_Mk^2)}}{2}.
```

For an overdamped mode, the measured slow pole obeys the exact identity

```math
\frac{r_-(k)[\gamma-r_-(k)]}{\gamma}
= \beta+D_Mk^2.
```

Thus a plot of the left-hand side versus `k^2` must be affine with

```text
intercept = beta
slope     = D_M.
```

This is stronger than fitting an arbitrary decay time independently at every wavelength.

## 5. Predicted crossover

The discriminant changes sign when

```math
\beta+D_Mk_c^2 = \gamma/4.
```

Hence

```math
k_c^2 = \frac{\gamma/4-\beta}{D_M}
```

when the numerator is positive.

Below the crossover, modes are overdamped. Above it, the completion predicts a damped oscillatory response with

```math
\Omega_k
= \sqrt{\gamma(\beta+D_Mk^2)-\gamma^2/4}.
```

Crucially, once `beta`, `D_M`, and an independently calibrated `gamma` are fixed at low frequency, `k_c` and the high-frequency dispersion are predictions, not extra fit parameters.

## 6. Causal-front relation

The same completion predicts

```math
c_M = \sqrt{\gamma D_M}.
```

A truly relativistic completion would additionally require an appropriate causal bound, schematically

```math
c_M \le c
```

in ordinary units, together with a covariant definition of the damping/environment sector.

A failure of the measured front speed to agree with `sqrt(gamma D_M)` would falsify this particular causal completion even if the late-time diffusion equation continued to fit.

## 7. Integrated-memory identity in the diffusion regime

For periodic or no-flux boundaries define

```math
Q_M(t)=\int M(x,t)\,dV,
\qquad
Q_C(t)=\int C_{obs}(x,t)\,dV.
```

The diffusion term integrates to zero, giving

```math
\dot Q_M = \alpha Q_C - \beta Q_M.
```

After the source ends,

```math
Q_M(t)=Q_M(t_0)e^{-\beta(t-t_0)}.
```

So `D_M` redistributes memory spatially but cannot change the total integrated memory in this closed-boundary effective model.

If a proposed experiment infers simultaneous source-free growth or loss of integrated `M` beyond the `beta` law, the current equation is incomplete.

## 8. Observation-source constraint

The observation program proposes

```math
C_{obs}=\kappa_{rec}\Gamma_{rec}
```

or a competing record-aware functional such as `Omega`.

Combining this with the integrated identity gives

```math
\dot Q_M
= \alpha\kappa_{rec}\int\Gamma_{rec}\,dV
- \beta Q_M.
```

Therefore, once the source functional is fixed, different record histories cannot receive arbitrary independent memory amplitudes. Their integrated response must be related by the same convolution kernel and the same coupling product `alpha*kappa_rec`.

This is a useful cross-protocol constraint even though a conventional reservoir could in principle be engineered to obey the same law.

## 9. What would count as stronger SoCT-specific evidence

A generic hidden reservoir remains an exact ontology competitor if it is allowed to copy the same source, damping, propagation, and probe-coupling laws.

The point of this derivation is to make that mimic increasingly constrained. A successful competitor must now reproduce simultaneously:

```text
record-derived source scaling
late-time beta
spatial D_M
independent fast damping gamma
finite front c_M = sqrt(gamma D_M)
mode crossover k_c
high-k dispersion Omega_k
fixed probe coupling
held-out protocol transfer.
```

A reservoir with exactly the same complete dynamical structure remains observationally degenerate; that is a naming/ontology problem, not something statistics can solve.

## 10. Scientific status

The current diffusion equation should therefore be treated as an **effective phenomenological law**, not yet as a complete fundamental field equation.

The new falsifiable target is cross-regime consistency:

> Fit the low-frequency/late-time memory law, independently calibrate the fast relaxation scale, and predict high-frequency/short-time propagation without new parameters.

SIM-04J tests this constraint synthetically.
