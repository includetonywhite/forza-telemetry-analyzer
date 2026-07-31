from dataclasses import dataclass


@dataclass(frozen=True)
class TelemetryData:
    """A dataclass representing a telemetry sample."""
    timestamp_ms: int
    engine_max_rpm: float
    engine_idle_rpm: float
    current_engine_rpm: float
    acceleration_x: float
    acceleration_y: float
    acceleration_z: float
    velocity_x: float
    velocity_y: float
    velocity_z: float
    throttle: float
    brake: float
    steering: float
    gear: int
