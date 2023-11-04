import smtplib
from email.mime.text import MIMEText

# Genera una contraseña de aplicaciones para tu cuenta de Gmail
app_password = "toli ekdw lcuz zzhv"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("esparta0987@gmail.com", app_password)

message = MIMEText("Este es el cuerpo del mensaje", "plain")
message["Subject"] = "Asunto del mensaje"
message["From"] = "esparta0987@gmail.com"
message["To"] = "esparta0987@gmail.com"

server.sendmail(message["From"], message["To"], message.as_string())

server.quit()
