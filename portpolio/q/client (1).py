import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.connect((ip, port))

    string = input("Enter the string: ")
    server.send(bytes(string, "utf-8"))

    

    file = open('q\server (1).py', 'wb')

    line = server.recv(1024)
    print(line)
    while(line):
        file.write(line)
        line = server.recv(1024)

    print('File has been received successfully.')
    
    file.close()