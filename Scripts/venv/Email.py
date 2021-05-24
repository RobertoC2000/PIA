from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import smtplib, ssl 
import logging
import getpass

def Enviar_Correo():
    try:
        print("Login to Gmail: \n") 
        sender_email = input("I. Dirección desde la que se enviará el correo: ")
        password = getpass.getpass("II. Contraseña de la cuenta desde donde se envía el correo : ")
        receiver_email = input("III. Dirección de destino: ")
        port_SSL = 465  # For SSL 
        port_TLS = 587  # For TSL 
        smtp_server = "smtp.gmail.com" 
        message = MIMEMultipart() 
        message["Subject"] = input("IV. Asunto del correo: ")
        message["From"] = sender_email 
        message["To"] = receiver_email 
        body = input("V. Cuerpo del correo: ")
     
        message.attach(MIMEText(body, "plain")) 
     
        filename = input("VI. Dirección de la imágen que se adjuntara ")
     
        with open(filename,"rb") as attachment: 
            part = MIMEBase("application","octet-stream") 
            part.set_payload(attachment.read()) 
     
        encoders.encode_base64(part) 
     
        part.add_header("Content-Disposition", f"attachment; filename={filename}") 
     
        message.attach(part) 
        text = message.as_string() 
     
        # Create a secure SSL context 
        context = ssl.create_default_context() 
     
        i = True 
     
        while(i): 
            protocol = input("Protocolo, favor de escribirlo tal cual el parentesis (SSL/TLS): ") 
            if (protocol == "SSL"): 
                with smtplib.SMTP_SSL(smtp_server, port_SSL, context=context) as server: 
                    server.login(sender_email, password) 
                    server.sendmail(sender_email, receiver_email, text) 
                    i = False 
            elif (protocol == "TLS"): 
                with smtplib.SMTP(smtp_server, port_TLS) as server: 
                    server.ehlo()  # Can be omitted 
                    server.starttls(context=context) 
                    server.ehlo()  # Can be omitted 
                    server.login(sender_email, password) 
                    server.sendmail(sender_email, receiver_email, text) 
                    i = False 
            else: 
                print("Protcolo incorrecto, vuelva a intentarlo")
                i = True 
        print("Correo enviado")
    except:
        logging.error("Error[email.py]! --> Algun dato fue ingresado erroneamente")
        print('********************************************************** Se ha detectado un error, revise el archivo logg.txt **********************************************************')