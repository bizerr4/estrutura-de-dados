class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = [None] * capacidade  # espaço fixo
        self.tamanho = 0  # quantidade real de elementos

    def inserir(self, valor):
        if self.tamanho < self.capacidade:
            self.dados[self.tamanho] = valor
            self.tamanho += 1
        else:
            print("lista cheia")

    def inserir_posicao(self, valor, posicao):
        if self.tamanho >= self.capacidade:
            print("lista cheia")
            return
        if posicao < 0 or posicao > self.tamanho:
            print("posição inválida")
            return
   
        for i in range(self.tamanho, posicao, -1):
            self.dados[i] = self.dados[i-1]
        
        self.dados[posicao] = valor
        self.tamanho += 1

    def remover(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            print("posição inválida")
            return

        for i in range(posicao, self.tamanho - 1):
            self.dados[i] = self.dados[i+1]
        
        self.dados[self.tamanho - 1] = None
        self.tamanho -= 1

    def buscar(self, valor):
        for i in range(self.tamanho):
            if self.dados[i] == valor:
                return i
        return -1

    def mostrar(self):
        print([self.dados[i] for i in range(self.tamanho)])