#       a b c d e f
#     a 0 1 1 0 0 0
#     b 1 0 0 1 1 0
#     c 1 0 0 0 0 1
#     d 0 1 0 0 0 0
#     e 0 1 0 0 0 1
#     f 0 0 1 0 1 0

#BUSCA EM LARGURA
#início: visita a. fila: [a]
#retira a. visita seus vizinhos b, c. fila: [b, c]
#retira b. visita seus vizinhos não visitados d, e. fila: [c, d, e]
#retira c. visita seu vizinho não visitado f. fila: [d, e, f]
#retira d. não há vizinhos novos. fila: [e, f]
#retira e. não há vizinhos novos. fila: [f]
#retira f. não há vizinhos novos. fila: []
#fila vazia, busca encerrada.
#ordem de percurso (bfs): a, b, c, d, e, f

#BUSCA EM PROFUNDIDADE
#início em a. visita a.
#de a, vai para o primeiro vizinho alfabético, b. visita b.
#de b, vai para d. visita d.
#de d, o único vizinho (b) já foi visitado. retrocede para b.
#de b, vai para o próximo vizinho, e. visita e.
#de e, vai para f. visita f.
#de f, vai para c. visita c.
#de c, todos os vizinhos (a, f) já foram visitados. retrocede para f.
#de f, todos os vizinhos foram explorados. retrocede para e.
#de e, todos os vizinhos foram explorados. retrocede para b.
#de b, todos os vizinhos foram explorados. retrocede para a.
#de a, todos os vizinhos foram explorados. busca encerrada.
#ordem de percurso (dfs): a, b, d, e, f, c