import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345

s.bind((host, port))

s.listen(2)
c, addr = s.accept()


def receive(c):
    while True:
        msg = c.recv(1024).decode('utf8')
        print(msg)


def send(c):
    while True:
        msg = input()
        c.send(msg.encode('utf8'))

trd1 = threading.Thread(target=receive, args=(c,))
trd2 = threading.Thread(target=send, args=(c,))
trd1.start()
trd2.start()
# while True:

#     msg = input()
#     c.send(msg.encode('utf8'))
s.close()
