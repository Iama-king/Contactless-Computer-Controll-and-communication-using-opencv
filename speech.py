import os
import smtplib
from email.message import EmailMessage as em
msg=em()
email_add ='20cs42@cit.edu.in'
msg['From'] = email_add
email_pass='thcpwodpirdsrftj'
msg['Subject']="hi"
msg.set_content("please ignore")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_add, email_pass)
    msg['To'] = 'sanjaypotter3523@gmail.com'
    smtp.send_message(msg)
    print("message sent")