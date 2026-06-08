# Intake Wave 03 — File Map and Repo Placement

Status: received in chat and mapped. This wave primarily strengthens **P6 / black-hole memory compression**, **P7 / unified framework**, and the CIH/Kerr/Engramon support package. It also clarifies that the roadmap sequence in the March report differs from the later P1-P7 canonical repo structure; these materials should be imported as source/support rather than used to overwrite the current canonical roadmap without review.

## Received files

| File | Type | Track | Recommended repo destination | Import action | Notes |
|---|---|---|---|---|---|
| `SoCT_Comprehensive_Report_PNT_Annotated.docx` | DOCX comprehensive report | P6 / P7 / simulations / P1-P5 support | `papers/p7-unified-framework/source/soct-comprehensive-report-pnt-annotated.md` after conversion; selected sections also copied into P6 support | Convert DOCX to Markdown; preserve source externally or as release asset if binary upload is desired | Comprehensive research report covering parent-universe directional memory transfer, CIH, Kerr-CMB, Engramon scale, simulations v1.0-v4.1, SPARC directional roadmap, open issues. |
| `kerr_to_cosmos.docx` | DOCX theoretical paper | P6 canonical support | `papers/p6-black-holes-memory-compression-nodes/source/kerr-to-cosmos.md` after conversion | Convert DOCX to Markdown | Derives mapping from parent Kerr black-hole spin to CMB hemispherical power asymmetry, with A = a/(2r_plus) and parent spin a/M ≈ 0.26. |
| `causal_inversion.docx` | DOCX theoretical paper | P6 canonical support / CIH | `papers/p6-black-holes-memory-compression-nodes/source/causal-inversion-hypothesis.md` and possibly `papers/p3-causal-inversion-directional-memory/source/` | Convert DOCX to Markdown | Formal CIH paper: singularities as causal horizon transitions, inversion map, matched metric, Israel junction memory layer, empirical tests. |
| `engramon_scale.docx` | DOCX theoretical paper | P6 / P7 support | `papers/p6-black-holes-memory-compression-nodes/source/engramon-scale.md` | Convert DOCX to Markdown | Pins CIH inversion scale from low quadrupole deficit; derives Engramon scale and E_E ≈ 0.034 eV while flagging amplification and parent-mass open issues. |

## Key content captured

### SoCT Comprehensive Report / PNT Annotated

Main placement: **P7 unified framework source**, with P6 extracts.

Important content:

- Report title: `Parent-Universe Directional Memory Transfer`.
- Status: active investigation; robust signal confirmed; SPARC analysis pending.
- Headline simulation result: real-space bounce simulation v4.1 reports **19/20 kernel configurations positive**, mean delta **+0.583**, zero negatives.
- Open issue: `M_parent` discrepancy between Kerr-CMB paper (~10^14 solar masses) and Engramon paper (~3.1×10^5 solar masses) must be resolved before final parameter unification.
- Core equations include `H_SOC`, memory kernel `K(r,tau,s)`, `g_total = g_baryonic + g_memory`, and collapse rate `lambda_eff = lambda_env + lambda_c exp(-beta I)`.
- Established empirical-result table records age vs dark matter fraction correlation, H0 environment dependence set aside due to insufficient data, and tau_memory convergence.
- CIH section ties Israel junction surface / surface stress-energy to the formal geometric address of the memory field.
- Simulation discipline section documents failed k-space attempts, Grok non-reproducibility, real-space breakthrough, and robustness scan.
- Critical open issues: parent mass discrepancy, missing preferred-axis derivation, need to derive A=f_Omega linear mapping, and N≈42 vs standard N>60 tension.
- SPARC directional analysis roadmap gives a decisive future test: compare SPARC memory gradient direction with CMB Axis of Evil.

Recommended extracted files later:

```text
papers/p7-unified-framework/source/soct-comprehensive-report-pnt-annotated.md
papers/p6-black-holes-memory-compression-nodes/source/parent-universe-directional-memory-report.md
simulations/parent-child-transfer/README.md
simulations/parent-child-transfer/roadmap.md
papers/p6-black-holes-memory-compression-nodes/open-issues.md
```

### Kerr to Cosmos

Main placement: **P6 black-hole memory compression source**.

Important content:

- Working title: `From Kerr to Cosmos: How Parent Black Hole Spin Encodes the CMB Axis of Evil`.
- Core claim: Big Bang and black-hole collapse are the same geometric event viewed from opposite sides of a causal inversion boundary.
- Kerr ring singularity supplies intrinsic orientation; Schwarzschild parent gives isotropic child, Kerr parent gives preferred-axis child.
- Core prediction: `A = f_Omega = a/(2 r_plus)`.
- Inversion from Planck 2018 `A = 0.066 ± 0.021` gives `a/M ≈ 0.2595`, interpreted as moderate parent spin.
- Three tests: axis alignment consistency, spin consistency across observables, entropy budget consistency.
- Interprets Axis of Evil, hemispherical asymmetry, low quadrupole, Cold Spot, and parity asymmetry as possible Kerr-encoded initial-condition fossils.

Recommended destination:

```text
papers/p6-black-holes-memory-compression-nodes/source/kerr-to-cosmos.md
```

### Causal Inversion Hypothesis

Main placement: **P6 / CIH support**.

Important content:

- Hypothesis: singularities are causal horizon boundaries where volume and density coordinates undergo inversion.
- Inversion map: `tau_child = ell^4 / V_parent`; `chi_child = rho_0 / rho_parent`.
- Matched metric section argues the singularity becomes a degenerate boundary rather than curvature blow-up.
- Israel junction condition `[K_mu_nu]_Sigma = 8piG S_mu_nu` identifies `S_mu_nu` as the memory encoding layer / formal location of the SoCT memory field.
- Solutions proposed for information paradox, inflation origin, and cosmological constant problem.
- Empirical tiers: CMB anisotropy, black-hole thermodynamics, primordial gravitational waves.

Recommended destination:

```text
papers/p6-black-holes-memory-compression-nodes/source/causal-inversion-hypothesis.md
papers/p3-causal-inversion-directional-memory/source/causal-inversion-hypothesis.md
```

Note: because the repo now uses canonical P3 for `SOC: From Concept to Equation`, the older `p3-causal-inversion-directional-memory` folder is support material, not canonical P3.

### Engramon Scale

Main placement: **P6 / P7 support**.

Important content:

- Attempts to pin the CIH inversion scale from the CMB low quadrupole deficit.
- The Kerr ring circumference is treated as a parent-side maximum encoding scale that maps to child-side infrared cutoff.
- Candidate amplification mechanisms: inflation as bridge, conformal factor, Engramon as geometric mean.
- Derives inversion scale `ell ≈ 9.4 × 10^-31 m ≈ 6×10^4 l_Pl` under the stated consistency equation.
- Derives Engramon energy `E_E ≈ 0.034 eV`, flagged as near the neutrino mass scale.
- Clearly states open issues: amplification mechanism and conformal-factor constraint.

Recommended destination:

```text
papers/p6-black-holes-memory-compression-nodes/source/engramon-scale.md
```

## Current have / need by paper after Wave 03

### P1 — Age-Dependent Galactic Rotation Curves / SPARC

Have:

- SPARC dataset, analysis code, result tables, mass-proxy comparison, figures, OSF methods PDF, and gravity-as-memory article from Waves 01–02.
- SoCT Comprehensive Report includes SPARC directional roadmap and prior age-DM correlation summary.

Still need:

- Formal P1 manuscript draft.
- Regression models CSV and scatter plot if available.
- Preferred stellar mass / B-V controls.

### P2 — High-Redshift Time-Dependent Gravity

Have:

- No canonical P2 source text yet.

Still need:

- Medium article export or full text from Feb 9 2026.
- Bibliography / references.

### P3 — SOC: From Concept to Equation

Have:

- No canonical P3 source text yet.
- Some math support exists in the comprehensive report and earlier math scaffold, but not the Medium article itself.

Still need:

- Medium article export or full text from Oct 23 2025.
- Equation derivations / Lindblad appendix.

### P4 — SOC-MZI-01 Awareness-Modulated Decoherence

Have:

- SOC-MZI visibility decay simulation script from Wave 01.
- OSF preregistration excerpt from Wave 02.
- Comprehensive report includes collapse-rate equation context but is not the full P4 protocol.

Still need:

- Full SOC-MZI-01 preregistration protocol if excerpt is incomplete.
- AI observer control arm details.
- Device-specific analysis plan / appendices.

### P5 — Hubble Tension as Memory Field Gradient

Have:

- PNT working paper.
- Void-filament mechanism note.
- Environment-H0 analysis figure.
- PNT support package.
- Comprehensive report mentions H0 environment dependence but marks Pantheon+ signal as set aside due to insufficient data.

Still need:

- Canonical P5 manuscript draft.
- Pantheon+ environment labels / real-data tables if available.
- Covariance-aware H0 fitting outputs if generated.

### P6 — Black Holes as Memory Compression Nodes

Have:

- Strongest new wave for P6: Causal Inversion Hypothesis, Kerr to Cosmos, Engramon Scale, and comprehensive directional-memory report.
- PNT working paper also supports black-hole nucleation and child-universe mechanism.

Still need:

- Dedicated P6 manuscript assembled from CIH + Kerr + Engramon + PNT pieces.
- Resolution of `M_parent` discrepancy.
- Explicit derivation of preferred axis direction.
- Formal derivation of `A = f_Omega` linear mapping.
- Additional simulation files if available: `anisotropic_sim.py`, `grok_sim.py`, `directional_sim.py`, `realspace_sim.py`, `robustness_scan.py`, `sparc_directional.py`.

### P7 — Unified Framework

Have:

- SoCT Comprehensive Report / PNT Annotated now provides a strong source corpus for P7.
- PNT working paper, Gravity as Memory article, CIH, Kerr, Engramon, and simulation record all support P7.

Still need:

- Current unified framework working paper if separate.
- Claim-boundary matrix / equation index if available.
- Decision on how to reconcile old comprehensive-report publication pathway with current seven-paper roadmap.

## Import priority after Wave 03

1. Convert and import `causal_inversion.docx`, `kerr_to_cosmos.docx`, and `engramon_scale.docx` into P6 source folders.
2. Convert and import `SoCT_Comprehensive_Report_PNT_Annotated.docx` into P7 source and selected P6 support.
3. Create a P6 `open-issues.md` recording parent-mass discrepancy, missing axis derivation, A=f_Omega derivation gap, and N≈42 inflation tension.
4. Add `simulations/parent-child-transfer/README.md` summarizing v1.0-v4.1 simulation record and pending simulation files.
5. Wait for P2/P3 Medium exports and full P4 protocol in later waves.
