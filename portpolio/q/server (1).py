import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 4444
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Connection Established: {address[0]} : {address[1]} ")

        string = client.recv(1024)
        string = string.decode("utf-8")
        print(string)

        # string = string.upper()
        # client.send(bytes(string, "utf-8"))

        
        path = "q\qwe (1).txt"
        file = open(path , 'rb')
        line = file.read(1024)
        while (line):
            client.send(line)
            line = file.read(1024)

        file.close()
        print('File has been transferred successfully.')
        client.close()