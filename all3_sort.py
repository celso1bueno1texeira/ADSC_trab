import random
import time

def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Vetor de 100 elementos
# arr_100 = generate_random_array(100)
# print("\nBubble Sort (100):")
# for _ in range(10):
#     print(f"Tempo: {measure_time(bubblesort, arr_100)} segundos")

# print("\nInsertion Sort (100):")
# for _ in range(10):
#     print(f"Tempo: {measure_time(insertionsort, arr_100)} segundos")

# print("\nMerge Sort (100):")
# for _ in range(10):
#     print(f"Tempo: {measure_time(mergesort, arr_100)} segundos")

# print("\nheapsort (100):")
# for _ in range(10):
#     print(f"Tempo: {measure_time(heapsort, arr_100)} segundos")     

# Vetor de 10000 elementos
arr_1000 = generate_random_array(10000) 
print("\nBubble Sort (10000):")
for i in range(10): 
    counter = i + 1  
    print(f"{counter}° Tempo: {measure_time(bubblesort, arr_1000)} segundos")


# print("\nBubble Sort (10000):")
# count_bubble = 0
# for _ in range(10): 
#     count_bubble += 1   
#     print(f"Tempo: count_bubble {measure_time(bubblesort, arr_1000)} segundos")

print("\nInsertion Sort (1000):")
for i in range(10):
    counter = i + 1
    print(f"{counter}° Tempo: {measure_time(insertionsort, arr_1000)} segundos")

print("\nMerge Sort (1000):")
for i in range(10):
    counter = i + 1
    print(f"{counter}° Tempo: {measure_time(mergesort, arr_1000)} segundos")

print("\nheapsort (1000):")
for i in range(10):
    counter = i + 1
    print(f"{counter}° Tempo: {measure_time(heapsort, arr_1000)} segundos")       