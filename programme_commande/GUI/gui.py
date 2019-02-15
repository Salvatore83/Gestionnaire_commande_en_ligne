from . import PythonLja_18 as Lja
from . import interface as logo


    #
    # Définition des dimensions de la fenêtre
    #

largeur = 1000
hauteur = 800

###########################################################################################################################################
#
#           f_creer_fenetre_attente()
#
#       para : aucun
#
#       do :
#               Crée une fenêtre de dimensions données et affiche un message d'attente de connexion du robot
#
#       return : rien
#
###########################################################################################################################################

def f_creer_fenetre_attente():
    
        #
        # Crée une fenêtre de dimensions données
        #

    Lja.init_window("Projet", largeur, hauteur)
         
        #
        # Affiche le texte "en attente de connexion..." au milieu de la fenêtre
        #
    Lja.current_font("calibri", 20, "center", "black")
    Lja.text(largeur/2, hauteur/2, "En attente de connexion...")
        
###########################################################################################################################################
#
#           f_creer_fenetre_projet()
#
#       para : aucun
#
#       do :
#               Affiche l'interface graphique de commande
#
#       return : rien
#
###########################################################################################################################################    

def f_creer_fenetre_projet():
    
        #
        # Nettoie l'écran
        #

    Lja.clear_screen()
             
        #
        # Affiche le texte "connexion établie" aux coordonnées souhaitées
        #

    Lja.text(largeur/2, hauteur/2, "connexion établie")
    Lja.clear_screen()

        #
        # Trace le logo "interdit" dans l'interface graphique
        #

    logo.f_arret()

###########################################################################################################################################
#
#           f_ouvrir_gestionnaire_commande()
#
#       para : aucun
#
#       do :
#               Crée la fenêtre d'interface graphique de commande dès que la connexion est établie
#
#       return : rien
#
###########################################################################################################################################


def f_ouvrir_gestionnaire():    

        #
        # Affiche le message souhaité
        #

    print('Ouverture du gestionnaire via GUI')
             
        #
        # Crée la fenêtre d'interface graphique
        #

    f_creer_fenetre_attente()
             
        #
        # Associe le clic gauche de la souris au démarrage du robot (A METTRE A JOUR)
        #
    Lja.assoc_button(1,f_creer_fenetre_projet)
         
        #
        # Fait durer la fenêtre sous Windows
        #

    Lja.main_loop()