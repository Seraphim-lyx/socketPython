import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header 
from email.mime.image import MIMEImage

mailserver = 'smtp.gmail.com:587'

f = open('pic.jpg', 'rb')
pic = MIMEImage(f.read())
pic.add_header('Content-ID', '<image1>')
f.close()

msg_html = MIMEText('<b>I love computer networks!</b>.<br><img src="cid:image1"><br>', 'html')
multi = MIMEMultipart('related')
mul_alt = MIMEMultipart('alternative')
multi.attach(mul_alt)
mul_alt.attach(msg_html)
multi.attach(pic)

server = smtplib.SMTP(mailserver)
server.ehlo()
server.starttls()
server.login('email','pwd')
server.set_debuglevel(True) # show communication with the server

try:
    server.sendmail('searphimlyx@gmail.com', ['seraphimlyx@gmail.com'], bytes(multi))
finally:
    server.quit()