from nodo import Nodo
import time
from lista_ordenada import ListaOrdenada
from utils import *
from interface import Interface


interface = Interface()

while True:
    lista_numeros_entrada = interface.receber_entrada()
    if not tem_solucao(lista_numeros_entrada):
        print("A configuração fornecida não tem solução! Por favor, insira outra.")
    else:
        break

matriz = transformar_lista_em_matriz(lista_numeros_entrada)

tempo_inicial = time.time()

lista_abertos = ListaOrdenada()
lista_visitados = []

nodo_origem = Nodo(matriz, None)
lista_abertos.inserir(nodo_origem)

achou_objetivo = False
while not achou_objetivo:
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
        interface.print_resultados(nodo_atual, lista_visitados, lista_abertos, tempo_inicial, tempo_final)


# Tem solução
# matriz = [[1, 8, 2],
#           ["X", 4, 3],
#           [7, 6, 5]]
# Entrada: 1 8 2 X 4 3 7 6 5

# matriz = [[5, 2, 8],
#           [4, 1, 7],
#           ["X", 3, 6]]
# Entrada: 5 2 8 4 1 7 X 3 6

# matriz = [[2, "X", 8],
#           [6, 4, 5],
#           [3, 1, 7]]
# Entrada: 2 X 8 6 4 5 3 1 7

# matriz = [[4, "X", 6],
#           [7, 2, 3],
#           [1, 8, 5]]
# Entrada: 4 X 6 7 2 3 1 8 5

# matriz = [[1, 2, 3],
#           [5, "X", 6],
#           [4, 7, 8]]
# Entrada: 1 2 3 5 X 6 4 7 8


# Não tem solução
# matriz = [[8, 1, 2],
#           ["X", 4, 3],
#           [7, 6, 5]]
# Entrada: 8 1 2 X 4 3 7 6 5

# matriz = [[1, 2, 3],
#           [4, 5, 6],
#           ["X", 8, 7]]
# Entrada: 1 2 3 4 5 6 X 8 7

# matriz = [["X", 2, 4],
#           [8, 5, 3],
#           [1, 6, 7]]
# Entrada: X 2 3 8 5 3 1 6 7
