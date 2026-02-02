""" 
Linear Search is the simplest searching algorithm. 
It works by iterating through each element in the array and comparing it 
to the target value until a match is found or the end of the array is reached.

Time Complexity: O(n) - In the worst case, we have to check every element in the array.
Space Complexity: O(1) - No additional space is used
"""

def search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1 # Return -1 to indicate the target was not found in the array