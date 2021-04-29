def perimeter(n):
    a, b = 0, 1
    lista = [1]
    for i in range(n):
        a, b = b, a + b
        lista.append(b)

    suma = sum(lista)

    return suma*4

print(perimeter(20))
