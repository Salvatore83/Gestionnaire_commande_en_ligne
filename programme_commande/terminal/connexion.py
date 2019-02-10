
###########################################################################################################################################
#
# Module de connexion du gestionnaire de commande
#
# Permet au gestionnaire de commande de creer le serveur et de communiquer avec le robot connecte
#
###########################################################################################################################################

#
# IMPORTS
#

import socket

def f_afficher_utilisation_socket():
    print('utilisation du module connexion, socket')


###########################################################################################################################################
#
#           f_creer_serveur()
#
#       para : aucun
#
#       do:
#           creer le socket serveur et ecrit l'adresse IP dans un fichier texte (connexion ainsi plus facile)
#
#       return : socket_serveur
#
###########################################################################################################################################

def f_creer_serveur():

    #
    # Creer le socket serveur
    #
    socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = ''
    port = 5566

    #
    # Attribut l'host et le port au socket serveur
    #
    socket_serveur.bind((host, port))

    print('socket serveur cree avec succes')
    return socket_serveur

###########################################################################################################################################
#
#           f_accepter_client()
#
#       para : socket_serveur
#
#       do :
#           attend une connxion et cree le socket client
#
###########################################################################################################################################

def f_accepter_client(para_socket_serveur):
    #
    # Attend la demande de connexion 3 echecs possible
    #
    para_socket_serveur.listen(3)

    #
    # Accepte la demande de connexion
    #
    socket_client, adresse = para_socket_serveur.accept()

    print('Un client vient de se connecter, {}'.format(adresse[0]))
    return socket_client, adresse


###########################################################################################################################################
#
#           f_attendre_message()
#
#       para : socket client
#
#       do :
#           attend un message du client et le decode
#
#       return : message du client (msg_client)
#
###########################################################################################################################################

def f_attendre_message(para_socket_client):
    #
    # Attend le message du client avec un maximum de 1024
    #
    msg_client = para_socket_client.recv(1024)

    #
    # Decode le message avec la clef de decodage 'utf8'
    #
    msg_client = msg_client.decode('utf8')

    return msg_client


###########################################################################################################################################
#
#           f_attendre_message()
#
#       para : socket client, message
#
#       do :
#           envoie un message au socket client
#
#       return : rien
#
###########################################################################################################################################

def f_envoyer_message(para_socket_client, para_message):
    #
    # Encode le message en utf8
    #
    para_message = para_message.encode('utf8')
    #
    # Envoie du message
    #
    para_socket_client.send(para_message)




###########################################################################################################################################
#
#           f_fermer_serveur()
#
#       para : socket_serveur, socket_client
#
#       do :
#               ferme les sockets / conenxions
#
#       return : rien
#
###########################################################################################################################################


def f_fermer_serveur(para_socket_serveur, para_socket_client):
    #
    # Ferme le socket serveur
    #
    para_socket_serveur.close()

    #
    # Ferme le socket client
    #
    para_socket_client.close()
