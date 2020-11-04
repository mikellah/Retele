#!/usr/bin/env python
#client
import socket
import sys

port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1',port)
print >>sys.stderr, 'connecting to %s port %s' % server_address
# Send message 
print >> sys.stderr, 'give data'
message = raw_input()
print >>sys.stderr, 'sending "%s"' % message
s.sendto(message, (server_address))

#Print received message from host/server 
data = s.recv(100)
print >>sys.stderr, 'received "%s"' % data, "from" , server_address 