def disemvowel(String):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    Lista = list(String)
    for i in range(len(String)):
        if String[i] in vowels:
            Lista.remove(String[i])
    StringNew = ''
    for i in Lista:
        StringNew += i

    return StringNew
