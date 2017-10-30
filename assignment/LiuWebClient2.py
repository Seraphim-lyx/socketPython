import sys
import socket
# import time
host = sys.argv[1]  # host name

port = int(sys.argv[2])  # port number

filename = sys.argv[3]  # filepath

msg = ''

msglength = 0  # initial the received message length

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketClient.connect((host, port))

socketClient.send(('GET /' + filename + ' HTTP/1.1\r\n\r\n').encode())
# send message with header and destination
while True:
    msg += socketClient.recv(1024).decode()
    if len(msg) == msglength:
        break
    else:
        msglength = len(msg)

print(msg)

socketClient.close()
