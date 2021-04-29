def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n == 3:
        return signature
    suma = []
    suma.append(signature[0])
    suma.append(signature[1])
    suma.append(signature[2])
    for i in range(n-3):
        suma.append(suma[i+2]+suma[i+1]+suma[i])
        
    return suma
  
# Other solution
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
