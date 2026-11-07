"""receiver.py - сервер
"""

import socket
import struct

from proto.user_pb2 import UserInfo, Role

# socket.AF_INET - семейство адресов, IPv4 (адрес вида ("127.0.0.1", 5000))
# socket.SOCK_STREAM - тип сокета, именно TCP (в отличие от SOCK_DGRAM — UDP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    try:
        server.bind(("127.0.0.1", 5000))
        server.listen()
        print("Server listening on port 5000!")

        client_socket, client_address = server.accept()
        print(f"Client connect: {client_address}")

        raw_data = client_socket.recv(4096)
        user = UserInfo()
        user.ParseFromString(raw_data[4:])
        print(user.email)

    except ConnectionRefusedError:
        print("Connection or sending error.")

# При выходе из with сокет закроется автоматически (client.close())
