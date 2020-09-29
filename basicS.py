import socket
import threading
import time

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
HEADER = 16
FORMAT = 'utf-8'
DISCONECT_MSG = '!OUT'
ACTIVE_CONN= []

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def send(msg,conn):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    conn.send(send_len)
    conn.send(message)

def recieve(conn):
    msg_len = conn.recv(HEADER).decode(FORMAT)
    if msg_len:
      msg_len= int(msg_len)
      msg = conn.recv(msg_len).decode(FORMAT)
      print(msg)
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
        print(f'[CLIENT - {addr}] {msg}')

        for c in ACTIVE_CONN:
            send(msg,c)


  ACTIVE_CONN.remove(conn)
  conn.close()
    

def start_s():
  server.listen()
  print(f'[SERVER] Listening on: {SERVER}')
  while True:
    conn,addr = server.accept()
    ACTIVE_CONN.append(conn)
    print(ACTIVE_CONN)
    thread = threading.Thread(target=handle_client,args=(conn,addr))
    thread.start()
    print(f'active connections: {threading.activeCount()-1}')


print('[SERVER] Starting....')
start_s()

# to do:
# add a way for others to see others message