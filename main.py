from domain.nodo import Nodo
import time
from utils.lista_ordenada import ListaOrdenada
from utils.utils import *
from interface.interface import Interface


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

    # print("\n>>> Nodo pai:")
    # nodo_atual.print_estado()

    novos_nodos: list = nodo_atual.gerar_filhos()

    lista_visitados.append(nodo_atual)
    lista_abertos.remover(nodo_atual)

    # print(">>> Nodos filhos adicionados:")
    for nodo in novos_nodos:
        if nodo not in lista_abertos.lista and nodo not in lista_visitados:
            lista_abertos.inserir(nodo)
            # nodo.print_estado()

    achou_objetivo = nodo_atual.esta_completo()
    if achou_objetivo == True:
        tempo_final = time.time()
        interface.print_resultados(nodo_atual, lista_visitados, lista_abertos, tempo_inicial, tempo_final)


# Caso fácil:
# 1 8 2
# X 4 3
# 7 6 5
# Entrada: 1 8 2 X 4 3 7 6 5

# Casos médios:
# 4 X 6
# 7 2 3
# 1 8 5
# Entrada: 4 X 6 7 2 3 1 8 5

# 2 X 8
# 6 4 5
# 3 1 7
# Entrada: 2 X 8 6 4 5 3 1 7

# Casos difíceis:
# 8 6 7
# 2 5 4
# 3 X 1
# Entrada: 8 6 7 2 5 4 3 X 1

# 6 4 7
# 8 5 X
# 3 2 1
# Entrada: 6 4 7 8 5 X 3 2 1
