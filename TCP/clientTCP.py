#!/usr/bin/env python
import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 2115)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    # Send data
    print >> sys.stderr, 'give data'
    message = raw_input()
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Receive data 
    data = sock.recv(100)
    print >>sys.stderr, 'received "%s"' % data, "from" , server_address
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()