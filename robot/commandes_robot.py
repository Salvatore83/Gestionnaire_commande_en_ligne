
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
import RPi.GPIO as GP
import time
import datetime


def f_initialisation_capteurs():

    try:
        GP.setmode(GP.BOARD)
        GP.setup(15, GP.OUT)
        GP.setup(13, GP.OUT)
        GP.setup(11, GP.OUT)
        GP.setup(12, GP.OUT)
        f_allumer_LED(13)
        return 'Succes'
    except:
        # changer en erreur lors du fonctionnement du programme.
        # comme je ne code pas avec le robot, obligé de faire ça
        # Pour les tests, ce sera en 'Succes'
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


def f_moteur():

    pwm = GP.PWM(12, 50)

    rapport = 3
    second_debut = datetime.datetime.now().second
    pwm.start(rapport)
    avancer = True
    while avancer == True:
        pwm.ChangeDutyCycle(1)
        maintenant = datetime.datetime.now().second
        print(maintenant)
        if (second_debut + 5) < maintenant:
            avancer = False


def f_calculer_distance(para_US):
    pass

def f_gerer_action_robot(para_socket_client, para_commande):

    print('action recue')
    f_allumer_LED(11)
    #
    # Grosse comparaison des commandes demandées par le terminal
    #
    if para_commande == 'avancer':
        f_moteur()
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
        f_allumer_LED(15)
    #
    # Eteind la LED
    #
    elif para_commande == 'ELED':
        f_eteindre_LED(15)
    #
    # Fais clignoter la LED
    #
    elif para_commande == 'CLILED':
        i = 0
        while i < 4:
            f_allumer_LED(15)
            time.sleep(1)
            f_eteindre_LED(15)
            time.sleep(1)
            i += 1

    time.sleep(1)
    CONrob.f_envoyer_message(para_socket_client, 'Action terminee')
    print("Action terminee.")
    f_eteindre_LED(11)