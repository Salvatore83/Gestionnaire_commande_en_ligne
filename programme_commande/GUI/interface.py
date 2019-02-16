from . import PythonLja_18 as Lja
from . import gui as gui
from . import actions as act

###########################################################################################################################################
#
#           f_arret()
#
#       para : aucun
#
#       do :
#               Crée le logo "interdit" qui servira a couper toute action en cours du robot
#
#       return : rien
#
###########################################################################################################################################

def f_arret():
        #
        # Met du rouge
        #
    Lja.current_color("red")
        #
        # Trace le cercle du logo
        #
    Lja.circle(935,735,50,20) 
        #
        # Trace la barre transversale
        #
    Lja.line(895,695,970,770,20)

###########################################################################################################################################
#
#           f_BoutonGauche()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la gauche
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonGauche(): 
        #
        # Met le violet du carré
        #
    Lja.current_color(135,50,110)
        #
        # Crée le cube basique
        #
    Lja.box(10,250,110,150)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(168,89,144)
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(10,150,17,155,17,245,10,250)
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(10,150,17,155,103,155,110,150)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(112,39,90)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(110,150,103,155,103,245,110,250)
        #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(92,29,73)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(10,250,17,245,103,245,110,250)
        #
        # Crée le reflet en bas
        #

"""
    Lja.current_color("black")
        #
        # Crée la flèche montante
        #
    Lja.line(80,180,60,200,10)
        #
        # Crée la flèche descendante
        #
    Lja.line(60,200,80,220,10)
    Lja.polygon(60,195,65,200,60,205,55,200)
"""

###########################################################################################################################################
#
#           f_BoutonGaucheClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la gauche quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonGaucheClic():
        #
        # Met le violet du carré
        #
    Lja.current_color(94,34,76)
        #
        # Crée le cube basique
        #
    Lja.box(10,250,110,150)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(125,66,107)
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(10,150,17,155,17,245,10,250)
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(10,150,17,155,103,155,110,150)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(134,65,113)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(110,150,103,155,103,245,110,250)
        #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(57,18,45)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(10,250,17,245,103,245,110,250)
        #
        # Crée le reflet en bas
        #


###########################################################################################################################################
#
#           f_BoutonAvant()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers l'avant
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonAvant():
        #
        # Met le violet du carré
        #
    Lja.current_color(135,50,110)
        #
        # Crée le cube basique
        #
    Lja.box(115,145,215,45)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(168,89,144) 
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(115,45,122,50,122,140,115,145)
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(115,45,115,50,208,50,215,45)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(112,39,90)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(215,45,208,50,208,145,215,145)
        #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(92,29,73)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(115,145,122,140,208,140,215,145)

###########################################################################################################################################
#
#           f_BoutonAvantClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers l'avant quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonAvantClic():
        #
        # Met le violet du carré
        #
    Lja.current_color(94,34,76)
        #
        # Crée le cube basique
        #
    Lja.box(115,145,215,45)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(125,66,107)
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(115,45,122,50,122,140,115,145)
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(115,45,115,50,208,50,215,45)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(134,65,113)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(215,45,208,50,208,145,215,145)
        #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(57,18,45)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(115,145,122,140,208,140,215,145)

###########################################################################################################################################
#
#           f_BoutonDroite()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la droite
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDroite():
        #
        # Met le violet du carré
        #
    Lja.current_color(135,50,110)
        #
        # Crée le cube basique
        #
    Lja.box(220,250,320,150)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(168,89,144) 
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(220,150,227,155,227,245,220,250) 
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(220,150,227,155,313,155,320,150)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(112,39,90)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(320,150,313,155,313,245,320,250)
        #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(92,29,73)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(220,250,227,245,313,245,320,250)

###########################################################################################################################################
#
#           f_BoutonDroiteClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la droite quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDroiteClic():
        #
        # Met le violet du carré
        #
    Lja.current_color(94,34,76)
        #
        # Crée le cube basique
        #
    Lja.box(220,250,320,150)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(125,66,107)
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(220,150,227,155,227,245,220,250) 
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(220,150,227,155,313,155,320,150)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(134,65,113)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(320,150,313,155,313,245,320,250)
        #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(57,18,45)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(220,250,227,245,313,245,320,250)

###########################################################################################################################################
#
#           f_BoutonArriere()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers l'arrière
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonArriere():
        #
        # Met le violet du carré
        #
    Lja.current_color(135,50,110)
        #
        # Crée le cube basique
        #
    Lja.box(115,355,215,255)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(168,89,144) 
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(115,255,122,260,122,350,115,355)
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(115,255,122,260,208,260,215,255)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(112,39,90)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(215,255,208,260,208,350,215,355)
         #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(92,29,73)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(115,355,122,350,208,350,215,355)

###########################################################################################################################################
#
#           f_BoutonArriereClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers l'arrière quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonArriereClic():
        #
        # Met le violet du carré
        #
    Lja.current_color(94,34,76)
        #
        # Crée le cube basique
        #
    Lja.box(115,355,215,255)
        #
        # Met la couleur "violet clair" du reflet à gauche
        #
    Lja.current_color(125,66,107)
        #
        # Crée le reflet à gauche
        #  
    Lja.polygon(115,255,122,260,122,350,115,355)
        #
        # Met la couleur "violet clair-moyen" du reflet en haut
        #
    Lja.current_color(175,86,148)
        #
        # Crée le reflet en haut
        #
    Lja.polygon(115,255,122,260,208,260,215,255)
        #
        # Met la couleur "violet sombre-moyen" du reflet à droite
        #
    Lja.current_color(134,65,113)
        #
        # Crée le reflet à droite
        #
    Lja.polygon(215,255,208,260,208,350,215,355)
        #
        # Met la couleur "violet sombre" du reflet en bas
        #
    Lja.current_color(57,18,45)
        #
        # Crée le reflet en bas
        #
    Lja.polygon(115,355,122,350,208,350,215,355)