import socket
from _thread import *
import numpy as np

#criando socket
ServerSideSocket = socket.socket()
host = '127.0.0.2'
port = 2002
ThreadCount = 0

#conectando socket a porta
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)


def fn():
    '''since all 3 functions were identical you can just use one ...'''
    x = 0
    while x < 10000000:
        if(x == 9999999):
            print("chegou ao topo")
        x += 1

rodar = 1
def multi_threaded_client(connection):
    global rodar

    if rodar == 1:
        fn()
        connection.sendall("".encode())
        connection.close()
        rodar=0

#loop que torda o servidor sempre disponivel pra toda solicitacao
while True:
    #sempre aceita uma coneccao
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))

    #comeca uma nova thread pra esse novo cliente conectado
    start_new_thread(multi_threaded_client, (Client, ))

    #conta quantos clientes esetao conectados
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()