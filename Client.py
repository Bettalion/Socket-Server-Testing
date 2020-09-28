import socket
import time

PORT = 5050
HEADER = 16
FORMAT = 'utf-8'
DISCONECT_MSG = '!OUT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_len = len(message)
  send_len = str(msg_len).encode(FORMAT)
  send_len += b' '*(HEADER - len(send_len))
  client.send(send_len)
  client.send(message)

send('Hello SERVER - Bettalion')

send(DISCONECT_MSG)
print('done')