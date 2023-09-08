import copy

# Creditos:

def tem_solucao(lista: list):
    index_vazio = lista.index("X")
    lista_copia = copy.deepcopy(lista)
    lista_copia[index_vazio] = 0

    contador = 0
    for i in range(8):
        for j in range(i + 1, 9):
            if lista_copia[j] and lista_copia[i] and lista_copia[i] > lista_copia[j]:
                contador += 1

    return contador % 2 == 0

def transformar_lista_em_matriz(lista: list):
    return [lista[i:i+3] for i in range(0, 9, 3)]
