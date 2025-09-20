class Node:

    def __init__ (self, valor):

        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:

    def __init__ (self):

        self.raiz = None

    def inserir (self, valor):

        if self.raiz is None:
            self.raiz = Node(valor)

        else:
            self.aux_inserir

    def aux_inserir (self, valor, no_atual):
        
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Node(valor)
        else:
            self.aux_inserir(valor, no_atual.esquerda)
        
        if valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = Node(valor)
            else:
                self.aux_inserir(valor, no_atual.direita)