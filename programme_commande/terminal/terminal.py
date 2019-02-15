
###########################################################################################################################################
#
# Gestionnaire de commandes via terminal
#
# gestion du gestionnaire via terminal
#
##########################################################################################################################################

from . import connexion
from . import commandes_gestionnaire as comgest

###########################################################################################################################################
#
#           f_ouvrir_gestionnaire()
#
#       para : aucun
#
#       do :
#           gere le gestionnaire via terminal
#
#       return : rien
#
###########################################################################################################################################


def f_ouvrir_gestionnaire():

    #
    # Creation du socket serveur
    #
    socket_serveur = connexion.f_creer_serveur()
    #
    # Attente et autorisation de connexion
    #
    socket_client = connexion.f_accepter_connexion(socket_serveur)
    #
    # Envoie un message au robot
    #
    connexion.f_envoyer_message(socket_client, '1')
    #
    # Attends que le robot puisse executer une action
    #
    connexion.f_attendre_robot_pret(socket_client)
    #
    # Affichage des commandes pour la premiere fois
    #
    comgest.f_afficher_commande()
    #
    # Gestion des commandes utilisateurs
    #
    commande = ''
    while commande != 'quitter':
        #
        # Demande a l'utilisateur la commande qu'il veut effectuer
        #
        commande = comgest.f_gerer_commande_utilisateur()
        #
        # Envoie la commande au robot et attend qu'il ait finit de l'executer
        #
        connexion.f_gerer_commande(socket_serveur, socket_client, commande)

    #
    # Dire au robot de se deconnecter
    #

    connexion.f_envoyer_message(socket_client, 'quitter')

    #
    # Fermeture des sockets
    #
    connexion.f_fermer_socket(socket_serveur)
    connexion.f_fermer_socket(socket_client)
