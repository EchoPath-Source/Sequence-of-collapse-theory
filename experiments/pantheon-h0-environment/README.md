# Pantheon+ Environment-Dependent H0 Test

Status: pipeline scaffold / preregistration-ready structure.

This experiment tests the Sequence of Collapse Theory / memory-gravity prediction that local expansion differs by cosmic environment:

```text
H0_void > H0_filament
```

The test uses Pantheon+ / SH0ES supernova distance moduli, a covariance-aware likelihood, and externally defined environment labels such as void, filament, and unclassified.

## Core principle

This pipeline is designed to prevent post-hoc tuning:

- environment cuts are defined before fitting;
- redshift cuts are locked before fitting;
- covariance-aware chi-square is used for all reported fits;
- permutation and jackknife tests are mandatory;
- synthetic injection tests are used before interpreting real labels.

## Primary observable

```text
Delta_H0 = H0_void - H0_filament
```

SoCT prediction: `Delta_H0 > 0`.

Expected magnitude: modest, approximately 1-5 km/s/Mpc. Large unblinded significances should be treated as suspicious until audited.

## Required inputs

Place externally obtained data files in the data folders described below. Large public datasets should not be committed unless licensing and file size are appropriate.

```text
data/pantheon/
  Pantheon+ data table
  Pantheon+ covariance matrix

data/environment/
  SN-to-environment crossmatch table
  void catalog metadata
  filament catalog metadata
```

## Pipeline modules

```text
src/soct_pantheon/
  config.py         fixed analysis configuration
  loaders.py        data/covariance/environment loading utilities
  cosmology.py      flat-LambdaCDM distance modulus model
  fit_h0.py         covariance-aware H0 fitting
  permutation.py    label-shuffle significance tests
  run_pipeline.py   command-line orchestration
```

## Outputs

```text
results/pantheon-h0-environment/
  primary_fit.json
  permutation_summary.csv
  jackknife_summary.csv
  audit_log.md
```

## Interpretation rules

A credible positive result requires:

1. correct sign: `H0_void > H0_filament`;
2. modest amplitude;
3. covariance-aware fit stability;
4. survival under permutation tests;
5. survival under sky/survey/redshift jackknife tests.

Null or opposite-sign results should be retained and reported without reinterpretation.
