def bst_verifica(self, no, min=float("-inf"), max=float("inf")):

    if no is None:
        return True
    
    if not (min < no.valor < max):
        return False
    
    return (self.bst_verifica(no.esquerda, min, no.valor) and
            self.bst_verifica(no.direita, no.valor, max))