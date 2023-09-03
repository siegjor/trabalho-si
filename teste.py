from nodo import Nodo

matriz1 = [["X", 2, 3],
          [1, 4, 5],
          [8, 7, 6]]

nodo = Nodo(matriz1, None)

nodo.gerar_filhos()

matriz1 = [[5, 2, 3],
           [1, 4, "X"],
           [8, 7, 6]]

nodo2 = Nodo(matriz1, nodo)

nodo2.gerar_filhos()
