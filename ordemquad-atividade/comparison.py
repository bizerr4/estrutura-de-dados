import time

def select_sort(vector):
    tamanho = len(vector)
    for i in range(tamanho):
        indice_minimo = i
        for j in range(i + 1, tamanho):
            if vector[j] < vector[indice_minimo]:
                indice_minimo = j
        
        if indice_minimo != i:
            vector[i], vector[indice_minimo] = vector[indice_minimo], vector[i]

def insert_sort(vector):
    for i in range(1, len(vector)):
        chave = vector[i]
        j = i - 1
        while j >= 0 and vector[j] > chave:
            vector[j + 1] = vector[j]
            j -= 1
        vector[j + 1] = chave

def cvectoregar_numeros_do_arquivo(path):
    with open(path, 'r') as f:
        return [int(linha.strip()) for linha in f]

def executar_e_medir(nome_algoritmo, funcao_ordenacao, dados_originais):
    dados_para_ordenar = dados_originais.copy()
    
    inicio = time.perf_counter()
    funcao_ordenacao(dados_para_ordenar)
    fim = time.perf_counter()
    
    duracao_ms = (fim - inicio) * 1000
    print(f"{nome_algoritmo} levou {duracao_ms:.2f} ms para ordenar")

def principal():
    try:
        path_arquivo = input("digite o caminho do arquivo de entrada: ")
        numeros = cvectoregar_numeros_do_arquivo(path_arquivo)
        
        print(f"\nanalisando arquivo com {len(numeros)} numeros...")
        
        executar_e_medir("selection sort", select_sort, numeros)
        executar_e_medir("insertion sort", insert_sort, numeros)

    except FileNotFoundError:
        print("arquivo nao encontrado.")
    except ValueError:
        print("o arquivo contem linhas que nao sao numeros inteiros validos")
    except Exception as e:
        print(f"ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    principal()