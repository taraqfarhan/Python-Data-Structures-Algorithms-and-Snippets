"""
We will be implementing the Queue using a singly linked list, that will have
both head an tail pointers. So this will make it easier for us to
enqueue (adding element at the end) and dequeue (removing element from the front)
in constant time O(1)
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        if self.next is None: return f"Node({self.data} -> None)"
        return f"Node({self.data} -> {self.next.data})"


class Queue:
    def __init__(self, queue=None):
        self._n = 0      # total nodes
        self.head = self.tail = None
        if queue is not None:
            for data in queue: self.enqueue(data)


    def enqueue(self, data):
        """Time Complexity O(1)"""
        new_node = Node(data)
        # case 1: if the queue is empty
        if self.isempty():
            self.head = self.tail = new_node
        # case 2: at least 1 node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._n += 1
    add = enqueue


    def dequeue(self):
        """Time Complexity O(1)"""
        # case 1: if the queue is empty
        if self.isempty():
            raise ValueError("Queue is empty")

        value = self.head.data
        # case 2: one node
        if self.head.next is None:
            self.head = self.tail = None
        # case 3: more than one node
        else:
            self.head = self.head.next

        self._n -= 1
        return value
    poll = dequeue


    def peek(self):
        """Time Complexity O(1)"""
        if self.isempty():
            raise ValueError("Queue is empty")
        return self.head.data
    first = peek


    def isempty(self):
        """Time Complexity O(1)"""
        return self._n == 0


    def __len__(self):
        """Time Complexity O(1)"""
        return self._n
    size = __len__


    def __repr__(self):
        return f"Queue({' -> '.join(map(str, self))})"


    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


    def tolist(self):
        return list(self)


    def getnode(self, index):
        if index < 0:
            index += self._n
        if index < 0 or index >= self._n:
            raise IndexError("Index out of range")
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index != index:
            current_index += 1
            current_node = current_node.next
        return current_node


    def __getitem__(self, key, node=False):
        """Time Complexity O(1) (indexing)"""
        """Time Complexity O(k * n) (slicing)"""
        if isinstance(key, (int, tuple)):
            if isinstance(key, tuple):
                key, node = key
            if key < 0:
                key += self._n
            if key < 0 or key >= self._n:
                raise IndexError("Index out of range")
            curr_node = self.getnode(key)
            if curr_node:
                if node: return curr_node
                return curr_node.data
            raise ValueError("Node doesn't exist")

        if isinstance(key, slice):
            start, stop, step = key.indices(self._n)
            return [self.getnode(i).data for i in range(start, stop, step)]
