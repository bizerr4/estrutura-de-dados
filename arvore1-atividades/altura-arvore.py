def altura(self, no):

    if no is None:
        return 0
    
    else:
        return 1 + max(self.altura(no.esquerda), self.altura(no.direita))