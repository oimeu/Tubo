import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(host, port):
    client.connect((host, port))

    print('connection')

    while True:
        console = str(input('tubo ({})> '.format(host)))

        parameter = console.split()
        parameter0 = parameter[0]
        parameter1 = parameter[1]

        namefile = parameter1
        match parameter0:
            case "send":
                connection, address = server.accept()
                namefile = connection.recv(1024).decode()

                with open(namefile, 'rb') as file:
                    for data in file.readlines():
                        connection.send(data)
            case "push":
                client.send(namefile.encode())
                with open(namefile, 'wb') as file:
                    while 1:
                        data = client.recv(1000000)
                        if not data:
                            break
                        file.write(data)
                        print("eu recebi")
                    
            case _:
                print("error")

