import struct

from forza_telemetry_analyzer.models import TelemetryData

#forza UDP Sled packet layout.
#We currently parse the fields need by telemetryData

_PACKET_FORMAT = "<IfffB"
_PACKET_SIZE = struct.calcsize(_PACKET_FORMAT)

class PacketParseError(ValueError):
    """Raised when a Forza telemetry packet cannot be parsed correctly"""

def parse_packet(data : bytes) -> TelemetryData:
    """Parse a Forza telemetry packet into a TelemetryData object.

    Args:
        data (bytes): Raw telemetry packet bytes.

    Returns:
        TelemetryData: The parsed telemetry data.

    Raises:
        PacketParseError: If the packet cannot be parsed correctly.
    """
    if len(data) != _PACKET_SIZE:
        raise PacketParseError(
            f"Packet is too short: expected at least {_PACKET_SIZE} bytes, "
            f"got {len(data)}"
        )
    (
        timestamp_ms,
        current_engine_rpm,
        velocity_x,
        throttle,
        gear,
    ) = struct.unpack(_PACKET_FORMAT, data)

    return TelemetryData(
        timestamp_ms = timestamp_ms,
        current_engine_rpm = current_engine_rpm,
        velocity_x = velocity_x,
        throttle = throttle,
        gear = gear,
    )
  