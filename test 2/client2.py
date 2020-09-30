from socket import *
from threading import *
try:
  from tkinter import *
except:
  pass

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = gethostbyname(gethostname())
portNumber = 7500

 

clientSocket.connect((hostIp, portNumber))

AKA=str(input('Hello Wellcome!\nEnter you Username:'))

win = Tk()
win.title(f"Connected To: {hostIp}:{portNumber} as {AKA}")

txtMessages = Text(win, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)
txtMessages.insert(END,'Type something to appear on the server (type HELP for more info)')

txtYourMessage = Entry(win, width=50)
txtYourMessage.insert(0,"Your message")
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

def getName():
  return gnn.get()
def commands(msg):
  commands = ['help','setname']
  if msg.lower() not in commands:
    return msg
  if msg == commands[0]:
    txtMessages.insert(END,'\nYou have typed HELP, the following commands are available to you:\n 1)To change your name: SETNAME')
  return '~¬Command'
def sendMessage():
    clientMessage = txtYourMessage.get()
    clientMessage=commands(clientMessage)
    if clientMessage != '~¬Command':
      myClientMessage = f'[{AKA}] {clientMessage}'
      clientMessage = f'{AKA}~¬ {clientMessage}'
      txtMessages.insert(END, "\n" + myClientMessage)
      clientSocket.send(clientMessage.encode("utf-8"))

btnSendMessage = Button(win, text="Send", width=20, command=sendMessage,bg='blue')
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        txtMessages.insert(END, "\n"+serverMessage)

recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

win.mainloop()