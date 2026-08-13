#Testing the unpacking the packet data into a tuple of values
import struct

import pytest

from forza_telemetry_analyzer.models import TelemetryData
from forza_telemetry_analyzer.parser import parse_packet


def test_parse_packet_returns_telemetry_data() -> None:
    packet_data = struct.pack(
        "<iIfffffffffffffffffffffffffffiiiiiiiiffffffffffffffffIIIIIIffffffff",
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
        5.2,
        2.5,
        3.5,
        4.2,
        3.6,
        2.1,
        1.5,
        4.5,
        1.00,
        0.50,
        0.75,
        1.00,
        1.0,
        2.0,
        3.4,
        2.6,
        1235,
        3,
        700,
        2,
        4,
        2,
        5.23,
        2.60,
        0.50,
        0.10,
        0.00,
        250.25,
        150.15,
        100.25,
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
        surface_rumble_front_left = 5.2,
        surface_rumble_front_right = 2.5,
        surface_rumble_rear_left = 3.5,
        surface_rumble_rear_right = 4.2,
        tire_slip_angle_front_left = 3.6,
        tire_slip_angle_front_right = 2.1,
        tire_slip_angle_rear_left = 1.5,
        tire_slip_angle_rear_right = 4.5,
        tire_combined_slip_front_left = 1.00,
        tire_combined_slip_front_right = 0.50,
        tire_combined_slip_rear_left = 0.75,
        tire_combined_slip_rear_right = 1.00,
        suspension_travel_meters_front_left = 1.0,
        suspension_travel_meters_front_right = 2.0,
        suspension_travel_meters_rear_left = 3.4,
        suspension_travel_meters_rear_right = 2.6,
        car_ordinal = 1235,
        car_class = 3,
        car_performance_index = 700,
        drivetrain_type = 2,
        num_cylinders = 4,
        car_group = 2,
        smashable_vel_diff = 5.23,
        smashable_mass = 2.60,
        position_x = 0.50,
        position_y = 0.10,
        position_z = 0.00,
        speed = 250.25,
        power = 150.15,
        torque = 100.25,

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
    assert result.wheel_in_puddle_front_left == expected_data.wheel_in_puddle_front_left
    assert result.wheel_in_puddle_front_right == expected_data.wheel_in_puddle_front_right
    assert result.wheel_in_puddle_rear_left == expected_data.wheel_in_puddle_rear_left
    assert result.wheel_in_puddle_rear_right == expected_data.wheel_in_puddle_rear_right
    assert result.surface_rumble_front_left == pytest.approx(expected_data.surface_rumble_front_left)
    assert result.surface_rumble_front_right == pytest.approx(expected_data.surface_rumble_front_right)
    assert result.surface_rumble_rear_left == pytest.approx(expected_data.surface_rumble_rear_left)
    assert result.surface_rumble_rear_right == pytest.approx(expected_data.surface_rumble_rear_right)
    assert result.tire_slip_angle_front_left == pytest.approx(expected_data.tire_slip_angle_front_left)
    assert result.tire_slip_angle_front_right == pytest.approx(expected_data.tire_slip_angle_front_right)
    assert result.tire_slip_angle_rear_left == pytest.approx(expected_data.tire_slip_angle_rear_left)
    assert result.tire_slip_angle_rear_right == pytest.approx(expected_data.tire_slip_angle_rear_right)
    assert result.tire_combined_slip_front_left == pytest.approx(expected_data.tire_combined_slip_front_left)
    assert result.tire_combined_slip_front_right == pytest.approx(expected_data.tire_combined_slip_front_right)
    assert result.tire_combined_slip_rear_left == pytest.approx(expected_data.tire_combined_slip_rear_left)
    assert result.tire_combined_slip_rear_right == pytest.approx(expected_data.tire_combined_slip_rear_right)
    assert result.suspension_travel_meters_front_left == pytest.approx(expected_data.suspension_travel_meters_front_left)
    assert result.suspension_travel_meters_front_right == pytest.approx(expected_data.suspension_travel_meters_front_right)
    assert result.suspension_travel_meters_rear_left == pytest.approx(expected_data.suspension_travel_meters_rear_left)
    assert result.suspension_travel_meters_rear_right == pytest.approx(expected_data.suspension_travel_meters_rear_right)
    assert result.car_ordinal == expected_data.car_ordinal
    assert result.car_class == expected_data.car_class
    assert result.car_performance_index == expected_data.car_performance_index
    assert result.drivetrain_type == expected_data.drivetrain_type
    assert result.num_cylinders == expected_data.num_cylinders
    assert result.car_group == expected_data.car_group
    assert result.position_x == pytest.approx(expected_data.position_x)
    assert result.position_y == pytest.approx(expected_data.position_y)
    assert result.position_z == pytest.approx(expected_data.position_z)








