from . import PythonLja_18 as Lja
from . import interfacef as img
from . import connexion_gestion as cg

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
    print("Attente de connexion du robot au gestionnaire")
    socket_serveur = cg.f_creer_serveur()
    socket_client = cg.f_accepter_connexion(socket_serveur)
    cg.f_envoyer_message(socket_client, "1")
    # cg.f_attendre_robot_pret(socket_client, 0)
    f_creer_fenetre_projet(socket_serveur, socket_client)

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


def f_creer_fenetre_projet(para_socket_serveur, para_socket_client):
    #
    # Affiche tous les éléments qui constituent la fenêtre
    #
    img.f_fondnoir(para_socket_serveur, para_socket_client)
    img.f_fondcroix()
    img.f_croixhaut()
    img.f_croixgauche()
    img.f_croixdroite()
    img.f_croixbas()
    img.f_carreb()
    img.f_carreo()
    img.f_carrevi()
    img.f_carreve()
    img.indications()
    img.f_layers()

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
    # Lja.assoc_button(3, f_creer_fenetre_projet)
    Lja.main_loop()
