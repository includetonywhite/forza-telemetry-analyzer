from forza_telemetry_analyzer.models import TelemetryData


def test_telemetry_data_model() -> None:
    TelemetryData(
        is_race_on = 1,
        timestamp_ms=123456,
        engine_max_rpm = 8000.0,
        engine_idle_rpm = 1000.0,
        current_engine_rpm=4521.7,
        acceleration_x = 0.0,
        acceleration_y = 0.1,
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
#        suspension_travel_meters_front_left = 1.0,
#        suspension_travel_meters_front_right = 2.0,
#        suspension_travel_meters_rear_left = 3.4,
#        suspension_travel_meters_rear_right = 2.6, 
    )

