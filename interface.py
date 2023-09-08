from nodo import Nodo

class Interface:
    def receber_entrada(self):
        print("Insira os números da matriz separados por espaço. Insira 'X' para representar a posição vazia.")
        string_entrada = input()
        lista_numeros = string_entrada.split()

        for i in range(len(lista_numeros)):
            if lista_numeros[i] != "X":
                lista_numeros[i] = int(lista_numeros[i])

        return lista_numeros

    def print_resultados(self, nodo: Nodo, lista_visitados: list, lista_abertos: list, tempo_inicial: int, tempo_final: int):
        print("Sucesso!")
        print(nodo.estado)

        print("Caminho (seq. de movimentos): ")
        print(nodo.get_sequencia_de_movimentos())

        print("Total de nodos visitados: " + str(len(lista_visitados)))
        print("Tempo decorrido: " + str(tempo_final - tempo_inicial) + " segundos")
        print("Tamanho do caminho (profundidade): " + str(nodo.profundidade))

        # print("\nlista abertos:")
        # lista_abertos_custos = list(
        # map(lambda x: x.custo_total, lista_abertos.lista))
        # print(lista_abertos_custos)

        # print("lista visitados:")
        # for nodo in lista_visitados:
        #     print(nodo.estado)
