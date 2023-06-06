import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Tamanho dos vetores
tamanhos = [100, 1000, 10000, 100000]

for tamanho in tamanhos:
    # Criar vetor aleatório
    vetor = random.sample(range(1, tamanho+1), tamanho)

    # Imprimir o vetor antes da ordenação (opcional)
    # print(f"Vetor antes da ordenação ({tamanho} elementos):")
    #print(vetor)

    # Medir o tempo de ordenação
    start_time = time.time()
    insertion_sort(vetor)
    end_time = time.time()

    # Imprimir o vetor após a ordenação (opcional)
    # print(f"Vetor após a ordenação ({tamanho} elementos):")
    # print(vetor)

    # Imprimir o tempo de ordenação
    elapsed_time = end_time - start_time
    print(f"Tempo de ordenação: {tamanho} {elapsed_time} segundos\n")
