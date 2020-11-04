#!/usr/bin/env python
# Clientul trimite 2 numere, serverul intoarce suma
#server 
import socket
import sys
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", port))
print "waiting on port:", port
while 1:
    # Receive data
    data, addr = s.recvfrom(1024)
    print "Received:", data, "from", addr
    list = data.split()
    sum = 0 
    for number in list : 
        sum = sum + int(number) 
    message = str(sum)
    
    # Send back the data
    print >>sys.stderr, 'sending data back to the client "%s"' %message
    s.sendto(message,addr)
    
    #Closing the server after giving answer
    #Or keep it open by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break