from email.message import EmailMessage
import Message
import smtplib
import getpass
import imghdr
import time
import ssl
import re
import os


class SendEmail(Message.Message):

    def __init__(self):
        super().__init__()
        self.email_account = ""
        self.password = ""
        self.opc = 0
        self.pictures = []
        self.to = ""


    ###################################################################
    def setOpc(self, opc):
        if opc == 1 or opc == 2:
            self.opc = opc

        elif opc == 3:
            print(":[*] Cerrando programa...")
            time.sleep(2)
            exit()

        else:
            print(":[!] Esta opcion no existe")

    def getOpc(self):
        return self.opc


    ####################################################################
    def setEmailAccount(self, email_account):
        # Si el usuario agrega un correo gmail,
        # entramos al siguiente condicioanl
        if self.getOpc() == 1:

            # Hay algunos caracteres que no son aceptados
            # para una cuenta de gmail
            cant_be = "|°¬!\"$%&/()='?\\¿¡´¨+*~{[^}]`,;:-_<>éýúíóáÉÝÚÍÓÁëÿüïöäËÜÏÖÄ"

            # Usamos este for para checar cada caracter
            # en la variable cant_be
            for character in cant_be:

                # Usamos el siguiente condocional para validar
                # si hay algun caracter o espacio en el
                # correo que el usuario agrego
                if character in email_account or " " in email_account:

                    email_account = ""

                    # Si entra a la sigiente condicion preguntamos por el
                    # correo de nuevo 
                    print(":[!] Caracter invalido")

            # Ahora usarmos una expresion regular para asegurarnos
            # que nuestro usuario uso una '@' y el dominio del gmail
            type_email = re.match(r"(.*?)@gmail.com", email_account)

            # Validamos la expresion regular
            if type_email:
                # Si la expresion regular exncuentra un correo valido
                # lo guardamos en la variable 'self.email_account'
                self.email_account = type_email[0]

        ############################################
        # Si el usuario escogio mandar un correo desde una cuenta
        # outlook/hotmail, entramos al siguiente condicional
        elif self.getOpc() == 2:

            # Hay algunos caracteres que no son aceptados para una cuenta
            # de outlook/hotmail, asi que los guardamos en 
            # la variable 'cant_be' por el momento
            cant_be = "|°¬!\"$%&/()='?\\¿¡´¨+*~{[^}]`,;:<>éýúíóáÉÝÚÍÓÁëÿüïöäËÜÏÖÄ"

            # Usamos este for para checar cada caracter
            # en la variable cant_be
            for character in cant_be:

                # Usamos el siguiente condocional para validar
                # si hay algun caracter o espacio en el
                # correo que el usuario agrego
                if character in email_account or " " in email_account:

                    email_account = ""

                    # Si entra a la sigiente condicion preguntamos
                    # por el correo de nuevo 
                    print(":[!] Caracter invalido")

            # Outlook acepat dos tipos de correos, outlook.com
            # y hotmail.com, asi que en la lista siguiente agregamos
            # una expresion regular para cada tipo de correo
            type_emails = [re.match(r"(.*?)@(outlook.es|outlook.com|uanl.edu.mx)", email_account), re.match(r"(.*?)@hotmail.com", email_account)]

            # Usamos el siguiente 'for' para cada expresion
            # regular
            for type_email in type_emails:

                # Si una de las expresiones estan bien
                # entra al siguiente condicional
                if type_email:

                    # Repetimos lo mismo que con el gmail
                    # guardamos el correo en 'self.email_account' 
                    self.email_account = type_email[0]

        if self.email_account == "":
            email_account = ""
            print(":[!] No agregaste un correo valido")

    def getEmailAccount(self):
        return self.email_account


    def setPassword(self, password):
        if "@gmail.com" in self.email_account:
            # Gmail requiere de una contraseña mayor a 
            # 8 caracteres
            if len(password) >= 8:
                self.password = password

        else:
            if len(password) >= 8:

                # La contraseña debe contener dos tipos de caracteres 
                # diferentes (una palabra en mayuscula y un numero)
                # Por lo que guardamos diferentes caracteres en diferentes 
                # variables
                cap = "ABDEFGHIJKLMNÑOPQRSTUVWXYZ"
                lower = "abdefghijklmnñopqrstuvwxyz"
                numbers = "0123456789"
                symbols = "|°¬!\"$%&/()='?\\¿¡´¨+*~{[^}]`,;:-_<>éýúíóáÉÝÚÍÓÁëÿüïöäËÜÏÖÄ"

                # Usamos contadores para 'contar' cuantos tipos
                # de caracteres hay en la contraseña
                c_cap = 0
                c_lower = 0
                c_numbers = 0
                c_symbols = 0
                counter = 0

                # Usamos un 'for' para lo antes mencionado
                for i in cap:
                    if i in password:
                        c_cap = c_cap + 1

                for j in lower:
                    if j in password:
                        c_lower = c_lower + 1

                for k in numbers:
                    if k in password:
                        c_numbers = c_numbers + 1

                for l in symbols:
                    if l in password:
                        c_symbols = c_symbols + 1

                # Usamos ls siguientes condicionales y el contador para
                # saber cuantos contadores tienen mas de 0
                if c_cap > 0:
                    counter = counter + 1

                if c_lower > 0:
                    counter = counter + 1

                if c_numbers > 0:
                    counter = counter + 1

                if c_symbols > 0:
                    counter = counter + 1

                # Si la longitud del contador es mayor a 1,
                # la contraseña satisface la condicion de 
                # outlook/hotmail, por lo que..
                if counter >= 2:

                    # La guardamos en 'self.password'
                    self.password = password

        # Usamos el siguiente condicional para validar
        # si 'self.password' esta vacia, por que eso significaria
        # que el usuario agrego una contraseña invalida, por lo que...
        if self.password == "":

            # Vaciamos la variable password y...
            password = ""

            # Se la pedimos al usuario de nuevo
            print(":[!] Agrego una contraseña invalida")

    def getPassword(self):
        return self.password


    #######################################################################
    def setTo(self, to):
        if " " not in to:
            # Ahora usamos una expresion regular para asegurarnos
            # que el usuario uso '@' y el dominio correcto de gmail 
            type_email = re.search(r"(.*?)@(.*?)", to)

            # Validamos la expresion regular
            if type_email:
                # Si la expresion regular exncuentra un correo valido
                # lo guardamos en la variable 'self.email_account'
                self.to = to

            else:
                to = ""
                print(":[!]Agrego un correo invalido")

        else:
            to = ""
            print(":[!] Agrego un correo invalido")

    def getTo(self):
        return self.to


    ######################################################################
    def setPictures(self, image, directory):
        pictures = []

        if '.jpeg' in image:
            image = image.replace(".jpeg", "jpg")

        verify_image = re.search(r'\w*.jpg', image)
        if verify_image:
            directory = directory.lower()
            print()

            if "c:\\" in directory:
                pictures.append(image)
                pictures.append(directory)
                self.pictures = pictures

        else:
            print(":[!] Esta no es una imagen")

    def getPictures(self):
           return self.pictures


    #####################################################################
    def sendEmail(self, subject, msg):
        message = EmailMessage()
        message["Asunto"] = subject
        message["De"] = self.email_account
        message["Para"] = self.to
        message.set_content(msg)

        if len(self.pictures) > 0:
            try:
                if self.pictures[1] == os.getcwd().lower():
                    os.chdir("c:\\")
                os.chdir(self.pictures[1])

                file = open(self.pictures[0], 'rb')
                f_name = file.name
                f_data = file.read()
                f_type = imghdr.what(file.name)
                file.close()

                message.add_attachment(f_data, maintype='image', subtype=f_type, filename=f_name)
            except:
                print(":[!] El directorio/imagen que agrego no exite")
                print(":::: o no es el directorio correcto.")
                exit()

        try:
            if self.opc == 1:
                server = smtplib.SMTP("smtp.gmail.com", 587)

            elif self.opc == 2:
                server = smtplib.SMTP("smtp-mail.outlook.com", 587)

            server.starttls(context=ssl.create_default_context())
            server.login(self.email_account, self.password)
            server.send_message(message)
            server.quit()

            print("[*] Correo enviado")
        except:
            print(":[!] No a habilitado acceso a apps")
            print(":[!] menos seguras en tu cuenta.")
            print(":[!] Cerrando programa...")
            time.sleep(2)
            exit()