# P5 — Memory Field Density Variation and the Hubble Tension

## Subtitle

Collapse-History Dependent Expansion Rates as an Alternative to Systematic Error

## Roadmap status

**Outlined — write after P1.**

Roadmap target: **Astrophysical Journal Letters**.

## Purpose

This is the canonical P5 folder from the March 2026 SOC Publication Roadmap.

P5 develops the Hubble tension prediction from the memory-field framework: void regions should have lower memory-field density and higher local H0, while filament regions should have higher memory-field density and lower local H0.

## Core prediction

> H0 measured from void environments should be greater than H0 measured from filament environments by an amount determined by memory-field density contrast.

## Roadmap motivation

The Hubble tension is a major unresolved discrepancy between early- and late-universe H0 measurements. The roadmap positions SOC as predicting an environment-dependent expansion difference rather than treating the discrepancy only as systematic error.

## Analysis target

Cross-correlate H0 residuals with large-scale-structure environment:

- voids;
- filaments;
- walls / sheets if available;
- local density estimates;
- memory-field density proxies.

## Relationship to existing repo work

Earlier repo folder:

```text
papers/pnt-dark-energy-hubble-window/
```

That folder remains as a P5 support package, especially for prompt exhaust, late memory residue, and Hubble-window modeling. This folder is the roadmap-canonical P5 paper folder.

Existing related scaffolds:

```text
data/pantheon/
notebooks/pantheon_environment_h0_fit_plan.md
docs/dark-sector-taxonomy.md
```

## Peer-review math audit dependency

P5 depends on the repository-wide PNT/SoCT covariance, conservation, and timescale audit:

```text
papers/math/pnt-soct-covariance-conservation-and-timescale-audit.md
```

That audit records four gates that must be addressed before peer-review-level claims:

1. memory kernels must be covariant/gauge safe;
2. memory stress-energy must be conservation-compatible;
3. junction-surface tensors must be explicitly defined for the relevant surface class;
4. the dark-energy / Hubble-window model must justify long-timescale memory survival.

For P5 specifically, the two-timescale bridge is the most relevant open item:

```text
M(x,t) = M_f(x,t) + M_p(x,t)
beta_p << beta_f
rho_eff(t) = rho_Lambda + rho_Mp(t)
```

Claim boundary: this is a candidate phenomenological bridge. It does not prove a dark-energy mechanism until derived from an action or constrained by data.

## Required work before publication

1. Pre-register the specific correlation analysis before running it.
2. Define void/filament labels and source catalog.
3. Define H0 residual model.
4. Use covariance-aware fitting.
5. Compare against systematics and selection effects.
6. Report null result criteria.
7. Resolve or explicitly bracket the peer-review math audit gates before making physical claims beyond a phenomenological scaffold.

## Dependency

The roadmap recommends writing P5 after P1 establishes the memory-field framework.

## OSF action

Create or update OSF project:

```text
SOC-P5: Hubble Tension Memory Gradient
```

Upload:

- outline;
- preregistered analysis plan;
- environment-label schema;
- Pantheon+ notes;
- preliminary analysis only after preregistration.