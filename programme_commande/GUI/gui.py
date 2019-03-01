#
#
#
#
#
# Imports: Interface graphique (PythonLja),  le répertoire des objets graphiques (interface), et le répertoire d'animations graphiques (actions)
#
#
#
#
#

from . import PythonLja_18 as Lja
from . import interface as logo
from . import actions as act

#
# Définition des dimensions de la fenêtre
#
largeur = 800
hauteur = 600

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
        #
        # Nettoie l'écran
        #
    Lja.clear_screen()
        #
        # Trace le logo "interdit" dans l'interface graphique
        #
    logo.f_arret()
        #
        # Trace le bouton de gauche dans l'interface graphique
        #
    logo.f_BoutonGauche()
        #
        # Trace le bouton du haut (vers l'avant) dans l'interface graphique
        #
    logo.f_BoutonAvant()
        #
        # Trace le bouton de droite dans l'interface graphique
        #
    logo.f_BoutonDroite()
        #
        # Trace le bouton du bas (vers l'arrière) dans l'interface graphique
        #
    logo.f_BoutonArriere()
        #
        # Trace le bouton du haut (vers le haut) d'une distance donnée dans l'interface graphique
        #
    logo.f_BoutonDistanceDefinieHaut()
        #
        # Trace le bouton du milieu haut (vers le bas) d'une distance donnée dans l'interface graphique
        #
    logo.f_BoutonDistanceDefinieBas()

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
        # Associe le clic droit de la souris au démarrage du robot (A METTRE A JOUR)
        #
    Lja.assoc_button(3,f_creer_fenetre_projet)
        #
        # Fait durer la fenêtre sous Windows
        #
    Lja.main_loop()