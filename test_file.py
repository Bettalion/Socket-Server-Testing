import threading

def r():
  print('ran')

t = threading.Thread(target=r())