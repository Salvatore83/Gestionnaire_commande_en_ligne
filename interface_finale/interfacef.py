import PythonLja_18 as Lja

largeur = 800
hauteur = 600
global BoutonActif

###########################################################################################################################################
#
#           f_fondnoir()
#
#       para : aucun
#
#       do :
#               Crée le fond gris foncé de l'interface graphique
#
#       return : rien
#
###########################################################################################################################################

def f_fondnoir():
        #
        # Nettoie l'écran
        #
    Lja.clear_screen()
        #
        # La couleur des prochains éléments tracés sera un gris foncé
        #
    Lja.current_color(22,22,22)
        #
        # Crée le fond de la taille de la fenêtre
        #
    Lja.box(0,600,800,0)

###########################################################################################################################################
#
#           f_fondcroix()
#
#       para : aucun
#
#       do :
#               Crée le rectangle gris clair qui accueille la croix directionnelle
#
#       return : rien
#
###########################################################################################################################################

def f_fondcroix():
    global fondcroix
    #
    # Importe l'image correspondante et la redimensionne
    #
    fondcroix = Lja.image("images/rectangle.png", 390,300)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(205,455, fondcroix)

###########################################################################################################################################
#
#           f_croixDIRECTION()
#
#       para : aucun
#
#       do :
#               Crée les flèches qui constituent la croix directionnelle
#
#       return : rien
#
###########################################################################################################################################

def f_croixhaut():
    global thaut
    #
    # Importe l'image correspondante et la redimensionne
    #
    thaut = Lja.image("images/thaut.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(200,530,thaut)

def f_croixgauche():
    global tgauche
    #
    # Importe l'image correspondante et la redimensionne
    #
    tgauche = Lja.image("images/tgauche.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(127,457,tgauche)

def f_croixdroite():
    global tdroite
    #
    # Importe l'image correspondante et la redimensionne
    #
    tdroite = Lja.image("images/tdroite.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(273,457,tdroite)

def f_croixbas():
    global tbas
    #
    # Importe l'image correspondante et la redimensionne
    #
    tbas = Lja.image("images/tbas.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(200,384,tbas)

###########################################################################################################################################
#
#           f_carréINDEXCOULEUR()
#
#       para : aucun
#
#       do :
#               Crée les quatre boutons de couleur pour les actions particulières
#
#       return : rien
#
###########################################################################################################################################

def f_carreb():
    global carreb
    #
    # Importe l'image correspondante et la redimensionne
    #
    carreb = Lja.image("images/bleu.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(480,95,carreb)

def f_carreo():
    global carreo
    #
    # Importe l'image correspondante et la redimensionne
    #
    carreo = Lja.image("images/orange.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(570,95, carreo)

def f_carrevi():
    global carrevi
    #
    # Importe l'image correspondante et la redimensionne
    #
    carrevi = Lja.image("images/violet.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(660,95, carrevi)

def f_carreve():
    global carreve
    #
    # Importe l'image correspondante et la redimensionne
    #
    carreve = Lja.image("images/vert.png",80,80)
    #
    # Applique l'image aux coordonnées demandées
    #
    Lja.image_draw(750,95, carreve)

def f_layers():
    global degrade
    degrade = Lja.image("images/degrade.png",800,50)
    Lja.image_draw(400,25,degrade)
    global layergauchecarres
    layergauchecarres = Lja.image("images/layergauchecarres.png",15,99)
    Lja.image_draw(425,105,layergauchecarres)

###########################################################################################################################################
#
#           f_RecupCoord()
#
#       para : aucun
#
#       do :
#               Rend l'interface cliquable
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
    #
    # Pour l'instant, aucun bouton n'est actif.
    #
    BoutonActif = 0
    #
    # Déclare et importe toutes les apparences cliquées des boutons
    #
    global carrebclic
    carrebclic = Lja.image("images/bleuclic.png",80,80)
    global carreoclic
    carreoclic = Lja.image("images/orangeclic.png",80,80)
    global carrevioclic
    carrevioclic = Lja.image("images/violetclic.png",80,80)
    global carreverclic
    carreverclic = Lja.image("images/vertclic.png",80,80)
    global thautclic
    thautclic = Lja.image("images/thautclic.png",80,80)
    global tgaucheclic
    tgaucheclic = Lja.image("images/tgaucheclic.png",80,80)
    global tdroiteclic
    tdroiteclic = Lja.image("images/tdroiteclic.png",80,80)
    global tbasclic
    tbasclic = Lja.image("images/tbasclic.png",80,80)
    #
    # Si le curseur est dans le carré bleu:
    #
    if 440 < sourisx < 520 and 465 < sourisy < 545:
        #
        # Applique l'apparence cliquée
        #
        Lja.image_draw(480,95,carrebclic)
        BoutonActif = 1
    #
    # Sinon, s'il est dans le carré orange:
    #
    elif 530 < sourisx < 610 and 465 < sourisy < 545:
        #
        # Applique l'apparence cliquée
        #
        Lja.image_draw(570,95,carreoclic)
        BoutonActif = 2
    #
    # Sinon, s'il est dans le carré violet:
    #
    elif 620 < sourisx < 700 and 465 < sourisy < 545:
        #
        # Applique l'apparence cliquée
        #
        Lja.image_draw(660,95,carrevioclic)
        BoutonActif = 3
    #
    # Sinon, s'il est dans le carré vert:
    #
    elif 710 < sourisx < 790 and 465 < sourisy < 545:
        #
        # Applique l'apparence cliquée
        #
        Lja.image_draw(750,95,carreverclic)
        BoutonActif = 4
    #
    # Sinon, s'il est dans la flèche du haut:
    #
    elif 162 < sourisx < 238 and 38 < sourisy < 103:
        #
        # Applique l'apparence cliquée
        #
        Lja.image_draw(200,530,thautclic)
        BoutonActif = 5
    #
    # Sinon, s'il est dans la flèche de gauche:
    #
    elif 93 < sourisx < 160 and 104 < sourisy < 182:
        #
        # Applique l'apparence cliquée
        #
        Lja.image_draw(127,457,tgaucheclic)
        BoutonActif = 6
    #
    # Sinon, s'il est dans la flèche de droite:
    #
    elif 240 < sourisx < 307 and 104 < sourisy < 182:
        #
        # Applique l'apparence cliquée 
        #
        Lja.image_draw(273,457,tdroiteclic)
        BoutonActif = 7
    #
    # Sinon, s'il est dans la flèche du bas:
    #
    elif 162 < sourisx < 238 and 183 < sourisy < 248:
        #
        # Applique l'apparence cliquée
        #
        Lja.image_draw(200,384,tbasclic)
        BoutonActif = 8

def indications():
    Lja.current_font("calibri",20,"center", "lightblue")
    Lja.text(60,400,"Bleu :")
    Lja.current_font("calibri",20,"center", "orange")
    Lja.text(75,430,"Orange :")
    Lja.current_font("calibri",20,"center", "purple")
    Lja.text(67,460,"Violet :")
    Lja.current_font("calibri",20,"center", "green")
    Lja.text(60,490,"Vert :")
    Lja.current_font("calibri",20,"center", "white")
    Lja.text(270,400," Action 1, remplir dans interfacef")
    Lja.text(170,430," Action 2")
    Lja.text(155,460," Action 1")
    Lja.text(145,490," Action 4")

#
# Associe le clic gauche au fait de pouvoir cliquer
# 
Lja.assoc_button(1,f_RecupCoord)