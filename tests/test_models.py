from forza_telemetry_analyzer.models import TelemetryData


def test_telemetry_data_model() -> None:
    TelemetryData(
        timestamp_ms=1000,
#        engine_max_rpm=8000,
#        engine_idle_rpm=1000,
        current_engine_rpm=4500.0,
#        acceleration_x=1.2,
#        acceleration_y=0.1,
#       acceleration_z=0.0,
        velocity_x=30.0,
#        velocity_y=0.0,
#        velocity_z=0.0,
        throttle=0.75,
#        brake=0.0,
#        steering=0.5,
        gear=4,
    )

#    assert sample.timestamp_ms == 1000
#    assert sample.throttle == 0.75
#    assert sample.gear == 3
