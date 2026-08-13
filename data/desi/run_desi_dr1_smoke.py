#!/usr/bin/env python3
"""Run the canonical DESI DR1 25-row smoke query through Astro Data Lab HTTP.

This script intentionally uses only the Python standard library so it does not
require the astro-datalab package. It is a schema/access smoke test only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[2]
SQL_PATH = ROOT / "data" / "desi" / "DESI_DR1_SMOKE_QUERY_v0_1.sql"
DEFAULT_OUT = ROOT / "data" / "desi" / "desi_dr1_smoke_v0_1.csv"
DEFAULT_META = ROOT / "data" / "desi" / "desi_dr1_smoke_v0_1.provenance.json"
SERVICE_ROOT = "https://datalab.noirlab.edu/query"
QUERY_URL = SERVICE_ROOT + "/query"
QUERY_VERSION = "desi-dr1-smoke-v0.1"


def load_sql() -> str:
    text = SQL_PATH.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if not line.lstrip().startswith("--")]
    return "\n".join(lines).strip()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT)
    parser.add_argument("--meta", type=pathlib.Path, default=DEFAULT_META)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    sql = load_sql()
    params = urllib.parse.urlencode(
        {
            "sql": sql,
            "ofmt": "csv",
            "out": "",
            "async": "False",
            "drop": "False",
            "profile": "default",
        }
    )
    url = QUERY_URL + "?" + params
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Sequence-of-collapse-theory/DESI-smoke-v0.1",
            "X-DL-AuthToken": "anonymous.0.0.anon_access",
        },
    )

    started = datetime.now(timezone.utc)
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            payload = response.read()
            http_status = getattr(response, "status", None)
            content_type = response.headers.get("Content-Type")
    except Exception as exc:
        print(f"DESI smoke query failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    text = payload.decode("utf-8", errors="replace")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(payload)

    lines = [line for line in text.splitlines() if line.strip()]
    header = lines[0].split(",") if lines else []
    row_count = max(len(lines) - 1, 0)

    meta = {
        "query_version": QUERY_VERSION,
        "source_release": "DESI DR1",
        "source_table": "desi_dr1.zpix",
        "service_root": SERVICE_ROOT,
        "profile": "default",
        "execution_mode": "anonymous synchronous HTTP",
        "execution_timestamp_utc": started.isoformat(),
        "http_status": http_status,
        "content_type": content_type,
        "row_count": row_count,
        "columns": header,
        "csv_sha256": sha256_bytes(payload),
        "sql_sha256": sha256_bytes(sql.encode("utf-8")),
        "sql_path": str(SQL_PATH.relative_to(ROOT)),
        "output_path": str(args.out.relative_to(ROOT)) if args.out.is_relative_to(ROOT) else str(args.out),
    }
    args.meta.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    print(text, end="" if text.endswith("\n") else "\n")
    print(f"\nrows={row_count}")
    print(f"csv_sha256={meta['csv_sha256']}")
    print(f"provenance={args.meta}")

    expected = {
        "targetid",
        "mean_fiber_ra",
        "mean_fiber_dec",
        "z",
        "zwarn",
        "zcat_primary",
        "objtype",
        "survey",
        "program",
        "spectype",
        "healpix",
    }
    missing = sorted(expected.difference(header))
    if missing:
        print("missing expected columns: " + ", ".join(missing), file=sys.stderr)
        return 3
    if row_count == 0:
        print("query returned zero rows; inspect sky patch and predicates", file=sys.stderr)
        return 4

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
