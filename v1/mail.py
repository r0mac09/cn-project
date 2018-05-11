import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#shit not done

fromaddr = "test1@example.com"
toaddr = "test2@example.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Mail"
body = "Test mail from python"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.example.com', 25)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

class Mail():
    def __init__(self):
        self.email = 'cnproject.pswdreset@gmail.com'
        self.password = 'cnproject2018'
        self.server = smtplib.SMTP('smtp.gmail.com', 25)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.email, self.password)

    def send_mail(self, to, subj, code):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subj
        body = "Your code is: " + code
        msg.attach(MIMEText(body, 'plain'))
        self.server.sendmail(self.email, to, msg.as_string())
        self.server.quit()


