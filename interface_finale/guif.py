import PythonLja_18 as Lja
import interfacef as img

###########################################################################################################################################
#
#           f_creer_fenetre_attente()
#
#       para : aucun
#
#       do :
#               Crée la fenêtre
#
#       return : rien
#
###########################################################################################################################################


def f_creer_fenetre_attente():
    #
    # Crée la fenêtre avec les dimensions données
    #
    Lja.init_window("Projet", 800,600)

###########################################################################################################################################
#
#           f_creer_fenetre_projet()
#
#       para : aucun
#
#       do :
#               Affiche tous les éléments basiques (non cliqués s'ils peuvent l'être) de la fenêtre
#
#       return : rien
#
###########################################################################################################################################


def f_creer_fenetre_projet():
    #
    # Affiche tous les éléments qui constituent la fenêtre
    #
    img.f_fondnoir()
    img.f_fondcroix()
    img.f_croixhaut()
    img.f_croixgauche()
    img.f_croixdroite()
    img.f_croixbas()
    img.f_carreb()
    img.f_carreo()
    img.f_carrevi()
    img.f_carreve()

###########################################################################################################################################
#
#           f_RecupCoord()
#
#       para : aucun
#
#       do :
#               Fait durer la fenêtre
#
#       return : rien
#
###########################################################################################################################################


def f_ouvrir_gestionnaire():
    f_creer_fenetre_attente()
    Lja.assoc_button(3, f_creer_fenetre_projet)
    Lja.main_loop()

f_ouvrir_gestionnaire()