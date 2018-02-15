#!/usr/bin/python           # This is client.py file

IP_DICT = {
    'ONEPLUS_3': '192.168.43.188',
}

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

print('Connecting...')
s.connect((IP_DICT['ONEPLUS_3'], port))
print('Connected!')
print(s.recv(1024))
s.close()                     # Close the socket when done