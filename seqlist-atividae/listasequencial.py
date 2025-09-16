class ListaCustom:
    def __init__(self, max_tamanho):
        self.max_tamanho = max_tamanho
        self.tamanho_atual = 0
        self.dados = [None] * max_tamanho

    def ta_vazia(self):
        return self.tamanho_atual == 0

    def ta_cheia(self):
        return self.tamanho_atual == self.max_tamanho

    def ver_tamanho(self):
        return self.tamanho_atual

    def pegar_elemento(self, posicao: int):
        if not (1 <= posicao <= self.tamanho_atual):
            return None
        return self.dados[posicao - 1]

    def trocar_valor(self, posicao: int, novo_dado: int):
        if 1 <= posicao <= self.tamanho_atual:
            self.dados[posicao - 1] = novo_dado
            return True
        return False

    def achar_posicao(self, dado: int):
        for i in range(self.tamanho_atual):
            if self.dados[i] == dado:
                return i + 1
        return -1

    def inserir(self, posicao: int, dado: int):
        if self.ta_cheia():
            return "lista cheia"

        if self.ta_vazia():
            if posicao != 1:
                return "lista vazia, voce so pode inserir na posicao 1"
        elif not (1 <= posicao <= self.tamanho_atual + 1):
             return f"posicao invalida. com {self.tamanho_atual} itens, voce pode inserir entre as posicoes 1 e {self.tamanho_atual + 1}"

        indice = posicao - 1
        for i in range(self.tamanho_atual, indice, -1):
            self.dados[i] = self.dados[i - 1]

        self.dados[indice] = dado
        self.tamanho_atual += 1
        return True

    def remover(self, posicao: int):
        if self.ta_vazia() or not (1 <= posicao <= self.tamanho_atual):
            return False

        indice = posicao - 1
        for i in range(indice, self.tamanho_atual - 1):
            self.dados[i] = self.dados[i + 1]

        self.tamanho_atual -= 1
        return True

def mostrar_menu():
    print("\n--------- menu ---------")
    print("1. colocar um numero")
    print("2. tirar um numero")
    print("3. trocar um valor")
    print("4. espiar um numero em uma posicao")
    print("5. achar em que posicao ta um numero")
    print("6. ver a lista toda")
    print("7. ver o tamanho atual")
    print("8. ta vazia?")
    print("9. ta cheia?")
    print("0. sair")
    print("------------------------")

def main():
    try:
        tamanho = int(input("qual vai ser o tamanho maximo da sua lista? "))
        if tamanho <= 0:
            print("tem que ser maior que zero")
            return
        lista = ListaCustom(tamanho)
    except ValueError:
        print("isso nao e um numero valido.")
        return

    while True:
        ver_menu = input("\nver as opcoes do menu? (s/n): ").strip().lower()
        if ver_menu == 's':
            mostrar_menu()

        opcao = input("escolha uma opcao: ")

        if opcao == '1':
            try:
                pos = int(input("em que posicao (a partir de 1)? "))
                valor = int(input("qual o valor? "))
                resultado = lista.inserir(pos, valor)
                if resultado is True:
                    print("inserido")
                else:
                    print(f"erro: {resultado}")
            except ValueError:
                print("digit um numero para a posicao e para o valor")

        elif opcao == '2':
            try:
                pos = int(input("tirar de qual posicao (a partir de 1)? "))
                if lista.remover(pos):
                    print("removido")
                else:
                    print(">> erro: posicao invalida ou lista vazia")
            except ValueError:
                print(">> ops, voce precisa digitar um numero para a posicao")

        elif opcao == '3':
            try:
                pos = int(input("qual posicao quer modificar (a partir de 1)? "))
                novo = int(input("qual o novo valor? "))
                if lista.trocar_valor(pos, novo):
                    print("modificado")
                else:
                    print("posicao invalida")
            except ValueError:
                print("voce precisa digitar numeros")

        elif opcao == '4':
            try:
                pos = int(input("ver qual posicao (a partir de 1)? "))
                valor = lista.pegar_elemento(pos)
                if valor is None:
                    print("posicao invalida.")
                else:
                    print(f"na posicao {pos} tem o valor: {valor}")
            except ValueError:
                print("ops, voce precisa digitar um numero para a posicao.")

        elif opcao == '5':
            try:
                valor = int(input("qual valor voce quer achar? "))
                pos = lista.achar_posicao(valor)
                if pos == -1:
                    print("esse valor nao foi encontrado")
                else:
                    print(f"o valor {valor} ta na posicao {pos}")
            except ValueError:
                print(">> ops, voce precisa digitar um numero para o valor")

        elif opcao == '6':
            print("lista atual:", lista.dados[:lista.ver_tamanho()])

        elif opcao == '7':
            print("tamanho atual da lista:", lista.ver_tamanho())

        elif opcao == '8':
            print("a lista esta vazia?", lista.ta_vazia())

        elif opcao == '9':
            print("a lista esta cheia?", lista.ta_cheia())

        elif opcao == '0':
            print("kitando")
            break
        
        else:
            print("\nopcao invalida, meu chapa")

if __name__ == "__main__":
    main()