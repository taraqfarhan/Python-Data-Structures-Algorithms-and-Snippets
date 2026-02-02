"""
A static stack has a predetermined (fixed) size and it can't be changed during the
program's execution
"""
import ctypes

class Stack:
    def __init__(self, capacity):
        """initializing a new static stack"""
        # Stack(6) : Creating a stack with capacity 6 and all of the positions being empty
        self._capacity = capacity
        self._stack = (self._capacity * ctypes.py_object)() # creating a low-level python array with size of self._capacity
        self._top = -1


    # Supporting Stack.from_iterable([13,25,26,73,17,63])
    # Or, Stack.from_iterable([13,25,26,73,17,63], 10)   # with capacity 10
    # Creating a stack with capacity 6 and all of the positions being filled from the given iterable
    @classmethod
    def from_iterable(cls, iterable, capacity=None):
        if capacity is None:
            capacity = len(iterable)
        if len(iterable) > capacity:
            raise ValueError("Capacity can't be smaller than the actual size of the iterable")

        instance = cls(capacity) # Create a standard instance first
        instance._capacity = capacity

        instance._top = len(iterable) - 1
        instance._stack = (instance._capacity * ctypes.py_object)() # creating a low-level python array
        # fill the stack with elements
        for i in range(len(iterable)):
            instance._stack[i] = iterable[i]

        return instance


    def push(self, item):
        """Time Complexity O(1)"""
        if len(self) == self._capacity:
            raise ValueError("The Stack is already full of it's capacity")

        self._stack[self._top + 1] = item
        self._top += 1


    def pop(self):
        """Time Complexity O(1)"""
        if self.isempty():
            raise ValueError("The Stack is empty")

        value = self._stack[self._top]
        self._stack[self._top] = None      # to be collected by the garbage collector
        self._top -= 1

        return value


    def top(self):
        """Time Complexity O(1)"""
        if self.isempty():
            raise ValueError("The Stack is empty")

        return self._stack[self._top]
    peek = top


    def isempty(self):
        """Time Complexity O(1)"""
        return self.size() == 0


    def index(self, item):
        """search for an item in the static stack and return the index of the first occurrence of that item"""
        """Time Complexity O(n)"""
        for i in range(self.size()):
            if self._stack[i] == item:
                return i
        raise ValueError("item doesn't exist in the array")


    def count(self, item):
        """Count the num of occurrences of an item in an array"""
        """Time Complexity O(n)"""
        return sum(1 for i in self if i == item)


    def __repr__(self):
        """Representation of a static stack"""
        return f"Stack({list(self)})"


    def __len__(self):
        """length of the static stack"""
        """Time Complexity O(1)"""
        return self._top + 1

    size = __len__


    def __iter__(self):
        """iterator for a static stack"""
        for i in range(self.size()):
            yield self._stack[i]


    def __getitem__(self, key):
        """accessing items using indexing and slicing"""
        """Time Complexity O(1) (indexing)"""
        """Time Complexity O(k) (slicing)"""
        if isinstance(key, int):
            if key < 0:
                key += self.size()
            if key < 0 or key >= self.size():
                raise IndexError("Index out of range")
            return self._stack[key]

        if isinstance(key, slice):
            start, stop, step = key.indices(self.size())   # handing slicing
            return self._stack[start:stop:step]
