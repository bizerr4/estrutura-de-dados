def contar_nos(self, no):

    if no is None:
        return 0
    
    return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)

def contar_folhas(self, no):

    if no is None:
        return 0
    
    if no.esquerda is None and no.direita is None:
        return 1
    
    return self.contar_folhas(no.esquerda) + self.contar_folhas(no.direita)