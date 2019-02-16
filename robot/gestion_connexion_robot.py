
###########################################################################################################################################
#
# Module principal de connexion du robot
#
# Premet de gerer la connexion du robot
#
###########################################################################################################################################

#
# IMPORTS
#

import socket
import commandes_robot as COMrob

###########################################################################################################################################
#
#           f_creer_socket()
#
#       para : aucun
#
#       do :
#           creer le socket de connexion du robot
#
#       return : socket client
#
###########################################################################################################################################

def f_creer_socket():

    #
    # Cree le socket client
    #
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return socket_client




###########################################################################################################################################
#
#           f_connecter_socket()
#
#       para : socket client, host et  port
#
#       do :
#           connecte le socket au serveur
#
#       return : socket client
#
###########################################################################################################################################

def f_connecter_socket(para_socket_client, para_host, para_port):

    #
    # Connecte le socket client a l'adresse ip passée via le port
    #
    para_socket_client.connect_ex((para_host, para_port))

    return para_socket_client




###########################################################################################################################################
#
#           f_reponse_connexion()
#
#       para : socket client
#
#       do :
#           attend une reponse positive du gestionnaire pour savoir qu'il a pu se connecté
#
#       return : rien
#
###########################################################################################################################################

def f_reponse_connexion(para_socket_client):

    message = ''

    while message != '1':
        message = para_socket_client.recv(1024)
        message = message.decode('utf8')




###########################################################################################################################################
#
#           f_envoyer_message()
#
#       para : socket client et message
#
#       do :
#           envoie un message via le socket client
#
#       return : rien
#
###########################################################################################################################################

def f_envoyer_message(para_socket_client, para_message):

    message = para_message.encode('utf8')

    para_socket_client.send(message)





###########################################################################################################################################
#
#           f_robot_initialisation()
#
#       para : socket client
#
#       do :
#           Verifie si tous les capteurs sont OK et envoie un message au gestionnaire quand il est pret
#
#       return : rien
#
###########################################################################################################################################

def f_robot_initialisation(para_socket_client):

    initialisation = ''

    while initialisation != 'Succes':
        initialisation = COMrob.f_initialisation_capteurs()

    f_envoyer_message(para_socket_client, 'Robot pret')




###########################################################################################################################################
#
#           f_fermer_socket()
#
#       para : socket client
#
#       do :
#           ferme socket client
#
#       return : rien
#
###########################################################################################################################################

def f_action_robot(para_socket_client):

    action_robot = True

    while action_robot != False:
        message = para_socket_client.recv(1024)
        message = message.decode('utf8')

        if message == 'quitter':
            action_robot = False
        else:
            f_envoyer_message(para_socket_client, 'Bien reçut')
            COMrob.f_gerer_action_robot(para_socket_client, message)


###########################################################################################################################################
#
#           f_fermer_socket()
#
#       para : socket client
#
#       do :
#           ferme socket client
#
#       return : rien
#
###########################################################################################################################################

def fermer_socket(para_socket_client):
    para_socket_client.close()
