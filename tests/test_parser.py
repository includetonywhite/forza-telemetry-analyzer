#Testing the unpacking the packet data into a tuple of values
import struct

import pytest

from forza_telemetry_analyzer.models import TelemetryData
from forza_telemetry_analyzer.parser import parse_packet


def test_parse_packet_returns_telemetry_data() -> None:
    packet_data = struct.pack(
        "<IfffB",
        123456,
        4521.7,
        32.4,
        0.87,
        4
    )
    expected_data = TelemetryData(
        timestamp_ms=123456,
        current_engine_rpm=4521.7,
        velocity_x=32.4,
        throttle=0.87,
        gear=4,
    )
    result = parse_packet(packet_data)
    
    assert result.timestamp_ms == expected_data.timestamp_ms
    assert result.current_engine_rpm == pytest.approx(expected_data.current_engine_rpm)
    assert result.velocity_x == pytest.approx(expected_data.velocity_x)
    assert result.throttle == pytest.approx(expected_data.throttle)
    assert result.gear == expected_data.gear