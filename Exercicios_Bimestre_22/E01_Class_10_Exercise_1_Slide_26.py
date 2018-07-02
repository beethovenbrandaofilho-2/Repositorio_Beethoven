# 1 DESENVOLVER UM SERVIDOR DE CHAT PARA MULTIPLOS USUARIOS

from socket import *
from time import ctime

HOST = ''
PORT = 8000
BUFSIZ = 1024

ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

print("Servidor funcionando!")
print("Adicionando os clientes...")

for i in range(5):
    tcpCliSock, addr = tcpSerSock.accept()
    print("Cliente ", i+1, " Conectado de:", addr)
    for i in range(5):
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        strdata = data.decode('utf-8')
        print("Mensagem Recebida:", strdata)
        tcpCliSock.send((ctime() + ' ' + strdata).encode('utf-8'))
    tcpCliSock.close()

tcpSerSock.close()