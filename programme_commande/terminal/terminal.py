
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
    connexion.f_attendre_robot_pret(socket_serveur)
    #
    # Affichage des commandes pour la premiere fois
    #
    comgest.f_afficher_commande()
    #
    # Gestion des commandes utilisateurs
    #
    commande = ''
    while commande != 'quitter':

        commande = comgest.f_gerer_commande_utilisateur()
        connexion.f_envoyer_commande()

    #
    # Fermeture des sockets
    #
    connexion.fermer_socket(socket_serveur)
    connexion.fermer_socket(socket_client)
