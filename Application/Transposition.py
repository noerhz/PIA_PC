import Message
import math

class Transposition(Message.Message):

	def __init__(self):
		super().__init__()
		self.key = 0

	def setKey(self, key):
		if len(key) >= len(self.message):
			key = ""
			print(":[!] Agrego una llave mayor/igual que el mensaje")
			exit()

		if " " in key:
			key = ""
			print(":[!] Agregaste un espacio en la llave")
			exit()

		elif key.isalpha() == False:
			key = ""
			print(":[!] La llave solo permite letras")
			exit()

		else:
			self.key = len(key)

	def getKey(self):
		return self.key


	######################################################################
	def encodeMessage(self):
		if super().verifyLanguage(super().getMessage()) < 50:
			print(":[!] Para el tipo de codificacion, solo se aceptan oraciones en ingles/español")
			exit()
		else:
			message = super().getMessage()
			key = self.getKey()
			columns = [''] * key
			counter = 0

			for letter in message:
			    while counter < key:
			        columns[counter] = columns[counter] + letter
			        counter = counter + 1
			        break

			    if counter == key:
			        counter = 0

			encoded_message = ""
			for column in columns:
				encoded_message = encoded_message +  column

			return encoded_message

	# Para darse una idea de como funciona el metodo de transposicion:
	# La funcion de decodificacion del metodo de transposicion simulara 'columnas'
	# y 'filas' de la cuadricula que es escrita en texto plano usando una lista
	# de caracteres. Primero necesitamos calcular unos valores.
	def unencodeMessage(self):
		message = super().getMessage()
		key = self.getKey()

		# El numero de columnas en nuestas cuadricula:
		n_columns = int(math.ceil(len(message) / float(key)))
		# El numero de filas que nuestras cuadricula necesesitara:
		n_rows = key
		# El numero de 'cuadros sombreados' en la ultima columna de la cuadricula:
		n_shaded_boxes = (n_columns * n_rows) - len(message)

		# Cada caracter en texto plano representa una columna de la cuadricula.
		plaintext = [''] * n_columns

		# Las columnas y filas de variables ubicaran a donde ira el 
		# siguiente caracter en la cuadricula del mensaje cifrado.
		column = 0
		row = 0

		for letter in message:
			plaintext[column] += letter
			column += 1 # Ubicamos la siguiente columna.

			# Si no hay mas columnas O estamos en un 'cuadro sombreado', volvemos
			# a la primera columna y la siguiente fila.
			if (column == n_columns) or (column == n_columns - 1 and row >= n_rows - n_shaded_boxes):
				column = 0
				row += 1

		unencodeMessage = ''.join(plaintext)
		if super().verifyLanguage(unencodeMessage) >= 50:
			return unencodeMessage

		elif super().verifyLanguage(unencodeMessage) < 50:
			print(":[!] Lo sentimos, pero no podemos decodificar el mensaje.")
			print(":::: Solo aceptamos ingles/español, tal vez")
			print(":::: el mensaje original fue escrito en otro idioma")
			print(":::: o agregaste una llave incorrecta.")
			return ""


	def hackMessage(self):
		if super().verifyLanguage(super().getMessage()) > 60:
			print(":[!] Este mensaje no esta codificado")
			print(super().verifyLanguage(super().getMessage()))
			exit()
		else:
			message = super().getMessage()

			for key in range(1, len(message)):

				# El numero de columnas en nuestra cuadricula de transposicion:
				n_columns = int(math.ceil(len(message) / float(key)))
				# El numero de filas que nuestra cuadricula necesitara:
				n_rows = key
				# El numero de 'cuadros sombreados en la ultima columna de la cuadricula:
				n_shaded_boxes = (n_columns * n_rows) - len(message)

				# Cada caracter en texto plano representa una columna en la cuadricula.
				plaintext = [''] * n_columns

				# Las columnas y filas de variables ubicaran a donde ira el 
				# siguiente caracter en la cuadricula del mensaje cifrado.
				column = 0
				row = 0

				for letter in message:
					plaintext[column] += letter
					column += 1 # Ubicamos la siguiente columna.

					# Si no hay mas columnas O estamos en un 'cuadro sombreado', volvemos
					# a la primera columna y la siguiente fila
					if (column == n_columns) or (column == n_columns - 1 and row >= n_rows - n_shaded_boxes):
						column = 0
						row += 1

				unencodeMessage = ''.join(plaintext)
				if super().verifyLanguage(unencodeMessage) > 60:
					return unencodeMessage
					break

			if super().verifyLanguage(unencodeMessage) <= 60:
				print(":[!] Lo sentimos, pero no podemos hackear el mensaje.")
				print(":::: Solo aceptamos ingles/español, tal vez")
				print(":::: el mensaje original fue escrito en otro idioma.")
				exit() 