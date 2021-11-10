# Tareas de Ciberseguridad Automatizadas

Para codificar un mensaje
-------------------------

	-opc 1
		
	-lang Escoge un idioma, 1 para ingles y 2 para español
			
	-msg "Escriba el mensaje que quiere codificar"

Cifrado cesar:

	-t_cifr 1 
	
	-rot Escriba un numero del 1-25
	
Cifrado de Transposicion: 

	-t_cifr 2 
	
	-key "Escriba una contraseña"

*Ejemplo(s):*

	Application.py -opc 1 -lang 1 -msg "This is a test message" -t_cifr 1 -rot 13

	Application.py -opc 1 -lang 2 -msg "Este es un mensaje de prueba" -t_cifr 2 -key "contraseña"


Para Decodificar un mensaje
---------------------------

	-opc 2
	
	-lang Escoge un idioma, 1 para ingles y 2 para español
	
	-msg "Escribe tu mensaje codificado"
	
Cifrado cesar:

	-t_cifr 1 
	
	-rot Escriba un numero del 1-25
	
Cifrado de Transposicion: 

	-t_cifr 2 
	
	-key "Escriba una contraseña"
	
*Ejemplo(s):*
	
	Application.py -opc 2 -lang 1 -msg "Write the encoded message" -t_cifr 1 -rot 13
	
	Application.py -opc 2 -lang 2 -msg "Escribe el mensaje codificado" -t_cifr 2 -key "contraseña"



Para Hackear un mensaje
-----------------------

	-opc 3

	-lang Escoge un idioma, 1 para ingles y 2 para español

	-msg "Escribe tu mensaje codificado"

*Ejemplo(s):*

Cifrado Cesar: 

	Application.py -opc 3 -lang 1 -msg "Write the encoded message" -t_cifr 1

Cifrado de Transposicion:

	Application.py -opc 3 -lang 2 -msg "Escribe el mensaje codificado" -t_cifr 2 

Para obtener obtener informacion de una organizacion con tu llave API de hunter, estas son las opciones:
--------------------------------------------------------------------------------------------------------	
	
	-opc 4
	
	-apikey "Escribe tu llave API"
	
	-domain "Escribe aqui el dominio"

*Ejamplo(s):*

	Application.py -opc 4 -apikey "31mn93abbx811o05q119lDp1mms931ml5c31jjj7" -domain "www.google.com"

	Application.py -opc 4 -apikey "31mn93abbx811o05q119lDp1mms931ml5c31jjj7" -domain "google.com"

	Application.py -opc 4 -apikey "31mn93abbx811o05q119lDp1mms931ml5c31jjj7" -domain "google"

Para mandar un correo (se puede adjuntar solo una imagen en el correo):
-----------------------------------------------------------------------

	-opc 5
	
	-t_email "Elija el tipo de correo con 1 para gmail y 2 para hotmail/outlook"
	
	-email "Escriba su correo"
	
	-passw "Escriba la contraseña de su correo"
	
	-to  "Escriba el correo a quien va dirigido"
						
	-subj "Escriba el asunto de su correo"
							
	-msg "Escriba su mensaje"
								
Si desea adjuntar una imagen a su correo:
	
	-pic "Escriba el nombre de su imagen","Escriba el directorio donde esta alojada la imagen"
	
*Ejemplo(s):*
	
	Application.py -opc 5 -t_email 2 -email "ejemplo@outlook.com" -passw "sucontraseña" -to "ejemplo2@account.com" 

	-subj "Asunto:" -msg "Su mensaje"

	
	Application.py -opc 5 -t_email 1 -email "ejemplo@gmail.com" -passw "sucontraseña" -to "ejemplo2@account.com" 

	-subj "Asunto:" -msg "Su mensaje" -pic "Picture.jpg","C:\Users\UserName\Documents"

	
	Application.py -opc 5 -t_email 2 -email "ejemplo@outlook.com" -passw "sucontraseña" -to "ejemplo2@account.com" 

	-subj "Asunto:" -msg "Su mensaje" -pic "Imagen.jpeg","C:\Users\UserName\Documents"

	
	Application.py -opc 5 -t_email 1 -email "ejemplo@gmail.com" -passw "sucontraseña" -to "ejemplo2@account.com" 
	
	-subj "Asunto:" -msg "Su mensaje" -pic "Imagen.jpg","C:\Users\UserName\Documents"

Para escaneo de puertos:
---------------------------------------

	-opc 6 
	
	-ip "Escriba la IP"
	
	-i Escriba el incio de los puertos a escanear
	
	-f Escriba el final de los puertos a escanear

*Ejemplo(s):*
	
	Application.py -opc 6 -ip "192.168.1.15" -i "88" -f "10030"

Para verficar el DNS del cache:
-------------------------------

	-opc 7

*Ejemplo(s):*
	
	Application.py -opc 7
