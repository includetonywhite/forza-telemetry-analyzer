from dataclasses import dataclass


@dataclass(frozen=True)
class TelemetryData:
    """A dataclass representing a telemetry sample."""
    timestamp_ms: int
    current_engine_rpm: float
    velocity_x: float
    throttle: float
    gear: int
