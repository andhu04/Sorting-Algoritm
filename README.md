1. Importing necessary modules:
```python
import random
import time
```
Here, the code imports the `random` module to generate random numbers and the `time` module to measure the execution time of sorting algorithms.

2. Merge Sort Algorithm:
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)
```
This is the implementation of the Merge Sort algorithm, a popular sorting algorithm based on the divide-and-conquer strategy. It sorts the input list `arr` by recursively dividing it into smaller halves, sorting each half, and then merging the sorted halves. The `merge` function (which is defined later) is used to merge the two sorted halves.

3. Merge function for Merge Sort:
```python
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
```
The `merge` function takes two sorted lists `left` and `right` and merges them into a single sorted list. It iterates through both lists and compares elements, placing them in the merged list in ascending order.

4. Quick Sort Algorithm:
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)
```
This is the implementation of the Quick Sort algorithm, another widely-used sorting algorithm based on the divide-and-conquer strategy. It selects a pivot element (usually the middle element), partitions the input list into elements smaller than the pivot, elements equal to the pivot, and elements greater than the pivot. It then recursively sorts the left and right partitions and concatenates them to form the final sorted list.

5. Heap Sort Algorithm:
```python
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
```
This is the implementation of the Heap Sort algorithm, which uses a binary heap data structure to perform the sorting. It first converts the input list into a max-heap (a binary heap where the parent nodes are greater than or equal to their children). Then, it repeatedly extracts the maximum element (the root of the heap) and rebuilds the heap until the list is sorted in ascending order.

6. Bubble Sort Algorithm:
```python
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
```
This is the implementation of the Bubble Sort algorithm, a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process continues until the list is sorted.

7. Selection Sort Algorithm:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```
This is the implementation of the Selection Sort algorithm, which repeatedly selects the minimum element from the unsorted part of the list and places it at the beginning. The sorted portion of the list grows from left to right.

8. Insertion Sort Algorithm:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```
This is the implementation of the Insertion Sort algorithm, which builds a sorted portion of the list from left to right. It takes each element and inserts it into its correct position in the already sorted part of the list.

9. Generating a random array:
```python
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]
```
This function generates a random list of integers with the given `size`, where each element is in the range of 1 to 1000.

10. Calculating the execution time of a sorting function:
```python
def calculate_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time
```
This function takes a sorting `func` and an input list `arr`. It measures the execution time of the sorting function by recording the start and end times and returns the time taken.

11. Sorting Efficiency Analysis:
```python
def sorting_efficiency():
    size = int(input("Enter the size of the array to sort: "))
    arr = generate_random_array(size)

    methods = {
        "Merge Sort": merge_sort,
        "Quick Sort": quicksort,
        "Heap Sort": heapsort,
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
    }
```
This function allows the user to analyze the efficiency of different sorting algorithms by sorting a random array of the specified `size`. It presents a menu of available sorting methods, and the user can choose one to perform the sorting and analyze its running time.

12. User input and method selection:
```python
    print("\nSelect a sorting method:")
    for i, method in enumerate(methods.keys(), 1):
        print(f"{i}. {method}")

    choice = int(input("Enter your choice (1, 2, ...): "))
    method_name = list(methods.keys())[choice - 1]
    sorting_method = methods[method_name]
```
This part of the code presents the user with a menu of available sorting methods and prompts them to choose one by entering a number. The `choice` variable stores the user's selection (1 for Merge Sort, 2 for Quick Sort, and so on). Then, the `method_name` variable is set to the name of the selected method, and the `sorting_method` variable is set to the corresponding sorting function from the `methods` dictionary.

```python
    print(f"\nUnsorted array: {arr}")

    worst_case_time = calculate_time(sorting_method, arr[::-1])
    best_case_time = calculate_time(sorting_method, sorted(arr))
    average_case_time = calculate_time(sorting_method, arr)

    print(f"\nSorted array using {method_name}: {sorting_method(arr)}")

    print("\nRunning Time Analysis:")
    print(f"Worst Case Time: {worst_case_time:.6f} seconds")
    print(f"Best Case Time: {best_case_time:.6f} seconds")
    print(f"Average Case Time: {average_case_time:.6f} seconds")
```
In this section, the program displays the unsorted array generated earlier. It then proceeds to measure the execution time of the selected sorting method for three cases: worst case (reverse sorted array), best case (already sorted array), and average case (randomly generated unsorted array). The `calculate_time` function is used to determine the execution time for each case.

After sorting the array using the chosen method, the program prints the sorted array and the running time analysis for each case.

```python
if __name__ == "__main__":
    sorting_efficiency()
```
Finally, this block of code ensures that the `sorting_efficiency` function is executed only when the script is run directly and not when it's imported as a module.

When you run this script, it will prompt you to enter the size of the array to sort and then ask you to choose a sorting method from the menu. After selecting a method, it will display the unsorted array, the sorted array using the chosen method, and the running time analysis for worst, best, and average cases. This way, you can compare the efficiency of different sorting algorithms based on the given input size and type of input data.
