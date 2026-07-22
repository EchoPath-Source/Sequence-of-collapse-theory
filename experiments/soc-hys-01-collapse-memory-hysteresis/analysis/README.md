# SOC-HYS-01 Analysis Plan

**Status:** ANALYSIS SCAFFOLD / SIMULATION-FIRST  
**Purpose:** Build the analysis pipeline before interpreting any physical data.

## Analysis principle

The analysis must be locked before physical data are collected or unblinded.

Primary rule:

```text
Do not tune the analysis after seeing whether the effect appears.
```

## Data model

Recommended per-trial columns:

```text
trial_id
run_id
block_id
condition_label_blinded
condition_true_unblinded_later
transition_type
trial_index_in_block
trial_index_after_switch
measured_signal
temperature_sensor
temperature_source
input_power
time_since_start_seconds
environmental_flags
excluded
exclusion_reason
```

## Primary endpoint

```text
Delta_HYS = mean(R_post(H -> L)) - mean(R_post(L -> H))
```

where `R_post` is the residual signal for the first preregistered N trials after a condition switch.

Default exploratory value:

```text
N = 100
```

## Residual correction

A minimal correction model should include:

```text
measured_signal ~ temperature_sensor + input_power + time_since_start_seconds + block_id
```

The residual from this model becomes the primary measurement stream.

## Required outputs

The analysis pipeline should generate:

```text
results/soc_hys_01_primary_summary.csv
results/soc_hys_01_bootstrap_summary.csv
results/soc_hys_01_permutation_summary.csv
results/soc_hys_01_run_metadata.json
figures/soc_hys_01_post_switch_residuals.png
```

Binary figures may be regenerated rather than committed, depending on repository policy.

## Simulation-first requirement

Before hardware data are interpreted, the repository should include a simulation script capable of generating:

1. pure-null data;
2. small hysteresis-injected data;
3. thermal-drift-only data;
4. sensor-settling-only data;
5. combined-confound data.

The analysis should correctly avoid false positives under confound-only simulations.

## Statistical checks

Minimum checks:

1. Primary difference in post-switch residuals.
2. Bootstrap confidence interval.
3. Permutation p-value.
4. Run-level consistency check.
5. Sensitivity report for alternative N values, marked exploratory unless preregistered.

## Interpretation boundary

A positive result is an anomaly candidate, not proof of SoCT.

A credible SoCT-relevant result requires:

1. preregistration;
2. locked analysis;
3. physical sensor data;
4. environmental controls;
5. repeatability across days;
6. independent replication;
7. a scaling law tied to a SoCT variable.
