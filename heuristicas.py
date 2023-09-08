class Heuristicas:
    coords_finais_por_posicao = {
        1: {"x": 0, "y": 0},
        2: {"x": 0, "y": 1},
        3: {"x": 0, "y": 2},
        4: {"x": 1, "y": 0},
        5: {"x": 1, "y": 1},
        6: {"x": 1, "y": 2},
        7: {"x": 2, "y": 0},
        8: {"x": 2, "y": 1},
    }

    def calcular_heuristica_simples(self, nodo):
        return self.__calcular_soma_manhattan_total(nodo.estado)

    def calcular_heuristica_precisa(self, nodo):
        distancia_manhattan_total = self.__calcular_soma_manhattan_total(
            nodo.estado)
        conflitos_lineares = self.calcular_conflitos_lineares(nodo.estado)

        return distancia_manhattan_total + conflitos_lineares

    def __calcular_distancia_manhattan(self, coords_atual: dict, posicao: int):
        coords_final = self.coords_finais_por_posicao[posicao]
        return abs(coords_atual["x"] - coords_final["x"]) + abs(coords_atual["y"] - coords_final["y"])

    def __calcular_soma_manhattan_total(self, estado: list):
        total = 0
        coords_atuais = self.__calcular_coords_estado(estado)
        for posicao, coord in coords_atuais.items():
            total += self.__calcular_distancia_manhattan(coord, posicao)

        return total

    def calcular_conflitos_lineares(self, estado: list):

        # matriz = [[6, 2, 0],
        #           [4, 5, 3],
        #           [1, 8, 7]]
        conflitos_lineares = 0

        coords_atuais = self.__calcular_coords_estado(estado)
        for posicao_atual, coord_atual in coords_atuais.items():
            coord_final_atual = self.coords_finais_por_posicao[posicao_atual]
            linha_atual = coord_atual["x"]
            coluna_atual = coord_atual["y"]

            for linha_temp in range(len(estado)):
                for coluna_temp in range(len(estado[linha_temp])):
                    posicao_temp = estado[linha_temp][coluna_temp]
                    if posicao_temp == "X":
                        continue

                    coord_final_temp = self.coords_finais_por_posicao[posicao_temp]

                    if linha_atual == linha_temp and coord_final_atual["x"] == coord_final_temp["x"]:
                        if coluna_temp < coluna_atual and coord_final_atual["y"] < coord_final_temp["y"]:
                            print("conflito em linha entre " + str(posicao_atual) + " e " + str(posicao_temp))
                            conflitos_lineares += 1
                            continue

                    if coluna_atual == coluna_temp and coord_final_atual["y"] == coord_final_temp["y"] and coluna_atual == coord_final_atual["y"]:
                        if linha_temp < linha_atual and coord_final_atual["x"] < coord_final_temp["x"]:
                            print("conflito em coluna entre " +
                                  str(posicao_atual) + " e " + str(posicao_temp))
                            conflitos_lineares += 1
                            continue

        return conflitos_lineares * 2


    def __calcular_coords_estado(self, estado: list):
        coords_atuais = {}
        for i in range(len(estado)):
            for j in range(len(estado[i])):
                posicao = estado[i][j]
                if posicao != "X":
                    coords_atuais[posicao] = {"x": i, "y": j}

        return coords_atuais
