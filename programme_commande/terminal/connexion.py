
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

    #
    # Creation du socket serveur
    #
    socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = ''
    port = 5566
    #
    # Ajout de l'adresse et du port au socket serveur
    #
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

    #
    # Ecoute des connexions sur l'adresse via le port
    #
    para_socket_serveur.listen(3)
    #
    # Accepte la connexion et retourne un nouveau socket, le socket client ainsi que l'adresse du client
    #
    socket_client, adresse = para_socket_serveur.accept()
    #
    # Affiche un message pour savoir qui vient de se connecter
    #
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
    #
    # Encode le message a envoyer
    #
    message = para_message.encode('utf8')
    #
    # Envoie le message par le socket
    #
    para_socket_client.send(message)



###########################################################################################################################################
#
#           f_recevoir_message()
#
#       para : socket client
#
#       do :
#           attend un message
#
#       return : message
#
###########################################################################################################################################

def f_recevoir_message(para_socket_client):
    #
    # Attend un message via la connexion et le sauvegarde dans la variable message
    #
    message = para_socket_client.recv(1024)
    #
    # Decode le message reçut (utf8)
    #
    message = message.decode('utf8')

    return message




###########################################################################################################################################
#
#           f_attendre_robot_pres()
#
#       para : socket serveur et para_erreur (nombre d'erreur rencontrée)
#
#       do :
#           attend que le robot soit pres
#
#       return : rien
#
###########################################################################################################################################

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


###########################################################################################################################################
#
#           f_gerer_commande()
#
#       para : socket client et commande
#
#       do :
#           envoie une commande au robot et attend qu'il execute l'action
#
#       return : rien
#
###########################################################################################################################################


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

###########################################################################################################################################
#
#           f_fermer_socket()
#
#       para : socket
#
#       do :
#           ferme le socket
#
#       return : rien
#
###########################################################################################################################################


def f_fermer_socket(para_socket):
    #
    # Ferme le socket passe en parametre
    #
    para_socket.close()
