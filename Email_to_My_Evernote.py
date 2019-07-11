import appex
import smtplib, ssl
import urllib.request
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

SENDER_EMAIL = ""
RECEIVER_EMAIL = ""
PASSWORD = ""

SMTP_SERVER = ""
# TLS is the more secure than SSL
PORT = 587  # for TLS (465 for SSL)


def get_title(url):
	with urllib.request.urlopen(url) as res:
		soup = BeautifulSoup(res, "html.parser")
		
		title = soup.title.string
		
		return title


def create_message():
	url = appex.get_url()
	
	title = get_title(url)
	
	msg = MIMEText(url)
	msg['Subject'] = title
	
	return msg
	

def send_email(sender_email, receiver_email, message):	
	with smtplib.SMTP(SMTP_SERVER, PORT) as smtp:
		# smtp.ehlo()
		context = ssl.create_default_context()  # According to Python's Security considerations, it is highly recommended to use create_default_context() from the ssl module
		smtp.starttls(context=context)  # .ehlo() is implicitly called if needed 
		
		smtp.login(SENDER_EMAIL, PASSWORD)
		
		smtp.sendmail(sender_email, receiver_email, message.as_string())  # .ehlo() is implicitly called if needed
		
if __name__ == "__main__":
	msg = create_message()
	send_email(SENDER_EMAIL, RECEIVER_EMAIL, msg)
