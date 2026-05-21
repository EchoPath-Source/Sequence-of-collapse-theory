# Pantheon+ Environment Labels Schema

**Status:** Schema scaffold / pending environment cross-match  
**Related experiment:** `experiments/cosmology/pantheon-environment-h0-test.md`  
**Related covariance note:** `data/pantheon/covariance-notes.md`

---

## Purpose

This file defines the required schema for the environment-label table used in the Pantheon+ environment-dependent H0 test.

The primary prediction is:

```text
H0_void > H0_filament
```

Primary statistic:

```text
Delta_H0 = H0_void - H0_filament
```

---

## Required Output File

Recommended path:

```text
data/pantheon/environment_labels.csv
```

or, for analysis-package mirroring:

```text
observations/pantheon/data/environment_labels.csv
```

---

## Required Columns

| Column | Type | Required | Description |
|---|---|---:|---|
| `sn_id` | string | yes | Pantheon+ supernova identifier, matching primary SN table. |
| `pantheon_index` | int | yes | Row index matching Pantheon+ table and covariance ordering. |
| `ra_deg` | float | yes | Right ascension in degrees. |
| `dec_deg` | float | yes | Declination in degrees. |
| `z_cmb` | float | yes | CMB-frame redshift or chosen primary analysis redshift. |
| `z_helio` | float | recommended | Heliocentric redshift, if available. |
| `host_z` | float | recommended | Host redshift, if available. |
| `environment_label` | categorical | yes | `void`, `filament`, `wall`, `cluster`, or `unclassified`. Primary test uses void/filament only. |
| `environment_binary` | categorical | yes | `void`, `filament`, or `unclassified` after binarization. |
| `void_id` | string | optional | Identifier of nearest void, if using void catalog. |
| `filament_id` | string | optional | Identifier of nearest filament, if using filament catalog. |
| `nearest_void_distance_mpc` | float | recommended | Comoving distance to nearest void center/boundary, depending on catalog definition. |
| `nearest_filament_distance_mpc` | float | recommended | Comoving distance to nearest filament spine or structure. |
| `local_density_delta` | float | recommended | Local density contrast, if available. |
| `catalog_source` | string | yes | Environment catalog / method used. |
| `classification_method` | string | yes | Rule used to assign label. |
| `classification_confidence` | float | recommended | Confidence score or distance margin if available. |
| `notes` | string | optional | Manual flags, caveats, or ambiguity notes. |

---

## Primary Analysis Filter

Primary Pantheon+ environment-H0 test should use:

```text
environment_binary in [void, filament]
0.01 < z < 0.15
```

Exclude from primary test:

```text
unclassified
wall
cluster
ambiguous labels without preregistered binning rule
```

These may be used only in secondary/exploratory analysis.

---

## Classification Rules Must Be Locked

Before fitting H0, document:

1. environment catalog source;
2. cosmology used to compute positions;
3. distance metric;
4. void/filament threshold;
5. how ambiguous cases are handled;
6. whether wall/cluster labels are excluded or folded into filament;
7. final counts:

```text
N_void
N_filament
N_unclassified
```

No threshold should be tuned after inspecting `Delta_H0`.

---

## Required Validation Checks

1. Every `pantheon_index` maps to the correct covariance row/column.
2. Every included SN has valid `z`, `mu_obs`, and covariance entry.
3. Redshift distributions of void and filament samples are compared.
4. Sky distribution is plotted and checked for survey-selection imbalance.
5. Environment labels are stable under alternate catalog/method if available.
6. Random permutation test is run.
7. Redshift-matched bootstrap is run.
8. Sky jackknife is run.

---

## Claim Boundary

This schema does not imply that environment labels have been generated or that the SoCT/PNT void-filament prediction is supported.

It only defines the required data structure for testing:

```text
Delta_H0 = H0_void - H0_filament
```

under a locked, covariance-aware analysis pipeline.
