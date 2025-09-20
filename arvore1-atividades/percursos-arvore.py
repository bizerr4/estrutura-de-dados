
def pre_ordem(self, no):

    if no is not None:

        print(no.valor, end=" ")
        self.pre_ordem(no.esquerda)
        self.pre_ordem(no.direita)

def in_ordem(self, no):

    if no is not None:

        self.in_ordem(no.esquerda)
        print(no.valor, end=" ")
        self.in_ordem(no.direita)

def pos_ordem(self, no):

    if no is not None:

        self.pos_ordem(no.esquerda)
        self.pos_ordem(no.direita)
        print(no.valor, end=" ")