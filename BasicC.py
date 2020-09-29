import socket
import time
import threading


PORT = 5050
HEADER = 16
FORMAT = 'utf-8'
DISCONECT_MSG = '!OUT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

CLIENT = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
CLIENT.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    CLIENT.send(send_len)
    CLIENT.send(message)

def recieve():
    msg_len = CLIENT.recv(HEADER).decode(FORMAT)
    if msg_len:
      msg_len= int(msg_len)
      msg = CLIENT.recv(msg_len).decode(FORMAT)
      print(msg)


connect = True
while connect:
  msg = input()
  if msg:
      send(msg)
  
  else:
    send(DISCONECT_MSG)
    print('You have disconnected!')
    quit()
  
  # recieve(CLIENT)
  threading.Thread(target=recieve).start()


# Protocol:
# ' [{name}] ~¬ {msg} '