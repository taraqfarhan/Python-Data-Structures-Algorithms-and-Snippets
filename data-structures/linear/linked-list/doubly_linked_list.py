class DoublyLinkedList:
    class Node:
        """each Node of a Linked List structure"""
        # Each Node has a data and two pointers
        # one pointer to the next Node
        # another to the prev Node
        def __init__(self, data, next=None, prev=None):
            self.data = data # data stored in the current Node

            # each Node points to the next and prev Node of the Linked List
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


    # Each Linked List has a head and tail pointer
    # head points to the first Node and tail points to the last Node
    # If there is no Node (the linked list is empty) then head and tail points to None
    def __init__(self, linkedlist=None):
        self.head = None  # the head pointer
        self.tail = None   # the tail pointer
        self._n = 0    # total nodes

        # DoublyLinkedList(['A', 'B', 'C', 'D']) to A ⇌ B ⇌ C ⇌ D
        if linkedlist is not None:
            for data in linkedlist: self.append(data)


    def index(self, data, start=0):
        """return the first index of data"""
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_node.data == data and current_index >= start:
                return current_index
            current_index += 1
            current_node = current_node.next
        raise ValueError("Value not in the Linked List")


    def append(self, data):
        """append a new Node at the end of the Linked List"""
        new_node = self.Node(data)   # create a new node

        # case 1: the list is empty
        if self.head is None:
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
        """append a new Node at the start of the Linked List"""
        new_node = self.Node(data)    # Create the new node

        # case 1: the list is empty
        if self.head is None:
            self.head = self.tail = new_node

        # case 2: the list has one or more elements
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self._n += 1


    def insert(self, index, data):
        """insert data before index"""
        if index < 0:
            if self._n == 0:
                self.append(data)
                return
            while index < 0:
                index += self._n    # handle negative indexing
        if index == 0:
            self.appendleft(data)
            return
        elif index >= self._n:
            self.append(data)
            return

        new_node = self.Node(data)

        # if index is smaller or equal than half of the total nodes
        # then start traversing from the head
        # else start from the tail
        if index <= self._n // 2:
            current_node = self.head
            current_index = 0

            # traverse to the index `index - 1`
            while current_node is not None and current_index != (index-1):
                current_node = current_node.next
                current_index += 1

            # current_node is in the index `index - 1`
            if current_node is not None:
                old_node = current_node.next
                current_node.next = new_node
                new_node.next = old_node
                new_node.prev = current_node
                old_node.prev = new_node
        else:
            current_node = self.tail
            current_index = self._n - 1

            # traverse to the index `index`
            while current_node is not None and current_index != index:
                current_node = current_node.prev
                current_index -= 1

            # current_node is in the index `index`
            if current_node is not None:
                old_node = current_node.prev
                current_node.prev = new_node
                new_node.prev = old_node
                new_node.next = current_node
                old_node.next = new_node

        self._n += 1


    def extend(self, other):
        """Extend current list with the elements from other list (in-place)"""
        self.tail.next = other.head
        other.head.prev = self.tail
        self.tail = other.tail

        self._n += other._n


    def pop(self, index=None):
        """Pop an item from the list using indexing"""
        if self._n == 0:   # no element can be popped from an empty list
            raise ValueError("Empty Linked List")
        if index is None or index >= self._n:   # default is the last item
            index = self._n - 1
        if index == 0:
            return self.popleft()
        if index < 0:
            index += self._n
        if index < 0:
            raise IndexError("Index out of range")

        if index == self._n - 1:
            if self.head.next is None:  # if there is only one element
                value = self.tail.data
                self.head = self.tail = None
            else:   # there is more than 1 element
                value = self.tail.data
                self.tail.prev.next = None
                self.tail = self.tail.prev

        # if index is smaller or equal than half of the total nodes
        # then start traversing from the head
        # else start from the tail
        elif index <= self._n // 2:
            current_node = self.head
            current_index = 0

            # traverse to the index `index - 1`
            while current_node is not None and current_index != (index-1):
                current_node = current_node.next
                current_index += 1

            # current_node is in the index `index - 1`
            if current_node is not None:
                value = current_node.next.data
                current_node.next = current_node.next.next
                current_node.next.prev = current_node

        else:
            current_node = self.tail
            current_index = self._n - 1

            # traverse to the index `index`
            while current_node is not None and current_index != (index+1):
                current_node = current_node.prev
                current_index -= 1

            # current_node is in the index `index`
            if current_node is not None:
                value = current_node.prev.data
                current_node.prev = current_node.prev.prev
                current_node.prev.next = current_node

        self._n -= 1
        return value


    def popleft(self):
        # Case 1: empty
        if self.head is None:
            raise ValueError("Empty Linked List")
        # Case 2: total nodes (1)
        elif self.head.next is None:
            value = self.head.data
            self.head = self.tail = None
        # Case 3: total nodes (> 1)
        else:
            value = self.head.data
            self.head = self.head.next
            self.head.prev = None

        self._n -= 1
        return value


    def remove(self, value):
        """Remove the first occurrence of Node that has Node.data == value"""
        current_node = self.head
        current_index = 0
        found = False
        while current_node is not None:
            if current_node.data == value:
                found = True
                break
            current_node = current_node.next
            current_index += 1

        if not found: raise ValueError("Value not in the list")
        self.pop(current_index)


    def reverse(self):
        """reverse the actual linked list in place
        like from A ⇌ B ⇌ C ⇌ D to D ⇌ C ⇌ B ⇌ A"""
        self.tail = self.head
        prev_visited = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_visited
            current_node.prev = next_node
            prev_visited = current_node

            current_node = next_node

        self.head = prev_visited


    def tolist(self):
        """traverse the whole Linked List and return that list"""
        res = []
        current_node = self.head

        while current_node is not None:
            res.append(current_node.data)
            current_node = current_node.next
        return res


    def getnode(self, index):
        """get Node from the Linked List using 0 indexing"""
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
        """get data from the Linked List using indexing and slicing"""
        # Supporting DoublyLinkList[2]
        # And Supporting DoublyLinkList[2, True]
        # We can achieve the same using DoublyLinkList.__getitem__(2, True)
        if isinstance(key, (int, tuple)):
            if isinstance(key, tuple): key, node = key
            if key < 0:
                key += self._n    # handle negative index
            if key < 0 or key >= self._n:
                raise IndexError("Linked List index out of range")

            curr_node = self.getnode(key)   # get the node at that index
            if curr_node:
                if node: return curr_node    # if node exits and `node` argument is True, return that node
                return curr_node.data   # else return the data

        # Supporting DoublyLinkList[2:3:2]
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return [self.getnode(k).data for k in range(start, stop, step)]


    def __iter__(self):
        """Iterator for the DoublyLinkedList object"""
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


    def __repr__(self):
        """Representation of a DoublyLinkedList object"""
        values = map(str, self.tolist())
        sep = ' \u21cc '
        return f"DoublyLinkedList({sep.join(values)})"


    def __len__(self):
        """Get the length of the Singly Linked List"""
        return self._n
    size = __len__
