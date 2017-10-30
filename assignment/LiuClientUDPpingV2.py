import socket
import time

host = '127.0.0.1'

port = 12000

packet_No = 0

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    t = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())

    message = "Sequence No:" + str(packet_No) + " Time:" + str(t)

    packet_No += 1

    clientsocket.sendto(message.encode("utf8"), (host, port))

    time.sleep(1)
