def imprimir(A, titulo):
    print(titulo)
    for linha in A:
        for value in linha:
            print(f"{value:6.7f} ", end="")
        print()
    print("")


def inversao(A):
    num_linhas = len(A)
    num_cols = len(A[0])

    m1 =  - 1
    n2 = num_cols * 2

    if num_linhas != num_cols:
        print("Error: La matriz no es cuadrada. Por tanto, no es invertible.")
        return None

    # Construção da matriz A | I
    for idx_linha in range(num_linhas):
        A[idx_linha] += [1 if idx_linha == j else 0 for j in range(num_linhas)]

    imprimir(A, "Matriz ampliada inicial:")

    # Algoritmo - Triangularização superior

    for idx_col in range(num_cols):
        # Busca de pivot
        print(f"Processando coluna {idx_col}")
        l = [(abs(A[idx_linha][idx_col]), idx_linha) for idx_linha in range(idx_col, num_linhas) if A[idx_linha][idx_col] != 0]
        if len(l) == 0:
            print("Erro: A matriz não é invertivel")
            return None

        idx_linha = min(l)[1]
        if idx_linha != idx_col:
            print(f"Trocar linha {idx_linha} com {idx_col}")
            A[idx_col], A[idx_linha] = A[idx_linha],  A[idx_col]
            imprimir(A, "Matriz Alterada")

        # Triangularização superior
        for idx_linha in [idx for idx in range(idx_col + 1, num_linhas) if A[idx][idx_col] != 0]:
            alpha = -A[idx_linha][idx_col] / A[idx_col][idx_col]
            print(f"Ajuste para linha {idx_linha} é {alpha}")
            for k in range(n2):
                A[idx_linha][k] += A[idx_col][k] * alpha
            imprimir(A, "Matriz ajustada")

    imprimir(A, "Matriz Triangularização superior")

    # Algoritmo - Triangularização inferior

    for idx_col in range(1, num_cols):
        print(f"Processando coluna {idx_col}")
        for idx_linha in range(idx_col):
            alpha = -A[idx_linha][idx_col] / A[idx_col][idx_col]
            print(f"linha {idx_linha}, fator {alpha}")
            for k in range(idx_col, n2):
                A[idx_linha][k] += A[idx_col][k] * alpha
            imprimir(A, "Ajustada")

    imprimir(A, "Matriz Triangularização inferior")
    # Algoritmo - Transformação da matriz identidade

    for idx_linha in range(num_linhas):
        alpha = A[idx_linha][idx_linha]
        for idx_col in range(idx_linha, n2):
            A[idx_linha][idx_col] /= alpha

    imprimir(A, "Matriz identidade")

    inversa = []
    for linha in A:
        inversa.append(linha[num_cols:])

    return inversa

A = [[1, 1, 1], 
         [10, -8, 0],
         [8, 0, -3]]
x = inversao(A)
imprimir(x, "Inversa")