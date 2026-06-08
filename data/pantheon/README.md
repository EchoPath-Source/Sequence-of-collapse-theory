# Pantheon+ Data Notes

**Status:** PRELIMINARY scaffold / missing required source tables

This directory documents the Pantheon+ environment-dependent H0 test inputs. It does **not** contain a completed Pantheon H0 result.

## Required files for the notebook

The notebook `notebooks/pantheon/pantheon_environment_h0_test.ipynb` refuses to run the primary fit unless all of the following are available:

| Required artifact | Expected path | Status | Label | Notes |
|---|---|---|---|---|
| Pantheon+ supernova table | `data/pantheon/pantheon_plus.csv` | MISSING | MISSING | Needed for redshifts, distance moduli, and covariance row alignment. |
| Environment labels | `data/pantheon/environment_labels.csv` | MISSING | MISSING | Must be a documented derived cross-match; schema is in `environment-labels-schema.md`. |
| Usable covariance file | see candidates below | PARTIAL | PRELIMINARY / EXTERNAL/DOCUMENTED | A covariance subset was requested but is not currently present; full covariance is documented as external pending redistribution clearance. |

Supported covariance candidate paths:

```text
data/pantheon/pantheon_covariance.txt
data/pantheon/Pantheon_cov_subset.txt
data/pantheon/Pantheon_SH0ES_cov.txt.gz
```

## Covariance subset

`data/pantheon/Pantheon_cov_subset.txt` is the preferred small in-repo covariance artifact if a verified subset is available. It is currently **MISSING** in this cleanup pass because no root-level `Pantheon_cov_subset.txt` file was present.

## Full Pantheon+/SH0ES covariance

A root upload named `Pantheon_SH0ES_cov.txt.gz` was inspected on 2026-06-08:

- compressed size: `10,334,474` bytes;
- readable as gzip text;
- first value: `1701`;
- remaining numeric value count: `2,893,401`, equal to `1701 * 1701` covariance entries.

Because this appears to be a full public-data covariance artifact and redistribution terms were not verified during cleanup, it is classified as **EXTERNAL/DOCUMENTED** rather than committed as canonical data. If redistribution is cleared and the project wants it in-repo, use Git LFS or a documented data-release workflow before adding `data/pantheon/Pantheon_SH0ES_cov.txt.gz`.

## Claim boundary

No Pantheon environment-H0 result is **ESTABLISHED** until the Pantheon+ SN table, environment-label table, and a usable covariance file are all present and the notebook is run without changing the locked interpretation rules. Do not claim a Pantheon H0 detection from the current repository state.
