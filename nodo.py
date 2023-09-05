import copy

class Nodo:
    def __init__(self, estado: list, pai):
        self.estado = estado
        self.pai = pai
        self.filhos = []

    def gerar_coords_vazio(self):
        linha: list
        for linha in self.estado:
            if "X" in linha:
                x = linha.index("X")
                y = self.estado.index(linha)

                print("vazio X: " + str(x))
                print("vazio Y: " + str(y))

                coords = {"x": x, "y": y}
                return coords

    def gerar_filhos(self):
        vazio_coords = self.gerar_coords_vazio()

        if vazio_coords["x"] - 1 >= 0:
            print("Move esquerda")
            self.move_vazio_esquerda(vazio_coords)

        if vazio_coords["x"] + 1 <= 2:
            print("Move direita")
            self.move_vazio_direita(vazio_coords)

        if vazio_coords["y"] + 1 <= 2:
            print("Move baixo")
            self.move_vazio_baixo(vazio_coords)

        if vazio_coords["y"] - 1 >= 0:
            print("Move cima")
            self.move_vazio_cima(vazio_coords)

        return self.filhos

    def move_vazio_cima(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"] - 1][vazio_coords["x"]]
        novo_estado[vazio_coords["y"] - 1][vazio_coords["x"]] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.print_estado()
        self.filhos.append(nodo_filho)

    def move_vazio_baixo(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"] + 1][vazio_coords["x"]]
        novo_estado[vazio_coords["y"] + 1][vazio_coords["x"]] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.print_estado()
        self.filhos.append(nodo_filho)

    def move_vazio_esquerda(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"]][vazio_coords["x"] - 1]
        novo_estado[vazio_coords["y"]][vazio_coords["x"] - 1] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.print_estado()
        self.filhos.append(nodo_filho)

    def move_vazio_direita(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"]][vazio_coords["x"] + 1]
        novo_estado[vazio_coords["y"]][vazio_coords["x"] + 1] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.print_estado()
        self.filhos.append(nodo_filho)

    def esta_completo(self):
        return self.estado == [[1, 2, 3], [4, 5, 6], [7, 8, "X"]]

    def print_estado(self):
        for i in self.estado:
            print('  '.join(map(str, i)))
        print()

    def __eq__(self, outro):
        return self.estado == outro.estado
