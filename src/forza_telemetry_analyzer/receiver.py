from __future__ import annotations

import socket

from forza_telemetry_analyzer.parser import PacketParseError, parse_packet

HOST = "0.0.0.0"
PORT = 5300
BUFFER_SIZE = 2048

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

            print(f"{telemetry_packet.timestamp_ms} ms |"
            # .0f: float to integer the number of decimal places
            f"RPM: {telemetry_packet.current_engine_rpm:.0f} |"
            f"Speed X : {telemetry_packet.velocity_x:.2f}"
            )
        
if __name__ == "__main__":
    receive_packets()