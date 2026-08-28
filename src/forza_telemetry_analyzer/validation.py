from __future__ import annotations

import csv
from pathlib import Path


def validate_timestamps(file_path: Path) -> tuple[int, float]:
    "Validate telemetry timestamps and return row count and duration"
    with file_path.open(newline="") as file:
        rows = list(csv.DictReader(file))

    timestamps = [int(row["timestamp_ms"]) for row in rows]

    if not timestamps:
        raise ValueError("Telemetry file contains no data.")

    if any(
        current <= previous for previous, current in zip(timestamps, timestamps[1:])
    ):
        raise ValueError("Telemetry timestamps are not strictly increasing.")

    duration_seconds = (timestamps[-1] - timestamps[0]) / 1000

    return len(rows), duration_seconds
