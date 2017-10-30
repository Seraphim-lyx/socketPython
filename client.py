import socket
import threading
"""
socket in client side
send and receive message asynchronously
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 12345))


def receive(s):
    while True:
        msg = s.recv(1024).decode("utf8")
        print(msg)


trd1 = threading.Thread(target=receive, args=(s,))
trd1.start()


while True:
    msg = input()
    s.send(msg.encode('utf8'))

s.close()
