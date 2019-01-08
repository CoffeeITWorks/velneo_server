#!/usr/bin/env python
# -*- coding: utf8 -*-

import smtplib
import os
import sys
from sys import stderr
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email.Utils import COMMASPACE, formatdate

# Parametros de configuracion del servidor
params = sys.argv[1].split(';')

mail_server = params[0]         # Servidor
mail_port = params[1]           # Puerto
mail_user = params[2]           # Usuario
mail_pwd = params[3]            # Contrasena
mail_name = params[4]           # Correo Origen Nombre <email@dominio.com>
mail_subject = params[5]        # Asunto
mail_body = params[6]           # Cuerpo

part1 = MIMEText(mail_body, 'plain')

# Direcciones destino
mailsBcc = sys.argv[2].split(';')

try:
        for mail in mailsBcc:
                # Adjuntos
                mail_attach = sys.argv[3].split(';');
                msg = MIMEMultipart()
                msg['From'] = mail_name
                msg['Subject'] = mail_subject
                msg.attach(part1)
                #Si se comenta esta linea se puede evitar que aparezcan las direcciones de los destinatarios.
                msg['To'] = mail
                #msg['Bcc']= COMMASPACE.join(mailsBcc)

                try:
                        if (mail_attach[0] != ""):
                                try:
                                        for line in mail_attach:
                                                part = MIMEBase('application', "octet-stream")
                                                part.set_payload(open(line, "rb").read())
                                                Encoders.encode_base64(part)
                                                part.add_header('Content-Disposition', 'attachment; filename = "%s"' % os.path.basename(line))
                                                msg.attach(part)
                                except:
                                        print "No puede adjuntar"

                        smtplib.stderr = sys.stdout
                        try:
                                msg['To']= COMMASPACE.join(mailsBcc)
                                mailServer = smtplib.SMTP(mail_server, mail_port)
                                mailServer.ehlo()
                                mailServer.starttls()
                                mailServer.set_debuglevel(1)
                                #No usa usuario y password
                                #mailServer.login(mail_user, mail_pwd)
                                mailServer.sendmail(mail_name, mail, msg.as_string())
                                mailServer.close()
                        except:
                                print "Revise los paraetros del servidor SMTP\n Parametros: {} ".format(params)

                except:
                        print "No se pudo enviar el mail"

except:
        print "Revisar el tema de cada correo"