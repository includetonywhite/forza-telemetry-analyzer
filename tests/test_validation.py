from pathlib import Path

import pytest

from forza_telemetry_analyzer.validation import (
    validate_required_columns,
    validate_telemetry_file,
    validate_timestamps,
)

def create_csv(tmp_path: Path, timestamps: list[int]) -> Path:
    file_path = tmp_path / "telemetry.csv"

    lines = ["timestamp_ms"]
    lines.extend(str(timestamp) for timestamp in timestamps)

    file_path.write_text("\n".join(lines) + "\n")

    return file_path


def test_validate_timestamps_returns_count_and_duration(
    tmp_path: Path,
) -> None:
    file_path = create_csv(tmp_path, [1000, 1016, 1032, 1048])

    row_count, duration = validate_timestamps(file_path)

    assert row_count == 4
    assert duration == pytest.approx(0.048)


def test_validate_timestamps_rejects_empty_file(tmp_path: Path) -> None:
    file_path = tmp_path / "telemetry.csv"
    file_path.write_text("timestamp_ms\n")

    with pytest.raises(ValueError, match="contains no data"):
        validate_timestamps(file_path)


def test_validate_timestamps_rejects_non_increasing_timestamps(
    tmp_path: Path,
) -> None:
    file_path = create_csv(tmp_path, [1000, 1016, 1016, 1048])

    with pytest.raises(
        ValueError,
        match="must not go backward",
    ):
        validate_timestamps(file_path)

def test_validate_required_columns_accepts_valid_csv(
    tmp_path: Path,
) -> None:
    file_path = tmp_path / "telemetry.csv"

    file_path.write_text(
        "timestamp_ms,engine_max_rpm,current_engine_rpm,"
        "acceleration_x,acceleration_y,acceleration_z,"
        "speed,power,torque,boost,fuel\n"
        "1000,8000,700,0,0,0,10,100,200,5,50\n"
    )

    validate_required_columns(file_path)

def test_validate_required_columns_rejects_missing_columns(
    tmp_path: Path, 
) -> None:
    file_path = tmp_path / "telemetry.csv"

    file_path.write_text(
        "timestamp_ms,engine_max_rpm,current_engine_rpm,"
        "acceleration_x,acceleration_y,acceleration_z,"
        "speed,power,boost,fuel\n"
    )
    
    with pytest.raises(
        ValueError,
        match = "Missing required telemetry columns: torque",
    ):
        validate_required_columns(file_path)

def test_validate_telemetry_file_returns_summary(tmp_path : Path) -> None:
    file_path = tmp_path / "telemetry.csv"
    file_path.write_text(
        "timestamp_ms,engine_max_rpm,current_engine_rpm,"
        "acceleration_x,acceleration_y,acceleration_z,"
        "speed,power,torque,boost,fuel\n"
        "1000,8000,700,0,0,0,10,100,200,5,50\n"
        "1016,8000,800,0,0,0,12,110,210,5,49\n"
    )

    row_count, duration = validate_telemetry_file(file_path)

    assert row_count == 2
    assert duration == pytest.approx(0.016)

