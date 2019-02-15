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
    Lja.current_color("red")
    Lja.circle(935,735,50,20)
    Lja.line(895,695,970,770,20)