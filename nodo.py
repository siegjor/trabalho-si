import copy
from algoritmos_enum import AlgoritmosEnum
from heuristicas import Heuristicas

class Nodo:
    __algoritmo = AlgoritmosEnum.HEURISTICA_PRECISA
    # __algoritmo = AlgoritmosEnum.HEURISTICA_SIMPLES
    # __algoritmo = AlgoritmosEnum.CUSTO_UNIFORME

    def __init__(self, estado: list, pai):
        self.estado = estado
        self.pai = pai
        self.filhos = []
        self.profundidade = 0
        self.heuristica = 0
        self.custo_total = 0
        self.ultimo_movimento = ""

    def __gerar_coords_vazio(self):
        linha: list
        for linha in self.estado:
            if "X" in linha:
                x = linha.index("X")
                y = self.estado.index(linha)

                coords = {"x": x, "y": y}
                return coords

    def gerar_filhos(self):
        vazio_coords = self.__gerar_coords_vazio()

        if vazio_coords["x"] - 1 >= 0:
            self.__move_vazio_esquerda(vazio_coords)

        if vazio_coords["x"] + 1 <= 2:
            self.__move_vazio_direita(vazio_coords)

        if vazio_coords["y"] + 1 <= 2:
            self.__move_vazio_baixo(vazio_coords)

        if vazio_coords["y"] - 1 >= 0:
            self.__move_vazio_cima(vazio_coords)

        filho: Nodo
        for filho in self.filhos:
            filho.profundidade = self.profundidade + 1
            self.__calcular_custo_total(filho)

        return self.filhos

    def __calcular_custo_total(self, nodo):
        heuristicas = Heuristicas()
        match self.__algoritmo:
            case AlgoritmosEnum.CUSTO_UNIFORME:
                nodo.custo_total = nodo.profundidade
            case AlgoritmosEnum.HEURISTICA_SIMPLES:
                nodo.heuristica = heuristicas.calcular_heuristica_simples(nodo)
                nodo.custo_total = nodo.heuristica + nodo.profundidade
            case AlgoritmosEnum.HEURISTICA_PRECISA:
                nodo.heuristica = heuristicas.calcular_heuristica_precisa(nodo)
                nodo.custo_total = nodo.heuristica + nodo.profundidade

    def __move_vazio_cima(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"] - 1][vazio_coords["x"]]
        novo_estado[vazio_coords["y"] - 1][vazio_coords["x"]] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.ultimo_movimento = "cima"

        self.filhos.append(nodo_filho)

    def __move_vazio_baixo(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"] + 1][vazio_coords["x"]]
        novo_estado[vazio_coords["y"] + 1][vazio_coords["x"]] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.ultimo_movimento = "baixo"

        self.filhos.append(nodo_filho)

    def __move_vazio_esquerda(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"]][vazio_coords["x"] - 1]
        novo_estado[vazio_coords["y"]][vazio_coords["x"] - 1] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.ultimo_movimento = "esquerda"

        self.filhos.append(nodo_filho)

    def __move_vazio_direita(self, vazio_coords):
        novo_estado = copy.deepcopy(self.estado)
        novo_estado[vazio_coords["y"]][vazio_coords["x"]] = novo_estado[vazio_coords["y"]][vazio_coords["x"] + 1]
        novo_estado[vazio_coords["y"]][vazio_coords["x"] + 1] = "X"

        nodo_filho = Nodo(novo_estado, self)
        nodo_filho.ultimo_movimento = "direita"

        self.filhos.append(nodo_filho)

    def esta_completo(self):
        return self.estado == [[1, 2, 3], [4, 5, 6], [7, 8, "X"]]

    def print_estado(self):
        print("Profundidade: " + str(self.profundidade))
        if (self.__algoritmo != AlgoritmosEnum.CUSTO_UNIFORME):
            print("Heuristica: " + str(self.heuristica))
        print("Custo total: " + str(self.custo_total))

        for i in self.estado:
            print('  '.join(map(str, i)))
        print()

    def get_sequencia_de_movimentos(self):
        nodo_temp: Nodo = self
        lista_movimentos = []
        while nodo_temp.pai != None:
            lista_movimentos.append(nodo_temp.ultimo_movimento)
            nodo_temp = nodo_temp.pai
        lista_movimentos.reverse()

        return lista_movimentos

    def __eq__(self, outro):
        if (outro == None):
            return False
        return self.estado == outro.estado
