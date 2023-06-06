import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos já estão em suas posições corretas
        for j in range(n - i - 1):
            # Trocar se o elemento atual for maior que o próximo
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Função para criar um vetor aleatório de tamanho n
def create_random_array(n):
    return [random.randint(1, 100000) for _ in range(n)]

# Tamanhos dos vetores
sizes = [100, 1000, 10000, 100000]

# Ordenação para cada tamanho de vetor
for size in sizes:
    # Criar vetor aleatório
    array = create_random_array(size)

    # Medir o tempo de ordenação
    start_time = time.time()
    bubble_sort(array)
    end_time = time.time()

    # Calcular o tempo de execução em segundos
    execution_time = end_time - start_time

    print(f"Tamanho do vetor: {size}\nTempo de ordenação: {execution_time:.6f} segundos\n")
