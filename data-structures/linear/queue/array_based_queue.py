import ctypes

class Queue:
    def __init__(self, queue=None):
        self._n = 0   # total elements
        self._capacity = 1  # default-capacity is 1
        self._queue = self._make_array(self._capacity) # getting a low-level array with default capacity
        if queue is not None:
            for item in queue: self.enqueue(item)


    def enqueue(self, item):
        """Adding an item at the end of the queue"""
        """Time Complexity O(1) (amortized)"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._queue[self._n] = item
        self._n += 1

    add = enqueue


    def dequeue(self):
        """Removing an item from the front of the queue"""
        """Time Complexity O(n) (amortized)"""
        if self.isempty():
            raise ValueError("Queue is empty")
        # if num of total elements is less than or euqal to
        # 1/4 th of the total capacity, half the capacity
        if 4 * self._n <= self._capacity:
            self._resize(self._capacity // 2)

        value = self._queue[0]
        for i in range(self._n - 1):
            self._queue[i] = self._queue[i + 1]

        self._n -= 1
        return value

    poll = dequeue


    def first(self):
        """Time Complexity O(1)"""
        """getting the first element without removing"""
        if self.isempty():
            raise ValueError("Queue is empty")
        return self._queue[0]

    peek = first


    def isempty(self):
        """Time Complexity O(1)"""
        """check if the queue is empty"""
        return self._n == 0


    def __repr__(self):
        """representation of a queue object"""
        return f"Queue({list(self)})"


    def __len__(self):
        """Time Complexity O(1)"""
        """length of the queue"""
        return self._n

    size = __len__


    def __iter__(self):
        """getting an queue iterator"""
        for i in range(self._n):
            yield self._queue[i]


    def __getitem__(self, key):
        """Time Complexity O(1) (indexing)"""
        """Time Complexity O(k) (slicing)"""
        if isinstance(key, int):
            if key < 0:
                key += self._n
            if key < 0 or key >= self._n:
                raise IndexError("Index out of range")
            return self._queue[key]
        if isinstance(key, slice):
            start, stop, step = key.indices(self._n)
            return self._queue[start:stop:step]


    def _resize(self, capacity):
        aux = self._make_array(capacity)
        for i in range(self._n):
            aux[i] = self._queue[i]
        self._queue = aux


    def _make_array(self, capacity):
        self._capacity = capacity
        return (self._capacity * ctypes.py_object)()
