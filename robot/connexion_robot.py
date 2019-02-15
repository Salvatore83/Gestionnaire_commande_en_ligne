
###########################################################################################################################################
#
# Module qui gere tout ce qui est connexion au niveau du robot
#
###########################################################################################################################################

#
# Imports
#

import socket

###########################################################################################################################################
#
#           f_creer_socket_client ()
#
#       para : aucun
#
#       do :
#           creer le socket client
#
#       return : socket client
#
###########################################################################################################################################


def f_creer_socket_client():

    #
    # Cree le socket client
    #
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return socket_client

###########################################################################################################################################
#
#           f_connexion_serveur()
#
#       para : para_socket_client
#
#       do :
#           se connecte au serveur
#
#       return : socket client
#
###########################################################################################################################################

def f_connexion_serveur(para_socket_client):

    #
    # Definit l'host et le port (pour la connexion)
    #
    host = ''
    port = 5566

    #
    # Connecte le socket au serveur (host) via le port
    #
    para_socket_client.connect_ex((host, port))

    return para_socket_client

###########################################################################################################################################
#
#           f_attendre_commande_server()
#
#       para : para_socket
#
#       do :
#           attend une commande du serveur
#
#       return : commande
#
###########################################################################################################################################

def f_attendre_commande_server(para_socket):

    commande = para_socket.recv(1024)
    commande = commande.decode('utf8')

    return commande

###########################################################################################################################################
#
#           f_fermer_socket()
#
#       para : para_socket
#
#       do :
#           ferme le para_socket
#
#       return : rien
#
###########################################################################################################################################

def f_fermer_socket(para_socket):

    #
    # ferme le para_socket
    #
    para_socket.close()
