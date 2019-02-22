###########################################################################################################################
#
#
# Module de gestion des erreurs
#
#
# Message predefinie, ne continent qu'une fonction, afficher les erreurs
#
#
###########################################################################################################################

def f_message_erreur(para_message_erreur):

	liste = []
	compt = 0

	while compt < len(para_message_erreur):
		liste.append("!")
		compt += 1

	cara_erreur = ""

	for e in liste:
		cara_erreur = cara_erreur + e

	print(cara_erreur)
	print(para_message_erreur)
	print(cara_erreur)


f_message_erreur("Erreur lors de l'ouverture du fichier")
