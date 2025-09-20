class NodeAVL:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        return y

    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        return y

    def inserir(self, raiz, valor):
        if raiz is None:
            return NodeAVL(valor)
        elif valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        else:
            raiz.direita = self.inserir(raiz.direita, valor)

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        
        balance = self.fator_balanceamento(raiz)

        if balance > 1 and valor < raiz.esquerda.valor:
            return self._rotacao_direita(raiz)

        if balance < -1 and valor > raiz.direita.valor:
            return self._rotacao_esquerda(raiz)

        if balance > 1 and valor > raiz.esquerda.valor:
            raiz.esquerda = self._rotacao_esquerda(raiz.esquerda)
            return self._rotacao_direita(raiz)

        if balance < -1 and valor < raiz.direita.valor:
            raiz.direita = self._rotacao_direita(raiz.direita)
            return self._rotacao_esquerda(raiz)

        return raiz

    def esta_balanceada(self, no):
        if no is None:
            return True
        
        balance = self.fator_balanceamento(no)

        if abs(balance) > 1:
            return False
        
        return self.esta_balanceada(no.esquerda) and self.esta_balanceada(no.direita)
    
    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(raiz.valor, end=' ')
            self.em_ordem(raiz.direita)