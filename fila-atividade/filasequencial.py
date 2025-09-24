class FilaSequencial:
    def __init__(self):
        self._dados = []

    def enfileirar(self, item):
        self._dados.append(item)
        print(f"enfileirado: {item}")

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("fila vazia, não tem como desenfileirar")
        item_removido = self._dados.pop(0)
        print(f" desenfileirado: {item_removido}")
        return item_removido

    def primeiro(self):
        if self.esta_vazia():
            raise IndexError("fila tá vazia")
        return self._dados[0]

    def esta_vazia(self):
        return len(self._dados) == 0

    def tamanho(self):
        return len(self._dados)

    def __str__(self):
        if self.esta_vazia():
            return "fila vazia"
        return f"fila: {self._dados}"
