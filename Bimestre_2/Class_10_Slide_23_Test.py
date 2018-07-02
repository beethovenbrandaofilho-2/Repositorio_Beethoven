#!/usr/bin/env python

from socket import *

HOST = 'localhost' # or 'localhost'
PORT = 21567
BUFSIZ = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)
ADDR = (HOST, PORT)
tcpCliSock.connect(ADDR)
host=tcpCliSock.getsockname() #  print client host name
print(host)

while True:
    data = (input('Client_2 > ')).encode('utf-8')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()