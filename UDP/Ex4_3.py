#!/usr/bin/env python
#4.3. Intoarce suma cifrelor din IP-ul clientului
#server 
import socket
import sys

port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Accept UDP datagrams, on the given port, from any sender
s.bind(("0.0.0.0", port))
print "waiting on port:", port
while True:
 # Receive data
    data, addr = s.recvfrom(1024)
    print "Received:", data, "from", addr
    
    list = addr[0].split(".")
    sum = 0 
    for number in list : 
        sum = sum + int(number)
    message=str(sum)
    print >>sys.stderr, 'sending data back to the client "%s"' %message
     
    s.sendto(message,addr)
    #Closing the server after giving answer
    #Or keep it open to listen further on by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break