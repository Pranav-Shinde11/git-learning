
import socket

message ="Hello UDP Server"

# bytesToSend = str.encode(msgFromClient)

address = ("127.0.0.1", 20001)

# Create a UDP socket at client side
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send to server using created UDP socket
client.sendto(bytes(message , "utf-8"), address)

msgFromServer = client.recvfrom(1024)

print(f"Message from Server {msgFromServer[0]}")
