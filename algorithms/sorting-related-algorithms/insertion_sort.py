"""Insertion Sort Algorithm is a simple sorting algorithm that builds 
the final sorted array one item at a time. It is much less efficient on large lists 
than more advanced algorithms such as quicksort, heapsort, or merge sort. However, 
it has several advantages, such as being simple to implement, efficient for small data sets, 
and stable (does not change the relative order of equal elements).

Time Complexity: O(n*n) in all cases (best, average, and worst) because we need to 
                 compare each element with the sorted portion of the array.
Space Complexity: O(1) for the in-place version, O(n) for the version that creates a new sorted array."""

# FASTER
def insertion_sort(array):
    """Time Complexity O(n*n)
    Space Complexity O(1)
    Algorithm: 
    1. Start from the second element (index 1) and iterate through the array.
    2. For each element, store it as the current element.
    3. Compare the current element with the elements in the sorted portion of the array (to its left).
    4. Shift all elements that are greater than the current element to the right.
    5. Insert the current element into its correct position in the sorted portion of the array.
    """
    for i in range(1, len(array)):
        current_element = array[i]

        j = i - 1
        # compare the current element with the elements in the sorted portion of the array (to its left) 
        # and j >= 0 to avoid index out of range error
        while j >= 0 and current_element < array[j]: 
            # right shift all the elements as we need one space to put the current_element
            array[j + 1] = array[j]   # shifting the element to the right
            j -= 1

        # the value of `j` for which the while condition fails
        # is the value of the range (inclusive) where the items are already sorted, so
        # `j + 1` th index is the position that needs to be updated to
        # sort the array till the index position `i`
        array[j + 1] = current_element

    return array



# SLOWER
def insertion_sort2(array):
    """Time Complexity O(n*n)
    Space Complexity O(1)
    Algorithm:
    1. Start from the second element (index 1) and iterate through the array.
    2. For each element, store it as the current element.
    3. Compare the current element with the elements in the sorted portion of the array (to its left).
    4. If the current element is smaller than the compared element, swap them.
    5. Repeat the process until the current element is in its correct position in the sorted portion of the array.
    """
    for i in range(1, len(array)):
        current_element = array[i]

        # start from the index `i - 1` (that means the immediate left element of our current element) 
        # and compare the current element with the elements in the sorted portion of the array (to its left)
        for j in range(i - 1, -1, -1): 
            if current_element < array[j]: # if the current element is smaller than the compared element, swap them
                # swapping elements to put the current element in its correct position in the sorted portion of the array
                array[j], array[j + 1] = array[j + 1], array[j]   
                # j represents the index of the compared element in the sorted portion of the array (to its left)
                # j + 1 represents the index of the current element that we are trying to place 
                # in its correct position in the sorted portion of the array
            else: break

    return array



"""
PERFORMANCE COMPARISON
============================================================

Size       Swap (ms)       Shift (ms)      Difference
------------------------------------------------------------
10         0.0069          0.0043          +61.1%
50         0.0758          0.0613          +23.7%
100        0.2570          0.2069          +24.2%
500        6.0198          4.1769          +44.1%
1000       20.5159         13.4861         +52.1%
"""
