def sol():
    lista = []
    for i in range(2, 101):
        for j in range(2, 101):
            lista.append(i**j)

    return len(set(lista))

print(sol())
