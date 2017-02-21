import smtplib

host = "smtp.mail.ru"
port = 465
username = "regina_sask@bk.ru"
password = "Mail2017!"
from_email = username
to_list = ["regina_sask@bk.ru"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Privet, eto pismo")
email_conn.quit()

from smtplib import SMTP
email_conn2 = SMTP(host, port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username, password)
email_conn2.sendmail(from_email, to_list, "Privet, eto pismo")
email_conn2.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
epass_wrong.ehlo()
pass_wrong.starttls()
try:
	pass_wrong.login(username, "wrong_password")
	pass_wrong.sendmail(from_email, to_list, "Privet, eto pismo")

except SMTPAuthenticationError:
	print("Could not login")

except:
	print("an error occured")

pass_wrong.quit()
