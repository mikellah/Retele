#!/usr/bin/env python
#1.2 Intoarce lungimea cuvantului
#server 
import socket
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Accept UDP datagrams, on the given port, from any sender
s.bind(("0.0.0.0", port))
print "waiting on port:", port
while 1:
    # Receive data
    data, addr = s.recvfrom(1024)
    print "Received:", data, "from", addr
    message = str(len(data))
    
    #Sending data
    print >>sys.stderr, 'sending data back to the client "%s"' %message
    s.sendto(message,addr)
    
    #Closing the server after giving answer
    #Or keep it open to listen further on by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break