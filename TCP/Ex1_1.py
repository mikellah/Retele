#!/usr/bin/env python
#1.1Se transmite o litera de la client la server, serveru trimite inapoi litera dublata
import socket
import sys

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 2115)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

while True:
    # Wait for a connection and accept it
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data 
        while True:
            data = connection.recv(100)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                data=data+data
                print >>sys.stderr, 'sending data back to the client "%s"' %data
                connection.sendall(data)
                break
    finally:
        # Clean up the connection
        connection.close()
    
    #Closing the server after giving answer
    # Or keep it open to listen for more clients by deleting the break below (and the print)
    print>>sys.stderr, 'closing server'
    break