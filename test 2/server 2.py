from socket import *
import threading

print('[SERVER] Starting....')

clients = set()


def clientThread(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(1024).decode("utf-8")
        print(clientAddress[0] + ":" + str(clientAddress[1]) +": "+ message)
        for client in clients:
            if client is not clientSocket:
                try:
                    name,msg = f"[{message.split('~¬')[0]}]",f"{message.split('~¬')[1]}"
                    client.send((name+msg).encode("utf-8"))
                except:
                    client.send((clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message).encode("utf-8"))
                    print('Failed to split name')

        if not message:
            clients.remove(clientSocket)
            print(f'[CLIENT] {clientAddress[0]}:{clientAddress[1]} disconnected')
            break

    clientSocket.close()

hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

hostIp = gethostbyname(gethostname())
portNumber = 7500

hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print(f'[SERVER] Listening on {hostIp} ...')


while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.add(clientSocket)
    print (f'[SERVER] NEW CONNECTION: {clientAddress[0]}:{clientAddress[1]} has connected')
    thread = threading.Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()
    print(f'[SERVER] Active Connections: {threading.activeCount()-1}')