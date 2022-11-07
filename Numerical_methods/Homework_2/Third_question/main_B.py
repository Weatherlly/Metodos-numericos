def gauss_det(A, b):
  n = len(A)
  for k in range (0, n-1):
    for i in range(k+1, n):
      m = - A[i][k]/A[k][k]
      for j in range(k+1, n):
        A[i][j] = m * A[k][j] + A[i][j]
      b[i] = m * b[k] + b[i]
      A[i][k] = 0

  det = 1

  for i in range(0, n):
    det = det * A[i][i]
  if det != 0:
    x = substituicoes_retroativas(A, b)
    return (det)
  else: 
    print("Erro! O sistema é singular: determinante da matriz A é zero.")
    return (det)

A2 = [[1, 1, 1],
      [10, -8, 0],
      [8, 0, -3]]
b2 = [0, 65, 120]
x = gauss_det(A2, b2)
print(x)