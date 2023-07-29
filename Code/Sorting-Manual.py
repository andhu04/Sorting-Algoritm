# Importing necessary modules
import time


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


# Calculating the execution time of sorting function
def calculate_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time


# Sorting Efficiency Analysis
def sorting_efficiency():
    # arr = [65, 58, 1025, 2, 87, 69, 5, 75, 150]
    arr = [79, 767, 645, 956, 70, 623, 33, 410, 618, 437, 46, 932, 512, 975, 15, 326, 889, 273, 296, 167, 255, 960, 556, 782, 209, 596, 397, 204, 648, 762, 399, 998, 676, 806, 624, 534, 60, 293, 231, 805, 929, 662, 805, 490, 241, 579, 825, 632, 249, 183, 833, 528, 545, 952, 633, 295, 185, 824, 725, 824, 903, 992, 44, 722, 280, 387, 504, 273, 893, 281, 469, 278, 101, 931, 496, 811, 331, 265, 889, 110, 912, 160, 606, 624, 399, 510, 719, 673, 873, 880, 353, 830, 424, 165, 308, 438, 404, 488, 684, 341, 34, 383, 141, 728, 98, 906, 947, 996, 213, 849, 370, 405, 151, 400, 916, 512, 31, 232, 433, 422, 183, 132, 176, 38, 734, 14, 530, 116, 706, 158, 236, 360, 429, 234, 794, 843, 699, 991, 830, 381, 652, 114, 687, 411, 778, 362, 562, 476, 357, 823, 943, 202, 209, 796, 87, 556, 95, 626, 308, 588, 336, 328, 1, 672, 982, 931, 707, 972, 405, 452, 118, 758, 434, 707, 913, 949, 454, 543, 308, 533, 54, 888, 285, 906, 658, 398, 341, 735, 527, 945, 772, 430, 506, 916, 891, 65, 475, 479, 543, 692, 647, 953, 310, 384, 167, 876, 516, 649, 153, 583, 692, 46, 654, 538, 71, 501, 131, 832, 609, 515, 807, 66, 817, 864, 428, 872, 119, 898, 451, 648, 872, 232, 544, 672, 271, 599, 350, 945, 249, 458, 513, 190, 240, 707, 812, 376, 837, 355, 190, 873, 966, 181, 971, 613, 602, 117, 385, 370, 308, 689, 821, 506, 706, 671, 526, 161, 324, 299, 339, 286, 326, 834, 38, 572, 856, 116, 834, 244, 623, 48, 59, 595, 837, 547, 669, 63, 219, 644, 456, 123, 168, 229, 494, 937, 287, 349, 360, 557, 270, 566, 890, 870, 788, 919, 978, 997, 429, 85, 476, 174, 480, 906, 387, 816, 433, 805, 402, 87, 369, 329, 499, 200, 496, 380, 947, 549, 467, 691, 518, 771, 602, 245, 585, 331, 812, 444, 320, 270, 720, 57, 4, 721, 333, 337, 708, 901, 339, 648, 695, 838, 635, 72, 59, 73, 987, 494, 199, 385, 594, 564, 924, 641, 644, 732, 30, 815, 513, 103, 552, 465, 343, 389, 194, 773, 863, 526, 214, 36, 812, 380, 609, 532, 53, 36, 478, 905, 226, 236, 614, 781, 923, 682, 801, 337, 222, 206, 237, 994, 140, 360, 765, 724, 863, 534, 935, 28, 565, 599, 695, 261, 864, 396, 99, 115, 80, 171, 285, 94, 599, 284, 376, 305, 451, 935, 874, 511, 210, 174, 280, 223, 703, 433, 806, 457, 167, 233, 695, 852, 479, 554, 798, 807, 789, 537, 480, 220, 513, 615, 218, 187, 844, 967, 176, 995, 711, 352, 431, 64, 145, 656, 545, 924, 454, 325, 360, 326, 314, 906, 796, 651, 518, 338, 647, 751, 111, 813, 136, 263, 18, 653, 463, 167, 461, 776, 946, 357, 456, 797, 725, 862, 628, 851, 939, 224, 418, 993, 117, 282, 214, 403, 407, 237, 488, 745, 163, 521, 81, 253, 758, 456, 228, 819, 368, 910, 603, 164, 724, 23, 344, 964, 775, 707, 5, 732, 311, 901, 257, 317, 1000, 704, 374, 382, 53, 934, 322, 822, 868, 160, 80, 801, 307, 390, 346, 39, 913, 573, 731, 837, 711, 788, 492, 307, 681, 586, 838, 59, 355, 221, 771, 932, 357, 26, 786, 549, 148, 340, 115, 187, 496, 633, 966, 58, 777, 108, 373, 420, 110, 71, 549, 778, 531, 451, 419, 829, 877, 239, 874, 115, 37, 762, 102, 15, 4, 680, 828, 60, 67, 799, 151, 269, 91, 391, 178, 230, 523, 594, 209, 489, 642, 717, 25, 790, 760, 58, 245, 339, 807, 294, 961, 634, 900, 527, 820, 385, 225, 668, 583, 328, 992, 344, 346, 968, 796, 59, 172, 929, 511, 778, 469, 542, 223, 682, 347, 33, 39, 814, 286, 196, 440, 853, 494, 337, 794, 987, 791, 1, 34, 410, 159, 658, 600, 194, 549, 804, 8, 327, 442, 944, 42, 336, 759, 317, 226, 64, 358, 986, 313, 428, 87, 875, 452, 556, 687, 706, 17, 281, 596, 165, 343, 411, 849, 966, 752, 85, 353, 482, 936, 24, 15, 730, 880, 230, 824, 236, 375, 431, 663, 286, 383, 980, 548, 956, 219, 182, 723, 189, 946, 206, 498, 595, 777, 349, 671, 147, 749, 46, 959, 786, 153, 886, 604, 590, 612, 372, 705, 869, 847, 671, 415, 638, 920, 454, 940, 546, 953, 644, 634, 232, 823, 637, 895, 708, 998, 915, 486, 1, 501, 92, 491, 751, 169, 486, 987, 954, 759, 807, 200, 321, 152, 401, 844, 436, 987, 617, 344, 956, 31, 988, 694, 406, 6, 574, 538, 929, 69, 921, 942, 211, 423, 280, 988, 476, 366, 745, 272, 376, 955, 849, 67, 519]

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

    print(f"\nRunning Time Analysis: ({method_name}) \n")
    print(f"1. Worst Case Time: {worst_case_time:.6f} seconds\n")
    print(f"2. Best Case Time: {best_case_time:.6f} seconds\n")
    print(f"3. Average Case Time: {average_case_time:.6f} seconds\n")

if __name__ == "__main__":
    sorting_efficiency()
