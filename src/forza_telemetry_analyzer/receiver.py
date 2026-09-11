from __future__ import annotations

import asyncio
from pathlib import Path

from forza_telemetry_analyzer.models import TelemetryData
from forza_telemetry_analyzer.parser import PacketParseError, parse_packet
from forza_telemetry_analyzer.recorder import write_telemetry

HOST = "0.0.0.0"
PORT = 5300
OUTPUT_FILE = Path("telemetry.csv")


class TelemetryProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None:
        packet = process_packet(data, addr)
        if packet is None:
            return
        write_telemetry(OUTPUT_FILE, packet)

        print(
            f"{packet.timestamp_ms} ms |"
            f"RPM: {packet.current_engine_rpm:.0f} |"
            f"Speed X : {packet.velocity_x:.2f}"
        )


async def receive_packets() -> None:
    "Listen for packets from the Forza Horizon 6 game"
    loop = asyncio.get_running_loop()
    transport, _protocol = await loop.create_datagram_endpoint(
        lambda: TelemetryProtocol(),
        local_addr=(HOST, PORT),
    )
    print(f"Listening for packets on {HOST}:{PORT}")
    try:
        await asyncio.Event().wait()  # waits until ctrl+c is pressed
    finally:
        print("Shutting down...")
        transport.close()


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
    asyncio.run(receive_packets())
