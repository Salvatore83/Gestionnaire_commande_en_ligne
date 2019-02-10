from . import PythonLja_18 as Lja

    
#######################################################################
#
#                   creer_fenetre()
#
#    paramètres : largeur, hauteur
#
#         do : crée la fenêtre de largeur et de hauteur définie
#         return : Rien
#
#######################################################################


def f_creer_fenetre(largeur,hauteur):

    #
    # Crée la fenêtre
    #

    Lja.init_window("Projet", largeur, hauteur)

    #
    # Fait durer la fenêtre sous windows
    #

    Lja.main_loop()


#######################################################################
#
#                   ouvrir_gestionnaire()
#
#    paramètres : 
#
#         do : ouvre le gestionnaire via l'interface graphique
#         return : Rien
#
#######################################################################

def f_ouvrir_gestionnaire():
    print('Ouverture du gestionnaire via GUI')
    largeur = int(input("Saisissez la largeur de votre fenêtre: "))
    print('\n')
    hauteur = int(input("Saisissez la largeur de votre fenêtre: "))
    f_creer_fenetre(largeur,hauteur)

