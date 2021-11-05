import time

class Message:

	def __init__(self):
		self.message = ""
		self.language = 0
		self.words_list = []

	################################################################
	def spanishDictionary(self):
		# Abrimos nuestro Archivo txt para leer
		file = open("dictEsp.txt", "r", encoding="utf-8")

		# Creamos una lista donde guardaremos las 
		# palabras de nuestro txt
		# 	** NO QUISE USAR UN DICCIONARIO (set())
		#   ** POR QUE DESPUES PIERDE EL ORDEN ALFABETICO
		dictionary = []

		for word in file:
			# Nos aseguramos de que las palabras no
			# incluyan un salto de linea ('\n') o 
			# un espacio (' ')
			word = word.replace("\n", "")
			word = word.replace(" ", "")
			word = word.lower()
			dictionary.append(word)
		# Como el contenido del txt ya esta en nuestro
		# dictionario ya podemos cerrarlo
		file.close()

		# Como el mensaje cifrado va a contener espacios
		# agregamos uno a la lista
		dictionary.append(" ")

		numbers = "0123456789"
		for number in numbers:
			dictionary.append(number)

		return dictionary


	def englishDictionary(self):
		# Abrimos nuestro archivo txt
		file = open("dictEng.txt", "r", encoding="utf-8")

		# Creamos una lista donde guardaremos las
		# palabras de nuestro txt
		dictionary = []

		for word in file:
			# Nos aseguramos de que las palabras no
			# incluyan un salto de linea ('\n') o 
			# un espacio (' ')
			word = word.replace("\n", "")
			word = word.replace(" ", "")
			word = word.lower()
			dictionary.append(word)
		file.close()

		# El mensaje cifrado puede tener espacios
		# asi que hay que agregarlo al diccionario
		dictionary.append(" ")

		# Tambien se aceptan numeros
		# por que los agregamos tambien
		numbers = "0123456789"
		for number in numbers:
			dictionary.append(number)


		return dictionary


	######################################################################
	def setLanguage(self, language):
		if language == 1:
			language = 0
			self.language = True

		elif language == 2:
			language = 0
			self.language =  False

		else:
			print()
			print("[!] Esa opcion no existe")
			print("::: Cerrando el programa...")
			time.sleep()
			exit()

	def getLanguage(self):
		return self.language


	#######################################################################
	def setMessage(self, message):
		if len(message) >= 3:
			print("[*] Mensaje valido")
			self.message = message.lower()

		else:
			print(":[!] El mensaje es muy corto")
			print("::: agrega uno mas largo.")
			exit()
			print()


	def getMessage(self):
		return self.message


	######################################################################
	def messageWords(self, sentence):
		cont = 0
		word = ""
		message = sentence + " "
		words_list = []

		# Leemos cada caracter del mensaje o
		# en este caso de la variable *message*
		for words_msg in message:

			# Las oraciones deben tener espacios
			# hay que validarlo y especificarle al programa
			if words_msg == " ":
				words_list.append(word)
				word = ""

			else:
				word = word + words_msg

		cont = 0
		nwords_list = []

		# No queremos que espacios en la lista
		# por lo que hay que asegurarnos que no haya
		for find_space in words_list:
			# En caso de que se guarde una palabra con espacios
			# la eliminamos
			without_space = find_space.replace(" ", "")

			if without_space != "":
				nwords_list.append(without_space)
			cont = cont + 1

		self.words_list = nwords_list

		# del nwords_list

		return self.words_list

	######################################################################
	def verifyLanguage(self, sentence):
		# Llamamos a la funcion messageWords() para saber 
		# el idioma que el usuario escogio
		words_list = self.messageWords(sentence)
		word_found = 0

		# Agregamos una condicional para verificar que
		# el mensaje esta escrito en el idioma correcto
		if self.getLanguage() == True:
			for word_list in words_list:
				for dict_word in self.englishDictionary():
					if word_list == dict_word:
						word_found = word_found + 1

		elif self.getLanguage() == False:
			for word_list in words_list:
				for dict_word in self.spanishDictionary():
					if word_list == dict_word:
						word_found = word_found + 1

		if word_found > 0:
			average = (word_found * 100) / len(words_list) 
			return average
		else:
			return 0
