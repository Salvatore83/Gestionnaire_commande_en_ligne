from . import PythonLja_18 as Lja
import time

#######################################################################
#
#                   f_creer_fenetre_attente()
#
#    paramètres : largeur, hauteur
#
#         do : crée la fenêtre de largeur et de hauteur définie
#         return : Rien
#
#######################################################################

def f_creer_fenetre_attente(largeur,hauteur):
    
    #
    # Crée la fenêtre
    #

    Lja.init_window("Panneau de contrôle", largeur, hauteur)
    Lja.text(largeur-largeur/2, hauteur-hauteur/2, "En attente de connexion...")
    robot_connecte = input("> ")

    #
    # Fait durer la fenêtre sous windows
    #
    
#######################################################################
#
#                   f_creer_fenetre_projet()
#
#    paramètres : largeur, hauteur
#
#         do : crée la fenêtre de largeur et de hauteur définie
#         return : Rien
#
#######################################################################


def f_creer_fenetre_projet(largeur,hauteur):

    #
    # Nettoie la fenêtre
    #

    Lja.clear_screen()
    Lja.text(largeur-largeur/2, hauteur-hauteur/2 ,"Connexion établie") 

    #
    # Fait durer la fenêtre sous windows
    #


#######################################################################
#
#                   f_ouvrir_gestionnaire()
#
#    paramètres : 
#
#         do : ouvre le gestionnaire via l'interface graphique
#         return : Rien
#
#######################################################################

def f_ouvrir_gestionnaire():

    #
    # Demande les dimensions de la fenêtre 
    #

    largeur = int(input("Saisissez la largeur de votre fenêtre: "))
    print('\n')
    hauteur = int(input("Saisissez la largeur de votre fenêtre: "))

    #
    # Affiche que le gestionnaire via interface graphique s'apprête à s'ouvrir
    #

    print('Ouverture du gestionnaire via GUI')

    #
    # Crée la fenêtre d'attente pendant trois secondes
    #

    f_creer_fenetre_attente(largeur,hauteur)
    while robot_connecte != "":
        
        #
        # Crée la fenêtre
        #

        f_creer_fenetre_projet(largeur,hauteur)
        Lja.main_loop()