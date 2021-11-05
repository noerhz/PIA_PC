import time
import re
import os

try:
	from pyhunter import PyHunter

except:
	print("[!] Instalando los modulos necesarios...")
	os.system("pip install PyHunter")
	print()

	print("::: Limpiando la terminal")
	os.system("cls")

	print("::: Ejecutando el programa de nuevo...")
	print()
	os.system("App.py")
	exit()


class Hunter:

	def __init__(self, apikey, domain):

		self.limit = 1

		self.setAPIKey(apikey)
		self.apikey = self.getAPIKey()

		self.setDomain(domain)
		self.domain = self.getDomain()


	def setAPIKey(self, apikey):
		if len(apikey) == 40:
			print("[*] Llave API valida")
			self.apikey = apikey

		else:
			print("[!] Esta no es una llave API de Hunter")
			print("::: Cerrando el programa...")
			time.sleep(1)

	def getAPIKey(self):
		return self.apikey


	#########################################################################
	def setDomain(self, domain):
		set_domain = re.match(r'(www.\w*.com|\w*.com|\w*)', domain)

		if(set_domain):
			print("[*] Dominio Valido")
			self.domain = domain

		else:
			print("[!] Esto no se ve como un dominio,")
			print("::: agregue la informacion de nuevo.")

			print("::: El dominio deberia verse asi:")
			print("::::: www.google.com")
			print("::::: google.com")
			print("::::: google")

			print("::: Cerrando el programa...")
			time.sleep(1)
			exit()

	def getDomain(self):
		return self.domain


	#########################################################################
	def search(self):
		hunter = PyHunter(self.apikey)
		result = hunter.domain_search(company=self.domain, limit=self.limit, emails_type='personal')

		return result


	def showInfo(self, results):
		try:
			if results['domain'] == None:
				print("[!] No se encontro a la organizacion")

			else:
				print('Dominio: ' + results['domain'])
			
				if results['organization'] == None:
					print("[!] No se encontro a la organizacion")
				
				else:
					print('Nombre de la organizacion: ' + results['organization'])
					
					if results['emails'] == None:
						print('[!] No se encontraron emails')
					
					else:
						print('Correos personales encontrados: ' + results['emails'][0]['value'])
						print('Nombres encontrados: ' +
							   results['emails'][0]['nombre'] +
							   ' ' + results['emails'][0]['apellido'])

		except:
			print("[!] Error")
			print("::: Cerrando el programa...")
			time.sleep(1)


	def saveInfo(self, results):
		try:
			file = open('Hunter' + self.domain + '.txt', 'w')
			if results['domain'] is None:
				pass
			else:
				file.write('Dominio: ' + results['domain'] + '\n')
			if results['organization'] is None:
				pass
			else:
				file.write('Nombre de la organizacion: ' + results['organization'] + '\n')
			if len(results['emails']) == 0:
				file.write('No se encontraron emails o nombres')
			else:
				file.write('Correos encontrados: ' + results['emails'][0]['value'] + '\n')
				file.write('Nombres encontrados: ' + results['emails'][0]['nombre'])
				file.write(' ' + results['emails'][0]['apellido'] + '\n')
			file.close()

		except:
			print("[!] Error")
			print("::: Cerrando programa...")
			time.sleep(1)