import socket
import struct, time

# server
HOST = "localhost"
PORT = 6660


def recvall(socket):
    str = ""
    maxRecvSize = 256
    finished = False
    while not finished:
        t = socket.recv(maxRecvSize).decode()
        str = "%s%s"%(str,t)

        finished = str[-3:] == 'EOD'

    return str


# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for i in range(1,10):
    t = recvall(s)
    print("received: %s"%t)

    bytes = s.sendall("ACK".encode())
    print(bytes)

s.close()
