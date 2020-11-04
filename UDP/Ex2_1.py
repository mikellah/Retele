#!/usr/bin/env python
# Intoare cuvintele concatenate
#server 
import socket
import sys
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Accept UDP 
s.bind(("0.0.0.0", port))
print ("waiting on port:", port)
while True:
    # Receive data
    data, addr = s.recvfrom(1024)
    print ("Received:", data, "from", addr)
    
    #Do stuff
    list = data.split()
    message =''
    for string in list : 
        message = message + string 
        
    # Send back the data
    print >>sys.stderr, 'sending data back to the client "%s"' %message
    s.sendto(message ,addr)
    
    #Closing the server after giving answer
    #Or keep it open by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break