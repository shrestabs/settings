# Import smtplib for the actual sending function
import smtplib
import socket

TO = 'FIXME'
SUBJECT = socket.gethostname() + ' sends a message.'
TEXT = 'Test Body'

gmail_sender = 'sourceFIXMEibi@gmail.com'
gmail_passwd = ''

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
