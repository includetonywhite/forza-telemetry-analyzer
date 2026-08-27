from __future__ import annotations

import socket
from pathlib import Path

from forza_telemetry_analyzer.models import TelemetryData
from forza_telemetry_analyzer.parser import PacketParseError, parse_packet
from forza_telemetry_analyzer.recorder import write_telemetry

HOST = "0.0.0.0"
PORT = 5300
BUFFER_SIZE = 2048
OUTPUT_FILE = Path("telemetry.csv")


def receive_packets() -> None:
    "Listen for packets from the Forza Horizon 6 game"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        print(f"Listening for packets on {HOST}:{PORT}")
        while True:
            data, address = sock.recvfrom(BUFFER_SIZE)

            try:
                telemetry_packet = process_packet(data, address)

                if telemetry_packet is None:
                    continue
            except PacketParseError as ERROR:
                print(f"Invalid packet received from {address[0]}: {ERROR}")
                continue

            write_telemetry(OUTPUT_FILE, telemetry_packet)
            print(
                f"{telemetry_packet.timestamp_ms} ms |"
                f"RPM: {telemetry_packet.current_engine_rpm:.0f} |"
                f"Speed X : {telemetry_packet.velocity_x:.2f}"
            )


def process_packet(
    data: bytes,
    address: tuple[str, int],
) -> TelemetryData | None:

    try:
        telemetry_packet = parse_packet(data)
    except PacketParseError as error:
        print(f"Invalid packet received from {address[0]}: {error}")
        return None

    return telemetry_packet


if __name__ == "__main__":
    receive_packets()
