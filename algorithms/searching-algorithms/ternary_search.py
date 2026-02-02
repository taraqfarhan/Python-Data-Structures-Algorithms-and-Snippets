"""
Ternary Search is a divide-and-conquer algorithm that works on sorted arrays. 
It divides the array into three parts and determines which part the target element belongs to, 
then continues searching in that part. 
The main idea is to divide the array into three equal parts and compare the target with the two middle elements.

Algorithm:
1. Calculate the two middle indices: mid1 and mid2.
2. Compare the target with the elements at mid1 and mid2.
3. If the target is equal to the element at mid1, return mid1.
4. If the target is equal to the element at mid2, return mid2.
5. If the target is less than the element at mid1, search in the left third.
6. If the target is greater than the element at mid2, search in the right third.
7. If the target is between the elements at mid1 and mid2, search in the middle third.
8. Repeat the process until the target is found or the search space is empty.
"""

def ternary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    # if the array is empty or the target is out of bounds, return -1 immediately
    if not arr or target < arr[left] or target > arr[right]:
        return -1
    
    # Check the first and last elements before entering the loop to handle edge cases efficiently
    if target == arr[left]:
        return left
    if target == arr[right]:
        return right

    # Use <= to ensure we check the last element when left == right
    # If we use <, we might miss checking the last element when left and right converge to the same index.
    while left <= right:
        # (right - left) // 3 calculates the size of one third of the current search space.        
        # mid1 is the index of the first middle element, and mid2 is the index of the second middle element.
        # This way, we are dividing the array into three parts: [left, mid1], [mid1 + 1, mid2 - 1], and [mid2, right].
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if target == arr[mid1]:
            return mid1
        if target == arr[mid2]:
            return mid2
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        elif arr[mid1] < target < arr[mid2]:
            left = mid1 + 1
            right = mid2 - 1

    return -1