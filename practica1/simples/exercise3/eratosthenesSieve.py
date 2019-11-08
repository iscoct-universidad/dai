number = int(input("Introduzca el número máximo a buscar los primos: "))

def eratosthenesSieve(number):
    multiples = set()
    result = []

    for i in range(2, number):
        if (i not in multiples):
            result.append(i)

            crossedNumbers = range(i * i, number + 1, i)

            multiples.update(crossedNumbers)
    
    return result

if (number > 2):
    primes = eratosthenesSieve(number)

    print(primes)
else:
    print("El número debe ser mayor de 2")