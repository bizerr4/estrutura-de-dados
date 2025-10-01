class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLinkada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def mostrar(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

    def remover(self, valor):
        atual = self.cabeca
        anterior = None
        while atual and atual.dado != valor:
            anterior = atual
            atual = atual.proximo
        if atual is None:
            print("valor não encontrado")
            return
        if anterior is None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo
