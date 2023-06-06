import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

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

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def create_random_array(size):
    arr = [random.randint(0, 100) for _ in range(size)]
    return arr

def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

sizes = [100, 1000, 10000]
sorting_algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Heap Sort", heap_sort)
]

for size in sizes:
    arr = create_random_array(size)
    print(f"Array size: {size}")
    print("{sorting_algorithms}\n")
    for algorithm_name, algorithm in sorting_algorithms:
        total_execution_time = 0        
        for _ in range(10):
            arr_copy = arr.copy()
            execution_time = time_sorting_algorithm(algorithm, arr_copy)
            total_execution_time += execution_time
            print(f"Tempo de ordenação para {size} elementos: {execution_time} segundos\n")
            #average_execution
