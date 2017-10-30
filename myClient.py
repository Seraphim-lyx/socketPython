import socket
import threading

"""
Client side socket for requesting
connection to the server socket
asynchronouly send to and receive message from server
"""


class myClient(object):

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 12345

    def send(self, s):
        while True:
            msg = input()
            s.send(msg.encode("utf8"))

    def receive(self):
        while True:
            msg = self.s.recv(1024).decode("utf8")
            print(msg)

    def buildConn(self):
        self.s.connect((self.host, self.port))
        trd = threading.Thread(target=self.send, args=(self.s,))
        trd.start()
        self.receive()

if __name__ == '__main__':
    mc = myClient()
    mc.buildConn()
