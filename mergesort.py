import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Função para criar um vetor aleatório de tamanho 'size'
def create_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Tamanhos dos vetores
sizes = [100, 1000, 10000, 100000]

for size in sizes:
    arr = create_random_array(size)
    start_time = time.time()
    
    sorted_arr = merge_sort(arr)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Tempo de ordenação para{size} elementos: {execution_time} segundos\n")
