import csv
from pathlib import Path

from forza_telemetry_analyzer.models import TelemetryData

FIELD_NAMES = [
    "timestamp_ms",
    "engine_max_rpm",
    "current_engine_rpm",
    "acceleration_x",
    "acceleration_y",
    "acceleration_z",
    "tire_slip_ratio_front_left",
    "tire_slip_ratio_front_right",
    "tire_slip_ratio_rear_left",
    "tire_slip_ratio_rear_right",
    "normalized_suspension_travel_front_left",
    "normalized_suspension_travel_front_right",
    "normalized_suspension_travel_rear_left",
    "normalized_suspension_travel_rear_right",
    "suspension_travel_meters_front_left",
    "suspension_travel_meters_front_right",
    "suspension_travel_meters_rear_left",
    "suspension_travel_meters_rear_right",
    "speed",
    "power",
    "torque",
    "boost",
    "fuel",
]


def write_telemetry(
    file_path: Path,
    telemetry: TelemetryData,
) -> None:
    file_exists = (file_path.exists(),)

    with file_path.open("a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=FIELD_NAMES,
            extrasaction="ignore",
        )

        if not file_exists or file_path.stat().st_size == 0:
            writer.writeheader()

        writer.writerow(vars(telemetry))
