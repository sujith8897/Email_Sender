import smtplib
import re
from email.message import EmailMessage

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check(email):
 
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, email)):
        return 1 #valid email
 
    else:
        return 0 #invalid email


msg = EmailMessage()

#input subject
print('Subject? ',end="")
msg['Subject'] = input()

msg['From'] = "cricketworld8897@gmail.com"

#incput body
print('Body? ',end="")
msg.set_content(input())

#input recipient address
print('Recipient? ',end="")
recipient = input()

#checking for valid email address
if(check(recipient)):
	msg['To'] = recipient
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("cricketworld8897", "sujith1234@")
	server.send_message(msg)
	server.quit()
	print('Email sent!')
else:
	print('Invalid Email!')