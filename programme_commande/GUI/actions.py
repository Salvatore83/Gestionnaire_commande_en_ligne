#
#
#
#
#
# Imports: Interface graphique (PythonLja), Le gestionnaire de l'interface graphique (gui), et le répertoire des objets graphiques (interface)
#
#
#
#
#

from . import PythonLja_18 as Lja
from . import gui as gui
from . import interface as logo

#
#
#
#
#
# Changement de l'apparence des boutons quand ils sont cliqués: Fonction "cliquabilité"
#
#
#
#
#

###########################################################################################################################################
#
#           f_RecupCoord()
#
#       para : aucun
#
#       do :
#               Affiche l'allure "cliquée" des boutons de façon coordonnée
#
#       return : rien
#
###########################################################################################################################################


def f_RecupCoord():
    #
    # Récupère les coordonnées de la souris
    #
    sourisx = Lja.get_mouse_x()
    sourisy = Lja.get_mouse_y()
    BoutonActif = 0
    #
    # Si un bouton est actuellement cliqué:
    #
    if BoutonActif != 0:
        #
        # Si la souris est sur le bouton carré de gauche:
        #
        if sourisx > 10 and sourisx < 110 and sourisy > 150 and sourisy < 250:
            #
            # Rétablit son apparence basique
            #
            logo.f_BoutonGauche()
            #
            # Aucun bouton n'est alors cliqué.
            #
            BoutonActif = 0
        #
        # Si la souris est sur le bouton carré du haut:
        #
        elif sourisx > 115 and sourisx < 215 and sourisy > 45 and sourisy < 145:
            #
            # Rétablit son apparence basique
            #
            logo.f_BoutonAvant()
            #
            # Aucun bouton n'est alors cliqué.
            #
            BoutonActif = 0
        #
        # Si la souris est sur le bouton carré de droite:
        #
        elif sourisx > 220 and sourisx < 320 and sourisy > 150 and sourisy < 250:
            #
            # Rétablit son apparence basique
            #
            logo.f_BoutonDroite()
            #
            # Aucun bouton n'est alors cliqué.
            #
            BoutonActif = 0
        #
        # Si la souris est sur le bouton carré du bas:
        #
        elif sourisx > 115 and sourisx < 215 and sourisy > 255 and sourisy < 355:
            #
            # Rétablit son apparence basique
            #
            logo.f_BoutonArriere()
             #
             # Aucun bouton n'est alors cliqué.
             #
            BoutonActif = 0
        #
        # Sinon, si l'on se trouve dans la zone (en abcisses) des boutons rectangulaires:
        #
        elif sourisx > 60 and sourisx < 270:
            #
            # Si l'on est dans le rectangle du haut
            #
            if sourisy > 385 and sourisy < 415:
                logo.f_BoutonDistanceDefinieHaut()
            #
            # Sinon, si l'on est dans le rectangle du milieu-haut
            #
            elif sourisy > 425 and sourisy < 455:
                logo.f_BoutonDistanceDefinieBas()
            #
            # Sinon, si l'on est dans le rectangle du milieu-bas
            #
            elif sourisy > 465 and sourisy < 495:
                logo.f_BoutonDistanceDefinieGauche()
            #
            # Sinon, si l'on est dans le rectangle du bas:
            #
            elif sourisy > 505 and sourisy < 535:
                logo.f_BoutonDistanceDefinieBas()
        elif sourisx > 685 and sourisx < 785 and sourisy > 485 and sourisy < 585:
            logo.f_arret()
            BoutonActif = 0
        #
        # Si l'on est dans aucun des boutons:
        #
        else:
            #
            # Rétablir l'apparence basique de tous les boutons
            #
            logo.f_BoutonGauche()
            logo.f_BoutonAvant()
            logo.f_BoutonDroite()
            logo.f_BoutonArriere()
            logo.f_BoutonDistanceDefinieHaut()
            logo.f_BoutonDistanceDefinieBas()
            logo.f_BoutonDistanceDefinieGauche()
            logo.f_BoutonDistanceDefinieDroite()
            logo.f_arret()
    #
    # Si aucun bouton n'est cliqué:
    #
    else:
        #
        # Rétablir l'apparence basique de tous les boutons
        # 
        logo.f_BoutonGauche()
        logo.f_BoutonAvant()
        logo.f_BoutonDroite()
        logo.f_BoutonArriere()
        logo.f_BoutonDistanceDefinieHaut()
        logo.f_BoutonDistanceDefinieBas()
        logo.f_BoutonDistanceDefinieGauche()
        logo.f_BoutonDistanceDefinieDroite()
        logo.f_arret()
        #
        # Si la souris est sur le bouton carré de gauche:
        #
        if sourisx > 10 and sourisx < 110 and sourisy > 150 and sourisy < 250:
            #
            # Applique l'apparence cliquée de ce bouton
            #
            logo.f_BoutonGaucheClic()
            #
            # Le bouton carré de gauche est cliqué.
            #
            BoutonActif = 1
        #
        # Sinon, si la souris est sur le bouton carré du haut:
        #
        elif sourisx > 115 and sourisx < 215 and sourisy > 45 and sourisy < 145:
            #
            # Applique l'apprence cliquée de ce bouton
            #
            logo.f_BoutonAvantClic()
            #
            # Le bouton carré du haut est cliqué.
            #
            BoutonActif = 2
        #
        # Sinon, si la souris est sur le bouton carré de droite:
        #
        elif sourisx > 220 and sourisx < 320 and sourisy > 150 and sourisy < 250:
            #
            # Applique l'apparence cliquée de ce bouton
            #
            logo.f_BoutonDroiteClic()
            #
            # Le bouton carré de droite est cliqué.
            #
            BoutonActif = 3
        #
        # Sinon, si la souris est sur le bouton carré du bas:
        #
        elif sourisx > 115 and sourisx < 215 and sourisy > 255 and sourisy < 355:
            #
            # Applique l'apparence cliquée de ce bouton
            #
            logo.f_BoutonArriereClic()
            #
            # Le bouton carré du bas est cliqué.
            #
            BoutonActif = 4
        #
        # Sinon, si l'on est dans la zone (en abcisses) des boutons rectangulaires:
        #
        elif sourisx > 60 and sourisx < 270:
            #
            # Si l'on est dans le bouton du haut
            #
            if sourisy > 385 and sourisy < 415:
                #
                # Applique l'apparence cliquée de ce bouton
                #
                logo.f_BoutonDistanceDefinieHautClic()
                #
                # Le bouton rectangulaire du haut est cliqué.
                #
                BoutonActif = 5
            #
            # Sinon, si l'on est dans le bouton du milieu-haut:
            #
            elif sourisy > 425 and sourisy < 455:
                #
                # Applique l'apparence cliquée de ce bouton
                #
                logo.f_BoutonDistanceDefinieBasClic()
                #
                # Le bouton rectangulaire du milieu-haut est cliqué.
                #
                BoutonActif = 6
            #
            # Sinon, si l'on est dans le bouton du milieu-bas:
            #
            elif sourisy > 465 and sourisy < 495:
                #
                # Applique l'apparence cliquée de ce bouton
                #
                logo.f_BoutonDistanceDefinieGaucheClic()
                #
                # Le bouton rectangulaire du milieu-bas est cliqué.
                #
                BoutonActif = 7
            #
            # Sinon, si l'on est dans le bouton du bas:
            #
            elif sourisy > 505 and sourisy < 535:
                #
                # Applique l'apparence cliquée de ce bouton
                #
                logo.f_BoutonDistanceDefinieDroiteClic()
                #
                # Le bouton rectangulaire du milieu-bas est cliqué.
                #
                BoutonActif = 8
        elif sourisx > 685 and sourisx < 785 and sourisy > 485 and sourisy < 585:
            logo.f_ArretClic()
            BoutonActif = 9
#
# Associe au clic gauche la fonction precédemment créée.
#
Lja.assoc_button(1,f_RecupCoord)

###########################################################################################################################################
#
#           f_SimulationFinSignal()
#
#       para : aucun
#
#       do :
#               Rétablit l'allure normale de tous les boutons: simule le message de fin d'opération du robot
#
#       return : rien
#
###########################################################################################################################################

def f_SimulationFinSignal():
    #
    # Rétablit l'allure initiale de tous les boutons
    #
    logo.f_BoutonGauche()
    logo.f_BoutonAvant()
    logo.f_BoutonDroite()
    logo.f_BoutonArriere()
    logo.f_BoutonDistanceDefinieHaut()
    logo.f_BoutonDistanceDefinieBas()
    logo.f_BoutonDistanceDefinieGauche()
#
# Associe la touche v à la fonction précedemment créée
#
Lja.assoc_key("v",f_SimulationFinSignal)