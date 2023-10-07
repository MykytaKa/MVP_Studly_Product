import logging
import argparse
import csv
import os.path
import shutil

import smtplib
import random
import string
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


logging.basicConfig(filename='file.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


class log_in:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def __str__(self):
        return f"class to sent random pass-hash to email"

    def generate_password(self, length=8):
        # make random password
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def send_password(self, recipient):
        password = self.generate_password()

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # sent email
            subject = 'new password'
            body = f'yours new password: {password}'
            message = f'Subject:{subject}\n\n{body}'
            server.sendmail(self.sender_email, recipient, message)
            server.quit()
            return "Password was successfully sent."
        except Exception as e:
            return f"Password wasn't successfully sent. Exception : {str(e)}"


if __name__ == '__main__':

    smtp_server = 'smtp.gmail.com'
    smtp_port = 25
    sender_email = 'your gmail'
    sender_password = 'The password that you use to log in to Gmail'

    login_manager = log_in(smtp_server, smtp_port, sender_email, sender_password)

    recipient_email = 'the mail should be sent tho this email ...'
    print(login_manager.send_password(recipient_email))

