# Sending mail with "html" parsing using "email.mime.text"(MIMEText) for plain 
# text and "email.mime.multipart"(MIMEMultipart) library for email 
# parsing...very very usefull
from smtplib import SMTP, SMTPAuthenticationError
from email.mime.text import MIMEText as Text
from email.mime.multipart import MIMEMultipart 


host = "smtp.gmail.com"
port = 587
usrname="smartashmat@gmail.com"
pswd = "9022230388"


plain_txt = "Hello im plainText"
html_txt = "<html><h1>Hello im an html txt<h1><html>"

obj = MIMEMultipart("alternative")
obj["Subject"]="Hello"
obj["From"]="smartashmat@gmail.com"
obj["To"] = "smartashmat@gmail.com"

plain_part = Text(plain_txt,"plain")
html_part=Text(html_txt,"html")

obj.attach(plain_part)
obj.attach(html_part)
parsemail = obj.as_string()
#print(parsemail)

mail = SMTP(host,port)
print(mail.ehlo())

try:
	mail.starttls()	
	mail.login(usrname,pswd)
	mail.sendmail(username,username,parsemail)
	print(mail.close())
except SMTPAuthenticationError:
	print("Login error")
