import threading
from time import sleep as ts

def r(se=1):
  ts(5)
  if se == '2':
    ts(5)
    print(34)
  print('ran')

t = threading.Thread(target=r,args='2').start()
t = threading.Thread(target=r).start()
t = threading.Thread(target=r).start()
