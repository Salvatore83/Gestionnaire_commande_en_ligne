
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

###########################################################################################################################################
#
#           f_creer_serveur()
#
#       para : aucun
#
#       do :
#           creer le serveur
#
#       return : socket serveur
#
###########################################################################################################################################

def f_creer_serveur():

    socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = ''
    port = 5566

    socket_serveur.bind((host, port))

    return socket_serveur



###########################################################################################################################################
#
#           f_accepter_connexion()
#
#       para : socket serveur
#
#       do :
#           attend une connexion et l'accepte
#
#       return : socket client
#
###########################################################################################################################################


def f_accepter_connexion(para_socket_serveur):

    para_socket_serveur.listen(3)
    socket_client, adresse = para_socket_serveur.accept()

    print('Une connexion a eut lieu {}'.format(adresse[0]))

    return socket_client


###########################################################################################################################################
#
#           f_envoyer_message()
#
#       para : socket client et message
#
#       do :
#           envoie le message au socket client
#
#       return : rien
#
###########################################################################################################################################

def f_envoyer_message(para_socket_client, para_message):

    message = message.encode('utf8')
    para_socket_client.send(message)

###########################################################################################################################################
#
#           f_attendre_robot_pres()
#
#       para : socket serveur
#
#       do :
#           attend que le robot soit pres
#
#       return : rien
#
###########################################################################################################################################

def f_attendre_robot_pret(para_socket_serveur):

    message = '0'

    while message != '1':

        message = para_socket_serveur.recv(1024)
        message = message.decode('utf8')

    print('robot pret')


def fermer_socket(para_socket):
    para_socket.close()
