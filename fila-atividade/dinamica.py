class FilaDinamica:
    def __init__(self, capacidade_inicial=4):
        self.capacidade = capacidade_inicial
        self.buffer = [None] * self.capacidade
        self.contagem = 0
        self.cabeca = 0
        self.cauda = -1

    def __len__(self):
        return self.contagem

    def __str__(self):
        if self.contagem == 0:
            return "fila: [ ]"
        
        itens = []
        for i in range(self.contagem):
            indice = (self.cabeca + i) % self.capacidade
            itens.append(str(self.buffer[indice]))
        return f"fila: [ {', '.join(itens)} ] (capacidade: {self.capacidade})"

    def esta_vazia(self):
        return self.contagem == 0

    def _redimensionar(self):
        nova_capacidade = self.capacidade * 2
        novo_buffer = [None] * nova_capacidade
        
        for i in range(self.contagem):
            indice_antigo = (self.cabeca + i) % self.capacidade
            novo_buffer[i] = self.buffer[indice_antigo]
        
        self.buffer = novo_buffer
        self.capacidade = nova_capacidade
        self.cabeca = 0
        self.cauda = self.contagem - 1
        print(f" fila redimensionada para capacidade {self.capacidade}")

    def enfileirar(self, valor):
        if self.contagem == self.capacidade:
            self._redimensionar()
        
        self.cauda = (self.cauda + 1) % self.capacidade
        self.buffer[self.cauda] = valor
        self.contagem += 1

    def espiar(self):
        if self.esta_vazia():
            raise ValueError("a fila esta vazia")
        return self.buffer[self.cabeca]

    def desenfileirar(self):
        if self.esta_vazia():
            raise ValueError("a fila esta vazia")
        
        valor = self.buffer[self.cabeca]
        self.cabeca = (self.cabeca + 1) % self.capacidade
        self.contagem -= 1
        return valor

def exibir_menu():
    print("\n--- menu da fila ---")
    print("1. adicionar)")
    print("2. remover")
    print("3. espiar")
    print("4. ver tamanho")
    print("5. mostrar fila completa")
    print("0. sair")

def main():
    fila = FilaDinamica()
    print("fila dinamica iniciada.")

    while True:
        exibir_menu()
        opcao = input("escolha uma acao: ")

        if opcao == '1':
            try:
                valor = int(input("digite o valor para adicionar: "))
                fila.enfileirar(valor)
                print(f"valor {valor} adicionado")
                print(fila)
            except ValueError:
                print("digite um numero inteiro")
        
        elif opcao == '2':
            try:
                removido = fila.desenfileirar()
                print(f"valor removido: {removido}")
                print(fila)
            except ValueError as e:
                print(f"erro: {e}")

        elif opcao == '3':
            try:
                primeiro = fila.espiar()
                print(f"o primeiro item da fila e: {primeiro}")
            except ValueError as e:
                print(f"erro: {e}")

        elif opcao == '4':
            print(f"a fila contem {len(fila)} item(ns)")

        elif opcao == '5':
            print(fila)
            
        elif opcao == '0':
            print("encerrando")
            break
        
        else:
            print("opcao invalida")

if __name__ == "__main__":
    main()