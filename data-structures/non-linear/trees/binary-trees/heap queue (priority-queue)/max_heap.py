class MaxHeap:
    """
    Max Heap implementation using a list-based representation.
    Properties:
    - Parent of node at index i is at (i-1) // 2
    - Left child of node at index i is at 2*i + 1
    - Right child of node at index i is at 2*i + 2
    - Root (maximum element) is always at index 0
    """

    def __init__(self, heap=None):
        """
        Initialize the max heap.
        
        Args:
            heap: Optional iterable to build the heap from.
                  If None, creates an empty heap.
        
        Time Complexity:
            - If heap is None: O(1)
            - If heap is provided: O(n) using bottom-up heapify approach
        
        Space Complexity: O(n) where n is the number of elements
        """
        if heap is None:
            # Initialize empty heap
            self._heap = []
        else: 
            # O(n) approach: convert to list and build heap bottom-up
            self.heapify(heap)
            
            # Alternative O(nlogn) approach (insert each element individually)
            # if heap is not None: 
            #     for value in heap:
            #         self.push(value)
            
            
    def heapify(self, iterable):
        """
        Build a max heap from an iterable of values.
        
        Algorithm:
        1. Convert iterable to list and assign to internal heap
        2. Use bottom-up heapify approach starting from last non-leaf node
        
        Time Complexity: O(n) - efficient heap construction
        Space Complexity: O(n) - for storing the heap elements
        
        Args:
            iterable: An iterable of values to build the heap from
        """
    
        # Start from the last non-leaf node and heapify down
        self._heap = list(iterable)   # copying input lsit to the heap O(n)
        
        # Why start from len(heap) // 2 - 1?
        # - In a complete binary tree with n nodes, the last non-leaf node is at index (n//2 - 1)
        # - All nodes after this index are leaf nodes (no children to compare with)
        # - By starting from the last non-leaf and going backwards, we ensure each parent
        #   is already in correct position before we process its parent
        # - This bottom-up approach is more efficient than inserting elements one by one
        for i in range(len(iterable) // 2 - 1, -1, -1):
            # heapify_down: moves a node down the tree by comparing with its children
            # and swapping with the larger child if needed, until heap property is restored
            self._heapify_down(i)


    def push(self, value):
        """
        Insert a new value into the heap.
        
        Algorithm:
        1. Add value at the end of the list
        2. Bubble up the value to its correct position by comparing with parent
        3. Swap if child > parent, continue until heap property is satisfied
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # Append value at the end of the heap
        self._heap.append(value)
        
        # Bubble up from the last index to restore heap property
        self._heapify_up(len(self._heap) - 1)
    
    # Alias for push (common naming convention)
    insert = push


    def pop(self):
        """
        Remove and return the maximum element (root) from the heap.
        
        Algorithm:
        1. Save the root value (maximum element)
        2. Move the last element to the root position
        3. Remove the last element from the list
        4. Bubble down from root to restore heap property
        5. Return the saved maximum value
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Raises:
            IndexError: If the heap is empty
        """
        if self.isempty():
            raise IndexError("pop from empty heap")
        if len(self._heap) == 1:
            return self._heap.pop()  # Just pop the only element
        
        # Save the maximum element (at root)
        value = self._heap[0]
        
        # Replace the root with the last element in the heap (while also removing the last element)
        # This effectively removes the last element and places it at the root, which may violate the heap property
        # We will restore the heap property by bubbling down this new root element to its correct position
        self._heap[0] = self._heap.pop()
        
        # Restore heap property by bubbling down from root
        # Only if heap is not empty after deletion
        if not self.isempty():
            # Bubble down from the root to restore the max heap property
            self._heapify_down(0)
        
        return value

    # Alias for pop (common naming convention)
    remove = pop
    extract_max = pop
    
    
    def peek(self):
        """
        Return the maximum element (root) without removing it from the heap.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Raises:
            IndexError: If the heap is empty
        """
        if self.isempty():
            raise IndexError("peek from empty heap")
        
        return self._heap[0]

    
    def clear(self):
        """
        Remove all elements from the heap.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._heap.clear()
    
    
    def tolist(self):
        """
        Return a copy of the internal heap list.
        
        Returns:
            A shallow copy of the heap list
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return self._heap.copy()
    
    
    
    def increase_key(self, i, new_value):
        """
        Increase the value at index i to new_value and restore heap property.
        
        Used when you want to increase a key value and re-heapify.
        
        Algorithm:
        1. Replace value at index i with new_value
        2. If new_value < old value, this is a decrease, so heapify down
        3. If new_value > old value, this is an increase, so heapify up
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            i: Index of the element to update
            new_value: The new value (should be >= old value for max heap)
            
        Raises:
            IndexError: If index is out of bounds
            ValueError: If new_value is less than current value (should use decrease_key)
        """
        if i < 0 or i >= len(self._heap):
            raise IndexError("index out of bounds")
        
        old_value = self._heap[i]
        if new_value < old_value:
            raise ValueError("new_value must be >= old_value. Use decrease_key instead")
        
        self._heap[i] = new_value
        # If new_value is greater than old_value, 
        # we need to bubble up to restore max heap property
        self._heapify_up(i)
    
    
    def decrease_key(self, i, new_value):
        """
        Decrease the value at index i to new_value and restore heap property.
        
        Used when you want to decrease a key value and re-heapify.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            i: Index of the element to update
            new_value: The new value (should be <= old value for max heap)
            
        Raises:
            IndexError: If index is out of bounds
            ValueError: If new_value is greater than current value (should use increase_key)
        """
        if i < 0 or i >= len(self._heap):
            raise IndexError("index out of bounds")
        
        old_value = self._heap[i]
        if new_value > old_value:
            raise ValueError("new_value must be <= old_value. Use increase_key instead")
        
        self._heap[i] = new_value
        # If new_value is less than old_value,
        # we need to bubble down to restore max heap property
        self._heapify_down(i)
    
    
    def heapsort(self, preserve=True):
        """
        Return a sorted list of heap elements in descending order.
        
        Note: This operation modifies the heap. Create a copy if you need to preserve it.
        Use tolist() before calling if you want to keep the heap intact.
        
        Algorithm:
        1. Repeatedly extract the maximum element (pop)
        2. Add to result list
        
        Time Complexity: O(n log n)
        Space Complexity: O(n) for the result list
        
        Returns:
            List of elements in descending order
        """
        result = []
        if preserve:
            temp = MaxHeap(self._heap)  # Create a copy to preserve original heap
            while not temp.isempty():
                result.append(temp.pop())
        else:
            while not self.isempty():
                result.append(self.pop())
            self._heap = result.copy()  # set original heap to sorted result
        return result
    
    
    def _heapify_up(self, i):
        """
        Bubble up a node to restore max heap property.
        
        Algorithm:
        1. Start from node at index i
        2. While node has a parent and node > parent:
            - Swap node with parent
            - Move to parent's position
        3. Continue until heap property is satisfied
        
        Time Complexity: O(log n) - height of binary heap
        Space Complexity: O(1) - iterative approach, no recursion
        
        Args:
            i: Index of the node to bubble up
    """
        # Compare with parent while within bounds
        while i and self._heap[self._parent(i)] < self._heap[i]:
            # Swap with parent if child is greater (max heap property)
            self._swap(self._parent(i), i)
            # Move to parent's position for next iteration
            i = self._parent(i)
    

    def _heapify_down(self, i):
        """
        Bubble down a node to restore max heap property.
        
        Algorithm:
        1. Start from node at index i
        2. Find the largest among node, left child, right child
        3. If node is not the largest:
           - Swap node with the largest child
           - Recursively heapify down from that child's position
        4. Continue until heap property is satisfied
        
        Time Complexity: O(log n) - height of binary heap
        Space Complexity: O(log n) - recursive call stack
        
        Args:
            i: Index of the node to bubble down
        """
        # Get indices of left and right children
        lcindex, rcindex = self._lchild(i), self._rchild(i)
        largest = i  # Assume current node is the largest
        
        # Check if left child exists and is greater than current largest
        if lcindex < len(self._heap) and self._heap[lcindex] > self._heap[largest]:
            largest = lcindex
        
        # Check if right child exists and is greater than current largest
        if rcindex < len(self._heap) and self._heap[rcindex] > self._heap[largest]:
            largest = rcindex
        
        # If largest is not the current node, swap and continue heapifying
        if largest != i:
            self._swap(i, largest)
            # Recursively heapify down from the new position
            self._heapify_down(largest)


    def _parent(self, i):
        """
        Get the index of the parent node.
        
        Formula: parent_index = (i - 1) // 2
        
        Args:
            i: Index of the child node
            
        Returns:
            Index of the parent node
            
        Time Complexity: O(1)
        """
        return (i - 1) // 2


    def _lchild(self, i):
        """
        Get the index of the left child node.
        
        Formula: left_child_index = 2*i + 1
        
        Args:
            i: Index of the parent node
            
        Returns:
            Index of the left child node
            
        Time Complexity: O(1)
        """
        return 2*i + 1


    def _rchild(self, i):
        """
        Get the index of the right child node.
        
        Formula: right_child_index = 2*i + 2
        
        Args:
            i: Index of the parent node
            
        Returns:
            Index of the right child node
            
        Time Complexity: O(1)
        """
        return 2*i + 2


    def _swap(self, i, j):
        """
        Swap two elements in the heap by their indices.
        
        Args:
            i: Index of first element
            j: Index of second element
            
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]


    def isempty(self):
        """
        Check if the heap is empty.
        
        Returns:
            True if heap contains no elements, False otherwise
            
        Time Complexity: O(1)
        """
        return len(self._heap) == 0
    is_empty = isempty  # Alias for isempty
    
    
    def __getitem__(self, key):
        """Allow indexing and slicing of the heap.
        Args:
            key: An integer index or a slice object
        Returns:
            The element at the specified index or a list of elements for a slice
        Time Complexity: O(1) for indexing, O(k) for slicing where k is the number of elements in the slice
        """
        if isinstance(key, int):
                return self._heap[key]
            
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return self._heap[start:stop:step]
    

    def __len__(self):
        """
        Get the number of elements in the heap.
        
        Returns:
            Number of elements currently in the heap
            
        Time Complexity: O(1)
        """
        return len(self._heap)
    
    # Alias for __len__ 
    size = __len__


    def __repr__(self):
        """
        Return a string representation of the heap.
        
        Returns:
            String representation showing the internal list structure
            
        Example:
            MaxHeap([10, 8, 5, 3, 2])
        """
        return f"MaxHeap({self._heap})"