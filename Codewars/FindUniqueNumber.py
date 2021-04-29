def find_uniq(listanum):
    listanum.sort()
    if listanum[0] < listanum[len(listanum)-1] and listanum[0] < listanum[len(listanum)-2]:
        element = listanum[0]
        return element
    else:
        element = listanum[-1]
        return element
        

print(find_uniq([2, 1, 1]))
