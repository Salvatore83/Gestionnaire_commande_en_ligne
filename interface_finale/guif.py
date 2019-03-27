import PythonLja_18 as Lja
import interfacef as img

hauteur = 800
largeur = 600

def f_creer_fenetre_attente():
    Lja.init_window("Projet", 800,600)

def f_creer_fenetre_projet():
    img.f_fondnoir()
    img.f_fondcroix()
    img.f_croixhaut()
    img.f_croixgauche()
    img.f_croixdroite()
    img.f_croixbas()
    img.f_carreb()
    img.f_carreo()
    img.f_carrevi()
    img.f_carreve()
    """
    img.f_tracer_image(img.liste[0],390,300,200,400)
    img.f_tracer_image(img.liste [1],80,80,200,550)
    """

def f_ouvrir_gestionnaire():
    f_creer_fenetre_attente()
    Lja.assoc_button(3, f_creer_fenetre_projet)
    Lja.main_loop()

f_ouvrir_gestionnaire()