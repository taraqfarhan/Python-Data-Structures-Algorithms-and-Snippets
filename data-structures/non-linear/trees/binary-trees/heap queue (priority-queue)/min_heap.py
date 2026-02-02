class MinHeap:
    def __init__(self, heap=None):
        self._heap = []
        if heap is not None:
            self.heapify(heap)
        

    def heapify(self, iterable):
        self._heap = list(iterable)
        for i in range(len(self._heap) // 2 - 1, -1, -1):
            self._heapify_down(i)


    def push(self, value):
        self._heap.append(value)
        self._heapify_up(len(self._heap) - 1)
    add = push


    def pop(self):
        if self.isempty():
            raise IndexError("Index out of bound")
        if len(self) == 1:
            return self._heap.pop()

        value = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(0)

        return value
    remove = pop
    extract_min = pop


    def peek(self):
        if self.isempty():
            raise IndexError("Index out of bound")
        return self._heap[0]
    

    def increase_key(self, i, new_value):
        if i < 0 or i >= len(self):
            raise IndexError("Index out of bound")
        if self[i] > new_value:
            raise ValueError("try decrease_key method instead")

        self._heap[i] = new_value
        self._heapify_down(i)
        

    def decrease_key(self, i, new_value):
        if i < 0 or i >= len(self):
            raise IndexError("Index out of bound")
        if self[i] < new_value:
            raise ValueError("try increase_key method instead")

        self._heap[i] = new_value
        self._heapify_up(i)


    def heapsort(self, preserve=True):
        result = []
        if preserve:
            temp = MinHeap(self._heap)  # Create a copy to preserve original heap
            while not temp.isempty():
                result.append(temp.pop())
        else:
            while not self.isempty():
                result.append(self.pop())
            self._heap = result.copy()  # set original heap to sorted result
        return result


    def _heapify_up(self, i):
        while i and self._heap[i] < self._heap[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)


    def _heapify_down(self, i):
        lowest = i
        lchild, rchild = self._lchild(i), self._rchild(i)

        if lchild < len(self) and self._heap[lchild] < self._heap[lowest]:
            lowest = lchild

        if rchild < len(self) and self._heap[rchild] < self._heap[lowest]:
            lowest = rchild

        if i != lowest:
            self._swap(i, lowest)
            self._heapify_down(lowest)
            
            
    def clear(self):
        self._heap.clear()

    def isempty(self):
        return len(self._heap) == 0

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _parent(self, i):
        return i // 2 - 1

    def _lchild(self, i):
        return 2*i + 1

    def _rchild(self, i):
        return 2*i + 2

    def __len__(self):
        return len(self._heap)

    def __iter__(self):
        for i in range(len(self)):
            yield self._heap[i]

    def __repr__(self):
        return f"MinHeap{self._heap}"
    
    def tolist(self):
        return self._heap.copy()
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._heap[key]
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return self._heap[start:stop:step]