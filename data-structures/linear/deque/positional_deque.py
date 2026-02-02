"""
We will implement the deque using a Positional List (which relies on using
a doubly linked list with sentinels under the hood).

Sentinels are used in a doubly linked list to simplify the implementations as using them removes the corner cases.
Two dummy nodes named generally `header` and `trailer`, work as sentinels (guards) in the Doubly Linked List
"""

class Deque:
    class Node:
        """each Node of a Linked List structure"""
        # Each Node has a data and two pointers
        # one pointer to the next Node
        # another to the prev Node
        def __init__(self, data, prev, next):
            self.data = data # data stored in the current Node

            # each Node points to the next and prev Node of the Linked List
            self.prev = prev
            self.next = next


        def __repr__(self):
            """Represenattion of a Node object"""
            return f"Node({self.prev.data} <- {self.data} -> {self.next.data})"


    # Each Linked List has a header and trailer sentinel (guard)
    # If there is no Node (the linked list is empty) then
    # Header's next pointer will point to Trailer
    # and Trailer's prev pointer will point to Header
    def __init__(self, linkedlist=None):
        self.header = self.Node(None, None, None)  # the header sentinel
        self.trailer = self.Node(None, None, None)   # the trailer sentinel
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self._n = 0    # total nodes

        # Deque(['A', 'B', 'C', 'D']) to A ⇌ B ⇌ C ⇌ D
        if linkedlist is not None:
            for data in linkedlist: self.append(data)


    def _insert_between(self, data, predecessor, successor):
        """Add new node with `data` between two existing nodes and return the new node"""
        new_node = self.Node(data, predecessor, successor)

        predecessor.next = new_node
        successor.prev = new_node

        self._n += 1
        return new_node


    def append(self, data):
        """append a new Node at the end of the Deque"""
        """Time Complexity O(1)"""
        self._insert_between(data, self.trailer.prev, self.trailer)


    def appendleft(self, data):
        """append a new Node at the start of the Deque"""
        """Time Complexity O(1)"""
        self._insert_between(data, self.header, self.header.next)


    def _delete(self, node):
        """Delete non-sentinel node from the list and return it's data"""
        value = node.data

        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor

        node.prev = node.next = node.data = None   # deprecate node

        self._n -= 1
        return value


    def pop(self):
        """Pop an item from the list using indexing"""
        """Time Complexity O(1)"""
        if self.isempty(): # no element can be popped from an empty list
            raise ValueError("Empty Deque")
        return self._delete(self.trailer.prev)


    def end(self):
        """Get the last item from the deque without removing it"""
        """Time Complexity O(1)"""
        if self.isempty(): # no element can be popped from an empty list
            raise ValueError("Empty Deque")
        return self.trailer.prev.data
    last = end


    def popleft(self):
        """Time Complexity O(1)"""
        if self.isempty():
            raise ValueError("Empty Deque")
        return self._delete(self.header.next)


    def front(self):
        """Get the first element from the deque"""
        """Time Complexity O(1)"""
        if self.isempty():
            raise ValueError("Empty Deque")
        return self.header.next.data
    first = front


    def __len__(self):
        """Get the length of the Singly Linked List"""
        """Time Complexity O(1)"""
        return self._n
    size = __len__


    def __iter__(self):
        """Iterator for a Deque object"""
        start = self.header.next
        while start.next is not None:
            yield start.data
            start = start.next


    def __repr__(self):
        """Representation of a Deque object"""
        return f"Deque({' -> '.join(map(str, self))})"


    def isempty(self):
        """Time Complexity O(1)"""
        return self._n == 0
