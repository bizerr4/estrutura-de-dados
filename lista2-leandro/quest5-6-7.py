class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserir(self, valor):
        if valor < self.valor:
            if self.esquerda is None:
                self.esquerda = Node(valor)
            else:
                self.esquerda.inserir(valor)
        elif valor > self.valor:
            if self.direita is None:
                self.direita = Node(valor)
            else:
                self.direita.inserir(valor)
    def buscar(self, valor):
        if valor == self.valor:
            return True
        elif valor < self.valor:
            if self.esquerda is None:
                return False
            return self.esquerda.buscar(valor)
        else:
            if self.direita is None:
                return False
            return self.direita.buscar(valor)

    def pre_ordem(self):
        print(self.valor, end=' ')
        if self.esquerda:
            self.esquerda.pre_ordem()
        if self.direita:
            self.direita.pre_ordem()

    def em_ordem(self):
        if self.esquerda:
            self.esquerda.em_ordem()
        print(self.valor, end=' ')
        if self.direita:
            self.direita.em_ordem()

    def pos_ordem(self):
        if self.esquerda:
            self.esquerda.pos_ordem()
        if self.direita:
            self.direita.pos_ordem()
        print(self.valor, end=' ')

