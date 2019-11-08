import numpy as np

def selectionSorting(array):
    length = len(array)

    for i in range(length):
        min = i

        for j in range(i, length):
            if (array[j] < array[min]):
                    min = j
        
        if (min != i):
            temp = array[i]
            array[i] = array[min]
            array[min] = temp

desiredLength = int(input("Introduzca la longitud del array deseado: "))
array = np.random.rand(desiredLength)

print("Unsorted array:", array)

selectionSorting(array)

print("Sorted array:", array)