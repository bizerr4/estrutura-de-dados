import sys

# só aumentando o limite de recursão pra não dar pau em labirinto grande
sys.setrecursionlimit(2000)

class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return not self.items

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("tentou desempilhar mas ta vazia")
        return self.items.pop()


def resolver_labirinto(labirinto):
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    # procurar onde ta o inicio
    inicio = None
    for i in range(linhas):
        for j in range(colunas):
            if labirinto[i][j] == 2:
                inicio = (i, j)
                break
        if inicio: break

    if not inicio:
        print("não achei o inicio...")
        return False

    pilha = Pilha()
    visitados = set()

    pilha.empilhar(inicio)
    visitados.add(inicio)

    while not pilha.esta_vazia():
        linha, coluna = pilha.desempilhar()

        if labirinto[linha][coluna] == 'T':
            print("achei o tesouro :)")
            return True

        # movimentos possíveis (cima, baixo, direita, esquerda)
        direcoes = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in direcoes:
            nx, ny = linha + dx, coluna + dy
            nova_pos = (nx, ny)

            if (0 <= nx < linhas and 
                0 <= ny < colunas and
                nova_pos not in visitados and
                labirinto[nx][ny] != 1):  # 1 = parede

                pilha.empilhar(nova_pos)
                visitados.add(nova_pos)

    print("sem caminho pro tesouro :(")
    return False