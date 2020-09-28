import socket
import threading
import time

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
HEADER = 16
FORMAT = 'utf-8'
DISCONECT_MSG = '!OUT'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
  print(f'[SERVER] NEW CONNECTION: {addr} has connected')
  connected = True
  while connected:
    msg_len = conn.recv(HEADER).decode(FORMAT)
    if msg_len:
      msg_len= int(msg_len)
      msg = conn.recv(msg_len).decode(FORMAT)
      if msg == DISCONECT_MSG:
        connected = False
      print(msg)

  print(f'[CLIENT - {addr}] {msg}')
    

def start():
  server.listen()
  print(f'[SERVER] Listening on: {SERVER}')
  c=0
  while True:
    conn,addr = server.accept()
    thread = threading.Thread(target=handle_client(conn,addr))#,args=(conn,addr))
    print(f'[SERVER] ACTIVE Connections: {threading.activeCount()-1}')
    # handle_client(conn,addr)
    # c+=1
    # print(c)
  

print('[SERVER] Starting....')
start()