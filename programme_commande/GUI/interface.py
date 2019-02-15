from . import PythonLja_18 as Lja
from . import gui as gui

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

def f_BoutonGauche():
    Lja.current_color(135,50,110)
    Lja.box(10,250,110,150)
    Lja.current_color(168,89,144)
    Lja.polygon(10,150,17,155,17,245,10,250)
    Lja.current_color(175,86,148)
    Lja.polygon(10,150,17,155,103,155,110,150)
    Lja.current_color(112,39,90)
    Lja.polygon(110,150,103,155,103,245,110,250)
    Lja.current_color(92,29,73)
    Lja.polygon(10,250,17,245,103,245,110,250)