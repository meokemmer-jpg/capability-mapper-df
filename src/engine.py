#!/usr/bin/env python3
"""
Engine for capability-mapper-df.

Capability: capability-mapper
Spawn reason: __pycache__ lacks discoverable capability metadata
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def append_jsonl(path: Path, event: str, **fields: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": now_iso(), "event": event, **fields}, sort_keys=True) + "\n")


def run(source_dir: Path, log_path: Path) -> int:
    source_dir = source_dir.expanduser()
    append_jsonl(
        log_path,
        "df_engine_started",
        df_name='capability-mapper-df',
        capability='capability-mapper',
        source_dir=str(source_dir),
    )

    artifacts = Path("./artifacts")
    artifacts.mkdir(exist_ok=True)
    report = artifacts / "report.json"
    report.write_text(
        json.dumps(
            {
                "df_name": 'capability-mapper-df',
                "capability": 'capability-mapper',
                "source_dir": str(source_dir),
                "status": "skeleton-ready",
            },
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )

    append_jsonl(log_path, "df_engine_completed", df_name='capability-mapper-df', report=str(report))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", default="~/Projects/dark-factories")
    parser.add_argument("--log-path", default="./spawned-dfs-log.jsonl")
    args = parser.parse_args()
    return run(Path(args.source_dir), Path(args.log_path))


if __name__ == "__main__":
    raise SystemExit(main())
