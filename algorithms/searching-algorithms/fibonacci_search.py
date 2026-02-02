"""
Conceptually, Fibonacci Search is similar to Binary Search 
but uses Fibonacci numbers to determine the next index to check.
The main idea is to divide the array into sections based on Fibonacci numbers, 
which can be more efficient in certain cases, especially when the size of the array is not a power of 2.

Algorithm:
1. Create a Fibonacci "Ruler" that grows until it covers the entire array.
2. Use the Fibonacci numbers to determine the index to check.
3. If the target is less than the value at the index, cut off the right side and shrink the ruler by 2 steps.
4. If the target is greater than the value at the index, cut off the left side and shrink the ruler by 1 step.
5. If the target is equal to the value at the index, return that index.
6. If we run out of Fibonacci numbers and haven't found the target, return -1.

Time Complexity: 
    Best Case: O(1) - If the target is found at the first index checked.
    Avg/Worst Case: O(log n) - Similar to Binary Search, but the number of comparisons can be less in some cases.
Space Complexity: O(1) - Only a few variables are used to keep track of the Fibonacci numbers and offsets.
"""

def fibonacci_search(arr, target):
    n = len(arr)
    if n == 0: return -1

    # Creating the Fibonacci "Ruler"
    # Starts with 0, 1, 1...
    fibMMinus2, fibMMinus1, fibM = 0, 1, 1

    # Keep growing the ruler until it covers the whole array
    # We want to find the smallest Fibonacci number (fibM) that is greater than or equal to n
    while fibM < n:
        fibMMinus2 = fibMMinus1
        fibMMinus1 = fibM
        fibM = fibMMinus1 + fibMMinus2

    offset = -1  # Tracks how much of the left side we eliminated
    # `offset` will track the index of the last element we eliminated from the left side.
    # If offset = 0, the math assumes index 0 is already eliminated or passed.
    # We effectively skip checking the first chunk of the array properly
    # That's why we start setting the `offset` to -1

    # While there are still elements to check.
    # Why not fibM > 0? Because we need at least 2 Fibonacci numbers to make a valid comparison.
    while fibM > 1:
        # Find the index to check using the ruler
        i = min(offset + fibMMinus2, n - 1)

        if arr[i] < target:
            # Target is in the RIGHT part
            # Cut off the left side, shrink ruler by 1 step
            fibM = fibMMinus1
            fibMMinus1 = fibMMinus2
            fibMMinus2 = fibM - fibMMinus1
            offset = i # We have eliminated all elements up to index i, so we update the offset to i

        elif arr[i] > target:
            # Target is in the LEFT part
            # Cut off the right side, shrink ruler by 2 steps
            fibM = fibMMinus2
            fibMMinus1 = fibMMinus1 - fibMMinus2
            fibMMinus2 = fibM - fibMMinus1

        else:
            return i  # Found it!

    # When the while loop finishes, there is often one single element left that hasn't been compared yet.
    # This condition checks exactly that element.
    # If fibMMinus1 is 1, it means there is one element left to check (the last one).
    # arr[offset + 1] is the index of that last element.
    if fibMMinus1 and arr[offset + 1] == target:
        return offset + 1

    return -1  # Not found