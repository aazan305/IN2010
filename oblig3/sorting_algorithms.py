def insertion_sort(arr):
    comparisons = swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
    return comparisons, swaps

def merge_sort(arr):
    comparisons = swaps = 0

    def merge(left, right):
        nonlocal comparisons, swaps
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:  
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                swaps += len(left) - i  
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr, comparisons, swaps

    mid = len(arr) // 2
    left, cmp_l, swp_l = merge_sort(arr[:mid])
    right, cmp_r, swp_r = merge_sort(arr[mid:])
    merged = merge(left, right)
    return merged, comparisons + cmp_l + cmp_r, swaps + swp_l + swp_r

def quick_sort(arr):
    comparisons = swaps = 0
    
    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        swaps += 1
        return i

    def quick_sort_recursive(low, high):
        nonlocal comparisons, swaps
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return comparisons, swaps

def bubble_sort(arr):
    comparisons = swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comparisons, swaps
