def find_outlier(integers):
    odd = []
    even = []
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            odd.append(integers[i])
        else:
            even.append(integers[i])
    if len(odd) > 1:
        return even[0]
    else:
        return odd[0]
    
# Other solution
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
