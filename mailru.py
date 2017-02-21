import smtplib   
from email.mime.text import MIMEText    
me = 'admin@mail.ru'
you = 'kot_smit@mail.ru'
smtp_server = 'smtp.mail.ru'
msg = MIMEText('Message e-mail')
msg['Subject'] = 'The contents of '
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP(smtp_server)
s.sendmail(me, [you], msg.as_string())
s.quit()