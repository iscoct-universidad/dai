import random

def askNumber():
    return int(input("Introduzca el número que cree que ha sido escogido al azar: "))

minValue = 1
maxValue = 100
maxAttemps = 10
attemps = 0
randomNumber = random.randint(minValue, maxValue)

number = askNumber()
found = number == randomNumber
attemps += 1

while not found and attemps < maxAttemps:
    if (number < randomNumber):
        print("El número buscado es mayor")
    else:
        print("El número buscado es menor")

    number = askNumber()
    found = number == randomNumber
    attemps += 1

if (number == maxAttemps):
    print("Lo siento, finalmente no encontró el número buscado")
else:
    print("Exacto. Muchas gracias por participar en la búsqueda")