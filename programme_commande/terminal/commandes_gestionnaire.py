
def f_afficher_commande():
    print('affichage commandes')

def f_gerer_commande_utilisateur():

    valide = 0

    while valide != True:
        print('Que voulez vous faire ?')
        commande = input('> ')

        #
        # Gestion de toutes les conditions des commandes AJOUTER PLUS TARD
        #
        if commande == 'avancer':
            valide = True
        if commande == 'quitter':
            valide = True

    return commande
