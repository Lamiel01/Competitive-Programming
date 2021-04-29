def duplicate_count(String):
    times = 0
    noAdd = []
    maxRelative = 0
    Lista = list(String)
    String = String.lower()
    for i in range(len(String)):
        if String[i] not in noAdd:
            noAdd.append(String[i])
            n = String.count(String[i])
            if n > maxRelative:
                maxRelative = n
                if maxRelative >= 2:
                    times += 1
                    maxRelative = 0
    
    return times


print(duplicate_count('wwbb'))
