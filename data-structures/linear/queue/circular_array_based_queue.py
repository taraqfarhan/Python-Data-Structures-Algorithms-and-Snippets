import ctypes

class Queue:
    def __init__(self, queue=None):
        self._n = 0   # total elements
        self._capacity = 1  # default-capacity is 1
        self._front = 0   # index of the first element of the queue
        self._queue = self._make_array(self._capacity) # getting a low-level array with default capacity
        if queue is not None:
            for item in queue: self.enqueue(item)


    def enqueue(self, item):
        """Adding an item at the end of the queue"""
        """Time Complexity O(1) (amortized)"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        end = (self._front + self._n) % self._capacity
        self._queue[end] = item
        self._n += 1
    add = enqueue


    def dequeue(self):
        """Removing an item from the front of the queue"""
        """Time Complexity O(1) (amortized)"""
        if self.isempty():
            raise ValueError("Queue is empty")
        # if num of total elements is less than or euqal to
        # 1/4 th of the total capacity, half the capacity
        if 4 * self._n <= self._capacity:
            self._resize(self._capacity // 2)

        value = self._queue[self._front]
        self._front = (self._front + 1) % self._capacity
        self._n -= 1
        return value
    poll = dequeue


    def first(self):
        """Time Complexity O(1)"""
        """getting the first element without removing"""
        if self.isempty():
            raise ValueError("Queue is empty")
        return self._queue[self._front]
    peek = first


    def isempty(self):
        """Time Complexity O(1)"""
        """check if the queue is empty"""
        return self._n == 0


    def tolist(self):
        """Get a list object from the Queue"""
        return list(self)


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
            yield self._queue[(self._front + i) % self._capacity]


    def __getitem__(self, key):
        """Time Complexity O(1) (indexing)"""
        """Time Complexity O(k) (slicing)"""
        if isinstance(key, int):
            if key < 0:
                key += self._n      # handling negative indexing
            if key < 0 or key >= self._n:
                raise IndexError("Index out of range")
            return self._queue[(self._front + key) % self._capacity]
        if isinstance(key, slice):
            start, stop, step = key.indices(self._n)
            return self._queue[start:stop:step]


    def _resize(self, capacity):
        old_capacity = self._capacity
        position = self._front

        aux = self._make_array(capacity)
        for i in range(self._n):
            aux[i] = self._queue[position]
            position = (position + 1) % old_capacity

        self._queue = aux
        self._front = 0


    def _make_array(self, capacity):
        self._capacity = capacity
        return (self._capacity * ctypes.py_object)()
