#!/usr/bin/env python
#1.1Se transmite o litera de la client la server, serveru trimite inapoi litera dublata
#server 
import socket
import sys

port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", port))
print "waiting on port:", port
while True:
    data, addr = s.recvfrom(1024)
    # Receive data
    print "Received:", data, "from", addr
    data=data+data
    
    #Send back data
    print >>sys.stderr, 'sending data back to the client "%s"' %data
    s.sendto(data,addr)
    
    
    #Closing the server after giving answer
    #Or keep it open to listen further on by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break