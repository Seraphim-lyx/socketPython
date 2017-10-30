import socket
import time
import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import tkinter

packetNum = 200
host = '127.0.0.1'
timeList = []
port = 12000
loss = 0
Min = 100000
Max = 0
total = 0


clientSocket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)  # set UDP connection

clientSocket.settimeout(1)  # packet wait for 1 sec


def stdDeviation(avg, timeList):
    """calculate standard deviation for the RTT"""
    unit = 0

    for i in timeList:
        # print(i)
        unit += (i - avg)**2
    return round((unit / len(timeList))**(1 / 2), 2)


for i in range(packetNum):
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

        print('RTT:'+ str(ptime) + 'ms')
        # calculate total time
        total += ptime
        timeList.append(ptime)
        if ptime < Min:
                # compare and get the min time
            Min = ptime

        if ptime > Max:
                # compare and get the max time
            Max = ptime
    except socket.timeout:
        # calculate loss packet number
        loss += 1

        print("***  time out ***")


print("Min: " + str(Min) + " Avg: " + str(round((total / (packetNum - loss)), 2)) +
      " Max: " + str(Max) + " Stardard Deviation: " +
      str(stdDeviation(total / (packetNum - loss), timeList)) +
      " Packet Loss: " + str(round((loss / packetNum) * 100)) + "%")


# matplotlib version (plot)

plt.hist(timeList, bins=[0, 0.2, 0.4, 0.6, 0.8, 1])
plt.xlabel('RTTs')
plt.ylabel('Number')
plt.show()

print(timeList)
