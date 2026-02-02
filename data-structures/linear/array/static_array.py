import ctypes

class StaticArray:
    def __init__(self, array):
        """initializing a new static array"""
        self._n = len(array)    # total elements
        self._array = (self._n * ctypes.py_object)() # creating a low-level python array with size of self._n
        for i in range(self._n):
            self._array[i] = array[i]

    def index(self, item):
        """search for an item in the static array and return the index of the first occurrence of that item"""
        """Time Complexity O(n)"""
        for i in range(self._n):
            if self._array[i] == item:
                return i
        raise ValueError("item doesn't exist in the array")


    def count(self, item):
        """Count the num of occurrences of an item in an array"""
        """Time Complexity O(n)"""
        return sum(1 for i in self if i == item)


    def __repr__(self):
        """Representation of a static array"""
        return f"StaticArray({list(self)})"


    def __len__(self):
        """length of the static array"""
        """Time Complexity O(1)"""
        return self._n

    size = __len__


    def __iter__(self):
        """iterator for a static array"""
        for i in range(self._n):
            yield self._array[i]


    def __getitem__(self, key):
        """accessing items using indexing and slicing"""
        """Time Complexity O(1) (indexing)"""
        """Time Complexity O(k) (slicing)"""
        if isinstance(key, int):
            # as it's a static array we don't have to manually
            # handle the negative indexing
            return self._array[key]
        if isinstance(key, slice):
            start, stop, step = key.indices(self._n)   # handing slicing
            return self._array[start:stop:step]
