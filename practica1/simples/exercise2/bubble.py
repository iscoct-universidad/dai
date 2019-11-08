import numpy as np

def bubbleSorting(array):
    length = len(array)

    for i in range(0, length - 1):
        for j in range(i, length):
            if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp

desiredLength = int(input("Introduzca la longitud del array deseado: "))
array = np.random.rand(desiredLength)

print("Unsorted array:", array)

bubbleSorting(array)

print("Sorted array:", array)