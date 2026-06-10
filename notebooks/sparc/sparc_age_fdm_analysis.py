"""
Compatibility wrapper for the canonical SPARC age--outer-fDM analysis.

Status: PRELIMINARY / reproducibility support
Claim level: Evidence-bearing only when run against committed CSV inputs and reviewed.

Why this file exists
--------------------
Earlier repo manifests and missing-file checklists expected this exact filename:

    notebooks/sparc/sparc_age_fdm_analysis.py

The runnable implementation currently lives at:

    notebooks/sparc/sparc_age_dm_analysis.py

This wrapper preserves the expected filename while delegating to the canonical implementation.

Run from repository root:

    python notebooks/sparc/sparc_age_fdm_analysis.py
"""

from __future__ import annotations

from sparc_age_dm_analysis import main


if __name__ == "__main__":
    main()
