#
# Client, sert a jouer le role du robot sans robot
#
# Pas besoin de commenter du coup


import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect_ex(('localhost', 5566))

message = socket_client.recv(1024)
message.decode('utf8')

print(message)

robot_pret = ''

while robot_pret != 'pret':
    robot_pret = input('Le robot est pret ? [oui/non]')
    if robot_pret == 'oui':
        robot_pret = 'pret'

message = 'Robot pret'
message = message.encode('utf8')
socket_client.send(message)

message = ''

while message != 'quitter':

    commande = socket_client.recv(1024)
    commande = commande.decode()

    if commande == 'avancer':
        print('Le gestionnaire demande au robot d avancer')

    reponse = input('Le message a t il ete reçut [Bien reçut]')
    reponse = reponse.encode('utf8')
    socket_client.send(reponse)

    while reponse != 'Action terminee':
        reponse = input('L action est elle terminee[Action terminee]')
        test = reponse
        reponse = reponse.encode('utf8')
        socket_client.send(reponse)
        reponse = test

socket_client.close()
