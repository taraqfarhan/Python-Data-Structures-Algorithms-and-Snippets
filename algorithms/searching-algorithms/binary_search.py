"""
Binary Search is a searching algorithm that finds the position of a target value within a sorted array.
It works by repeatedly dividing the search interval in half. 
If the value of the search key is less than the item in the middle of the interval, 
it continues searching in the lower half, 
or if it is greater, it continues searching in the upper half. 
This process continues until the value is found or the interval is empty.

Algorithm:
1. Start with two pointers, one at the beginning of the array (left) and one at the end of the array (right).
2. Calculate the middle index (mid) of the current interval.
3. If the target value is equal to the value at the middle index, return that index.
4. If the target value is less than the value at the middle index, 
   move the right pointer to mid - 1, effectively cutting off the upper half of the array.
5. If the target value is greater than the value at the middle index, 
   move the left pointer to mid + 1, effectively cutting off the lower half of the array.
6. Repeat steps 2-5 until the target value is found or the left pointer exceeds the right pointer, 
   indicating that the target value is not present in the array.
   
Python Binary Search Template: https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8
Binary Search Implementations: https://codeforces.com/blog/entry/9901
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    # If the array is empty or the target element is outside the range of the sorted array, return -1 immediately.
    if not arr or target < arr[left] or target > arr[right]:
        return -1

    while left <= right:
        mid = left + (right - left) // 2 # mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            right = mid - 1
        else: 
            left = mid + 1
    return -1


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)
    
    
def binary_search_optimized(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1

    return left if arr[left] == target else -1


def binary_search_linea_approach(arr, target):
    current_index, step = 0, len(arr)
    while step > 0:
        while current_index + step < len(arr) and arr[current_index + step] <= target:
            current_index += step
        step //= 2
    return current_index if arr[current_index] == target else -1