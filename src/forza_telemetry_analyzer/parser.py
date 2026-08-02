import struct

from forza_telemetry_analyzer.models import TelemetryData

#forza UDP Sled packet layout.
#We currently parse the fields need by telemetryData

_PACKET_FORMAT = ("<iIffffffffff")
_PACKET_SIZE = struct.calcsize(_PACKET_FORMAT)

class PacketParseError(ValueError):
    """Raised when a Forza telemetry packet cannot be parsed correctly"""

def parse_packet(data: bytes) -> TelemetryData:
    """Parse a Forza telemetry packet into a TelemetryData object.

    Args:
        packet_bytes (bytes): The raw bytes of the telemetry packet.

    Returns:
        TelemetryData: The parsed telemetry data.

    Raises:
        PacketParseError: If the packet cannot be parsed correctly.
    """
    if len(data) < _PACKET_SIZE:
        raise PacketParseError(
            f"Packet is too short: expected at least {_PACKET_SIZE} bytes, "
            f"got {len(data)}"
        )
    (
        is_race_on,
        timestamp_ms,
        engine_max_rpm,
        engine_idle_rpm,
        current_engine_rpm,
        acceleration_x,
        acceleration_y,
        acceleration_z,
        velocity_x,
        velocity_y,
        velocity_z,
        _unused,
    ) = struct.unpack(_PACKET_FORMAT, data)

    if is_race_on not in (0, 1):
        raise PacketParseError(f"Invalid isRaceOn value: {is_race_on}")

    return TelemetryData(
        timestamp_ms=timestamp_ms,
        engine_max_rpm=engine_max_rpm,
        engine_idle_rpm=engine_idle_rpm,
        current_engine_rpm=current_engine_rpm,
        acceleration_x=acceleration_x,
        acceleration_y=acceleration_y,
        acceleration_z=acceleration_z,
        velocity_x=velocity_x,
        velocity_y=velocity_y,
        velocity_z=velocity_z,
        throttle=0.0,  # Placeholder, as throttle is not in the packet
        brake=0.0,     # Placeholder, as brake is not in the packe
        steering=0.0,  # Placeholder, as steering is not in the packet
        gear=0,        # Placeholder, as gear is not in the packet
    )
  