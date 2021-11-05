# Este codigo solo se utilizo para sacar el valor hash de cada archivo

import hashlib
import argparse
import os


parser = argparse.ArgumentParser(description="Description")
parser.add_argument("-file", type=str, help="asdf")
data = parser.parse_args()

try:
	# Tratamos de abrir el archivo que se agrego
	file = open(data.file, "rb")
	# Guardamos el contenido en el archivo 'info'
	info = file.read()

	# Y generamos el hash
	the_hash = hashlib.sha512(info)
	hashed = the_hash.hexdigest()
	print(hashed)
except:
	print("[!] 'Hash.py' tiene que estar en el mismo folder")
	print("::: que el archivo")