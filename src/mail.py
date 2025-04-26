import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# --- Configuration ---
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = '****@gmail.com'
receiver_email = '****@gmail.com'
password = '****' 

# --- Send the Email ---
def sendMessage(body):
    try:
        # --- Email Content ---
        subjectTime = datetime.datetime.now()
        subject = '[HOMENET - DOOR] ' + body + ' ' + str(subjectTime)
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        currentTime = datetime.datetime.now()
        messageBody = body + '\n\n[TIME]: ' + str(currentTime) + '\n\n'
        msg.attach(MIMEText(messageBody, 'plain'))
        server.send_message(msg)
        print('EMAIL SUCCESSFULLY SEND TO OWNER!')
    except Exception as e:
        print(f'Error sending email: {e}')
    finally:
        server.quit()

sendMessage('[SERVER]: starting ...')
