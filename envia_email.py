import smtplib  # biblioteca voltada para o protocolo SMTP, para envio de emails
# mime = norma padrão envio de mensagens pela internet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import json


# class EnviaEmail():
#     def __init__(self):
#         pass

def send_email(email, codigo, nome):  # parametro é o email do destinatário
    # importando nossa senha do email (que vamos enviar) de outro arquivo (mais seguro assim)
    with open("token.json", "r") as f:
        # load: mesmo quando fecha o arquivo, você continua tendo ele carregado.
        TOKEN = json.load(f)

    host = "smtp.gmail.com"
    port = 587
    login = "joaoarthurdev@gmail.com"
    senha = TOKEN

    server = smtplib.SMTP(host, port)

    server.ehlo()
    # protocolo de segurança da informação. "Transport Layer Security".
    server.starttls()
    server.login(login, senha)
    message = f"Olá, {nome}, o seu código de verificação é {codigo}."

    email_msg = MIMEMultipart()
    email_msg["From"] = login
    email_msg["To"] = email
    email_msg["subject"] = "Testando"
    email_msg.attach(MIMEText(message, "plain"))  # corpo da mensagem.

    try:
        server.sendmail(email_msg["From"],
                        email_msg["To"], email_msg.as_string())
        return print("Email enviado com sucesso."), server(quit())
    except smtplib.SMTPRecipientsRefused:
        return print("Email não encontrado.")
