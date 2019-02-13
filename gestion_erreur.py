
###########################################################################################################################################
#
# Module de gestion d'erreur
#
# Premet de gerer les erreurs dans les differents fichiers
#
###########################################################################################################################################

def f_gestion_erreur(para_fonction):

    try:
        para_fonction()
    except Exception as socket.error:
        print('Une erreur a ete genere')
    except:
        pass
    finally:
        pass
