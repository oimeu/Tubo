import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def run(host, port): 
    server.bind(('192.168.0.104', 19200))
    server.listen(1)

    connection, address = server.accept()
    namefile = connection.recv(1024).decode()

    with open(namefile, 'rb') as file:
        for data in file.readlines():
            connection.send(data)

        print('Arquivo enviado')
