
from yapsy.IPlugin import IPlugin
from plugins.categories import HandleEmail
from email.mime.text import MIMEText

from plugins.gmail.bll import send_mail_from_gmail
import re
import smtplib

class Gmail(HandleEmail):
    def setup(self, parent):
        self.parent = parent        
        print(f"{parent.name} loaded: ok.")

    def is_the_question(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match        

    def send_mail(self, subject, message):
        send_mail_from_gmail(subject, message)
        print("success!")

    def run(self, input):
        # Send email
        match = self.is_the_question(r'enviar e-mail com o título (?P<subject>.*) e a mensagem (?P<message>.*)', input)
        if match:
            subject = match.group('subject')
            message = match.group('message')

            self.send_mail(subject, message)
            return "e-mail enviado com sucesso."
