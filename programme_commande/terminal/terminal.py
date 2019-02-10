
###########################################################################################################################################
#
# Gestionnaire de commandes via terminal
#
# gestion du gestionnaire via terminal
#
##########################################################################################################################################

from . import connexion

##########################################################################################################################################
#
#           f_afficher_commande()
#
#       para : aucun
#
#       do :
#           affiche la liste des commandes
#
#       return : rien
#
##########################################################################################################################################


def f_afficher_commande():
    print('')
    print('-------------------------------')
    print('Liste des commandes')
    print('afficher la liste des commandes : li_com')
    print('faire avancer le robot : avancer')
    print('faire reculer le robot : reculer')
    print('faire tourner le robot : gauche ou droite')
    print('-------------------------------')

##########################################################################################################################################
#
#           f_attendre_reponse_robot()
#
#       para : socket client
#
#       do :
#           attends le message de confirmation d'action du robot
#
#       return : rien
#
##########################################################################################################################################

def f_attendre_reponse_robot(para_socket_client):

    message_robot = '0'

    while message_robot != '1':
        message_robot = connexion.f_attendre_message(para_socket_client)
        print('Le robot execute l action')

    print("Le robot a execute l'action, il est pret a executer une nouvelle action.")

##########################################################################################################################################
#
#           f_gestion_robot()
#
#       para : para_socket_client
#
#       do :
#           gere les commandes a envoyer au robot
#
#       return : rien
#
##########################################################################################################################################


def f_gestion_robot(para_socket_client):

    print('gestion du robot')
    print('voici les commandes')

    commande = True
    #
    # Affichage de la liste des commandes
    #
    f_afficher_commande()

    #
    # Tant que l'utilisateur ne rentre pas quitter (ne veut donc pas quitter)
    #
    while commande != 'quitter':
        #
        # Demande de la commande à l'utilisateur
        #
        print('')
        commande = input('>')

        #
        # SI l'utilisateur a rentre 'li_com', il veut donc afficher la liste des commandes
        #
        if commande == 'li_com':
            f_afficher_commande()

        #
        # SINON SI l'utilisateur a rentre 'avancer', il veut faire avancer le robot
        #
        elif commande == 'avancer':
            print('Envoie de la commande avancer au robot')
            connexion.f_envoyer_message(para_socket_client, 'avancer')

        #
        # SINON SI l'utilisateur a rentre 'reculer', il veut faire reculer le robot
        #
        elif commande == 'reculer':
            print('Envoie de la commande reculer au robot')
            connexion.f_envoyer_message(para_socket_client, 'reculer')

        #
        # SINON SI l'utilisateur a rentre 'gauche', il veut faire tourner le robot a gauche
        #
        elif commande == 'gauche':
            print('Envoie de la commande gauche au robot')
            connexion.f_envoyer_message(para_socket_client, 'gauche')

        #
        # SINON SI l'utilisateur a rentre 'droite', il veut faire tourner le robot a droite
        #
        elif commande == 'droite':
            print('Envoie de la commande droite au robot')
            connexion.f_envoyer_message(para_socket_client, 'droite')

        #
        # SINON l'utilisateur a rentre autre chose (ne fait rien)
        #
        else:
            pass

        f_attendre_reponse_robot(para_socket_client)

##########################################################################################################################################
#
#           f_ouvrir_gestionnaire()
#
#       para : aucun
#
#       do :
#           ouvre le gestionnaire via terminal et l'initialise
#
#       return : rien
#
##########################################################################################################################################

def f_ouvrir_gestionnaire():
    print('ouverture du gestionnaire via terminal')

    connexion.f_afficher_utilisation_socket()
    #
    # Cree le socket serveur
    #
    socket_serveur = connexion.f_creer_serveur()
    #
    # Recupere la connexion du serveur client
    #
    socket_client, adresse = connexion.f_accepter_client(socket_serveur)

    robot_pret = False

    while robot_pret != True:
        #
        # attente message
        #
        msg_client = connexion.f_attendre_message(socket_client)

        #
        # SI le message recut est '1', le robot est pret
        #
        if msg_client == '1':
            print('robot pret')
            f_gestion_robot(socket_client)
            robot_pret = True

        #
        # SINON le robot n'est pas pret
        #
        else:
            print('robot pas pres')

        connexion.f_fermer_serveur(socket_serveur, socket_client)
