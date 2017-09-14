
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(tosend,data,subject):
        sender = 'tempemailpython@gmail.com'
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = tosend
        msg['CC']='rahulraghuv@gmail.com'
        html_data = MIMEText(data, 'html')
        msg.attach(html_data)
        try:
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpObj.starttls()
                smtpObj.login("tempemailpython@gmail.com","yahoo.com")
                smtpObj.sendmail(sender,tosend, msg.as_string()) 
                smtpObj.quit()        
                print("Successfully sent email")
        except Exception as err:
                print("Error: unable to send email",err)




msgbody='''\
<html>
<body>
  <a href='www.google.com'>Click Here</a>
</body>
</html>
'''
sendEmail(tosend='tempemailpython@gmail.com',data=msgbody,subject='Test Email From Rahul')

