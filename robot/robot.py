
###########################################################################################################################################
#
# Module principal (premier lance dans le programme) du robot
#
# Premet de gerer le robot
#
###########################################################################################################################################

#
# IMPORTS
#

import gestion_connexion_robot as CONrob
import commandes_robot as COMrob



if __name__ == '__main__':

    #
    # Crée le socket client par lequel passera toutes les données de connexion
    #
    socket_client = CONrob.f_creer_socket()
    #
    # Connecte le socket client a l'adresse via le port
    #
    host = '192.168.43.107'
    port = 5566
    socket_client = CONrob.f_connecter_socket(socket_client, host, port)
    #
    # Attend que le gestionnaire lui renvoit qu'il s'est bien connecté
    #
    CONrob.f_reponse_connexion(socket_client)
    print('connexion reussie')
    #
    # Le robot initialise tous ces capteurs et regarde s'il n'a pas d'erreur en interne puis il envoie une reponse au gestionnaire
    #
    CONrob.f_robot_initialisation(socket_client, 0)
    print('initialisation reussie')
    #
    # La fonction qui gere toutes les actions du robot
    #
    CONrob.f_action_robot(socket_client)
    #
    # Fermer le socket client
    #
    CONrob.fermer_socket(socket_client)
