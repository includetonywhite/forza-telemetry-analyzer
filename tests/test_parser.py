
#Testing the unpacking the packet data into a tuple of values
from forza_telemetry_analyzer.parser import parse_packet
from forza_telemetry_analyzer.models import TelemetryData

def test_parse_packet_returns_telemetry_data() -> None:
    packet_data = b"\x8a\x01\x00\x00"
    expected_data = TelemetryData(
        timestamp_ms=123456,
        current_engine_rpm=4521.7,
        velocity_x=0.87,
        throttle=.87,
        gear=4,
    )
    
    result = parse_packet(packet_data)
    assert result == expected_data
    return None