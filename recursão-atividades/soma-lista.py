def soma_lista(lista):

# caso base onde a lista possui somente 1 elemento

    if len(lista) == 1:
        return lista[0]

# aqui não tem mt oq explicar, quando é chegado ao caso base o código efetua a soma de todos elementos da lista

    else:
        return lista[0] + soma_lista(lista[1:])
    
lista = [1, 2, 3, 4]
print(f"soma da lista = {soma_lista(lista)}")