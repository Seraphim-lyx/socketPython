import socketserver
import threading
from socketserver import StreamRequestHandler as SRH

host = "127.0.0.1"
port = 12345
addr = (host, port)


""" 
server side socket class implemented from socketserver
can accpet and maintain multiple 
client requests by threads
unblocking send and receive message with clients

"""


class myServer(SRH):
    conns = []  # connections array
    trd = None  # Singleton send thread

    def send():
        """input and send message to multiple client at the same time"""
        while True:
            msg = input()
            for c in myServer.conns:
                c.send(msg.encode('utf8'))

    def handle(self):
        conn = self.request
        myServer.conns.append(conn)
        if myServer.trd is None:
            myServer.trd = threading.Thread(target=myServer.send)
            # build thread for input to prevent blocking
            myServer.trd.start()

        while True:
            data = conn.recv(1024).decode("utf8")
            if data is 'exit':
                break
            print(data)


server = socketserver.ThreadingTCPServer(
    (host, port), myServer)  # build thread for each client
server.serve_forever()
