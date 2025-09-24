class FilaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade  # vetor fixo
        self.inicio = 0  # índice do primeiro elemento
        self.fim = -1    # índice do último elemento
        self.tamanho = 0 # quantidade de elementos na fila

    def esta_vazia(self):
        return self.tamanho == 0

    def esta_cheia(self):
        return self.tamanho == self.capacidade

    def enfileirar(self, valor):
        if self.esta_cheia():
            print("Fila cheia! Não é possível adicionar:", valor)
            return
        self.fim = (self.fim + 1) % self.capacidade
        self.fila[self.fim] = valor
        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            print("Fila vazia! Nada a remover.")
            return None
        valor = self.fila[self.inicio]
        self.fila[self.inicio] = None  # opcional, só para visualização
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor

    def frente(self):
        if self.esta_vazia():
            return None
        return self.fila[self.inicio]

    def mostrar(self):
        return self.fila
