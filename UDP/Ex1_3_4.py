#!/usr/bin/env python
# 1.3/1.4 Intoarce numarul vocalelor/consoanelor
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
    
    #Do stuff with it 
    num_vowels=0
    for char in data:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    message = str(num_vowels)
    message2 = str(len(data)-num_vowels)
    
    #Send result back to client
    s.sendto("Vocale : " + message + " Consoane : "+message2,addr)
    
    #Closing the server after giving answer
    #Or keep it open to listen further on by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break
    