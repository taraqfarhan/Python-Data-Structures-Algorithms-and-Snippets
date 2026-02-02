def bubble_sort(arr):
    """
    Idea: Repeatedly step through the list, compare adjacent elements and swap them if they are in the wrong order. 
    The process is repeated until the list is sorted.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubble_sort_optimized(arr):
    """
    Optimized Bubble Sort: If no swaps occur in a pass, the array is already sorted.
    """
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


def bubble_sort_recursive(arr, n=None):
    """
    Idea: Recursively call the function to sort the first n-1 elements, then compare the last two elements and swap if necessary.
    """
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return bubble_sort_recursive(arr, n-1)


def bubble_sort_optimized_recursive(arr, n=None):
    """
    Optimized Recursive Bubble Sort: If no swaps occur in a pass, the array is already sorted.
    """
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    swapped = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True
    if not swapped:
        return arr
    return bubble_sort_optimized_recursive(arr, n-1)


def bubble_sort_bidirectional(arr):
    """
    Idea: Bubble Sort in both directions. In the first pass, the largest element is moved to the end of the list. 
    In the second pass, the smallest element is moved to the beginning of the list. 
    This process is repeated until the list is sorted.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
        swapped = False
        for j in range(n-i-2, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def bubble_sort_bidirectional_optimized(arr):
    """
    Idea: Optimized Bubble Sort in both directions. If no swaps occur in a pass, the array is already sorted.
    """
    n = len(arr)
    start = 0
    end = n - 1
    while start < end:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        start += 1
    return arr