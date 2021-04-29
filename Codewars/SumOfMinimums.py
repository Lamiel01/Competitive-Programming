def sum_of_minimums(numbers):
    suma = 0
    for i in range(len(numbers)):
        x = min(numbers[i])
        suma += x
        
    return suma
