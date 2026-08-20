from __future__ import annotations

import socket
from pathlib import Path

from forza_telemetry_analyzer.parser import PacketParseError, parse_packet
from forza_telemetry_analyzer.recorder import write_telemetry
from forza_telemetry_analyzer.models import TelemetryData

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
                telemetry_packet = parse_packet(data)
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
    address: tuple[str,int],
) -> TelemetryData | None:

if __name__ == "__main__":
    receive_packets()
