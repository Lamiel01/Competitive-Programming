def digital_root(n):
    if len(str(n)) > 1:
        suma=0
        lista = list(map(int, str(n)))
        for i in lista:
            suma = suma + i
        return digital_root(suma)
    else:
        return n


print(digital_root(1))
