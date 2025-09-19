def max_lista(lista):

# caso base é quando a lista possui apenas 1 item
    
    if len(lista) == 1:
        return lista[0]
    
# aqui eu utilizei a função max para diminuir o código, ao inves de criar uma condicional
# na versão com condicional, eu teria duas variaveis, uma com o primeiro item e outra com a função max_lista(lista[1:]), o resto
# caso o primeiro item fosse maior que o resto da lista, então era retornado. basicamente o que a max faz, compara duas variaveis e retorna a maior

    else:
        return max(lista[0], max_lista(lista[1:]))

lista = [123, 349, 1, 2, 1223, 1300, 10000]
print(f"maior numero da lista : {max_lista(lista)}")