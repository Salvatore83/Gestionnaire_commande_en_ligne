###########################################################################################################################################
#
# Module de connexion pour l'interface graphique
#
#
#
#
###########################################################################################################################################

#
# Imports
#

import socket

def f_creer_serveur():
    
    socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = ""
    port = 5566

    socket_serveur.bind((host, port))

    return socket_serveur


def f_accepter_connexion(para_socket_serveur):
    
    para_socket_serveur.listen(3)

    socket_client, adresse = para_socket_serveur.accept()

    print('Une connexion a eut lieu {}'.format(adresse[0]))

    return socket_client

def f_envoyer_message(para_socket_client, para_message):

    message = para_message.encpde("utf8")

    para_socket_client.send(message)

def f_recevoir_message(para_socket_client):

    message = para_socket_client.recv(1024)

    message = message.decode("utf8")

    return message

def f_attendre_robot_pret(para_socket_serveur, para_erreur):

    message = '0'
    #
    # Tant que le robot n'est pas pret
    #
    while message != 'Succes' and message != "Erreur":
        #
        # Attendre message et le decoder
        #
        message = para_socket_serveur.recv(1024)
        message = message.decode('utf8')

    if message == 'Succes':
        print('robot pret')
    else:
        print("Le robot a rencontré un problème.")
        para_erreur += 1
        if para_erreur < 3:
            f_attendre_robot_pret(para_socket_serveur, para_erreur)
        else:
            quit()

def f_gerer_commande(para_socket_serveur, para_socket_client, para_commande):

    #
    # Envoie la commande au socket client (robot)
    #
    f_envoyer_message(para_socket_client, para_commande)

    message = ''
    #
    # Tant que le robot n'a pas reçut le message
    #
    while message != 'Bien reçut':
        message = f_recevoir_message(para_socket_client)

    print('Le robot a bien reçut l action')
    message = ''
    #
    # Tant que le robot n'a pas finit l'action
    #
    while message != 'Action terminee':
        message = f_recevoir_message(para_socket_client)
        print('Le robot execute l action ...')

    print('Le robot a finit l action')

def f_fermer_socket(para_socket):
    #
    # Ferme le socket passe en parametre
    #
    para_socket.close()