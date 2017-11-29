import socket
import struct
import sys
import time

NTP_SERVER = "pool.ntp.org" # server domain

port = 123 # server port

TIME1970 = 2208988800 # 1970-01-01 00:00:00

def sntp_client():
	msg = '\x1b' + 47 * '\0'  # default sending message
	ntpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket object
	ntpSocket.sendto(msg.encode(),(NTP_SERVER, port)) # send UDP packet
	data, address = ntpSocket.recvfrom(1024)  # response from server

	if data:
		print ('Response received from:', address) # print address
	t = struct.unpack( "!12I", data )[10] # extract timestamp
	t -= TIME1970 #calculate time
	print ('\tTime=%s' % time.ctime(t))

if __name__ == '__main__':
	
	sntp_client()