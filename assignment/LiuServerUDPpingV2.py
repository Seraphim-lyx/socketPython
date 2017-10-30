import time
import socketserver
import threading
# from socketserver import DatagramRequestHandler as DRH
# from socketserver import StreamRequestHandler as SRH

"""
UDP service implemented by socktserver module
Handler class must be implemented to deal with
the message sent from the client
If exception control is required
the Server class must be implemented instead of
using the default server class
provided by socketserver module
"""


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
        Handler module for UDPServer
        handle method must be overrided
    """

    def handle(self):

        message, socket = self.request[0], self.request[1]

        print(message)

        # socket.sendto(message, self.client_address)


class MyUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    """
        self-implementing UDPServer class extends from default UDPServer class
        if timeout handled is needed
        then override handle_timeout method
    """

    def handle_timeout(self):
        print("*** timeout ***")


host = '127.0.0.1'

port = 12000

# server = socketserver.ThreadingUDPServer((host, port), MyUDPServer)

# server.serve_forever()

server = MyUDPServer((host, port), MyUDPHandler)

server.timeout = 3

while True:

    # use handle_request() instead of serve_forever() for timeout handle.
    server.handle_request()
