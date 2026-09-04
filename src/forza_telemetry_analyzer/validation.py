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
        current <= previous 
        for previous, current in zip(timestamps, timestamps[1:])
    ):
        raise ValueError("Must not go backward.")

    duration_seconds = (timestamps[-1] - timestamps[0]) / 1000

    return len(rows), duration_seconds

def validate_required_columns(file_path: Path) -> None:
    """Validate that telemtrey CSV contains required columns."""
    required_columns = {
        "timestamp_ms",
        "engine_max_rpm",
        "current_engine_rpm",
        "acceleration_x",
        "acceleration_y",
        "acceleration_z",
        "speed",
        "power",
        "torque",
        "boost",
        "fuel",
    }
    
    with file_path.open(newline = "") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("Telemetry file has no header.")
        
        missing_columns = required_columns - set(reader.fieldnames)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required telemetry columns: {missing}")
        
def validate_telemetry_file(file_path: Path) -> tuple[int,float]:
    """Validate a telemetry CSV and return row count and duration."""
    validate_required_columns(file_path)
    return validate_timestamps(file_path)

if __name__ == "__main__":
    import sys

    file_path = Path(sys.argv[1])

    try:
        row_count, duration = validate_telemetry_file(file_path)
    except (OSError, ValueError) as error:
        print(f"Validation failed: {error}")
        raise SystemExit(1)

    print("Telemetry validation passed. ")
    print(f"Rows: {row_count}")
    print(f"Duration: {duration:.2f} seconds")