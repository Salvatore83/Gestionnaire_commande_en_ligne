
###########################################################################################################################################
#
#
#
#
#
###########################################################################################################################################

def f_creer_socket_client():

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 5566
    socket_client.bind((host, port))

    return socket_client
