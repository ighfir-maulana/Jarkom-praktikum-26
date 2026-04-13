from socket import *

# membuat socket untuk server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# menghubungkan (bind) socket dengan port
serverSocket.bind(
    ("", serverPort)
    )

print("[SYSTEM] Server siap digunakan")

running = True
while running:
    # menerima pesan dari client
    message, clientAddress = serverSocket.recvfrom(2048)
    
    print("[SYSTEM] Pesan telah diterima dari: ", clientAddress)
    
    decodedMessage = message.decode()
    
    if decodedMessage.lower() == "exit":
        print("[SYSTEM] Server telah diberhentikan")
        running = False
        continue
    
    modifiedMessage = decodedMessage.upper()
    print("[SERVER] diterima dari ", clientAddress, "message: ", decodedMessage)
    
    # mengirim pesan kembali ke client
    serverSocket.sendto(
        modifiedMessage.encode(),
        clientAddress
    )
serverSocket.close()
print("[SYSTEM] Socket server telah ditutup")