def solve(n):
  if n == 1:
      return 'chirp'
  else:
      return 'chirp' + '-' + solve(n-1)
print(solve(5))
