# import socket module
import threading
from socket import *
import sys  # In order to terminate the program


class HTTPServer(object):
    """An HTTP Server that is implemeneted by raw socket"""

    def __init__(self):
        self.serverSocket = socket(
            AF_INET, SOCK_STREAM)  # generate socketObject
        self.port = 6789
        self.host = '127.0.0.1'

    def mainServer(self, serverSocket):
        """bind server to host and port"""
        serverSocket.bind((self.host, self.port))
        serverSocket.listen(5)

    def startConn(self):
        """start connection"""
        threading.Thread(target=self.mainServer,
                         args=(self.serverSocket,)).start()
        # create a thread for main socket

        while True:
            # Establish the client connection
            print('Ready to serve...')
            connectionSocket, addr = self.serverSocket.accept()
            threading.Thread(target=self.clientConn, args=(
                connectionSocket,)).start()

            # build new thread for every connection from client

    def clientConn(self, connectionSocket):
        """receive from and response to message"""
        try:
            print(threading.current_thread())
            message = connectionSocket.recv(1024).decode()
            print(message)
            filename = message.split()[1]
            print(filename)
            f = open(filename[1:])
            outputdata = f.read()
            # Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n\r\n".encode())
            connectionSocket.close()
        except IOError:
            # Send response message for file not found
            header = 'HTTP/1.1 404 Not Found\r\n\r\n'
            content = '<html><meta charset="UTF-8"/>'
            content += '<h1>404 Not Found</h1></html>'
            connectionSocket.send(header.encode())
            connectionSocket.send(content.encode())
            # Close client socket
            connectionSocket.close()

    def endConn(self):
        self.serverSocket.close()
        sys.exit()  # Terminate the program


server = HTTPServer()
server.startConn()
server.endConn()
