"""
We will implement the deque (double-ended-queue) using a doubly linked list
In this implementation we can append, appendleft, pop and popleft in constant
time. The deque will have two pointers (head and tail) and each node in the deque
will have two pointers (prev and next)
"""

class Deque:
    class Node:
        """each Node of a Deque"""
        # Each Node has a data and two pointers
        # one pointer to the next Node
        # another to the prev Node
        def __init__(self, data, next=None, prev=None):
            self.data = data # data stored in the current Node

            # each Node points to the next and prev Node of the Deque
            # if there is no Node after/prev current Node then next/prev points to None
            self.next = next
            self.prev = prev


        def __repr__(self):
            """Represenattion of a Node object"""
            if self.prev is None and self.next is None:
                 return f"Node({None} <- {self.data} -> {None})"
            elif self.prev is None:
                 return f"Node({None} <- {self.data} -> {self.next.data})"
            elif self.next is None:
                 return f"Node({self.prev.data} <- {self.data} -> {None})"
            return f"Node({self.prev.data} <- {self.data} -> {self.next.data})"


    # Each Deque has a head and tail pointer
    # head points to the first Node and tail points to the last Node
    # If there is no Node (the linked list is empty) then head and tail points to None
    def __init__(self, linkedlist=None):
        self.head = None  # the head pointer
        self.tail = None   # the tail pointer
        self._n = 0    # total nodes

        # Deque(['A', 'B', 'C', 'D']) to A ⇌ B ⇌ C ⇌ D
        if linkedlist is not None:
            for data in linkedlist: self.append(data)


    def append(self, data):
        """append a new Node at the end of the Deque"""
        """Time Complexity O(1)"""
        new_node = self.Node(data)   # create a new node

        # case 1: the list is empty
        if self.isempty():
            self.head = self.tail = new_node

        # case 2: the list has already one or more elements
        else:
            # current node is now the last node
            # link the new node from the last node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._n += 1


    def appendleft(self, data):
        """append a new Node at the start of the Deque"""
        """Time Complexity O(1)"""
        new_node = self.Node(data)    # Create the new node

        # case 1: the list is empty
        if self.isempty():
            self.head = self.tail = new_node

        # case 2: the list has one or more elements
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self._n += 1


    def pop(self):
        """Pop an item from the list using indexing"""
        """Time Complexity O(1)"""
        if self.isempty(): # no element can be popped from an empty list
            raise ValueError("Empty Deque")

        value = self.tail.data
        if self.head.next is None:  # if there is only one element
            self.head = self.tail = None
        else:   # there is more than 1 element
            self.tail.prev.next = None
            self.tail = self.tail.prev

        self._n -= 1
        return value


    def end(self):
        """Get the last item from the deque without removing it"""
        """Time Complexity O(1)"""
        if self.isempty(): # no element can be popped from an empty list
            raise ValueError("Empty Deque")

        return self.tail.data
    last = end


    def popleft(self):
        """Time Complexity O(1)"""
        # Case 1: empty
        if self.isempty():
            raise ValueError("Empty Deque")

        value = self.head.data
        # Case 2: total nodes (1)
        if self.head.next is None:
            self.head = self.tail = None
        # Case 3: total nodes (> 1)
        else:
            self.head = self.head.next
            self.head.prev = None

        self._n -= 1
        return value


    def front(self):
        """Get the first element from the deque"""
        """Time Complexity O(1)"""
        if self.isempty():
            raise ValueError("Empty Deque")

        return self.head.data
    first = front


    def isempty(self):
        """Time Complexity O(1)"""
        return self._n == 0


    def index(self, data, start=0):
        """return the first index of data"""
        """Time Complexity O(n)"""
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_node.data == data and current_index >= start:
                return current_index
            current_index += 1
            current_node = current_node.next
        raise ValueError("Value not in the Deque")


    def tolist(self):
        """traverse the whole Deque and return that list"""
        return list(self)


    def getnode(self, index):
        """get Node from the Deque using 0 indexing"""
        if index < 0:
            index += self._n
        if index < 0 or index >= self._n:
            raise IndexError("Index out of range")

        if index <= self._n // 2:
            current_node = self.head
            current_index = 0

            while current_node is not None and current_index != index:
                current_node = current_node.next
                current_index += 1
        else:
            current_node = self.tail
            current_index = self._n - 1

            while current_node is not None and current_index != index:
                current_node = current_node.prev
                current_index -= 1

        if current_node is not None:
            return current_node


    def __getitem__(self, key, node=False):
        """get data from the Deque using indexing and slicing"""
        """Time Complexity O(1) (indexing)"""
        """Time Complexity O(k * k) (slicing)"""
        # Supporting Deque[2]
        # And Supporting Deque[2, True]
        # We can achieve the same using Deque.__getitem__(2, True)
        if isinstance(key, (int, tuple)):
            if isinstance(key, tuple): key, node = key
            if key < 0:
                key += self._n    # handle negative index
            if key < 0 or key >= self._n:
                raise IndexError("Deque index out of range")

            curr_node = self.getnode(key)   # get the node at that index
            if curr_node:
                if node: return curr_node    # if node exits and `node` argument is True, return that node
                return curr_node.data   # else return the data

        # Supporting Deque[2:3:2]
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return [self.getnode(k).data for k in range(start, stop, step)]


    def __iter__(self):
        """Iterator for the Deque object"""
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


    def __repr__(self, verbose=False):
        """Representation of a Deque object"""
        if verbose:
            values = ["head"]
            values.extend(map(str, self.tolist()))
            values.append("None")
        else: values = map(str, self.tolist())
        sep = ' \u21cc '
        return f"Deque({sep.join(values)})"


    def __len__(self):
        """Get the length of the Deque"""
        return self._n
    size = __len__
