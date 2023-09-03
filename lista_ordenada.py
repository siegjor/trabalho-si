class ListaOrdenada:
    def __init__(self):
        self.lista = []

    def inserir(self, item):
        indice = 0
        while indice < len(self.lista) and self.lista[indice] < item:
            indice += 1

        self.lista.insert(indice, item)

    def remover(self, item):
        if item in self.lista:
            self.lista.remove(item)

    def __str__(self):
        return str(self.lista)
