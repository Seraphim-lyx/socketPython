import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header 
from email.mime.image import MIMEImage

mailserver = 'smtp.gmail.com:587'

#load picture 'pic.jpg'
f = open('pic.jpg', 'rb')
#put image into Image object
pic = MIMEImage(f.read())
#match image into html
pic.add_header('Content-ID', '<image1>')

f.close()

#create html object
msg_html = MIMEText('<b>I love computer networks!</b>.<br><img src="cid:image1"><br>', 'html')

multi = MIMEMultipart('related')

mul_alt = MIMEMultipart('alternative')

multi.attach(mul_alt)
#attach html into mail object
mul_alt.attach(msg_html)
#attath image into mail object
multi.attach(pic)

#build server obejct
server = smtplib.SMTP(mailserver)
#greeting
server.ehlo()
#tls protocol
server.starttls()
#login 
server.login('email','pwd')
#show return message
server.set_debuglevel(True) # show communication with the server

try:
	#send mail
    server.sendmail('searphimlyx@gmail.com', ['seraphimlyx@gmail.com'], bytes(multi))
finally:
    server.quit()