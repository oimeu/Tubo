import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.0.104', 19200))

print('connection')

namefile = str(input('Arquivo> '))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
       data = client.recv(1000000)
       if not data:
            break
       file.write(data)

print("eu recebi")
