def solvable(matriz):
    """
    Check whether a 3x3 sliding puzzle is solvable.

    Checks the number of "inversions". If this is odd then the puzzle configuration is not solvable.

    An inversion is when two tiles are in the wrong order.

    For example, the sequence 1, 3, 4, 7, 0, 2, 5, 8, 6 has six inversions:

    3 > 2
    4 > 2
    7 > 2
    7 > 5
    7 > 6
    8 > 6

    The empty tile is ignored.
    """

    matriz_em_uma_linha = []
    for lista in matriz:
        for numero in lista:
            matriz_em_uma_linha.append(numero)

    count = 0

    for i in range(8):
        for j in range(i+1, 9):
            if matriz_em_uma_linha[j] and matriz_em_uma_linha[i] and matriz_em_uma_linha[i] > matriz_em_uma_linha[j]:
                count += 1

    return count % 2 == 0
