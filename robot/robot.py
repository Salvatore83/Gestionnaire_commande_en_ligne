
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

from * import connexion_robot as Connrob
from * import commandes_robot as Commrob



if __name__ == '__main__':
    socket_robot = Connrob.f_creer_socket_client()
    socket_robot = Connrob.f_connexion_serveur(socket_robot)


    Connrob.f_fermer_socket(socket_robot)
