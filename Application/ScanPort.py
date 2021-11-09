import re
from socket import *
import csv
pMin = 1
pMax = 49151


# Función para validar IP
def validarIP(address):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)
    if bool(match) is False:
        return False
    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            return False
    return True


# Función validar rango de puertos a escanear
def validarPuertos(begin, end):
    if (begin in range(pMin, pMax)) and (end in range(pMin, pMax)):
        if (begin <= end):
            return True
        else:
            return False
    else:
        return False


# Función para el escaneo de puertos
def scanPort(ip, begin, end):
    puertosAbiertos = False
    # validar si la dirección ip es correcta
    if validarIP(ip) is False:
        print("*La dirección IP ingresada es inválida")
    if validarPuertos(begin, end) is False:
        print("*El rango ingresada es inválido")
    # Comienzo del escaneo
    if (validarIP(ip) is True) and (validarPuertos(begin, end) is True):
        print("** ESCANEANDO PUERTOS **\n**Esto puede tomar un momento**")
        resultado = [["Ip:", ip]]
        for port in range(int(begin), int(end) + 1):
            socket_instance = socket(AF_INET, SOCK_STREAM)
            scanner_response = socket_instance.connect_ex((ip, port))
            if scanner_response == 0:
                puertosAbiertos = True
                resultado.append(["Puerto Abierto:", port])
            socket_instance.close()
        if puertosAbiertos is True:
            myFile = open("ResultadoEscaneo.csv", "w", newline="")
            with myFile:
                writer = csv.writer(myFile)
                writer.writerows(resultado)
            print("** FIN DEL ESCANEADO **")
            print("Revisa el archivo ResultadoEscaneo.csv")
        else:
            print("[!] No se encontraron puertos abiertos")
            print("::: no hay puertos abiertos en el rango establecido")
