import heapq

"""In a binary heap, for a min-heap, each parent node is less than or equal to its children, 
and for a max-heap, each parent node is greater than or equal to its children. 
This property ensures that the minimum (or maximum) element is always at the root of the heap.

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements. 
The algorithm works by first building a heap from the input data, and then repeatedly extracting 
the maximum (or minimum) element from the heap and rebuilding the heap until it is empty. The result is a sorted array.

Algorithm (ascending order):
1. Build a min-heap from the input data. [O(n) time complexity.]
2. Pop the smallest element from the heap and append it to the sorted list. [O(log n) time complexity.]
3. Repeat step 2 while the size of the heap is greater than 1.

Time Complexity: O(n log n) in all cases (best, average, and worst) because we need to build the heap and then extract elements.
Space Complexity: O(1) for the in-place version, O(n) for the version that creates a new sorted array.
"""

def heapsort(arr):
    """Sort an array in ascending order using the heapsort algorithm.
    Time Complexity: O(n log n) in all cases (best, average, and worst)
                     because we need to build the heap and then extract elements.
    Space Complexity: O(n) for the version that creates a new sorted array.
    """
    heapq.heapify(arr) # Create a min-heap from the input array
    
    # Pop elements from the heap and append to the sorted list
    sorted_arr = []
    while arr:
        smallest = heapq.heappop(arr)
        sorted_arr.append(smallest)
    
    return sorted_arr



# For descending order, we can use a max-heap by negating the values
def heapsort_desc(arr):
    """Sort an array in descending order using the heapsort algorithm.
    Time Complexity: O(n log n) in all cases (best, average, and worst)
                     because we need to build the heap and then extract elements.
    Space Complexity: O(n) for the version that creates a new sorted array."""
    heapq.heapify_max(arr) # Create a max-heap
    
    # Pop elements from the max-heap and append to the sorted list
    sorted_arr = []
    while arr:
        largest = heapq.heappop_max(arr)
        sorted_arr.append(largest)
    
    return sorted_arr



def heapsort_desc2(arr):
    """Sort an array in descending order using the heapsort algorithm by negating values to create a max-heap.
    Time Complexity: O(n log n) in all cases (best, average, and worst) 
                     because we need to build the heap and then extract elements.
    Space Complexity: O(n) for the version that creates a new sorted array."""
    # Negate the values to create a max-heap using the min-heap implementation
    negated_arr = [-x for x in arr]
    heapq.heapify(negated_arr) # Create a min-heap from the negated values
    
    # Pop elements from the heap and append the negated values back to the sorted list
    sorted_arr = []
    while negated_arr:
        largest = -heapq.heappop(negated_arr) # Negate again to get the original value
        sorted_arr.append(largest)
    
    return sorted_arr


# - -- - - - - - - - - -- - - - - - - - - -- - - - - - - - - -- - - - - - - - - -      
# - -- - - - - - - - - - - - - - - IN PLACE-- - - - - - - - - - - - - - - - - - - 
# - -- - - - - - - - - -- - - - - - - - - -- - - - - - - - - -- - - - - - - - - -

"""Algorithm (in-place, ascending order):
1. Build a max-heap from the input data. [O(logn) time complexity.]
2. Swap the root (maximum element) with the last element of the heap and reduce the heap size by one. [O(1) time complexity.]
3. Heapify the root of the reduced heap to maintain the max-heap property. [O(log n) time complexity.]
4. Repeat steps 2 and 3 until the heap size is greater than 1."""

def heapify_max(arr, n, i):
    """
    Ensure the subtree rooted at index i is a max heap.
    
    Parameters:
        arr (list): The array representing the heap
        n (int): Size of the heap
        i (int): Index of the root of the subtree
    
    Time Complexity: O(log n) for each call to heapify, where n is the size of the heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_max(arr, n, largest)


def heapsort_inplace(arr):
    """Sort (ascending) an array in-place using the heapsort algorithm.
    Time Complexity: O(n log n) in all cases (best, average, and worst)
                     because we need to build the heap and then extract elements.
    Space Complexity: O(1) for the in-place version."""
    heapq.heapify_max(arr) # Build max heap (O(log n) time complexity)
    
    n = len(arr)
    # Extract elements one by one
    for i in range(n - 1, 0, -1): # O(n logn) time complexity
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify_max(arr, i, 0)               # Heapify reduced heap

    return arr



def heapify_min(arr, n, i):
    """
    Ensure the subtree rooted at index i is a min heap.
    
    Parameters:
        arr (list): The array representing the heap
        n (int): Size of the heap
        i (int): Index of the root of the subtree
    
    Time Complexity: O(log n) for each call to heapify, where n is the size of the heap.
    Space Complexity: O(1) for the in-place version.
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right< n and arr[right] < arr[smallest]:
        smallest = right
    
    if i != smallest:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)


def heapsort_desc_inplace(arr):
    """Sort (descending) an array in-place using the heapsort algorithm.
    Time Complexity: O(n log n) in all cases (best, average, and worst)
                     because we need to build the heap and then extract elements.
    Space Complexity: O(1) for the in-place version."""
    heapq.heapify(arr) # Build min heap O(log n) time complexity
    
    n = len(arr)
    # Extract elements one by one
    for i in range(n - 1, 0, -1): # O(n logn) time complexity
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify_min(arr, i, 0)   # Heapify reduced heap

    return arr