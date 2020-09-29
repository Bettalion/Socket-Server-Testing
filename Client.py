import socket
import time
import threading


PORT = 5050
HEADER = 16
FORMAT = 'utf-8'
DISCONECT_MSG = '!OUT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  try:
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
  except:
    pass

def recieve(conn):
  print('made it to  123456')
  try:
    msg_len = conn.recv(HEADER).decode(FORMAT)
    if msg_len:
      msg_len= int(msg_len)
      msg = conn.recv(msg_len).decode(FORMAT)
      print(msg)
  except:
    pass
def commands(msg):
 # help
 if msg == 'HELP':
      r = '''  To contribute to the chat type something and then press enter\n
  To exit chat press enter without typing\n
  To change your name type SETNAME''' # extend as neccesary
      print(r)
      return False
# set your name
 if msg.upper() in ['SET NAME','SETNAME']:
      aka=str(input('Enter your new name!'))
      msg = f'Name is changed to {aka}'
      return msg
 else:
   return msg

send('Hello SERVER - Bettalion')
connect = True
aka=str(input('Hello Wellcome!\nEnter you Username:'))
print('Type something to appear on the server or leave an empty (type HELP for more info)')
while connect:
  # recieve(client)
  print(((threading.activeCount()-1)))
  if ((threading.activeCount()-1)) < 1:
    threading.Thread(target=recieve,args=client).start()
    print(13456789009876)
  msg = input()
  if msg:
    msg=commands(msg)
    if msg !=  False:
      msg=f'[{aka}] ~¬ {msg}'
      send(msg)
  else:
    send(DISCONECT_MSG)
    print('You have disconnected!')
    quit()


# Protocol:
# ' [{name}] ~¬ {msg} '