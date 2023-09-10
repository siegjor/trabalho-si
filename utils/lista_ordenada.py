from domain.nodo import Nodo

class ListaOrdenada:
    def __init__(self):
        self.lista = []

    def inserir(self, nodo:Nodo):
        i = 0
        while i < len(self.lista) and self.lista[i].custo_total < nodo.custo_total:
            i += 1

        self.lista.insert(i, nodo)

    def remover(self, nodo: Nodo):
        if nodo in self.lista:
            self.lista.remove(nodo)

    def primeiro(self):
        return self.lista[0]

    def __str__(self):
        return str(self.lista)
