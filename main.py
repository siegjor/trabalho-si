from nodo import Nodo
import copy

matriz = [["X", 2, 3],
          [1, 4, 5],
          [8, 7, 6]]

# [[(0, 0), (1, 0), (2, 0)],
#  [(0, 1), (1, 1), (2, 1)],
#  [(0, 2), (1, 2), (2, 2)]]

def main(matriz):
    lista_abertos = []
    lista_visitados = []

    nodo_origem = Nodo(matriz, None)
    lista_abertos.append(nodo_origem)

    while not esta_completo(lista_abertos[0].matriz):
        vazio_y:int
        vazio_x:int

        linha:list
        temp_nodo: Nodo = lista_abertos[0]
        for linha in temp_nodo.matriz:
            if "X" in linha:
                vazio_x = linha.index("X")
                vazio_y = temp_nodo.matriz.index(linha)

        print("vazio X: " + str(vazio_x))
        print("vazio Y: " + str(vazio_y))

        if vazio_y - 1 >= 0:
            novo_nodo = move_bloco(vazio_x, vazio_y, vazio_x, vazio_y - 1, temp_nodo)

            if not nodo_esta_em_abertos(novo_nodo, lista_abertos):
                lista_abertos.append(novo_nodo)

        if vazio_x + 1 <= 2:
            novo_nodo = move_bloco(vazio_x, vazio_y, vazio_x + 1, vazio_y, temp_nodo)
            if not nodo_esta_em_abertos(novo_nodo, lista_abertos):
                lista_abertos.append(novo_nodo)

        if vazio_y + 1 <= 2:
            novo_nodo = move_bloco(vazio_x, vazio_y, vazio_x, vazio_y + 1, temp_nodo)
            if not nodo_esta_em_abertos(novo_nodo, lista_abertos):
                lista_abertos.append(novo_nodo)


        if vazio_x - 1 >= 0:
            novo_nodo = move_bloco(vazio_x, vazio_y, vazio_x - 1, vazio_y, temp_nodo)
            if not nodo_esta_em_abertos(novo_nodo, lista_abertos):
                lista_abertos.append(novo_nodo)

        lista_abertos.remove(temp_nodo)
        lista_visitados.append(temp_nodo)

        print("\nlista abertos:")
        for nodo in lista_abertos:
            print(nodo.matriz)

        print("lista visitados:")
        for nodo in lista_visitados:
            print(nodo.matriz)

    print("sucesso!")
    print(lista_abertos[0].matriz)

def move_bloco(x_original, y_original, novo_x, novo_y, temp_nodo: Nodo):
    temp_matriz = copy.deepcopy(temp_nodo.matriz)
    valor_temp = temp_matriz[novo_x][novo_y]

    temp_matriz[novo_x][novo_y] = "X"
    temp_matriz[x_original][y_original] = valor_temp

    novo_nodo = Nodo(temp_matriz, temp_nodo)

    print("\nNovo nodo:")
    print(novo_nodo.matriz)
    return novo_nodo

def esta_completo(matriz):
    return matriz[0] == [1, 2, 3] and matriz[1] == [4, 5, 6] and matriz[2] == [7, 8, "X"]

def nodo_esta_em_abertos(novo_nodo: Nodo, lista_abertos: list):
    nodo:Nodo

    for nodo in lista_abertos:
        # print("nodo da lista:")
        # print(nodo.matriz)
        # print("novo nodo:")
        # print(novo_nodo.matriz)
        if nodo.matriz == novo_nodo.matriz:
            return True

    return False


main(matriz)
