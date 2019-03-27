#
#
#
#
#
# Imports: Interface graphique (PythonLja), Le gestionnaire de l'interface graphique (gui), et le répertoire d'animations graphiques (actions)
#
#
#
#
#

from . import PythonLja_18 as Lja
from . import gui as gui
from . import actions as act

#
#
#
#
#
# Bouton d'arrêt (logo"interdit")
#
#
#
#
#

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
    Lja.circle(735,535,50,20) 
        #
        # Trace la barre transversale
        #
    Lja.line(695,495,770,570,20)

###########################################################################################################################################
#
#           f_ArretClic()
#
#       para : aucun
#
#       do :
#               Crée le logo "interdit" qui servira a couper toute action en cours du robot dans son apparence cliquée
#
#       return : rien
#
###########################################################################################################################################

def f_ArretClic():
        #
        # Met du rouge
        #
    Lja.current_color(186,0,0)
        #
        # Trace le cercle du logo
        #
    Lja.circle(735,535,50,20) 
        #
        # Trace la barre transversale
        #
    Lja.line(695,495,770,570,20)

#
#
#
#
#
# RADAR
#
#
#
#
#

###########################################################################################################################################
#
#           f_Radar()
#
#       para : aucun
#
#       do :
#               Crée le radar
#
#       return : rien
#
###########################################################################################################################################

def f_Radar():
    Lja.current_color("green")
    Lja.disc(533,115,100)

#
#
#
#
# Touches Directionnelles Basiques et leurs Animations de Clic (Ordre de définition: Direction1, Clic1, Direction2, Clic2 ...)
#
#
#
#
#

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
    #
    # FLECHE
    #
        #
        # Applique la couleur noire
        #
    Lja.current_color("black")
        #
        # Crée le triangle
        #
    Lja.polygon(37,200,74,175,74,225)


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
    #
    # FLECHE
    #
        #
        # Applique la couleur blanche
        #
    Lja.current_color("white")
        #
        # Crée le triangle
        #
    Lja.polygon(37,200,74,175,74,225)

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
    #
    # FLECHE
    #
        #
        # Applique la couleur noire
        #
    Lja.current_color("black")
        #
        # Crée le triangle
        #
    Lja.polygon(165,70,140,115,190,115)

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
    #
    # FLECHE
    #
        #
        # Applique la couleur blanche
        #
    Lja.current_color("white")
        #
        # Crée le triangle
        #
    Lja.polygon(165,70,140,115,190,115)


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
    #
    # FLECHE
    #
        #
        # Applique la couleur noire
        #
    Lja.current_color("black")
        #
        # Crée le triangle
        #
    Lja.polygon(295,200,253,175,253,225)

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
    #
    # FLECHE
    #
        #
        # Applique la couleur blanche
        #
    Lja.current_color("white")
        #
        # Crée le triangle
        #
    Lja.polygon(295,200,253,175,253,225)

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
    #
    # FLECHE
    #
        #
        # Applique la couleur noire
        #
    Lja.current_color("black")
        #
        # Crée le triangle
        #   
    Lja.polygon(165,330,140,288,190,288)

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
    #
    # FLECHE
    #
        #
        # Applique la couleur blanche
        #
    Lja.current_color("white")
        #
        # Crée le triangle
        #
    Lja.polygon(165,330,140,288,190,288)


#
#
#
#
#
# Boutons d'action prédéfinie de direction (Le robot bouche d'une distance x)
#
#
#
#
#

###########################################################################################################################################
#
#           f_BoutonDistanceDefinieHaut()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers le haut sur une distance définie
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieHaut():
    #
    # Met le bleu du bouton
    #
    Lja.current_color("blue")
    #
    # Crée le rectangle basique
    #
    Lja.box(60,415,270,385)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(77,107,206)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,385,65,390,65,410,60,415)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(59,114,155)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,385,65,390,265,390,270,385)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(5,5,81)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,385,265,390,265,410,270,415)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(0,0,73)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,415,65,410,265,410,270,415)

###########################################################################################################################################
#
#           f_BoutonDistanceDefinieHautClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers le haut sur une distance définie quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieHautClic():
    #
    # Met le bleu du bouton
    #
    Lja.current_color(18,23,186)
    #
    # Crée le rectangle basique
    #
    Lja.box(60,415,270,385)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(55,83,175)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,385,65,390,65,410,60,415)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(40,85,119)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,385,65,390,265,390,270,385)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(3,3,50)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,385,265,390,265,410,270,415)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(2,3,28)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,415,65,410,265,410,270,415)

###########################################################################################################################################
#
#           f_BoutonDistanceDefinieBas()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers le bas sur une distance définie
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieBas():
    #
    # Met le bleu du bouton
    #
    Lja.current_color("blue")
    #
    # Crée le rectangle basique
    #
    Lja.box(60,455,270,425)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(77,107,206)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,425,65,430,65,450,60,455)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(59,114,155)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,425,65,430,265,430,270,425)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(5,5,81)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,425,265,430,265,450,270,455)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(0,0,73)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,455,65,450,265,450,270,455)

###########################################################################################################################################
#
#           f_BoutonDistanceDefinieBasClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers le bas sur une distance définie quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieBasClic():
    #
    # Met le bleu du bouton
    #
    Lja.current_color(18,23,186)
    #
    # Crée le rectangle basique
    #
    Lja.box(60,455,270,425)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(55,83,175)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,425,65,430,65,450,60,455)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(40,85,119)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,425,65,430,265,430,270,425)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(3,3,50)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,425,265,430,265,450,270,455)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(2,3,28)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,455,65,450,265,450,270,455)


###########################################################################################################################################
#
#           f_BoutonDistanceDefinieGauche()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la gauche sur une distance définie
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieGauche():
    #
    # Met le bleu du bouton
    #
    Lja.current_color("blue")
    #
    # Crée le rectangle basique
    #
    Lja.box(60,495,270,465)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(77,107,206)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,465,65,470,65,490,60,495)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(59,114,155)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,465,65,470,265,470,270,465)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(5,5,81)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,465,265,470,265,490,270,495)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(0,0,73)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,495,65,490,265,490,270,495)

###########################################################################################################################################
#
#           f_BoutonDistanceDefinieGaucheClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la gauche sur une distance définie quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieGaucheClic():
    #
    # Met le bleu du bouton
    #
    Lja.current_color(18,23,186)
    #
    # Crée le rectangle basique
    #
    Lja.box(60,495,270,465)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(55,83,175)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,465,65,470,65,490,60,495)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(40,85,119)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,465,65,470,265,470,270,465)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(3,3,50)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,465,265,470,265,490,270,495)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(2,3,28)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,495,65,490,265,490,270,495)


###########################################################################################################################################
#
#           f_BoutonDistanceDefinieDroite()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la droite sur une distance définie
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieDroite():
    #
    # Met le bleu du bouton
    #
    Lja.current_color("blue")
    #
    # Crée le rectangle basique
    #
    Lja.box(60,535,270,505)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(77,107,206)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,505,65,510,65,530,60,535)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(59,114,155)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,505,65,510,265,510,270,505)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(5,5,81)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,505,265,510,265,530,270,535)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(0,0,73)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,535,65,530,265,530,270,535)

###########################################################################################################################################
#
#           f_BoutonDistanceDefinieDroiteClic()
#
#       para : aucun
#
#       do :
#               Crée le bouton de direction (de déplacement) du robot vers la droite sur une distance définie quand il est cliqué
#
#       return : rien
#
###########################################################################################################################################

def f_BoutonDistanceDefinieDroiteClic():
    #
    # Met le bleu du bouton
    #
    Lja.current_color(18,23,186)
    #
    # Crée le rectangle basique
    #
    Lja.box(60,535,270,505)
    #
    # Crée la couleur "bleu très clair" pour le reflet à gauche du rectangle
    #
    Lja.current_color(55,83,175)
    #
    # Crée le reflet "bleu très clair" à gauche du rectangle
    #
    Lja.polygon(60,505,65,510,65,530,60,535)
    #
    # Crée la couleur "bleu clair" pour le reflet en haut du rectangle
    #
    Lja.current_color(40,85,119)
    # 
    # Crée le reflet "bleu clair" en haut du rectangle
    #
    Lja.polygon(60,505,65,510,265,510,270,505)
    #
    # Crée la couleur "bleu sombre" pour le reflet à droite du rectangle
    #
    Lja.current_color(3,3,50)
    #
    # Crée le reflet "bleu sombre" à droite du rectangle
    #
    Lja.polygon(270,505,265,510,265,530,270,535)
    #
    # Crée la couleur "bleu très sombre" en bas du rectangle
    #
    Lja.current_color(2,3,28)
    #
    # Crée le reflet "bleu très sombre" en bas du rectangle
    #
    Lja.polygon(60,535,65,530,265,530,270,535)

