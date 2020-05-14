
import smtplib
from email.mime.text import MIMEText

def send_mail_from_gmail(subject, message):
    # conexão com os servidores do google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # username ou email para logar no servidor

    username = "alex.caranha@gmail.com"  # substitua <seuemail> pelo seu email.
    # password = "22AlLu1205ge"
    password = "ctbtozxnwmicnzay"

    from_addr = 'alex.caranha@gmail.com'
    to_addrs = ['alex.caranha@gmail.com']

    # a biblioteca email possuí vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    message = MIMEText(message)
    message['subject'] = subject
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()