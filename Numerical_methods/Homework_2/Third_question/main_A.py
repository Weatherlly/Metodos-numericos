def substituicoes_retroativas(A, b):
    '''Executa o método das substituições retroativas para resolver o sistema 
       linear triangular superior Ax=b.
       Parâmetros de entrada: A é uma matriz triangular superior e b é o vetor constante. 
    '''
    ## n é a ordem da matriz A
    n = len(A)
    
    ## inicializa o vetor x com tamanho n e elementos iguais a 0
    x = n * [0] 
    
    for i in range(n-1, -1, -1):
      S = 0
      for j in range(i+1, n):
        S = S + A[i][j] * x[j]
      x[i] = (b[i] - S)/A[i][i]
    
    return x

def gauss(A, b):
  n = len(A)
  for k in range(0, n-1):
    for i in range(k+1, n):
      m = - A[i][k]/A[k][k]
      for j in range(k+1, n):
        A[i][j] = m * A[k][j] + A[i][j]
      b[i] = m *b[k] + b[i]
      A[i][k] = 0
  x = substituicoes_retroativas(A, b)
  return x

A1 = [[1, 1, 1],
      [10, -8, 0],
      [8, 0, -3]]
b1 = [0, 65, 120]
x = gauss(A1, b1)
print("Os coeficientes de I1, I2 e I3 são respectivamente: ", x)