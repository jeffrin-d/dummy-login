from email.mime.text import MIMEText
import smtplib
def send_email(email, height, average_height, count):
    from_email="data.sender.connect@gmail.com"
    from_password="v2yCveCSRrztJyD"
    to_email=email

    subject="Height Data"
    message="Hey there, thank you for submitting your data! Your height is <strong>%s</strong>. Average height of all entries is <strong>%s</strong>. For sampling context, there have been <strong>%s</strong> users who have participated." % (height, average_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    
    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)