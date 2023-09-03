from nodo import Nodo

matriz = [["X", 2, 3],
          [1, 4, 5],
          [8, 7, 6]]

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
    nodo_atual: Nodo = lista_abertos[0]
    novos_nodos: list = nodo_atual.gerar_filhos()

    lista_visitados.append(nodo_atual)
    lista_abertos.remove(nodo_atual)

    for nodo in novos_nodos:
        if nodo not in lista_abertos:
            lista_abertos.append(nodo)

    print("\nlista abertos:")
    for nodo in lista_abertos:
        print(nodo.estado)

    print("lista visitados:")
    for nodo in lista_visitados:
        print(nodo.estado)

    achou_objetivo = nodo_atual.esta_completo()

print("sucesso!")
print(lista_abertos[0].estado)
