import re

chain = input("Introduzca el correo electrónico: ")

found = re.match("^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$", chain)

if found:
    print("Correo electrónico correcto")
else:
    print("El correo electrónico no es válido")