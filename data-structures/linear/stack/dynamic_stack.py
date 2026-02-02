import ctypes

class Stack():
    def __init__(self, array=None):
        """initializing a new stack"""
        self._n = 0    # total elements
        self._capacity = 1   # default capacity
        self._stack = self._make_array(self._capacity)
        if array is not None:
            for item in array: self.push(item)


    def push(self, item):
        """Push a new element on the top of the stack"""
        """Time Complexity O(1) (amortized)"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._stack[self._n] = item
        self._n += 1


    def pop(self):
        """Pop the top element from the stack"""
        """Time Complexity O(1) (amortized)"""
        if not self.isempty():
            if 4 * self._n <= self._capacity:
                self._resize(self._capacity // 2)
            value = self._stack[self._n - 1]
            self._n -= 1
            return value
        raise ValueError("Can't pop from an empty array")


    def isempty(self):
        """check if the stack is empty or not"""
        """Time Complexity O(1)"""
        return self._n == 0


    def top(self):
        """get the top element on the stack, also known as peek"""
        """Time Complexity O(1)"""
        if self.isempty():
            raise ValueError("Stack is empty")
        return self._stack[self._n - 1]
    peek = top # top is also known as peek


    def __repr__(self):
        """Representation of a stack"""
        return f"Stack({list(self)})"


    def __len__(self):
        """length of the stack"""
        """Time Complexity O(1)"""
        return self._n
    size = __len__


    def __iter__(self):
        """iterator for a stack"""
        for i in range(len(self)):
            yield self._stack[i]


    def __getitem__(self, key):
        """accessing items using indexing and slicing"""
        """Time Complexity O(1) (indexing)"""
        """Time Complexity O(k) (slicing)"""
        if isinstance(key, int):
            if key < 0:
                key += self._n
            if key < 0 or key >= self._n:
                raise IndexError("Index out of range")
            return self._stack[key]

        if isinstance(key, slice):
            start, stop, step = key.indices(self._n)
            return self._stack[start:stop:step]


    def _resize(self, capacity):
        """Resizing the current array with a diff capacity"""
        aux = self._make_array(capacity)
        for i in range(len(self)):
            aux[i] = self._stack[i]
        self._stack = aux


    def _make_array(self, capacity):
        """Creating a lower-level array"""
        self._capacity = capacity
        return (self._capacity * ctypes.py_object)()
