
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
# import RPi.GPIO as GP
import time


def f_initialisation_capteurs():

    try:
        GP.setmode(GP.BOARD)
        ledPin = 12
        GP.setup(ledPin, GP.OUT)
        return 'Succes'
    except:
        # changer en erreur lors du fonctionnement du programme. 
        # comme je ne code pas avec le robot, obligé de faire ça
        return 'Erreur'

# allumer une LED
def f_allumer_LED(para_LED):
    print("La LED ", para_LED, " va s'allumer")
    GP.output(para_LED, GP.HIGH)
    print("La LED ",  para_LED, " est allumé")

#eteindre une LED
def f_eteindre_LED(para_LED):
    print("La LED ", para_LED, " va s'éteindre")
    GP.output(para_LED, GP.LOW)
    print("LA LED", para_LED, "est éteinte")

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
    #
    # Allume la LED
    #
    elif para_commande == 'ALED':
        f_allumer_LED(12)
    #
    # Eteind la LED
    #
    elif para_commande == 'ELED':
        f_eteindre_LED(12)
    #
    # Fais clignoter la LED
    #
    elif para_commande == 'CLILED':
        i = 0
        while i < 4:
            f_allumer_LED(12)
            time.sleep(2)
            f_eteindre_LED(12)
            i += 1

    time.sleep(1)
    CONrob.f_envoyer_message(para_socket_client, 'Action terminee')
    print("Action terminee.")
