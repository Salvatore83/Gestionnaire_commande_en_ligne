import PythonLja_18 as Lja

"""
global liste
liste = ["rectangle.png", "thaut.png"]
"""

largeur = 800
hauteur = 600

def f_fondnoir():
    Lja.clear_screen()
    Lja.current_color(22,22,22)
    Lja.box(0,600,800,0)
    Lja.current_font("calibri", 10,"center", "red")
    Lja.text(200,400,"bleu")

def f_tracer_image(para_nom, width, height, pos_x, pos_y):
    global image
    image = Lja.image(para_nom, width, height)
    Lja.image_draw(pos_x, pos_y, image)

def f_fondcroix():
    global fondcroix
    fondcroix = Lja.image("rectangle.png", 390,300)
    Lja.image_draw(205,455, fondcroix)

def f_croixhaut():
    global thaut
    thaut = Lja.image("thaut.png",80,80)
    Lja.image_draw(200,530,thaut)

def f_croixgauche():
    global tgauche
    tgauche = Lja.image("tgauche.png",80,80)
    Lja.image_draw(127,457,tgauche)

def f_croixdroite():
    global tdroite
    tdroite = Lja.image("tdroite.png",80,80)
    Lja.image_draw(273,457,tdroite)

def f_croixbas():
    global tbas
    tbas = Lja.image("tbas.png",80,80)
    Lja.image_draw(200,384,tbas)

def f_carreb():
    global carreb
    carreb = Lja.image("bleu.png",80,80)
    Lja.image_draw(480,95,carreb)

def f_carreo():
    global carreo
    carreo = Lja.image("orange.png",80,80)
    Lja.image_draw(570,95, carreo)

def f_carrevi():
    global carrevi
    carrevi = Lja.image("violet.png",80,80)
    Lja.image_draw(660,95, carrevi)

def f_carreve():
    global carreve
    carreve = Lja.image("vert.png",80,80)
    Lja.image_draw(750,95, carreve)
"""
def f_layerdroitecroix():
    global ldc
    ldc = Lja.image("layerdroitecroix.png",350,350)
    Lja.image_draw(415,455,ldc)
"""