import os.path
import datetime
import smtplib
from email.encoders import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.utils import formatdate
from configs.email import *

def create_message(attachments=[]):
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = FROM_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Cc'] = CC_ADDRESS
    msg['Date'] = formatdate()

    # Insert body
    #body = MIMEText(body)
    #msg.attach(body)

    # Attach all attachments
    for attachment in attachments:
        file = open(attachment, encoding='utf-8', errors='replace')
        attachment_file = MIMEBase('application', 'pdf')
        attachment_file.set_payload(file.read())
        encode_base64(attachment_file)
        attachment_file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
        msg.attach(attachment_file)
    return msg


def send(msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(FROM_ADDRESS, TO_ADDRESS, msg.as_string())
    smtpobj.close()
