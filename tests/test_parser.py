#Testing the unpacking the packet data into a tuple of values
import struct

import pytest

from forza_telemetry_analyzer.models import TelemetryData
from forza_telemetry_analyzer.parser import parse_packet


def test_parse_packet_returns_telemetry_data() -> None:
    packet_data = struct.pack(
        "<iIfffffffffffffffffffffffffffiiiiiiii",
        1,
        123456,
        8000.0,
        1000.0,
        4521.7,
        0.1,
        0.2,
        0.3,
        32.4,
        1.5,
        0.0,
        1.0,
        2.0,
        3.0,
        1.5,
        3.0,
        0.0,        
        0.2,
        0.4,
        0.6,
        0.8,
        0.0,
        0.1,
        0.2,
        0.3,
        1.05,
        1.07,
        2.00,
        2.02,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
#        tire_slip_ratio_front_left,
#        tire_slip_ratio_front_right,
#        tire_slip_ratio_rear_left,
#        tire_slip_ratio_rear_right,
#        wheel_rotation_speed_front_left,
#        wheel_rotation_speed_front_right,
#        wheel_rotation_speed_rear_left,
#        wheel_rotation_speed_rear_right,
#        wheel_on_rumble_strip_front_left,
#        wheel_on_rumble_strip_front_right,
#        wheel_on_rumble_strip_rear_left,
#        wheel_on_rumble_strip_rear_right,
#        wheel_in_puddle_front_left,
#        wheel_in_puddle_front_right,
#        wheel_in_puddle_rear_left,
#        wheel_in_puddle_rear_right,
#        surface_rumble_front_left,
#        surface_rumble_front_right,
#        surface_rumble_rear_left,
#        surface_rumble_rear_right,
#        tire_slip_angle_front_left,
#        tire_slip_angle_front_right,
#        tire_slip_angle_rear_left,
#        tire_slip_angle_rear_right,
#        tire_combined_slip_front_left,
#        tire_combined_slip_front_right,
#        tire_combined_slip_rear_left,
#        tire_combined_slip_rear_right,
#        1.0,
#        2.0,
#        3.4,
#        2.6,
#        car_ordinal,
#        car_class,
#        car_performance_index,
#        drivetrain_type,
#        num_cylinders,
#        car_group,
#        smashable_vel_diff,
#        smashable_mass,
#        position_x,
#        position_y,
#        position_z,
#        speed,
#        power,
#        torque,
#        tire_temp_front_left,
#        tire_temp_front_right,
#        tire_temp_rear_left,
#        tire_temp_rear_right,
#        boost,
#        fuel,
#        distance_traveled,
#        best_lap,
#        last_lap,
#        current_lap,
#        current_race_time,
#        lap_number,
#        race_position,
#        accel,
#        brake,
#        clutch,
#        hand_brake,
#        gear,
#        steer,
#        normalized_driving_line,
#        normalized_ai_brake_difference,
    )
    expected_data = TelemetryData(
        is_race_on = 1,
        timestamp_ms = 123456,
        engine_max_rpm = 8000.0,
        engine_idle_rpm = 1000,
        current_engine_rpm = 4521.7,
        acceleration_x = 0.1,
        acceleration_y = 0.2,
        acceleration_z = 0.3,
        velocity_x = 32.4,
        velocity_y = 1.5,
        velocity_z = 0.0,
        angular_velocity_x = 1.0,
        angular_velocity_y = 2.0,
        angular_velocity_z = 3.0,
        yaw = 1.5,
        pitch = 3.0,
        roll = 0.0,
        normalized_suspension_travel_front_left = 0.2,
        normalized_suspension_travel_front_right = 0.4,
        normalized_suspension_travel_rear_left = 0.6,
        normalized_suspension_travel_rear_right = 0.8,
        tire_slip_ratio_front_left = 0.0,
        tire_slip_ratio_front_right = 0.1,
        tire_slip_ratio_rear_left = 0.2,
        tire_slip_ratio_rear_right = 0.3,
        wheel_rotation_speed_front_left = 1.05,
        wheel_rotation_speed_front_right = 1.07,
        wheel_rotation_speed_rear_left = 2.00,
        wheel_rotation_speed_rear_right = 2.02,
        wheel_on_rumble_strip_front_left = 1,
        wheel_on_rumble_strip_front_right = 0,
        wheel_on_rumble_strip_rear_left = 1,
        wheel_on_rumble_strip_rear_right = 0,
        wheel_in_puddle_front_left = 1,
        wheel_in_puddle_front_right = 0,
        wheel_in_puddle_rear_left = 1,
        wheel_in_puddle_rear_right = 0,
#        suspension_travel_meters_front_left = 1.0,
#        suspension_travel_meters_front_right = 2.0,
#        suspension_travel_meters_rear_left = 3.4,
#        suspension_travel_meters_rear_right = 2.6,
    )
    result = parse_packet(packet_data)
    
    assert result.is_race_on == expected_data.is_race_on
    assert result.timestamp_ms == expected_data.timestamp_ms
    assert result.engine_max_rpm == pytest.approx(expected_data.engine_max_rpm)
    assert result.engine_idle_rpm == pytest.approx(expected_data.engine_idle_rpm)
    assert result.current_engine_rpm == pytest.approx(expected_data.current_engine_rpm)
    assert result.acceleration_x == pytest.approx(expected_data.acceleration_x)
    assert result.acceleration_y == pytest.approx(expected_data.acceleration_y)
    assert result.acceleration_z == pytest.approx(expected_data.acceleration_z)
    assert result.velocity_x == pytest.approx(expected_data.velocity_x)
    assert result.velocity_y == pytest.approx(expected_data.velocity_y)
    assert result.velocity_z == pytest.approx(expected_data.velocity_z)
    assert result.angular_velocity_x == pytest.approx(expected_data.angular_velocity_x)
    assert result.angular_velocity_y == pytest.approx(expected_data.angular_velocity_y)
    assert result.angular_velocity_z == pytest.approx(expected_data.angular_velocity_z)
    assert result.yaw == pytest.approx(expected_data.yaw)
    assert result.pitch == pytest.approx(expected_data.pitch)
    assert result.roll == pytest.approx(expected_data.roll)
    assert result.normalized_suspension_travel_front_left == pytest.approx(expected_data.normalized_suspension_travel_front_left)
    assert result.normalized_suspension_travel_front_right == pytest.approx(expected_data.normalized_suspension_travel_front_right)
    assert result.normalized_suspension_travel_rear_left == pytest.approx(expected_data.normalized_suspension_travel_rear_left)
    assert result.normalized_suspension_travel_rear_right == pytest.approx(expected_data.normalized_suspension_travel_rear_right)
    assert result.tire_slip_ratio_front_left == pytest.approx(expected_data.tire_slip_ratio_front_left)
    assert result.tire_slip_ratio_front_right == pytest.approx(expected_data.tire_slip_ratio_front_right)
    assert result.tire_slip_ratio_rear_left == pytest.approx(expected_data.tire_slip_ratio_rear_left)
    assert result.tire_slip_ratio_rear_right == pytest.approx(expected_data.tire_slip_ratio_rear_right)
    assert result.wheel_rotation_speed_front_left == pytest.approx(expected_data.wheel_rotation_speed_front_left)
    assert result.wheel_rotation_speed_front_right == pytest.approx(expected_data.wheel_rotation_speed_front_right)
    assert result.wheel_rotation_speed_rear_left == pytest.approx(expected_data.wheel_rotation_speed_rear_left)
    assert result.wheel_rotation_speed_rear_right == pytest.approx(expected_data.wheel_rotation_speed_rear_right)
    assert result.wheel_on_rumble_strip_front_left == expected_data.wheel_on_rumble_strip_front_left
    assert result.wheel_on_rumble_strip_front_right == expected_data.wheel_on_rumble_strip_front_right
    assert result.wheel_on_rumble_strip_rear_left == expected_data.wheel_on_rumble_strip_rear_left
    assert result.wheel_on_rumble_strip_rear_right == expected_data.wheel_on_rumble_strip_rear_right








