###########################################################################################################################################
#
# Module principale (premier lance dans le programme) du gestionnaire de commande
#
# Permet d'ouvrir le gestionnaire de commande soit via terminal soit via interface graphique
#
###########################################################################################################################################

#
# IMPORTS
#

import terminal.terminal as terminal
import GUI.gui as gui


###########################################################################################################################################
#
#           f_ouvrir_gestionnaire_commande()
#
#       para : aucun
#
#       do :
#               demande a l'utilisateur quel gestionnaire il veut ouvrir
#
#       return : rien
#
###########################################################################################################################################

def f_ouvrir_gestionnaire_commande():

    demande = True

    #
    # demande a l'utilisateur tant qu'une des options n'a pas ete selectionnee
    #
    while demande != False:

        print('Quel gestionnaire voulez vous ouvrir ?')
        print('[term/GUI/quitter]')
        ouvrir = input('> ')

        #
        # SI l'utilisateur veut quitter
        #
        if ouvrir.lower() == 'quitter':
            demande = False

        #
        # SI l'utilisateur veut ouvrir le gestionnaire de commandes via terminal
        #
        elif ouvrir.lower() == 'term':

            #
            # Ouvre le gestionnaire via terminal
            #
            terminal.f_ouvrir_gestionnaire()
            demande = False

        #
        # SI l'utilisateur veut ouvrir le gestionnaire de commandes via GUI / interface graphique
        #
        elif ouvrir.upper() == 'GUI':

            #
            # Ouvre le gestionnaire via GUI
            #
            gui.f_ouvrir_gestionnaire()
            demande = False

        #
        # SI l'utilisateur a entre une action qui n'a pas ete definie
        #
        else:
            print('\n')
            print("!!! Votre commande n'est pas definie !!!")
            print('\n')


if __name__ == '__main__':
    f_ouvrir_gestionnaire_commande()
