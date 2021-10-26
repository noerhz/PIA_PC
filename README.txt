------------------------------------------------------------------------------------------
Opcion para codificar mensaje
# -lang *Escoje un idioma 1 para ingles 2 para español*
# -msg *"Escribe tu mensaje"*
# -rot *Escoje un numero del 1-25*
# -key *"Escribe una contraseña"*
# Ejemplo(s):
#:::: cifrado_cesar.py -lang 1 -msg "This is a test message" -rot 13
#:::: cifrado_cesar.py -lang 2 -msg "Este es un mensaje de prueba" -key "contraseña"

------------------------------------------------------------------------------------------

Opcion para Decodificar mensaje
# -lang *Escoje un idioma 1 para ingles 2 para español*
# -msg *"Escribe tu mensaje codificado"*
# -rot *Escoje un numero del 1-25*
# - -key *"Escribe una contraseña"*
# Ejemplo(s):
#:::: cifrado_cesar.py -lang 1 -msg "Write the encoded message" -rot 13
#:::: cifrado_cesar.py -lang 2 -msg "Escribe el mensaje codificado" -key "contraseña"

------------------------------------------------------------------------------------------

Opcion para Hackear mensaje
# -lang *Escoje un idioma 1 para ingles 2 para español*
# -msg *"Escribe tu mensaje codificado"*

# Ejemplo(s):
#:::: cifrado_cesar.py -lang 1 -msg "Write the encoded message" -t_cifr 1
#:::: cifrado_cesar.py -lang 2 -msg "Escribe el mensaje codificado" -t_cifr 2 

------------------------------------------------------------------------------------------
[*] Si quieres obtener informacion de una organizacion con tu llave API de hunter,
::: estas son las opciones:
	-opc 4
		-apikey *"Escribe tu llave API"*
			-domain *"Escribe aqui el dominio"*

[+] Example(s):
:::: Application.py -opc 4 -apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7' -domain "www.google.com"
:::: Application.py -opc 4 -apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7' -domain "google.com"
:::: Application.py -opc 4 -apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7' -domain "google"
