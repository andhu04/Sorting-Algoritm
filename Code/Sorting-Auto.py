# Importing necessary modules
import time
import random

# Bubble Sort Algorithm 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Insertion Sort Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Merge Sort Algorithm using divide and conquer method
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half_part = merge_sort(arr[:mid])
    right_half_part = merge_sort(arr[mid:])

    return merge(left_half_part, right_half_part)

# Merge function for Merge Sort
def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


# Quick Sort Algorithm using pivoting algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Heap Sort Algorithm using binary heap data structure
def heapsort(arr):
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

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

# Generating a random array from 1 to 1000
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


# Calculating the execution time of sorting function
def calculate_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time


# Sorting Efficiency Analysis
def sorting_efficiency():
    size = int(input("Enter the size of the array to sort: "))
    arr = generate_random_array(size)

    methods = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quicksort,
        "Heap Sort": heapsort,
    }


    # User input and method selection
    print("\nSelect a sorting method:")
    for i, method in enumerate(methods.keys(), 1):
        print(f"{i}. {method}")

    choice = int(input("Enter your choice (1, 2, 3, 4, 5, 6): "))
    method_name = list(methods.keys())[choice - 1]
    sorting_method = methods[method_name]


    # measure the execution time of the selected sorting method for three cases: 
    print(f"\nUnsorted array: {arr}")
    # worst case (reverse sorted array)
    worst_case_time = calculate_time(sorting_method, arr[::-1])
    # best case (already sorted array)
    best_case_time = calculate_time(sorting_method, sorted(arr))
    # average case (randomly generated unsorted array)
    average_case_time = calculate_time(sorting_method, arr)

    print(f"\nSorted array using {method_name}: {sorting_method(arr)}")
    print(f"\nRunning Time Analysis: ({method_name})\n")
    print(f"1. Worst Case Time: {worst_case_time:.6f} seconds\n")
    print(f"2. Best Case Time: {best_case_time:.6f} seconds\n")
    print(f"3. Average Case Time: {average_case_time:.6f} seconds\n")

if __name__ == "__main__":
    sorting_efficiency()
