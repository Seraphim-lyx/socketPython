# import socket module
from socket import *
import threading
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
port = 6789
host = '127.0.0.1'
serverSocket.bind((host, port))
serverSocket.listen(5)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        print(filename[1:])
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        # connectionSocket.send(
        #     'HTTP/1.0 200 OK Content-Type: text/html'.encode())
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        content = '<html><meta charset="UTF-8"/><h1>404 Not Found</h1></html>'
        connectionSocket.send(header.encode())
        connectionSocket.send(content.encode())
        # Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
