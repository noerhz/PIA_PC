from CifradoCesar import *
from Transposition import *
from Email import *
from ScanPort import *
from Hunter import *
import argparse
import re
import logging
import time
import os


logging.basicConfig(filename="Info.log", level="DEBUG")

parser = argparse.ArgumentParser(description=":Descripcion de los parametros:")
# opc: opciones
help1 = """-opc (1=codificar mensaje, 2=decodificar mensaje,
           3=hackear mensaje codificado, 4=investigar con llave API,
           5=Enviar un email, 6=escaneo de puertos, 7=DNS cache)"""
parser.add_argument("-opc", type=int, help=help1)
# Si quieres codificar/decodificar/hackear un mensaje
# tienes que escoger entre cifrado cesar o de transposicion
help2 = "-t_cifr (1=Cesar, 2=Transposicion)"
parser.add_argument("-t_cifr", type=int, help=help2)
# Hay que definir el tipo de idioma de tu mensaje
parser.add_argument("-lang", type=int, help='-lang (1=Ingles,2=Español)')
# msg: agrega tu mensaje
parser.add_argument("-msg", type=str, help='-msg "Este es un mensaje"')
# Si escogiste cifrado cesar, escribe el numero de veces que
# quieres que se roten las palabras
parser.add_argument("-rot", type=int, help='-rot (entre 1 y 25)')
# Si escogiste transposicion, escribe la contraseña
parser.add_argument("-key", type=str, help="-key 'keyword'")
# Si quieres investigar a una organizacion con su llave API de hunter
help3 = "-apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7'"
parser.add_argument("-apikey", type=str, help=help3)
help4 = "-domain '(www.twitter.com / twitter.com / twitter)'"
parser.add_argument("-domain", type=str, help=help4)
# Si quieres enviar un mensaje especifica el tipo de correo
# puede ser: 1=gmail, 2=outlook/hotmail
help5 = "-t_email (1=gmail, 2=hotmail/outlook)"
parser.add_argument("-t_email", type=int, help=help5)
# Agrega tu correo y tu contraseña para accesaar a tu cuenta de correo
parser.add_argument("-email", type=str, help='-email "email@example.com"')
parser.add_argument("-passw", type=str, help='-pass "your_password"')
# Agrega el correo al que quieres enviar tu mensaje
parser.add_argument("-to", type=str, help='-to "email@example.com"')
# Agrega el asunto del correo
parser.add_argument("-subj", type=str, help='-subj "subject"')
# Si quieres enviar una imagen en tu correo, agrega estos parametros
help6 = '-pic "nombre_imagen.jpg","c:\\users\\name\\pictures"'
parser.add_argument("-pic", type=str, help=help6)
# Si quieres saber que puertos estan abiertos
# parser.add_argument("-ip", type=str, help='-ip "192.168.1.19"')
parser.add_argument("-ip", type=str, help="-ip IP a escanear ")
parser.add_argument("-i", type=int, help="-i Inicio de los puertos a escanear")
parser.add_argument("-f", type=int, help="-f Final de los puertos a escanear")
data = parser.parse_args()


# try:
if __name__ == '__main__':
    if(data.t_cifr == 1 or data.t_cifr == 2):
        # Cifrado cesar
        if data.t_cifr == 1:
            # Mandamos llamar al modulo que creamos del cifrado cesar
            mold = CifradoCesar(data.opc, data.msg, data.rot)
            # Si el usuario eligio este mentodo de cifrado
            # entramos al siguiente condicional
            if(data.opc == 1):
                print(":[*] Mensaje codificado:", mold.codifyMessage())
            # decifrado de mensajes
            elif(data.opc == 2):
                print(":[*] Mensaje decodificado:", mold.decodeMessage())
            # hackeo de mensajes
            elif(data.opc == 3):
                print(":[*] Mensaje hackeado:", mold.hackMessage())
        # Cifrado de Transposicion
        elif data.t_cifr == 2:
            t = Transposition()
            t.setLanguage(int(data.lang))
            t.setMessage(str(data.msg))
            try:
                if data.opc == 1:
                    t.setKey(data.key)
                    print(":[*] Mensaje codificado:", t.encodeMessage())
                    print()
                elif data.opc == 2:
                    t.setKey(data.key)
                    print(":[*] Mensaje decodificado:", t.unencodeMessage())
                    print()
                elif data.opc == 3:
                    print(":[*] Mensaje hackeado:", t.hackMessage())
                    print()
                else:
                    mensage = "Escogiste una opcion que no existe"
                    logging.error(mensage, data.opc)
                    print("[!] Agregaste una opcion invalida")
                    print("::: Cerrando programa...")
            except:
                data.warning("Agregaste un mensaje invalido")
                print(":[!] Agregaste una oracion/caracter invalido.")
                print(":::: Cerrando programa...")
                time.sleep(1)

    elif(data.t_cifr is None):
        # Investiga una organizacion con llave API
        if data.opc == 4:
            h = Hunter(data.apikey, data.domain)
            h.search()
            h.showInfo(h.search())
            h.saveInfo(h.search())

        elif data.opc == 5:
            se = SendEmail()
            t_email = data.t_email
            email = data.email
            password = data.passw
            to = data.to
            subject = data.subj
            se.setMessage(data.msg)
            msg = se.getMessage()

            part = ""
            if(t_email is not None and email is not None and
               password is not None and to is not None and
               subject is not None and msg is not None and
               data.pic is not None):

                part = ""
                picture = ""
                directory = ""
                if((data.pic).count(",") == 1):
                    data.pic = data.pic + ","
                    for letter in data.pic:
                        if letter != ",":
                            part = part + letter

                        elif letter == ",":
                            if ".jpg" in part or ".jpeg" in part:
                                picture = part
                            else:
                                directory = part
                            part = ""

                    se.setOpc(int(t_email))
                    se.setEmailAccount(email)
                    se.setPassword(password)
                    se.setTo(to)
                    se.setPictures(picture, directory)
                    se.sendEmail(subject, msg)

                else:
                    mensage = "! agrega el nombre de la imagen y su directorio"
                    logging.warning(mensage)
                    print("[!] Solo puedes agregar una imagen y un directorio")
                    print("::: Cerrando programa...")
                    time.sleep(2)
                    exit()

            elif(t_email is not None and email is not None and
                 password is not None and to is not None and
                 subject is not None and msg is not None and data.pic is None):

                se.setOpc(int(t_email))
                se.setEmailAccount(email)
                se.setPassword(password)
                se.setTo(to)
                se.sendEmail(subject, msg)

            else:
                logging.warning("Tienes que agregar mas parametros")
                print("[!] Se necesitan mas parametros para enviar el correo")

        elif data.opc == 6:
            if ((data.ip is not None) and (data.i is not None)and
               (data.f is not None)):
                scanPort(data.ip, data.i, data.f)
            else:
                print("No se puede realizar el escaneo", end=", ")
                print("revisa los parametros ingresados")
                print("Para realizar el escaneo debe tener lo siguiente:")
                print("* Ip: -ip")
                print("* Puerto de inicio del escaneo: -i")
                print("* Puerto de final del escaneo: -f")

        elif data.opc == 7:
            directory = os.getcwd()
            os.system(f"powershell -ExecutionPolicy ByPass ./DNS.ps1 -TargetFolder \"{directory}\"")

        else:
            logging.warning("Tienes que agregar una opcion valida")
            print("[!] Error")
            print("::: Probablemente no agrego ninguna opcion")
            print("::: o la opcion seleccionada no existe.")
    else:
        logging.error("Ese tipo de cifrado no existe", str(data.t_cifr))
        print("[!] Ese tipo de cifrado no existe")

# except:
# logging.warning("Tal vez no agrego un parametro necesario/correcto")
# print("[!] Error")
# print("::: Tal vez no agrego un parametro necesario/correcto")
# print("::: o agrego uno invalido")
