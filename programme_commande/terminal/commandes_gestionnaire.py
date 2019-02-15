
def f_afficher_commande():
    print('affichage commandes')

def f_gerer_commande_utilisateur():

    valide = 0

    while valide != True:
        #
        # Demande a l'utilisateur ce qu'il veut que le robot fasse
        #
        print('Que voulez vous faire ?')
        commande = input('> ')

        #
        # Gestion de toutes les conditions des commandes AJOUTER PLUS TARD
        #
        #
        # Si l'utilisateur veut faire avancer le robot
        #
        if commande == 'avancer':
            valide = True
        #
        # Si l'utilisateur veut quitter
        #
        if commande == 'quitter':
            valide = True

    return commande
