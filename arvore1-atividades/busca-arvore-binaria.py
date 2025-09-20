def buscar(self, valor, no):
    
    if no is None:
        return False
    
    if valor == no.valor:
        return True
    
    elif valor < no.valor:
        return self.buscar(valor, no.esquerda)
    
    else:
        return self.buscar(valor, no.direita)