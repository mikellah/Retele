#!/usr/bin/env python
#4.1 Clientul trimite serverului un sir de caractere (de exemplu numele utilizatorului citit de la tastatura). Serverul afiseaza pe ecran sirul primit si portul clientului si ii raspunde acestuia cu suma cifrelor din Portul clientului. Clientul va afisa pe ecran numarul primit.


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
            print >>sys.stderr, 'received "%s"' % data, "from client port" , client_address[1] 
            if data:
                sum = 0 
                client_port = int(client_address[1])
                while client_port:
                    sum += client_port % 10
                    client_port //= 10
                message = str(sum)
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