from nodo import Nodo

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, "X"]]

nodo = Nodo(matriz1, None)

nodo.gerar_filhos()

matriz1 = [[5, 2, 3],
           [1, 4, "X"],
           [8, 7, 6]]

nodo2 = Nodo(matriz1, nodo)


esta_completo = [[1, 2, 3], [4, 5, 6], [7, 8, "X"]] == nodo.estado
print(esta_completo)
