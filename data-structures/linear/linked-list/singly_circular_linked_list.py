class CircularLinkedList:
    class Node:
        """each Node of a Linked List structure"""
        # Each Node has a data and a pointer to the next Node
        def __init__(self, data, next=None):
            self.data = data # data stored in the current Node

            # each Node points to the next Node of the Linked List
            # in circular linked list, the last Node's next pointer
            # points to the first Node, making it a circle
            self.next = next


        def __repr__(self):
            """Represenattion of a Node object"""
            if self.next is None:
                return f"Node({self.data} -> {None})"
            return f"Node({self.data} -> {self.next.data})"


    def __init__(self, linkedlist=None):
        # we use `tail` pointer instead of `head`
        # because `tail.next` equals to `head`
        # so using tail, we can access head easily, but not the vice-versa
        self.tail = None  # the tail pointer (points to the last element)
        self._n = 0    # total nodes

        # CircularLinkedList(['A', 'B', 'C', 'D']) to A -> B -> C -> D -> A -> B -> C -> ...
        if linkedlist is not None:
            for data in linkedlist: self.append(data)


    def index(self, data, start=0):
        """return the first index of data"""
        if self.isempty():
            raise ValueError("Empty list")

        current_node = self.tail.next
        current_index = 0

        for _ in range(self._n):
            if current_node.data == data and current_index >= start:
                return current_index
            current_index += 1
            current_node = current_node.next

        raise ValueError("Value not in the Linked List")


    def append(self, data):
        """append a new Node at the end of the Linked List"""
        new_node = self.Node(data)

        # case 1: the list is empty
        if self.isempty():
            self.tail = new_node
            new_node.next = self.tail

        # case 2: the list has already one or more elements
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node   # modify the new_tail
        self._n += 1


    def appendleft(self, data):
        """append a new Node at the start of the Linked List"""
        new_node = self.Node(data)     # Create the new node
        # case 1: the list is empty
        if self.isempty():
            self.tail = new_node
            new_node.next = self.tail

        # case 2: the list has already one or more elements
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node      # modify the new_tail
        self._n += 1


    def insert(self, index, data):
        """insert data before index"""
        if index < 0:
            if self.isempty():
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

        current_node = self.tail.next
        current_index = 0
        new_node = self.Node(data)

        # traverse to the index `index - 1`
        while current_index != (index-1):
            current_node = current_node.next
            current_index += 1

        # current_node is in the index `index - 1`
        old_node = current_node.next
        current_node.next = new_node
        new_node.next = old_node
        self._n += 1


    def extend(self, other):
        """extend current linked list with the items from another list in-place"""
        if self.isempty() or other.isempty():
            raise ValueError("Empty list")

        head = self.tail.next
        self.tail.next = other.tail.next
        self.tail = other.tail
        other.tail.next = head
        self._n += other._n


    def pop(self, index=None):
        """Pop an item from the list using indexing"""
        if self.isempty():
            raise ValueError("Empty Linked List")
        if index is None or index >= self._n:   # default is the last item
            index = self._n - 1
        if index < 0:
            index += self._n  # handling negative indexing
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            return self.popleft()

        current_index = 0
        current_node = self.tail.next

        # traverse to the index `index - 1`
        while current_index != (index - 1):
            current_node = current_node.next
            current_index += 1

        # current_node is in (index - 1)th position
        if current_index == self._n - 2:  # popping the last item
            value = self.tail.data
            current_node.next = self.tail.next
            self.tail = current_node
        else:
            value = current_node.next.data
            current_node.next = current_node.next.next
        self._n -= 1
        return value


    def popleft(self):
        # Case 1: empty
        if self.isempty():
            raise ValueError("Empty Linked List")

        # Case 2: total nodes (1)
        if self._n == 1:
            value = self.tail.data
            self.tail = None
        # Case 3: total nodes (> 1)
        else:
            value = self.tail.next.data
            self.tail.next = self.tail.next.next

        self._n -= 1
        return value


    def remove(self, value):
        """Remove the first occurrence of Node that has Node.data == value"""
        if self.isempty():
            raise ValueError("Empty Linked List")

        current_node = self.tail.next
        current_index = 0
        found = False
        for _ in range(self._n):
            if current_node.data == value:
                found = True
                break
            current_node = current_node.next
            current_index += 1

        if not found: raise ValueError("Value not in the list")
        self.pop(current_index)


    def tolist(self):
        """traverse the whole Linked List"""
        res = []
        if self.isempty(): return res

        current_node = self.tail.next
        for _ in range(self._n):
            res.append(current_node.data)
            current_node = current_node.next
        return res


    def reverse(self):
        """reverse the actual linked list in place
        like from A -> B -> C -> A -> ... to A <- B <- C <- A ..."""
        if self.isempty():
            raise ValueError("Empty linked list")

        prev_visited = self.tail
        current_node = self.tail.next

        for _ in range(self._n):
            next_node = current_node.next
            current_node.next = prev_visited
            prev_visited = current_node

            current_node = next_node

        self.tail = current_node


    def isempty(self):
        return self._n == 0


    def getnode(self, index):
        """get Node from the Linked List using 0 indexing"""
        if index < 0:
            index += self._n
        if index < 0 or index >= self._n:
            raise IndexError("Index out of range")

        current_node = self.tail.next
        current_index = 0

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node


    def __getitem__(self, key, node=False):
        """get data from the Linked List using indexing and slicing"""
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

        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return [self.getnode(k).data for k in range(start, stop, step)]


    def __iter__(self):
        """Iterator for the CircularLinkedList object"""
        if self.isempty():
            return None

        current_node = self.tail.next
        for _ in range(self._n):
            yield current_node.data
            current_node = current_node.next


    def __repr__(self):
        """Representation of a CircularLinkedList object"""
        if not self._n: return "CircularLinkedList()"
        values = map(str, self.tolist())
        return f"CircularLinkedList({" -> ".join(values)}" + " -> ...)"


    def __len__(self):
        """Get the length of the Circular Linked List"""
        return self._n

    size = __len__
