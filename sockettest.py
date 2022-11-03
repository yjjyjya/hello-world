#服务器
import socket

s = socket.socket( , )
s.bind((, ))

s.listen()

while True:
    clt, adress = s.accept()
    print()
    clt.send(bytes())
    
#客户端
s = socket.socket( , )
s.connect((, )) #区别是这里的connect方法
msg = s.recv() #客户端从服务器获取信息





