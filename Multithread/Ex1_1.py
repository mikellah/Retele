#!/usr/bin/env python
#1.1 Se transmite o litera de la client la server, serveru trimite inapoi litera dublata
import time
import socket
from threading import Thread
def f(cs,i):
    while True:
        print ("Procesez client"+str(i))
        data=cs.recv(100)
        time.sleep(10)
        if not data : 
            print("No further data received from client"+str(i))
            break;
        #else do stuff with data 
        data = data+data
        #Send data back
        cs.send(data)
    #Close connection
    cs.close()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7777))
s.listen(5)
print("socket is listening") 
i=0
while True:
    i=i+1
    cs,addr=s.accept()
    print('Connected to :', addr[0], ':', addr[1])
    t=Thread(target=f,args=(cs,i,))
    t.start()
s.close()