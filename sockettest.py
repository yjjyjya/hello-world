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
msg = s.recv(1024) #客户端从服务器获取信息，一次传输最多1024Bytes

#CS交互
#写好两个py文件后，打开两个终端分别运行



