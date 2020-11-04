#!/usr/bin/env python
#3.4. Clientul trimite 2 numere, serverul intoarce cel mai mare numar
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
                list = data.split()
                message =''
                nb1 = int(list[0])
                nb2 = int(list[1])
                if nb1 > nb2 : 
                    bigger = nb1
                else:
                    bigger = nb2
                message = str(bigger)
                print >>sys.stderr, 'sending data back to the client "%s"' %message
                connection.sendall(message)
                break
    finally:
        # Clean up the connection
        connection.close()
    
    #Closing the server after giving answer
    #Or keep it open to listen further on by deleting the print+break below 
    print>>sys.stderr, 'closing server'
    break