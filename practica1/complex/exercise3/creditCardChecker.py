import re

chain = input("Introduzca la tarjeta de crédito:")

found = re.match("^([0-9]{4}[ |-]){3}[0-9]{4}", chain)

if found:
    print("Tarjeta de crédito válida")
else:
    print("Tarjeta de crédito no válida")