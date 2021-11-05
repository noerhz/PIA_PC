import Message
import time

class CifradoCesar(Message.Message):
	def __init__(self, mode, message, key):
		super().__init__()
		self.mode = mode
		self.verifyMode()

		super().setMessage(message)
		self.message = super().getMessage()

		self.key = key
		self.verifyKey()

	#######################################################
	def verifyMode(self):
		mode = self.mode
		if(mode == None):
			print("[!] No agrego el parametro '-mode'")
			exit()
		elif(mode < 1 or mode > 3):
			print("[!] El modo '" + str(mode) + "' no existe.")
			exit()
		else:
			print("[*] Modo valido")
			return mode

	def verifyKey(self):
		key = self.key
		if(self.mode == 1 or self.mode == 2):
			if(key == None):
				print("[!] No agrego el parametro '-key'")
				exit()
			elif(key < 1 or key > 25):
				print("[!] La llave '" + str(key) + "' no existe.")
				exit()
			else:
				print("[*] Llave valida")
				key = key
				return key

		elif(self.mode == 3):
			# Si el usuario agrega un parametro, mandamos una advertencia
			# por que no es necesario
			if(key != None):
				print("[!] No es necesario agregar una llave para hacekar")
				print("::: el mensaje")
				exit()
			
			elif(key == None):
				return True


	############################################################
	def codifyMessage(self):
		for i in range(1, 3, 1):
			super().setLanguage(i)
			average = super().verifyLanguage(self.message)

			if(average >= 50):
				alphabet = "abcdefghijklmnopqrstuvwxyz"
				msg = super().getMessage().lower()
				message = msg.replace("ñ", "n")

				key = self.key
				codify_message = ""
				cont = 0

				for letter in message:
					if(letter not in alphabet):
						codify_message = codify_message + letter
					else:
						for letter2 in alphabet:
							if(letter == letter2):
								j = cont + key
								if j > 25:
									j = j - 26
								codify_message = codify_message + alphabet[j]
							cont = cont + 1
						cont = 0				
				return codify_message
				break

		if(average < 50):
			print("[!] Tu mensaje no fue codificado.")
			print("::: Solo aceptamos Español/Ingles tal vez")
			print("::: el mensaje original fue escrito en otro ")
			print("::: idioma.")
			time.sleep(1)
			exit()


	def decodeMessage(self):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		msg = super().getMessage().lower()
		message = msg.replace("ñ", "n")

		key = self.key
		decode_message = ""
		cont = 0

		for letter in message:
			if(letter not in alphabet):
				decode_message = decode_message + letter
			else:
				for letter2 in alphabet:
					if(letter == letter2):
						j = cont - key
						if j > 25:
							j = j - 26
						decode_message = decode_message + alphabet[j]
					cont = cont + 1
				cont = 0

		aux = False
		# Verificamos el idioma
		for i in range(1, 3, 1):
			super().setLanguage(i)

			average = super().verifyLanguage(decode_message)
			if(average >= 30):
				aux = True
				return decode_message
				break
			else:
				continue

		if aux == False:
			print("[!] Tu mensaje no fue decodificado.")
			print("::: Solo aceptamos Español/Ingles, tal vez")
			print("::: el mensaje original fue escrito en otro")
			print("::: idioma.")
			time.sleep(1)
			exit()


	#####################################################
	def hackMessage(self):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		msg = super().getMessage().lower()
		message = msg.replace("ñ", "n")

		for key in range(0, 26, 1):
			decode_message = ""
			cont = 0

			for letter in message:
				if(letter not in alphabet):
					decode_message = decode_message + letter
				else:
					for letter2 in alphabet:
						if(letter == letter2):
							j = cont - key
							if j > 25:
								j = j - 26
							decode_message = decode_message + alphabet[j]
						cont = cont + 1
					cont = 0

			aux = False
			# Verificamos el idioma
			for i in range(1, 3, 1):
				super().setLanguage(i)

				average = super().verifyLanguage(decode_message)
				if(average >= 30):
					aux = True
					#regresa decode_message
					break
				else:
					continue

			if aux == True:
				break

		if aux == True:
			return decode_message

		elif aux == False:
			print("[!] Lo sentimos, no podemos hackear el mensaje.")
			print("::: Solo aceptamos Español/Ingles, tal vez")
			print("::: el mensaje original fue escrito en otro")
			print("::: idioma.")
			time.sleep(1)
			exit()
