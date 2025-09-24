class Pilha:
    def __init__(self):
        self.itens = []  # lista interna que guarda os elementos

    def push(self, item):
        self.itens.append(item)  # adiciona no final da lista (peek da pilha)

    def pop(self):
        if not self.vazia():
            return self.itens.pop()  # remove e retorna o último elemento
        return None  # se estiver vazia

    def vazia(self):
        return len(self.itens) == 0  # retorna True se a pilha não tiver elementos

    def peek(self):
        if not self.vazia():
            return self.itens[-1]  # olha o elemento  do topo sem remover
        return None

# função para carregar o labirinto do arquivo
def carregar_labirinto(labirinto1):
    labirinto = []
    with open(labirinto1, "r") as f:
        for linha in f:
            labirinto.append(list(map(int, linha.strip().split(",")))) #converte os 0,1 em [0,1] e o strip
    return labirinto


# o tal do backtracking
def resolver_labirinto(labirinto, inicio, objetivo):
    pilha = Pilha()          # cria a pilha
    visitados = set()        # guarda posições já visitadas
    pilha.push(inicio)       # insere posição inicial

    while not pilha.vazia(): #enquanto a pilha não estiver vazia
        pos = pilha.pop()    # retira posição do topo atual
        x, y = pos

        # verifica se achou o objetivo
        if pos == objetivo:
            print("Tesouro encontrado em:", pos)
            return True

        # marca posição como visitada
        if pos not in visitados:
            visitados.add(pos)

            # movimentos possíveis: cima, baixo, esquerda, direita
            movimentos = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for nx, ny in movimentos:       
                if 0 <= nx < len(labirinto) and 0 <= ny < len(labirinto[0]):    #garante que não saia do mapa
                    if labirinto[nx][ny] == 1 and (nx, ny) not in visitados:    # só anda em caminhos livres (1)
                        pilha.push((nx, ny))

    print("Não existe caminho até o tesouro.")
    return False

#exec
labirinto = carregar_labirinto("C:\\Users\\Desktop\\Documents\\GitHub\\estrutura-de-dados\\labirinto-atividade\\labirinto1.txt")

inicio = (1, 2)      # posição inicial
objetivo = (1, 3)  # posição do tesouro #exemplo

resolver_labirinto(labirinto, inicio, objetivo)
