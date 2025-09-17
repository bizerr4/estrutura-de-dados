class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLinkada:
    def __init__(self):
        self.inicio = None
        self.quantidade = 0

    def __str__(self):
        if self.quantidade == 0:
            return "[ lista vazia ]"
        
        elementos = []
        ponteiro = self.inicio
        while ponteiro:
            elementos.append(str(ponteiro.valor))
            ponteiro = ponteiro.proximo
        return "[ " + " -> ".join(elementos) + " ]"

    def __len__(self):
        return self.quantidade
    
    def __iter__(self):
        ponteiro = self.inicio
        while ponteiro:
            yield ponteiro.valor
            ponteiro = ponteiro.proximo

    def _pegar_no(self, posicao):
        if not (0 <= posicao < self.quantidade):
            raise IndexError("posicao invalida")
        
        ponteiro = self.inicio
        for _ in range(posicao):
            ponteiro = ponteiro.proximo
        return ponteiro

    def vazia(self):
        return self.quantidade == 0

    def adicionar(self, valor, posicao):
        if not (0 <= posicao <= self.quantidade):
            raise IndexError("posicao invalida para adicao")

        novo_no = No(valor)
        if posicao == 0:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            no_anterior = self._pegar_no(posicao - 1)
            novo_no.proximo = no_anterior.proximo
            no_anterior.proximo = novo_no
        
        self.quantidade += 1

    def remover(self, posicao):
        if self.vazia():
            raise IndexError("nao e possivel remover de uma lista vazia")
        
        if not (0 <= posicao < self.quantidade):
            raise IndexError("posicao invalida para remocao")

        if posicao == 0:
            valor_removido = self.inicio.valor
            self.inicio = self.inicio.proximo
        else:
            no_anterior = self._pegar_no(posicao - 1)
            valor_removido = no_anterior.proximo.valor
            no_anterior.proximo = no_anterior.proximo.proximo
        
        self.quantidade -= 1
        return valor_removido

    def valor_em(self, posicao):
        no = self._pegar_no(posicao)
        return no.valor

    def alterar_em(self, posicao, novo_valor):
        no = self._pegar_no(posicao)
        no.valor = novo_valor
        
    def posicao_de(self, valor_procurado):
        ponteiro = self.inicio
        posicao_atual = 0
        while ponteiro:
            if ponteiro.valor == valor_procurado:
                return posicao_atual
            ponteiro = ponteiro.proximo
            posicao_atual += 1
        return -1
# ex: aqui o vinte empurra o 30 p direita
if __name__ == '__main__':
    lista = ListaLinkada()
    print("estado inicial:", lista)
    print("tamanho:", len(lista))
    
    print("\nadicionando 10 na posicao 0")
    lista.adicionar(10, 0)
    print("adicionando 30 na posicao 1")
    lista.adicionar(30, 1)
    print("adicionando 20 na posicao 1")
    lista.adicionar(20, 1)
    print("lista atual:", lista)
    print("tamanho:", len(lista))

    print("\nvalor na posicao 2:", lista.valor_em(2))
    
    print("alterando valor na posicao 2 para 99")
    lista.alterar_em(2, 99)
    print("lista atual:", lista)

    print("\nremovendo da posicao 0...")
    removido = lista.remover(0)
    print("valor removido:", removido)
    print("lista atual:", lista)
    print("tamanho:", len(lista))

    print("\nprocurando pela posicao do valor 20:", lista.posicao_de(20))
    print("procurando pela posicao do valor 55:", lista.posicao_de(55))
    
    print("\npercorrendo a lista com um for:")
    for item in lista:
        print("item:", item)