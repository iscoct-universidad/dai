import numpy as np

def insertionSorting(array):
    length = len(array)

    for i in range(1, length):
        temp = array[i]
        j = i

        while (j > 0 and array[j - 1] > temp):
            array[j] = array[j - 1]
            j -= 1

        array[j] = temp

desiredLength = int(input("Introduzca la longitud del array deseado: "))
array = np.random.rand(desiredLength)

print("Unsorted array:", array)

insertionSorting(array)

print("Sorted array:", array)