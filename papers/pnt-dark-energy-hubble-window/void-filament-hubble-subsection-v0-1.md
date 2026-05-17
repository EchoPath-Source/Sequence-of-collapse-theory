# Paper-Ready Subsection v0.1

## Environmental Dark-Energy Differentials and the Local Hubble Tension

**Intended destination:** P2 — Planck Nucleation Exhaust as a Two-Timescale Dark Energy Model  
**Status:** paper-ready draft subsection, not yet peer reviewed  
**Claim level:** preliminary toy-model result with explicit caveats

### 4.3 Environmental Dark-Energy Differentials and the Local Hubble Tension

A distinctive prediction of Planck Nucleation Theory (PNT) is that the effective dark-energy contribution should not be perfectly homogeneous across cosmic environments. In the PNT picture, failed Planck-scale nucleation attempts return energy to the accessible low-energy sector as nucleation exhaust. Dense environments, such as filaments and cluster-forming regions, convert a larger fraction of nucleation attempts into bound structures, stellar collapse products, or black-hole-like causal separations. Underdense environments, by contrast, have fewer successful conversions and therefore retain a larger failed-exhaust fraction. The resulting prediction is a void–filament dark-energy differential:

```text
rho_DE,void > rho_DE,filament
```

This environmental contribution is not identical to standard matter-underdensity void effects. Conventional local-void explanations of the Hubble tension rely primarily on reduced matter density and peculiar-flow corrections. PNT instead predicts an additional vacuum-sector contribution: underdense regions should carry an enhanced effective dark-energy density because the failed-nucleation channel is less depleted by successful structure formation. The observable consequence is that locally inferred expansion rates should depend on environmental overdensity even after standard density-field and peculiar-velocity corrections are applied.

A minimal toy implementation can be written by modeling the failed-nucleation fraction as a function of local overdensity `delta`:

```text
f_fail(delta) = 1 - f_succ,mean * max(0, 1 + delta)^n
```

with a physical cap:

```text
0 <= f_fail(delta) <= 1
```

The local dark-energy ratio is then approximated by:

```text
rho_DE(delta) / rho_DE,mean = f_fail(delta) / f_fail(0)
```

and the corresponding local expansion estimate is modeled as:

```text
H0(delta) = H0_CMB * sqrt[(Omega_m + Omega_DE * rho_DE(delta)/rho_DE,mean) / (Omega_m + Omega_DE)]
```

Using fiducial parameters

```text
H0_CMB = 67.4 km/s/Mpc
H0_local,obs = 73.0 km/s/Mpc
Omega_m = 0.315
Omega_DE = 0.685
f_succ,mean = 0.15
n = 1.5
```

and a representative local underdensity of approximately

```text
delta ≈ -0.35
```

the toy model gives

```text
H0_PNT,local ≈ 69.3 km/s/Mpc
```

corresponding to an upward shift of approximately

```text
Delta H0 ≈ +1.9 km/s/Mpc
```

relative to the CMB-inferred baseline. Compared against the nominal local-CMB discrepancy

```text
73.0 - 67.4 = 5.6 km/s/Mpc
```

this void/filament dark-energy differential accounts for roughly

```text
1.9 / 5.6 ≈ 34%
```

of the observed Hubble tension in the fiducial toy model.

This result should be interpreted cautiously. It does not show that PNT solves the Hubble tension. It shows that the void–filament exhaust mechanism has the correct sign and a non-negligible amplitude in a bounded environmental toy model. The calculation is most useful because it generates a specific and falsifiable prediction: if PNT is correct, locally inferred expansion residuals should correlate with cosmic environment in a way that includes a dark-energy-like component, not merely a matter-underdensity or peculiar-flow component.

### 4.4 High-Density Breakdown and Domain Restriction

The simple Schmidt–Kennicutt-inspired scaling used above is not valid at arbitrarily high overdensity. If extrapolated into cluster-core regimes, the raw formula can drive `f_fail` below zero, which is unphysical. The model therefore requires both a bounded domain and an explicit cap:

```text
0 <= f_fail <= 1
```

The current toy calculation should be restricted to approximately

```text
-0.9 <= delta <= +0.5
```

where the environmental scaling remains a controlled phenomenological approximation. Cluster cores, nonlinear collapse regions, and highly virialized environments should not be used as evidence against the model unless a more appropriate high-density transfer function has been defined. In future versions, the power-law scaling should be replaced by a saturating collapse-efficiency function, for example a logistic or other bounded mapping from overdensity to successful-nucleation fraction.

This boundary condition is not a cosmetic correction. It is a required physical constraint. A viable PNT environmental model must preserve

```text
0 <= f_succ(delta) <= 1
0 <= f_fail(delta) <= 1
```

for all cosmic environments.

### 4.5 Observational Discriminants

The key observational distinction is that PNT predicts two separable contributions to environment-dependent expansion:

1. a conventional matter-density / peculiar-flow contribution, and
2. an additional effective dark-energy contribution sourced by the failed-nucleation fraction.

Therefore, the relevant test is not simply whether the local universe is underdense. That question has already been studied in standard cosmology. The PNT-specific test is whether expansion residuals, Type Ia supernova residuals, or environmental Hubble-flow reconstructions show a dark-energy-like dependence on void/filament classification after standard density and peculiar-velocity corrections.

A minimal test program would compare:

```text
H0(void hosts or void-dominated lines of sight)
```

against

```text
H0(filament / wall / cluster environments)
```

while controlling for:

- peculiar velocities,
- host-galaxy properties,
- calibration-ladder systematics,
- survey selection,
- Malmquist bias,
- redshift binning,
- local density reconstruction method,
- large-scale-flow model.

The PNT prediction is

```text
H0,void > H0,filament
```

with an environmental scaling that should not be fully absorbed by standard matter-density corrections. A related supernova test is that Type Ia residuals should encode a weak but systematic environmental signature if the local dark-energy sector varies with void/filament classification.

### 4.6 Relation to the Broader Hubble-Tension Picture

The void–filament mechanism should be considered one contribution within the broader PNT Hubble-tension framework. Current status can be summarized as:

```text
Void dark-energy differential:   ~1-3 km/s/Mpc   calculated toy estimate
Prompt EDE component:            ~1-2 km/s/Mpc   toy-model feasibility window
Memory-field gravity correction: unknown         not yet calculated
Parent-universe contribution:    unknown         not yet calculated
```

The combined picture is therefore suggestive but incomplete. PNT currently provides a concrete environmental contribution of order one-third of the observed tension in the fiducial void calculation, while the prompt-exhaust channel may supply an additional partial sound-horizon shift. Whether the remaining discrepancy can be closed by memory-field gravity or parent-universe initial-condition contributions remains an open calculation.

The correct claim at this stage is:

> PNT does not yet solve the Hubble tension, but it predicts a novel void–filament dark-energy differential that can account for a meaningful fraction of the local-CMB discrepancy and can be tested with existing large-scale-structure and distance-ladder data.

### 4.7 Falsification Conditions

The void–filament mechanism is weakened or falsified if:

1. local expansion residuals show no correlation with void/filament environment after standard controls,
2. any observed environment dependence is fully explained by conventional matter-density and peculiar-velocity effects,
3. the inferred sign is opposite to the PNT prediction,
4. the required dark-energy differential violates BAO, CMB, supernova, or structure-growth constraints,
5. the model requires an unconstrained or unphysical environmental transfer function to fit the data.

The preferred next step is to replace the current toy scaling with a bounded environmental transfer function and test the prediction against supernova and large-scale-structure catalogs.
