from nodo import Nodo
import time
from lista_ordenada import ListaOrdenada

# Tem solução
# matriz = [[1, 8, 2],
#           ["X", 4, 3],
#           [7, 6, 5]]
# matriz = [[5, 2, 8],
#           [4, 1, 7],
#           ["X", 3, 6]]

matriz = [[2, 1, 8],
          [6, 4, 5],
          ["X", 3, 7]]

# matriz = [["X", 2, 4],
#           [8, 5, 3],
#           [1, 6, 7]]


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


lista_abertos = ListaOrdenada()
lista_visitados = []

tempo_inicial = time.time()
nodo_origem = Nodo(matriz, None)
lista_abertos.inserir(nodo_origem)

achou_objetivo = False
while not achou_objetivo:
# for i in range(10):
    nodo_atual: Nodo = lista_abertos.primeiro()

    print("\n>>> Nodo pai:")
    nodo_atual.print_estado()

    novos_nodos: list = nodo_atual.gerar_filhos()

    lista_visitados.append(nodo_atual)
    lista_abertos.remover(nodo_atual)

    print(">>> Nodos filhos adicionados:")
    for nodo in novos_nodos:
        if nodo not in lista_abertos.lista and nodo not in lista_visitados:
            lista_abertos.inserir(nodo)
            nodo.print_estado()

    achou_objetivo = nodo_atual.esta_completo()
    if achou_objetivo == True:
        tempo_final = time.time()
        print("sucesso!")
        print(nodo_atual.estado)

        # print("\nlista abertos:")
        # lista_abertos_custos = list(
        # map(lambda x: x.custo_total, lista_abertos.lista))
        # print(lista_abertos_custos)
        print("tamanho visitados: " + str(len(lista_visitados)))
        print("tempo decorrido: " + str(tempo_final - tempo_inicial) + " segundos")
        print("tamanho do caminho (profundidade): " + str(nodo_atual.profundidade))
        # print("lista visitados:")
        # for nodo in lista_visitados:
        #     print(nodo.estado)
