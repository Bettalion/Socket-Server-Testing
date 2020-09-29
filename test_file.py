# import threading
# from time import sleep as ts

# def r():
#  print('hey')

# t = threading.Thread(target=r).start()


# print(threading.activeCount())
# ts(5)
# print(threading.activeCount())
def format_txt(msg):
  if msg == 'HELP':
    r = '''To ocntribute to the chat type something and then press enter\n
To exit chat press enter without typing\n
To change your name type SETNAME'''
    print(r)
  if msg.upper() in ['SET NAME','SETNAME']:
    input()


format_txt(i)
