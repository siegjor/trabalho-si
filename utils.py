def tem_solucao(matriz):
    matriz_em_uma_linha = []
    for lista in matriz:
        for numero in lista:
            matriz_em_uma_linha.append(numero)

    contador = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if matriz_em_uma_linha[j] and matriz_em_uma_linha[i] and matriz_em_uma_linha[i] > matriz_em_uma_linha[j]:
                contador += 1

    return contador % 2 == 0
