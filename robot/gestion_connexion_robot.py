
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
import time

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
    #
    # Tant que le robot n'envoie pas 1, il n'est pas pret
    #
    while message != '1':
        #
        # Reception du message par le socket
        #
        message = para_socket_client.recv(1024)
        #
        # Decodage du message (utf8)
        #
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

    #
    # Encodage du message en utf8
    #
    message = para_message.encode('utf8')
    #
    # Envoie du message via le socket
    #
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
    #
    # Tant que l'initialisation des capteurs n'est pas valide
    #
    while initialisation != 'Succes' and initialisation != 'Erreur':
        #
        # Gere l'initialisation des capteurs
        #
        initialisation = COMrob.f_initialisation_capteurs()

    #
    # Lorsque l'initialisation des capteurs s'est faite avec succes, envoie du message Robot pret, via le socket
    #
    f_envoyer_message(para_socket_client, initialisation)
    if initialisation == 'Erreur':
        time.sleep(1)
        f_robot_initialisation(para_socket_client)




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

    #
    # Defini l'action du robot a True
    #
    action_robot = True

    #
    # Tant que l'action robot n'est pas egale a False
    #
    while action_robot != False:
        #
        # Recoit un message via le socket
        #
        message = para_socket_client.recv(1024)
        #
        # Decode le message et le sauvegarde dans une variable (utf8)
        #
        message = message.decode('utf8')
        #
        # Si le message est egal a quitter, quitte le programme
        #
        if message == 'quitter':
            action_robot = False
        #
        # Sinon executer l'action
        #
        else:
            #
            # Envoie au gestionnaire qu'il a bien recut la commande
            #
            f_envoyer_message(para_socket_client, 'Bien reçut')
            #
            # Le robot execute l'action
            #
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

def fermer_socket(para_socket):
    #
    # Ferme le socket
    #
    para_socket.close()
