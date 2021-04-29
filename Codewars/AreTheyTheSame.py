def comp(array1, array2):
    if array1 == None or array2 == None:
        return False    
    if len(array1) != len(array2):
        return False
    
    array1.sort(key=abs)
    array2.sort(key=abs)

    if isinstance(array1, list) and isinstance(array2, list):
        for item in range(len(array1)):
            num_a = array1[item]
            num_b = array2[item]
            if num_b != num_a**2:
                return False
    return True
