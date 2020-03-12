import smtplib
import socket

TO = 'shbellar@ucsc.edu'
SUBJECT = socket.gethostname() + ' Complete'
TEXT = 'Test Body'

gmail_sender = 'linqsibi@gmail.com'
gmail_passwd = '' # Edit

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

server.sendmail(gmail_sender, [TO], BODY)

server.quit()
