from . import PythonLja_18 as Lja

###########################################################################################################################################
#
#           f_creer_fenetre_attente()
#
#       para : largeur, hauteur
#
#       do :
#               Crée une fenêtre de dimensions données et affiche un message d'attente de connexion du robot
#
#       return : rien
#
###########################################################################################################################################

def f_creer_fenetre_attente(largeur, hauteur):

        #
        # Crée une fenêtre de dimensions données
        #

    Lja.init_window("Panneau de contrôle", largeur, hauteur)
     
        #
        # Affiche le texte "en attente de connexion..." au milieu de la fenêtre
        #

    Lja.text(largeur-largeur/2, hauteur-hauteur/2, "En attente de connexion...")

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
        # Récupère les coordonnées de la fenêtre pour les associer à longueur et à largeur
        #

    largeur = Lja.get_screen_width()
    hauteur = Lja.get_screen_height()
     
        #
        # Nettoie l'écran
        #

    Lja.clear_screen()
         
        #
        # Affiche le texte "connexion établie" aux coordonnées souhaitées
        #

    Lja.text(largeur//2, hauteur//2 ,"Connexion établie") 

###########################################################################################################################################
#
#           f_ouvrir_gestionnaire_commande()
#
#       para : aucun
#
#       do :
#               Demande à l'utilisateur les dimensions souhaitées de la fenêtre, puis crée la fenêtre d'interface graphique de commande
#
#       return : rien
#
###########################################################################################################################################

def f_ouvrir_gestionnaire():     

        #
        # Demande les coordonnées souhaitées pour la fenêtre à l'utilisateur
        #

    largeur = int(input("Saisissez la largeur de votre fenêtre: "))
    print('\n')
    hauteur = int(input("Saisissez la largeur de votre fenêtre: "))
     
        #
        # Affiche le message souhaité
        #

    print('Ouverture du gestionnaire via GUI')
         
        #
        # Crée la fenêtre d'interface graphique
        #

    f_creer_fenetre_attente(largeur,hauteur)
         
        #
        # Associe le clic gauche de la souris au démarrage du robot (A METTRE A JOUR)
        #

    Lja.assoc_button(1, f_creer_fenetre_projet)
     
        #
        # Fait durer la fenêtre sous Windows
        #

    Lja.main_loop()