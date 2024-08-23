import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "frederickkankam7@gmail.com"
    password = "nskk ztvf dqnr iynv"

    receiver = "frederickkankam7@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)