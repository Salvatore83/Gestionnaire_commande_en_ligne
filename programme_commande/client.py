import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect_ex(('localhost', 5566))

msg = input('> ')

msg = msg.encode('utf8')
socket_client.send(msg)

message = socket_client.recv(1024)
message = message.decode('utf8')
print(message)

while True:
    msg = input('> ')

    msg = msg.encode('utf8')
    socket_client.send(msg)
