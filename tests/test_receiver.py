import struct


import pytest

from forza_telemetry_analyzer.models import TelemetryData
from forza_telemetry_analyzer.parser import _PACKET_FORMAT
from forza_telemetry_analyzer.receiver import process_packet


def test_process_packet_returns_telemetry() -> None:
    values = [0] * 88

    values[0] = 1
    values[1] = 123456
    values[2] = 8000.0
    values[3] = 1000.0
    values[4] = 4521.7
    values[5] = 0.1
    values[6] = 0.2
    values[7] = 0.3
    values[8] = 32.4
    values[9] = 1.5
    values[10] = 0.0

    packet_data = struct.pack(_PACKET_FORMAT, *values)

    address = ("10.0.0.149", 5300)

    result = process_packet(packet_data, address)

    assert isinstance(result, TelemetryData)
    assert result.timestamp_ms == 123456
    assert result.current_engine_rpm == pytest.approx(4521.7)
    assert result.acceleration_x == pytest.approx(0.1)
    assert result.velocity_x == pytest.approx(32.4)
