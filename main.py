from nodo import Nodo
import asyncio

# Tem solução
# matriz = [[1, 8, 2],
#           ["X", 4, 3],
#           [7, 6, 5]]
matriz = [[5, 2, 8],
          [4, 1, 7],
          ["X", 3, 6]]



# Não tem solução
# matriz = [[8, 1, 2],
#           ["X", 4, 3],
#           [7, 6, 5]]
# matriz = [[1, 2, 3],
#           [4, 5, 6],
#           ["X", 8, 7]]

# [[(0, 0), (1, 0), (2, 0)],
#  [(0, 1), (1, 1), (2, 1)],
#  [(0, 2), (1, 2), (2, 2)]]


lista_abertos = []
lista_visitados = []

nodo_origem = Nodo(matriz, None)
lista_abertos.append(nodo_origem)

# for i in range(4):
achou_objetivo = False
while not achou_objetivo:
# for i in range(10):
    nodo_atual: Nodo = lista_abertos[0]

    print(">>> Nodo pai:")
    nodo_atual.print_estado()

    novos_nodos: list = nodo_atual.gerar_filhos()

    lista_visitados.append(nodo_atual)
    lista_abertos.remove(nodo_atual)

    print("\n>>> Nodos filhos adicionados:")
    for nodo in novos_nodos:
        if nodo not in lista_abertos and nodo not in lista_visitados:
            lista_abertos.append(nodo)
            nodo.print_estado()

    # print("\nlista abertos:")
    # for nodo in lista_abertos:
    #     print(nodo.estado)

    # print("lista visitados:")
    # for nodo in lista_visitados:
    #     print(nodo.estado)

    achou_objetivo = nodo_atual.esta_completo()
    if achou_objetivo == True:
        print("sucesso!")
        print(nodo_atual.estado)

# print("sucesso!")
# print(lista_visitados[0].estado)
