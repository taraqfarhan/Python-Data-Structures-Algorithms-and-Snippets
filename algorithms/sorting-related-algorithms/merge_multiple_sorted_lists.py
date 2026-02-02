import heapq

def merge_k_sorted_lists(*lists):
    """Merge k sorted lists into one sorted list using a min-heap
    Algorithm used:
    1. Initialize an empty list called merged to store the merged result and an empty min-heap (priority queue) called heap.
    2. Push the first element of each list along with its list index and element index onto the heap. 
       This allows us to keep track of which list the element came from and its position in that list.
    3. While the heap is not empty, repeat the following steps:
       a. Pop the smallest element from the heap, which gives us the value, the index of the list it came from,
          and the index of the element within that list.
       b. Append the value to the merged list.
       c. If there is a next element in the same list (i.e., if the element index + 1 is less than the length of the list), 
          push the next element onto the heap along with its list index and the new element index.
    4. Once the heap is empty, all elements from all lists have been merged into the merged list, which is then returned.
    
    Time Complexity: O(n log k), where n is the total number of elements across all lists and k is the number of lists. 
                     The log k factor comes from the heap operations.
    Space Complexity: O(n) for the merged list, and O(k) for the heap, which is O(n) in total since k is typically much smaller than n.
    
    An example of this would be if we have three lists: [1, 4, 7], [2, 5, 8], and [0, 6, 9]. 
    Initially, we push the first element of each list onto the heap: (1, 0, 0), (2, 1, 0), and (0, 2, 0). 
    The heap will pop (0, 2, 0) first since it is the smallest. 
    After appending 0 to the merged list, we check if there is a next element in the same list (list index 2). 
    Since there is a next element (6), we push (6, 2, 1) onto the heap. 
    The heap now contains (1, 0, 0), (2, 1, 0), and (6, 2, 1). The process continues until all elements are merged.
    
    merge_k_sorted_lists([1, 4, 7], [2, 5, 8], [3, 6, 9])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_k_sorted_lists(*[[1, 4], [2, 5, 15], [3, 6, 9]])  # Output: [1, 2, 3, 4, 5, 6, 9, 15]
    """
    merged = []
    heap = []

    # Push the first element of each list along with list index and element index
    for i, lst in enumerate(lists):
        # Check if the list is not empty. 
        # Because if the list is empty, there is no element to push onto the heap, 
        # and we want to avoid pushing None or causing an error.
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_index, element_index)

    while heap: # While the heap is not empty
        # Pop the smallest element from the heap
        value, list_idx, elem_idx = heapq.heappop(heap)
        merged.append(value) 

        # If there is a next element in the same list, push it onto the heap
        if elem_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, elem_idx + 1))

    return merged


# for descending order, we can use a max-heap by negating the values
def merge_k_sorted_lists_desc(*lists):
    heap, merged = [], []
    for i, l in enumerate(lists):
        if l: heapq.heappush_max(heap, (l[0], i, 0))
        
    while heap:
        value, lindex, eindex = heapq.heappop_max(heap)
        merged.append(value)
        
        if eindex + 1 < len(lists[lindex]):
            heapq.heappush_max(heap, (lists[lindex][eindex + 1], lindex, eindex + 1))
    return merged