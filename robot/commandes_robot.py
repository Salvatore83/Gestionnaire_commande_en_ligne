
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

# Fais actionne le moteur des roues du robot
def f_robot_moteur_roues():

    GPIO.setmode(GPIO.BOARD)   ##je prefere la numerotation BOARD plutot que BCM

    Moteur1A = 16      ## premiere sortie du premier moteur, pin 16
    Moteur1B = 18      ## deuxieme sortie de premier moteur, pin 18
    Moteur1E = 22      ## enable du premier moteur, pin 22

    GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
    GPIO.setup(Moteur1B,GPIO.OUT)
    GPIO.setup(Moteur1E,GPIO.OUT)

    pwm = GPIO.PWM(Moteur1E,50)   ## pwm de la pin 22 a une frequence de 50 Hz
    pwm.start(100)   ## on commemnce avec un rapport cyclique de 100%


    print ("Rotation sens direct, vitesse maximale (rapport cyclique 100%)")
    GPIO.output(Moteur1A,GPIO.HIGH)
    GPIO.output(Moteur1B,GPIO.LOW)
    GPIO.output(Moteur1E,GPIO.HIGH)

    sleep(5)  ## on laisse tourner le moteur 5 secondes avec des parametres

    pwm.ChangeDutyCycle(20)  ## modification du rapport cyclique a 20%

    print ("Rotation sens direct, au ralenti (rapport cyclique 20%)")

    time.sleep(5)

    print ("Rotation sens inverse, au ralenti (rapport cyclique 20%)")
    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.HIGH)

    time.sleep(5)

    pwm.ChangeDutyCycle(100)
    print("Rotation sens inverse, vitesse maximale (rapport cyclique 100%)")
    time.sleep(5)


    print ("Arret du moteur")
    GPIO.output(Moteur1E,GPIO.LOW)

    pwm.stop()    ## interruption du pwm

    GPIO.cleanup()


def f_calculer_distance(para_US):
    pass

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
