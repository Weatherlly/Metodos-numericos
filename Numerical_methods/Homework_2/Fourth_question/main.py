def norma(v, x):
  """ Calcula a norma entre dois vetores v e x. """
  n = len(v)
  maxnum = 0
  maxden = 0
  for i in range(0, n):
    num = abs(v[i] - x[i])
    if num > maxnum:
      maxnum = num
    den = abs(v[i])
    if den > maxden:
      maxden = den
  return maxnum/maxden

def seidel(A, b, epsilon, iterMax=50):
  n = len(A)
  x = n * [0]
  v = n * [0]

  for i in range(0, n):
    for j in range(0, n):
      if i != j:
        A[i][j] = A[i][j]/A[i][i]
    b[i] = b[i]/A[i][i]

  for k in range(1, iterMax+1):
    for i in range(0, n):
      S = 0
      for j in range(0, n):
        if i != j:
          S = S + A[i][j] * x[j]
      x[i] = b[i] - S
    d = norma(x, v)
    if d <= epsilon:
      return x

    v = x[:]

A = [[17, -2, -3],
     [-5, 21, -2],
     [-5, -5, 22]]

b = [500, 200, 30]
eps = 0.0005
x = seidel(A, b, eps)
print(x)
##Resultado obtido em 5 iterações