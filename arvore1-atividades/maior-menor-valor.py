def maior_valor(self, no):
        
    atual = no

    while atual.direita is not None:
        atual = atual.direita

    return atual.valor

def menor_valor(self, no):

    atual = no

    while atual.esquerda is not None:
        atual = atual.esquerda
    
    return atual.valor