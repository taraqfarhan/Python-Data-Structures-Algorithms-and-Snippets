"""
Variations of binary search include:
1. Find the first or last occurrence of a target value in a sorted array that may contain duplicate values.
2. Finding the number of occurrences of a target value in a sorted array.
3. Finding the smallest element greater than or equal to the target.
4. Finding the largest element less than or equal to the target.
5. Finding the square root of a number using binary search.
6. Finding the peak element in an array.
7. Finding the rotation point in a rotated sorted array.
8. Finding the first bad version in a series of versions.
9. Finding the minimum element in a rotated sorted array.
10. Finding the maximum element in a rotated sorted array.
11. Finding the closest element to a target value in a sorted array.

Python Binary Search Template: https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8
"""


"""
1. Find the first or last occurrence of a target value in a sorted array that may contain duplicate values.
2. Finding the number of occurrences of a target value in a sorted array.

Algorithm (fast occurrence):
1. Start with two pointers, one at the beginning of the array (left) and one at the end of the array (right).
2. Calculate the middle index (mid) of the current interval.
3. If the middle element is equal to the target value, update the result to mid and move the right pointer to mid - 1, 
   effectively cutting off the right half of the array, because we are looking for the first occurrence of the target value.
4. If the middle element is less than the target value, move the left pointer to mid + 1, 
   effectively cutting off the left half of the array, because the first occurrence must be in the right half.
5. If the middle element is greater than the target value, move the right pointer to mid - 1, 
   effectively cutting off the right half of the array, because the first occurrence must be in the left half.
6. Repeat steps 2-5 until the left pointer exceeds the right pointer, at which point the result 
   will be the index of the first occurrence of the target value, or -1 if the target value is not present in the array.
"""


def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in the right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def num_of_occurrences(arr, target):
    # using two binary searches to find the first and last occurrence of the target value, 
    # and then calculating the number of occurrences based on their indices
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    return last_occurrence(arr, target) - first + 1


def num_of_occurrences_optimized(arr, target):
    # using only one binary search to find the first occurrence and then 
    # count the occurrences by iterating through the array
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    count = 0
    for i in range(first, len(arr)):
        if arr[i] == target:
            count += 1
        else:
            break
    return count


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


"""
3. Finding the smallest element greater than or equal to the target.
4. Finding the largest element less than or equal to the target.

Algorithm (for smallest element greater than or equal to the target):
1. Start with two pointers, one at the beginning of the array (left) and one at the end of the array (right).
2. Calculate the middle index (mid) of the current interval.
3. If the middle element is greater than or equal to the target, update the result to mid 
   and move the right pointer to mid - 1, effectively cutting off the right half of the array, 
   because we are looking for the smallest element greater than or equal to the target.
4. If the middle element is less than the target, update the result to mid and move the left pointer to mid + 1, 
   effectively cutting off the left half of the array, 
   because we are looking for the largest element less than or equal to the target.
5. Repeat steps 2-4 until the left pointer exceeds the right pointer, at which point the result will be 
   the index of the smallest element greater than or equal to the target or the largest element 
   less than or equal to the target, depending on which function you are implementing.
"""

def smallest_greater_or_equal(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            result = mid
            right = mid - 1  # Continue searching in the left half
        else:
            left = mid + 1
    return result


def largest_element_smaller_or_equal(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            result = mid
            left = mid + 1  # Continue searching in the right half
        else:
            right = mid - 1
    return result



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


"""
5. Finding the square root of a number using binary search.

Algorithm:
1. Start with two pointers, one at the beginning of the range (left) and one at the end of the range (right). 
   The range can be from 0 to num, since the square root of a number cannot be greater than the number itself.
2. Calculate the middle point (mid) of the current range.
3. If mid * mid is less than or equal to num, it means that mid is a potential candidate for the square root, 
   so we update the result to mid and move the left pointer to mid + 1, 
   effectively cutting off the left half of the range, because we are looking for the largest element 
   less than or equal to the target value (the number for which we want to find the square root).
4. If mid * mid is greater than num, it means that mid is too large to be the square root, 
   so we move the right pointer to mid - 1, effectively cutting off the right half of the range.
5. Repeat steps 2-4 until the left pointer exceeds the right pointer, at which point the result 
   will be the largest integer whose square is less than or equal to num, which is the integer part of the square root of num.
"""

# same as finding the largest element smaller than or equal to the target value, 
# where the target value is the number for which we want to find the square root, 
# and the array is the range of possible square root values from 0 to num.
def sqrt(num):
    left, right = 0, num
    result = 0
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= num:
            result = mid
            left = mid + 1   # Continue searching in the right half
        else:
            right = mid - 1
    return result


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


"""
6. Finding the peak element in an array.

A peak element is an element that is greater than its neighbors.
For corner elements, we need to consider only one neighbor.
For example, in the array [1, 2, 3, 1], the peak element is 3, because it is greater than its neighbors (2 and 1).
In the array [1, 2, 1, 3, 5, 6, 4], the peak elements are 2 and 6, 
because they are greater than their neighbors (1 and 1 for 2, and 5 and 4 for 6).

Algorithm:
1. Start with two pointers, one at the beginning of the array (left) and one at the end of the array (right).
2. Calculate the middle index (mid) of the current interval.
3. If the middle element is less than its right neighbor, the peak must be in the right half. 
   Why? Because if arr[mid] < arr[mid + 1], it means that the slope is rising towards the right, 
   so there must be a peak element in the right half. If arr[mid] >= arr[mid + 1], 
   it means that the slope is falling towards the right, so there must be a peak element in the left half or at mid.
4. If the middle element is less than its right neighbor, move the left pointer to mid + 1, 
   effectively cutting off the left half of the array.
5. If the middle element is greater than or equal to its right neighbor, move the right pointer to mid, 
   effectively cutting off the right half of the array.
6. Repeat steps 2-5 until the left pointer is equal to the right pointer, which will be the index of a peak element.
"""

def find_peak_element(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        # If the middle element is less than its right neighbor, the peak must be in the right half. 
        # Why? Because if arr[mid] < arr[mid + 1], it means that the slope is rising towards the right, 
        # so there must be a peak element in the right half. If arr[mid] >= arr[mid + 1], 
        # it means that the slope is falling towards the right, so there must be a peak element in the left half or at mid.
        if arr[mid] < arr[mid + 1]: 
            left = mid + 1  # Peak is in the right half
        else:
            right = mid     # Peak is in the left half or at mid
    return left  # or right, since left == right at the end of the loop


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


"""
7. Finding the rotation point in a rotated sorted array.

Example: The array [4, 5, 6, 7, 0, 1, 2] is a rotated sorted array. 
The rotation point is the index of the smallest element, which is 4 in this case (the element 0). 

Algorithm:
1. Start with two pointers, one at the beginning of the array (left) and one at the end of the array (right).
2. Calculate the middle index (mid) of the current interval.
3. If the middle element is greater than the rightmost element, it means that the rotation point 
   is in the right half of the array, so move the left pointer to mid + 1.
4. If the middle element is less than or equal to the rightmost element, it means that the rotation point 
   is in the left half of the array, so move the right pointer to mid.
5. Repeat steps 2-4 until the left pointer is equal to the right pointer, which will be the index 
   of the rotation point (the smallest element in the rotated sorted array).
"""

def find_rotation_point(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]: 
            left = mid + 1  # Rotation point is in the right half
        else:
            right = mid     # Rotation point is in the left half or at mid
    return left  # or right, since left == right at the end of the loop


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

"""
8. Finding the first bad version in a series of versions.

Example: Suppose we have n versions [1, 2, ..., n] and we want to find out the first bad one, 
which causes all the following ones to be bad. 
We are given an API bool is_bad_version(version) which returns whether version is bad.

Algorithm:
1. Start with two pointers, one at the beginning of the versions (left) and one at the end of the versions (right).
2. Calculate the middle index (mid) of the current interval.
3. If the middle version is bad, it means that the first bad version is in the left half of the versions, 
   so move the right pointer to mid - 1, and update the result to mid, because mid could be the first bad version.
4. If the middle version is not bad, it means that the first bad version is in the right half of the versions, 
   so move the left pointer to mid + 1.
5. Repeat steps 2-4 until the left pointer exceeds the right pointer, at which point the result 
   will be the index of the first bad version, or -1 if there are no bad versions.
   
Optimized Algorithm:
1. Start with two pointers, one at the beginning of the versions (left) and one at the end of the versions (right).
2. Calculate the middle index (mid) of the current interval.
3. If the middle version is bad, it means that the first bad version is in the left half of the versions, 
   so move the right pointer to mid, because mid could be the first bad version.
4. If the middle version is not bad, it means that the first bad version is in the right half of the versions, 
   so move the left pointer to mid + 1.
5. Repeat steps 2-4 until the left pointer is equal to the right pointer, at which point the left (or right) pointer
   will be the index of the first bad version.
"""

def is_bad_version(version):
    # This is a placeholder function. In a real scenario, this function would be provided 
    # and would return True if the version is bad and False otherwise.
    # randomly simulating bad versions for demonstration purposes
    from random import choice
    return choice([True, False])

# n means there are n versions, and we want to find the first bad version among them.
def first_bad_version(n):
    left, right = 1, n
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            result = mid
            right = mid - 1  # Continue searching in the left half
        else:
            left = mid + 1   # Continue searching in the right half
    return result


def first_bad_version_optimized(n):
    left, right = 1, n

    while left < right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid     # Continue searching in the left half
        else:
            left = mid + 1 # Continue searching in the right half
    return left  # or right, since left == right at the end of the loop


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

"""
9. Finding the minimum element in a rotated sorted array.
10. Finding the maximum element in a rotated sorted array.

Algorithm (for finding the minimum element):
1. Start with two pointers, one at the beginning of the array (left) and one at the end of the array (right).
2. Calculate the middle index (mid) of the current interval.
3. If the middle element is greater than the rightmost element, it means that the minimum element 
   is in the right half of the array, so move the left pointer to mid + 1.
4. If the middle element is less than or equal to the rightmost element, it means that the minimum element 
   is in the left half of the array, so move the right pointer to mid.
5. Repeat steps 2-4 until the left pointer is equal to the right pointer, which will be the 
   index of the minimum element in the rotated sorted array.
"""

def find_minimum_in_rotated_sorted_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]: 
            left = mid + 1  # Minimum is in the right half
        else:
            right = mid     # Minimum is in the left half or at mid
    return arr[left]  # or arr[right], since left == right at the end of the loop


def find_maximum_in_rotated_sorted_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]: 
            right = mid     # Maximum is in the left half or at mid
        else:
            left = mid + 1  # Maximum is in the right half
    return arr[left]  # or arr[right], since left == right at the end of the loop


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

"""
11. Finding the closest element to a target value in a sorted array.
"""

def closest_element(arr, target):
    left, right = 0, len(arr) - 1
    closest = arr[0]  # Initialize closest to the first element

    while left <= right:
        mid = left + (right - left) // 2
        
        # Update closest if the current middle element is closer to the target
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return arr[mid]  # If the middle element is exactly the target, return it immediately

    return closest