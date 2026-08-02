from _future_ import annotations

import socket

HOST = "0.0.0.0"
PORT = 5300
BUFFER_SIZE = 2048

Def receive_packets() -> None:
    "Listen for packets from the Forza Horizon 5 game
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        s.bind((HOST, PORT))
        print(f"Listening for packets on {HOST}:{PORT}")
        while True:
            data, address = sock.recvfrom(BUFFER_SIZE)

            print(f"Received {len(data)} bytes packet from {address[0]}: {data[1]}")
        
if __name__ == "__main__":
    receive_packets()