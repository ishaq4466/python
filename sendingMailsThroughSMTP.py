#SMTP libary example
#Method: SMTP(host,password), .ehlo(), .starttls(), .login(), .quit()
#.sendmail(from,to,bodyofmail)
#https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python

#.sendmail() only send plain string msg and it cannot parse any email render 
#msg for 

from smtplib import SMTP, SMTPAuthenticationError

host = "smtp.gmail.com"
port = 587
username = "smartashmat@gmail.com"
paswd = "9022230388"
from_email = username
to_list =["smartashmat@gmail.com"]
body = "hesasllo Its me buddy"

email_conn = SMTP(host,port)
print(email_conn.ehlo())
email_conn.starttls()
#print(email_conn.quit())


try:
 	email_conn.login(username, paswd)
 	email_conn.sendmail(from_email,to_list,body)
 	print(email_conn.quit())
except SMTPAuthenticationError as e:
 	print("Login error Occured!! please check ur credentials\n" + str(e))
 	print(email_conn.quit())
except all as e:
	print("Oops !! Something when wrong\n\n" + str(e))
	print(email_conn.quit())
 	


