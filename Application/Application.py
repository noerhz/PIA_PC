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

FORMAT='%(asctime)s:%(message)s'
logging.basicConfig(filename="Info.log", format=FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

parser = argparse.ArgumentParser(description="Descripcion de los parametros:")
# opc: opciones
parser.add_argument("-opc", type=int,
help = """-opc (1=codificar mensaje, 2=decodificar mensaje,
           3=hackear mensaje codificado, 4=investigar con llave API,
           5=Enviar un email, 6=escaneo de puertos, 7=DNS cache)""")
# Si quieres codificar/decodificar/hackear un mensaje,
# tienes que escoger entre cifrado cesar o de transposicion
parser.add_argument("-t_cifr", type=int, help="-t_cifr (1=Cesar, 2=Transposicion)")
# Hay que definir el tipo de idioma de tu mensaje
parser.add_argument("-lang", type=int, help='-lang (1=Ingles,2=Español)')
# msg: agrega tu mensaje
parser.add_argument("-msg", type=str, help='-msg "Aqui va el mensaje"')
# Si escogiste cifrado cesar, escribe el numero de permutaciones 
# que deseas que tenga tu mensaje
parser.add_argument("-rot", type=int, help='-rot (entre 1 y 25)')
# Si escogiste transposicion, escribe una llave
parser.add_argument("-key", type=str, help="-key 'llave'")
# Si quieres investigar a una organizacion con su llave API de hunter
parser.add_argument("-apikey", type=str, help="-apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7'")
parser.add_argument("-domain", type=str, help="-domain '(www.twitter.com / twitter.com / twitter)'")
# Si quieres enviar un mensaje especifica el tipo de correo
# puede ser: 1=gmail, 2=outlook/hotmail
parser.add_argument("-t_email", type=int, help='-t_email (1=gmail, 2=hotmail/outlook)')
# Agrega tu correo y tu contraseña para accesar a tu cuenta de correo
parser.add_argument("-email", type=str, help='-email "email@ejemplo.com"')
parser.add_argument("-passw", type=str, help='-pass "tu_contraseña"')
# Agrega el correo al que quieres enviar tu mensaje
parser.add_argument("-to", type=str, help='-to "email@ejemplo.com"')
# Agrega el asunto del correo
parser.add_argument("-subj", type=str, help='-subj "subject"')
# Si quieres enviar una imagen en tu correo, agrega estos parametros
parser.add_argument("-pic", type=str, help='-pic "nombre_imagen.jpg","c:\\users\\name\\pictures"')
# Si quieres saber que puertos estan abiertos
parser.add_argument("-ip", type=str, help='-ip "IP a escanear"')
parser.add_argument("-i", type=int, help='-i "Inicio de los puertos a escanear"')
parser.add_argument("-f", type=int, help='-f "Final de los puertos a escanear"')
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
            logging.info("Mensaje con Cifrado Cesar")
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
                    message = "[!] Error en transposicion, escogiste una opcion que no existe."
                    logging.error(message, data.opc)
                    print("[!] Agregaste una opcion invalida")
                    print("::: Cerrando programa...")
                logging.info("Mensaje con cifrado de Transposicion.")
            except:
                data.warning("Transposicion, gregaste un mensaje invalido")
                print(":[!] Agregaste una oracion/caracter invalido.")
                print(":::: Cerrando programa...")
                time.sleep(1)

    elif(data.t_cifr is None):
        # Investiga una organizacion con llave API
        if data.opc == 4:
            if(data.apikey is not None and data.domain is not None):
                h = Hunter(data.apikey, data.domain)
                h.search()
                h.showInfo(h.search())
                h.saveInfo(h.search())
                loggin.info("Investigar organizacion")
            else:
                logging.warning("[!]Error en investigar organizacion, hacen falta parametros.")    
                print(":[!] Hacen falta parametros para ejecutar el programa")
                print(":::: Cerrando programa...")
                time.sleep(1)

        elif data.opc == 5:
            se = SendEmail()
            t_email = data.t_email
            email = data.email
            password = data.passw
            to = data.to
            subject = data.subj
            se.setMessage(data.msg)
            msg = se.getMessage()
            logging.info("Envio de correos")

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
                    logging.info("Envio de correos con imagen")         

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
                logging.warning("[!]Error en envio de correos, hacen falta parametros")
                print("[!] Se necesitan mas parametros para enviar el correo.")

        elif data.opc == 6:
            if ((data.ip is not None) and (data.i is not None)and
               (data.f is not None)):
                scanPort(data.ip, data.i, data.f)
                print("* Ip: ", str(data.ip))
                print("* Puerto de inicio del escaneo: ", str(data.i))
                print("* Puerto de final del escaneo: ", str(data.f))
                logging.info("Escaneo de puertos.")

            else:
                logging.warning("[!]Error en escaneo de puertos, hacen falta parametros.")
                print("[!] No se puede realizar el escaneo", end=", ")
                print("hacen falta parametros.")
                print("::: Cerrando programa...")
                time.sleep(1)

        elif data.opc == 7:
            directory = os.getcwd()
            os.system(f"powershell -ExecutionPolicy ByPass ./DNS.ps1 -TargetFolder \"{directory}\"")
            logging.info("DNS del cache")

        else:
            logging.warning("[!]Error, agrego una opcion que no existe o ninguna.")
            print("[!] Error")
            print("::: Probablemente no agrego ninguna opcion")
            print("::: o la opcion seleccionada no existe.")
    else:
        logging.error("Ese tipo de cifrado no existe", str(data.t_cifr))
        print("[!] Ese tipo de cifrado no existe")

# except:
# logging.warning("[!]Error, tal vez no agrego un parametro necesario/correcto")
# print("[!] Error")
# print("::: Tal vez no agrego un parametro necesario/correcto")
# print("::: o agrego uno invalido")


