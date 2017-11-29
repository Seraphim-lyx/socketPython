from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
username = ''
password = ''
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
ssl_socket = ssl.wrap_socket(clientSocket)
ssl_socket.connect((mailserver, 465))
recv = ssl_socket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
ssl_socket.send(heloCommand.encode())
recv1 = ssl_socket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send Login command and print server respose

authMsg = 'AUTH LOGIN\r\n'
crlfMesg = '\r\n'
ssl_socket.send(authMsg.encode())
recv11 = ssl_socket.recv(1024).decode()
print(recv11)
user64 = base64.b64encode(username.encode())
pass64 = base64.b64encode(password.encode())
ssl_socket.send(user64)
ssl_socket.send(crlfMesg.encode())
respon = ssl_socket.recv(1024)
print(respon.decode())
# print(pass64)
ssl_socket.send(pass64)
ssl_socket.send(crlfMesg.encode())
respon = ssl_socket.recv(1024)
print(respon.decode())
# Send MAIL FROM command and print server response.
MAIL_From = 'Mail From: <seraphimlyx@gmail.com> \r\n'
ssl_socket.send(MAIL_From.encode())
recv2 = ssl_socket.recv(1024).decode()
print(recv2)
# Send RCPT TO command and print server response.
RCPT_To = 'RCPT To: <seraphimlyx@gmail.com> \r\n'
ssl_socket.send(RCPT_To.encode())
recv3 = ssl_socket.recv(1024).decode()
print(recv3)

# Send DATA command and print server response.
DATA = 'DATA\r\n'
ssl_socket.send(DATA.encode())
recv4 = ssl_socket.recv(1024).decode()
print(recv4)

# Send message data.
ssl_socket.send(msg.encode())

# Message ends with a single period.
ssl_socket.send(endmsg.encode())

# Send QUIT command and get server response.
QUIT = 'QUIT\r\n'
ssl_socket.send(QUIT.encode())
recv5 = ssl_socket.recv(1024).decode()
print(recv5)

ssl_socket.close()