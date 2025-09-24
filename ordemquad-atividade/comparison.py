import random #optei por pegar um numero aleatório dentre 0 e 10000 já q eu nn tinha o arquivo .in 
import time

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
    return vetor

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        valor = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > valor:
            vetor[j+1] = vetor[j]
            j -= 1
        vetor[j+1] = valor
    return vetor

#compara tempo
def comparar(n):

    lista = [random.randint(0, 10000) for _ in range(n)]
    
    # select sort
    lista_sel = lista.copy()
    inicio = time.time()
    selection_sort(lista_sel)
    tempo_selection = time.time() - inicio
    
    # insert sorte
    lista_ins = lista.copy()
    inicio = time.time()
    insertion_sort(lista_ins)
    tempo_insertion = time.time() - inicio
    
    print(f"tamanho da lista: {n}")
    print(f"selection sort: {tempo_selection:.6f} segundos")
    print(f"insertion sort: {tempo_insertion:.6f} segundos")
    print("-"*40)

for tamanho in [100, 1000, 5000]:
    comparar(tamanho)
