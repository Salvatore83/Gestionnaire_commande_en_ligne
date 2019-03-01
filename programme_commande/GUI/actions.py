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
    # Si La connexion (simulée pour l'instant avec un clic droit) n'est pas établie:
    #
    if gui.OuvrirFenetre == 0:
        #
        # Rien ne se passera.
        #
        pass
    #
    # Sinon, si la personne a bien fait "clic droit" pour simuler l'établissement de la connexion:
    #    
    else:
        PositionClic = 0
        #
        # Récupère la postion de la souris sur les axes x et y
        #
        sourisx = Lja.get_mouse_x()
        sourisy = Lja.get_mouse_y()
        #
        # Si la souris est dans le carré de gauche:
        #
        if sourisx > 10 and sourisx < 110 and sourisy > 150 and sourisy < 250:
            #
            # Affiche l'allure cliquée du bouton de gauche
            #
            logo.f_BoutonGaucheClic()
            #
            # Rétablit l'allure normale des autres boutons
            #
            logo.f_BoutonAvant()
            logo.f_BoutonDroite()
            logo.f_BoutonArriere()
            logo.f_BoutonDistanceDefinieHaut()
            logo.f_BoutonDistanceDefinieBas()
            logo.f_BoutonDistanceDefinieGauche()
            logo.f_BoutonDistanceDefinieDroite()
            PositionClic = 1
            #
            # Sinon, si la souris est dans le carré du haut:
            #
        elif sourisx > 115 and sourisx < 215 and sourisy > 45 and sourisy < 145:
            #
            # Affiche l'allure cliquée du bouton du haut
            #
            logo.f_BoutonAvantClic()
            #
            # Rétablit l'allure normale des autres boutons
            #
            logo.f_BoutonGauche()
            logo.f_BoutonDroite()
            logo.f_BoutonArriere()
            logo.f_BoutonDistanceDefinieHaut()
            logo.f_BoutonDistanceDefinieBas()
            logo.f_BoutonDistanceDefinieGauche()
            logo.f_BoutonDistanceDefinieDroite()
            PositionClic = 2
            #
            # Sinon, si la souris est dans le carré de droite:
            #
        elif sourisx > 220 and sourisx < 320 and sourisy > 150 and sourisy < 250:
            #
            # Affiche l'allure cliquée du bouton de droite
            #
            logo.f_BoutonDroiteClic()
            #
            # Rétablit l'allure normale des autres boutons
            #
            logo.f_BoutonGauche()
            logo.f_BoutonAvant()
            logo.f_BoutonArriere()
            logo.f_BoutonDistanceDefinieHaut()
            logo.f_BoutonDistanceDefinieBas()
            logo.f_BoutonDistanceDefinieGauche()
            logo.f_BoutonDistanceDefinieDroite()
            PositionClic = 3
            # Sinon, si la souris est dans le carré du bas:
        elif sourisx > 115 and sourisx < 215 and sourisy > 255 and sourisy < 355:
            #
            # Affiche l'allure cliquée du bouton du bas
            #
            logo.f_BoutonArriereClic()
            #
            # Rétablit l'allure normale des autres boutons
            #
            logo.f_BoutonGauche()
            logo.f_BoutonDroite()
            logo.f_BoutonAvant()
            logo.f_BoutonDistanceDefinieHaut()
            logo.f_BoutonDistanceDefinieBas()
            logo.f_BoutonDistanceDefinieGauche()
            logo.f_BoutonDistanceDefinieDroite()
            PositionClic = 4
        #
        # Sinon, si la souris est dans la zone des boutons rectangulaires:
        #
        elif sourisx > 60 and sourisx < 270:
            #
            # Si la souris est dans le bouton du haut:
            #
            if sourisy > 385 and sourisy < 415:
                #
                # Affiche l'allure cliqué du bouton du haut
                # 
                logo.f_BoutonDistanceDefinieHautClic()
                #
                # Rétablit l'allure normale des autres boutons
                #
                logo.f_BoutonGauche()
                logo.f_BoutonDroite()
                logo.f_BoutonAvant()
                logo.f_BoutonArriere()
                logo.f_BoutonDistanceDefinieBas()
                logo.f_BoutonDistanceDefinieGauche()
                logo.f_BoutonDistanceDefinieDroite()
                PositionClic = 5
            #
            # Sinon, si la souris est dans le bouton du milieu-haut:
            #
            elif sourisy > 425 and sourisy < 455:
                #
                # Affiche l'allure cliquée du bouton du milieu-haut
                #
                logo.f_BoutonDistanceDefinieBasClic()
                #
                # Rétablit l'allure normale des autres boutons
                #
                logo.f_BoutonGauche()
                logo.f_BoutonDroite()
                logo.f_BoutonAvant()
                logo.f_BoutonArriere()
                logo.f_BoutonDistanceDefinieHaut()
                logo.f_BoutonDistanceDefinieGauche()
                logo.f_BoutonDistanceDefinieDroite()
                PositionClic =6
            #
            # Sinon, si le bouton est dans le  bouton du milieu-bas:
            #
            elif sourisy > 465 and sourisy < 495:
                #
                # Affiche l'allure cliqué du bouton du milieu-bas
                #
                logo.f_BoutonDistanceDefinieGaucheClic()
                #
                # Rétablit l'allure normale des autres boutons
                #
                logo.f_BoutonGauche()
                logo.f_BoutonDroite()
                logo.f_BoutonAvant()
                logo.f_BoutonArriere()
                logo.f_BoutonDistanceDefinieHaut()
                logo.f_BoutonDistanceDefinieBas()
                logo.f_BoutonDistanceDefinieDroite()
                PositionClic = 7
            #
            # Sinon, si le bouton est dans le bouton du bas:
            #
            elif sourisy > 505 and sourisy < 535:
                #
                # Affiche l'allure cliquée du bouton du bas
                #
                logo.f_BoutonDistanceDefinieDroiteClic()
                #
                # Rétablit l'allure normale des autres boutons
                #
                logo.f_BoutonGauche()
                logo.f_BoutonDroite()
                logo.f_BoutonAvant()
                logo.f_BoutonArriere()
                logo.f_BoutonDistanceDefinieHaut()
                logo.f_BoutonDistanceDefinieGauche()
                logo.f_BoutonDistanceDefinieBas()
                PositionClic = 8
                
            ###############################################################################################################################################################
            # ATTENTION: A PARTIR D'ICI, C'EST POUR FAIRE EN SORTE QUE LES BOUTONS SOIENT EUX-MEMES "DECLIQUABLES"; NE MARCHE PAS ENCORE, DONC ARRETE AUX BOUTONS CARRES. #
            ###############################################################################################################################################################

            #
            # Si on est sur le carré de gauche et qu'il a déjà été cliqué:
            #
        elif sourisx > 10 and sourisx < 110 and sourisy > 150 and sourisy < 250 and PositionClic == 1:
            #
            # Rétablit l'apparence basique du bouton
            # 
            PositionClic = 0
            logo.f_BoutonGauche()
            #
            # Si on est sur le carré du haut et qu'il a déjà été cliqué:
            #
        elif sourisx > 115 and sourisx < 215 and sourisy > 45 and sourisy < 145 and PositionClic == 2:
            #
            # Rétablit l'apparence basique du bouton
            # 
            PositionClic = 0
            logo.f_BoutonAvant()
            #
            # Si on est sur le carré de droite et qu'il a déjà été cliqué:
            #
        elif sourisx > 220 and sourisx < 320 and sourisy > 150 and sourisy < 250 and PositionClic == 3:
            #
            # Rétablit l'apparence basique du bouton
            # 
            PositionClic = 0
            logo.f_BoutonDroite()
            #
            # Si on est sur le carré du bas et qu'il a déjà été cliqué:
            #
        elif sourisx > 115 and sourisx < 215 and sourisy > 255 and sourisy < 355 and PositionClic == 4:
            #
            # Rétablit l'apparence basique du bouton
            # 
            PositionClic = 0
            logo.f_BoutonArriere()
            #
            # Sinon, si la souris n'est sur aucun des boutons:
            #
        else:
            #
            #  Rétablit l'allure normale de tous les boutons
            #
            logo.f_BoutonGauche()
            logo.f_BoutonAvant()
            logo.f_BoutonDroite()
            logo.f_BoutonArriere()
            logo.f_BoutonDistanceDefinieHaut()
            logo.f_BoutonDistanceDefinieBas()
            logo.f_BoutonDistanceDefinieGauche()
            logo.f_BoutonDistanceDefinieDroite()
            PositionClic = 0

            ######################################
            # FIN DE LA PARTIE NON FONCTIONNELLE.#
            ######################################

        #
        # Associe le clic gauche de la souris à la fonction ci-dessus
        #
Lja.assoc_button(1,f_RecupCoord)