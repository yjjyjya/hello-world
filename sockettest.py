import socket

s = socket.socket( , )
s.bind((, ))

s.listen()

while True:
    clt, adress = s.accept()
    print()
    clt.send(bytes())
    
