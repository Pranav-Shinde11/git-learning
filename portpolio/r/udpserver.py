
import socket
ip = "127.0.0.1"
port = 20001

msgFromServer = "Hello UDP Client"

# bytesToSend   = str.encode(msgFromServer)

# Create a datagram socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
server.bind((ip, port))
print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    message_AddressPair = server.recvfrom(1024)
    message = message_AddressPair[0]
    address = message_AddressPair[1]

    print(f"Message from Client:{message}")
    print(f"Client IP Address:{address}")

    # Sending a reply to client
    server.sendto(bytes(msgFromServer , "utf-8"), address)