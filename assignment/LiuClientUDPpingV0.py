import socket
import time


clientSocket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)  # set UDP connection

clientSocket.settimeout(1)  # packet wait for 1 sec
host = '127.0.0.1'
port = 12000

for i in range(10):
            # send 10 packets
    try:
        # packet start time
        start = time.time()
        # time format
        t = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        # message to be sent
        message = "Ping:" + str(i) + " " + t
        # sending message by UDP
        clientSocket.sendto(message.encode("utf8"), (host, port))
        # get response from server
        print(clientSocket.recvfrom(1024))
        # calculate sending time
        ptime = round((time.time() - start) * 1000, 2)

        print("RTT:" + str(ptime) + "ms")

    except socket.timeout:

        print("***  time out ***")
