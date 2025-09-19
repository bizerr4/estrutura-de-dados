def inverte_string(palavra):

# caso base, se for unico caractere encerra a run e retorna a string
   
    if len(palavra) <= 1:
        return palavra
    
# assim, para obama: bama + o -> ama + b -> ma + a -> a + m, entrando no caso base, vai ocorrer a ''volta"
# na volta, vão ser concatenados os chars que ficaram armazenados na memória.
   
    else:
        return inverte_string(palavra[1:]) + palavra[0]
    
stringOG = "barack obama"
print(f"string og = {stringOG}")
print(f"string invertida = {inverte_string(stringOG)}")