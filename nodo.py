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
                y = linha.index("X")
                x = self.estado.index(linha)

                print("vazio X: " + str(x))
                print("vazio Y: " + str(y))

                coords = {"x": x, "y": y}
                return coords

    def gerar_filhos(self):
        vazio_coords = self.gerar_coords_vazio()

        print(">>> Nodo pai:")
        self.print_estado(self.estado)

        print("\n>>> Nodos filhos:")

        if vazio_coords["x"] - 1 > 0:
            print("> Moveu X para cima")
            self.move_vazio_cima(vazio_coords)

        if vazio_coords["x"] + 1 <= 2:
            print("> Moveu X para baixo")
            self.move_vazio_baixo(vazio_coords)

        if vazio_coords["y"] + 1 <= 2:
            print("> Moveu X para direita")
            self.move_vazio_direita(vazio_coords)

        if vazio_coords["y"] - 1 > 0:
            print("> Moveu X para esquerda")
            self.move_vazio_esquerda(vazio_coords)

        return self.filhos

    def move_vazio_cima(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["x"]][vazio_coords["y"]] = novo_estado[vazio_coords["x"] - 1][vazio_coords["y"]]
        novo_estado[vazio_coords["x"] - 1][vazio_coords["y"]] = "X"

        self.print_estado(novo_estado)
        nodo_filho = Nodo(novo_estado, self)
        self.filhos.append(nodo_filho)

    def move_vazio_baixo(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["x"]][vazio_coords["y"]] = novo_estado[vazio_coords["x"] + 1][vazio_coords["y"]]
        novo_estado[vazio_coords["x"] + 1][vazio_coords["y"]] = "X"

        self.print_estado(novo_estado)
        nodo_filho = Nodo(novo_estado, self)
        self.filhos.append(nodo_filho)

    def move_vazio_esquerda(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["x"]][vazio_coords["y"]] = novo_estado[vazio_coords["x"]][vazio_coords["y"] - 1]
        novo_estado[vazio_coords["x"]][vazio_coords["y"] - 1] = "X"

        self.print_estado(novo_estado)
        nodo_filho = Nodo(novo_estado, self)
        self.filhos.append(nodo_filho)

    def move_vazio_direita(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["x"]][vazio_coords["y"]] = novo_estado[vazio_coords["x"]][vazio_coords["y"] + 1]
        novo_estado[vazio_coords["x"]][vazio_coords["y"] + 1] = "X"

        self.print_estado(novo_estado)
        nodo_filho = Nodo(novo_estado, self)
        self.filhos.append(nodo_filho)

    def esta_completo(self):
        return self.estado == [[1, 2, 3], [4, 5, 6], [7, 8, "X"]]

    def print_estado(self, estado):
        for i in estado:
            print('\t'.join(map(str, i)))

    def __eq__(self, outro):
        return self.estado == outro.estado
