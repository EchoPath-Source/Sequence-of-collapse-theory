# Effective-G Memory Model

**Status:** scaffold / phenomenological model note  
**Claim level:** exploratory / effective-theory layer  
**Related tracks:** SPARC age-fDM, Pantheon+ environment-H0, PM void-filament simulations

## Purpose

This note separates the effective gravity-memory model from deeper substrate hypotheses such as PNT or Planck-scale nucleation.

The working effective model is:

```math
G_{eff}(x,t) = G_0 [1 + \alpha M(x,t)]
```

where:

- `G_0` is the locally measured Newtonian gravitational coupling;
- `alpha` is a small phenomenological coupling;
- `M(x,t)` is an accumulated memory/history field.

The model does not require changing `c`, `hbar`, or the fundamental definition of Planck units. It is treated as a low-energy effective modification unless otherwise specified.

## Minimal Memory Kernel

A minimal scalar memory term may be written as:

```math
M(t) = 1 - e^{-t/\tau}
```

or, more generally:

```math
M(x,t) = \int_{-\infty}^{t} K(t-t') S(x,t') dt'
```

where:

- `K` is a causal/retarded kernel;
- `S` is a source such as density, curvature, or collapse-history proxy;
- `tau` is the accumulation/decay timescale.

## SPARC Weak-Field Connection

For circular motion:

```math
V^2(r) = r g(r)
```

With a memory-amplified effective coupling:

```math
V^2_{obs}(r,t) = V^2_{bar}(r) [1 + \alpha M(t)]
```

The outer dark fraction becomes:

```math
f_{DM}(t) = 1 - \frac{1}{1 + \alpha M(t)}
```

For weak coupling:

```math
f_{DM}(t) \approx \alpha (1 - e^{-t/\tau})
```

This motivates the SPARC fitting model:

```math
f_{DM}(t) = f_0 + A_{mem}(1 - e^{-t/\tau})
```

## Cosmology / Environment Connection

The same memory structure may be explored phenomenologically as an environment-dependent expansion bias:

```text
voids: lower accumulated memory -> faster effective expansion
filaments: higher accumulated memory -> slower effective expansion
```

Primary Pantheon+ prediction:

```text
H0_void > H0_filament
```

## Simulation Requirements

Any simulation using this model should report:

```text
alpha
tau
source field S
kernel K
spatial smoothing length
redshift/time convention
random seed
comparison baseline
output observable
```

## Claim Boundary

This file defines an effective phenomenological model. It does not establish the physical origin of the memory field. PNT or Planck-scale interpretations should be treated as separate substrate hypotheses unless directly constrained by data.
