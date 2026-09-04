import csv
import struct
from pathlib import Path

import pytest

from forza_telemetry_analyzer.models import TelemetryData
from forza_telemetry_analyzer.parser import _PACKET_FORMAT
from forza_telemetry_analyzer.receiver import process_packet
from forza_telemetry_analyzer.recorder import FIELD_NAMES, write_telemetry


def create_test_telemetry() -> TelemetryData:
    return TelemetryData(
        is_race_on=1,
        timestamp_ms=123456,
        engine_max_rpm=8000.0,
        engine_idle_rpm=1000.0,
        current_engine_rpm=4521.7,
        acceleration_x=0.0,
        acceleration_y=0.1,
        acceleration_z=0.3,
        velocity_x=32.4,
        velocity_y=1.5,
        velocity_z=0.0,
        angular_velocity_x=1.0,
        angular_velocity_y=2.0,
        angular_velocity_z=3.0,
        yaw=1.5,
        pitch=3.0,
        roll=0.0,
        normalized_suspension_travel_front_left=0.2,
        normalized_suspension_travel_front_right=0.4,
        normalized_suspension_travel_rear_left=0.6,
        normalized_suspension_travel_rear_right=0.8,
        tire_slip_ratio_front_left=0.0,
        tire_slip_ratio_front_right=0.1,
        tire_slip_ratio_rear_left=0.2,
        tire_slip_ratio_rear_right=0.3,
        wheel_rotation_speed_front_left=1.05,
        wheel_rotation_speed_front_right=1.07,
        wheel_rotation_speed_rear_left=2.00,
        wheel_rotation_speed_rear_right=2.02,
        wheel_on_rumble_strip_front_left=1,
        wheel_on_rumble_strip_front_right=0,
        wheel_on_rumble_strip_rear_left=1,
        wheel_on_rumble_strip_rear_right=0,
        wheel_in_puddle_front_left=1,
        wheel_in_puddle_front_right=0,
        wheel_in_puddle_rear_left=1,
        wheel_in_puddle_rear_right=0,
        surface_rumble_front_left=5.2,
        surface_rumble_front_right=2.5,
        surface_rumble_rear_left=3.5,
        surface_rumble_rear_right=4.2,
        tire_slip_angle_front_left=3.6,
        tire_slip_angle_front_right=2.1,
        tire_slip_angle_rear_left=1.5,
        tire_slip_angle_rear_right=4.5,
        tire_combined_slip_front_left=1.00,
        tire_combined_slip_front_right=0.50,
        tire_combined_slip_rear_left=0.75,
        tire_combined_slip_rear_right=1.00,
        suspension_travel_meters_front_left=1.0,
        suspension_travel_meters_front_right=2.0,
        suspension_travel_meters_rear_left=3.4,
        suspension_travel_meters_rear_right=2.6,
        car_ordinal=1235,
        car_class=3,
        car_performance_index=700,
        drivetrain_type=2,
        num_cylinders=4,
        car_group=2,
        smashable_vel_diff=5.23,
        smashable_mass=2.60,
        position_x=0.50,
        position_y=0.10,
        position_z=0.00,
        speed=250.25,
        power=150.15,
        torque=100.25,
        tire_temp_front_left=100.5,
        tire_temp_front_right=100.2,
        tire_temp_rear_left=50.2,
        tire_temp_rear_right=50.5,
        boost=18,
        fuel=0.31,
        distance_traveled=100,
        best_lap=1.20,
        last_lap=2.12,
        current_lap=4,
        current_race_time=0.40,
        lap_number=1,
        race_position=5,
        accel=100,
        brake=150,
        clutch=200,
        hand_brake=250,
        gear=1,
        steer=0,
        normalized_driving_line=100,
        normalized_ai_brake_difference=-50,
    )


def test_write_telemetry_create_csv(tmp_path: Path) -> None:
    file_path = tmp_path / "telemetry.csv"
    telemetry = create_test_telemetry()

    write_telemetry(file_path, telemetry)

    assert file_path.exists()


def test_write_telemetry_writes_header_and_data(tmp_path: Path) -> None:
    file_path = tmp_path / "telemetry.csv"
    telemetry = create_test_telemetry()

    write_telemetry(file_path, telemetry)

    with file_path.open(newline="") as file:
        reader = csv.DictReader(file)
        row = list(reader)

    assert len(row) == 1


def test_write_telemetry_appends_data(tmp_path: Path) -> None:
    file_path = tmp_path / "telemetry.csv"
    telemetry = create_test_telemetry()

    write_telemetry(file_path, telemetry)
    write_telemetry(file_path, telemetry)

    with file_path.open(newline="") as file:
        reader = csv.DictReader(file)
        row = list(reader)
    assert len(row) == 2
    assert reader.fieldnames == FIELD_NAMES

    assert row[0]["timestamp_ms"] == "123456"
    assert row[0]["engine_max_rpm"] == "8000.0"
    assert row[0]["current_engine_rpm"] == "4521.7"
    assert row[0]["acceleration_x"] == "0.0"
    assert row[0]["acceleration_y"] == "0.1"
    assert row[0]["acceleration_z"] == "0.3"
    assert row[0]["tire_slip_ratio_front_left"] == "0.0"
    assert row[0]["tire_slip_ratio_front_right"] == "0.1"
    assert row[0]["tire_slip_ratio_rear_left"] == "0.2"
    assert row[0]["tire_slip_ratio_rear_right"] == "0.3"
    assert row[0]["normalized_suspension_travel_front_left"] == "0.2"
    assert row[0]["normalized_suspension_travel_front_right"] == "0.4"
    assert row[0]["normalized_suspension_travel_rear_left"] == "0.6"
    assert row[0]["normalized_suspension_travel_rear_right"] == "0.8"
    assert row[0]["suspension_travel_meters_front_left"] == "1.0"
    assert row[0]["suspension_travel_meters_front_right"] == "2.0"
    assert row[0]["suspension_travel_meters_rear_left"] == "3.4"
    assert row[0]["suspension_travel_meters_rear_right"] == "2.6"
    assert row[0]["speed"] == "250.25"
    assert row[0]["power"] == "150.15"
    assert row[0]["torque"] == "100.25"
    assert row[0]["boost"] == "18"
    assert row[0]["fuel"] == "0.31"


def test_process_packet_returns_telemetry(tmp_path: Path) -> None:
    values: list[int | float] = [0] * 88

    values[0] = 1
    values[1] = 123456
    values[4] = 4521.7
    values[5] = 0.1
    values[6] = 0.2
    values[7] = 0.3
    values[8] = 0.0

    packet_data = struct.pack(_PACKET_FORMAT, *values)

    address = ("10.0.0.149", 5300)

    result = process_packet(
        packet_data,
        address,
    )

    assert result is not None

    assert result.timestamp_ms == 123456
    assert result.current_engine_rpm == pytest.approx(4521.7)
    assert result.acceleration_x == pytest.approx(0.1)
    assert result.tire_slip_ratio_front_left == pytest.approx(0.0)
