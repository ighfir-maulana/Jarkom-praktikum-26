from socket import *

# membuat socket untuk server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# menghubungkan (bind) socket dengan port
serverSocket.bind(
    ("", serverPort)
    )