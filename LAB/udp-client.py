from socket import *

serverName = "localhost"
serverPort = 12000

#AF_INET = IP ADRR V4 | SOCK_DGRAM = UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

running = True
while running:
    message = input("> ") #input dari users
    
    if message.lower() == "exit":
        clientSocket.sendto(
            message.encode(),
            
            (serverName, serverPort)
        )
        print("[SYSTEM] Keluar dari program")
        running = False
        continue
    
    clientSocket.sendto(
            message.encode(),
            
            (serverName, serverPort)
        )
    clientSocket.recvfrom(2048)
    
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    
    print("[SYSTEM] Pesan telah diterima dari: ", serverAddress)
    print(modifiedMessage.decode())
    
clientSocket.close()
print("[SYSTEM] Koneksi telah ditutup")