#!/usr/bin/env python
#server 
import socket
import sys

port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print "waiting on port:", port
while True:
 # Receive data
    data, addr = s.recvfrom(1024)
    print "Received:", data, "from", addr
    list = data.split()
    sum = 0 
    for number in list : 
        sum = sum + int(number)
    message=str(sum)
    
    print >>sys.stderr, 'sending data back to the client "%s"' %message
    s.sendto(message,addr)
    #Closing the server after giving answer
    #Or keep it open by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break