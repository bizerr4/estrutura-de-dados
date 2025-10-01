class ListaSequencial:
    def __init__(self, tamanho_max):
        self.tamanho_max = tamanho_max
        self.tamanho = 0
        self.vetor = [None] * tamanho_max

    def inserir(self, valor):
        if self.tamanho < self.tamanho_max:
            self.vetor[self.tamanho] = valor
            self.tamanho += 1
        else:
            print("lista cheia")

    def mostrar(self):
        for i in range(self.tamanho):
            print(self.vetor[i], end=" ")
        print()

    def buscar(self, valor):
        for i in range(self.tamanho):
            if self.vetor[i] == valor:
                return i
        return -1

    def remover(self, valor):
        pos = self.buscar(valor)
        if pos == -1:
            print("alor não encontrado")
            return
        for i in range(pos, self.tamanho - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.vetor[self.tamanho - 1] = None
        self.tamanho -= 1
