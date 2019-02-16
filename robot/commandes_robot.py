
###########################################################################################################################################
#
# Module principal de gestion des commandes du robot
#
# Premet de gerer les commandes robot (ACTIONS)
#
###########################################################################################################################################

#
# Imports
#

import gestion_connexion_robot as CONrob


def f_initialisation_capteurs():

    return 'Succes'


def f_gerer_action_robot(para_socket_client, para_commande):

    print('action recue')

    #
    # Grosse comparaison des commandes demandées par le terminal
    #
    if para_commande == 'avancer':
        # f_avancer_robot()
        CONrob.f_envoyer_message(para_socket_client, 'En cours')
    elif para_commande == 'reculer':
        # f_reculer_robot()
        pass
    elif para_commande == 'droite':
        # f_tourner_robot(droite)
        pass
    elif para_commande == 'gauche':
        # f_tourner_robot(gauche)
        pass

    CONrob.f_envoyer_message(para_socket_client, 'Action terminee')
