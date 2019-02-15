
###########################################################################################################################################
#
# Gestionnaire de commandes via terminal
#
# gestion du gestionnaire via terminal
#
##########################################################################################################################################

from . import connexion

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
    # Boucle de gestion du robot
    #
    commande = ''
    compt_i = 0
    while commande != 'quitter':

        if compt_i == 0:
            f_afficher_commande()
            compt_i += 1

        
