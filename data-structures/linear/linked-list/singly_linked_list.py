class SinglyLinkedList:
    class Node:
        """each Node of a Linked List structure"""
        # Each Node has a data and a pointer to the next Node
        def __init__(self, data, next=None):
            self.data = data # data stored in the current Node

            # each Node points to the next Node of the Linked List
            # if there is no Node after current Node then next points to None
            self.next = next


        def __repr__(self):
            """Represenattion of a Node object"""
            if self.next is None:
                return f"Node({self.data} -> {None})"
            return f"Node({self.data} -> {self.next.data})"


    # Each Linked List has a head pointer
    # which points to the head (first Node) of the Linked List
    # If there is no Node (the linked list is empty)
    # then head points to None
    def __init__(self, linkedlist=None):
        self.head = None  # the head pointer
        self._n = 0    # total nodes

        # SinglyLinkedList(['A', 'B', 'C', 'D']) to A -> B -> C -> D
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
        current_node = self.head
        new_node = self.Node(data)

        # case 1: the list is empty
        if current_node is None:
            self.head = new_node

        # case 2: the list has already one or more elements
        else:
            # while current_node is not the last node
            while current_node.next is not None:
                current_node = current_node.next

            # current_node is now the last node
            # link the new node from the last node
            current_node.next = new_node
        self._n += 1


    def appendleft(self, data):
        """append a new Node at the start of the Linked List"""
        new_node = self.Node(data)    # Create the new node
        new_node.next = self.head     # new_node points it to the old head
        self.head = new_node          # Make it the new head
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

        current_node = self.head
        current_index = 0
        new_node = self.Node(data)

        # traverse to the index `index - 1`
        while current_node is not None and current_index != (index-1):
            current_node = current_node.next
            current_index += 1

        # current_node is in the index `index - 1`
        if current_node is not None:
            old_node = current_node.next
            current_node.next = new_node
            new_node.next = old_node
        self._n += 1


    def extend(self, other):
        """extend current linked list with the items from another list in-place"""
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        # curr_node is the last node
        curr_node.next = other.head
        self._n += other._n


    def pop(self, index=None):
        """Pop an item from the list using indexing"""
        if self._n == 0:
            raise ValueError("Empty Linked List")

        if index is None or index >= self._n:   # default is the last item
            index = self._n - 1
        if index < 0:
            index += self._n
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            return self.popleft()

        current_index = 0
        current_node = self.head
        # traverse to the index `index - 1`
        while current_node is not None and current_index != (index - 1):
            current_node = current_node.next
            current_index += 1

        # current_node is in (index - 1)th position
        value = current_node.next.data
        current_node.next = current_node.next.next
        self._n -= 1
        return value


    def popleft(self):
        # Case 1: empty
        if self.head is None:
            raise ValueError("Empty Linked List")

        # Case 2: total nodes (>= 1)
        value = self.head.data
        self.head = self.head.next

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


    def tolist(self):
        """traverse the whole Linked List"""
        res = []
        current_node = self.head

        while current_node is not None:
            # yield current_node.data   # for a generator
            res.append(current_node.data)
            current_node = current_node.next
        return res


    def reverse(self):
        """reverse the actual linked list in place
        like from A -> B -> C -> D to A <- B <- C <- D"""
        prev_visited = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_visited
            prev_visited = current_node

            current_node = next_node

        self.head = prev_visited


    def getnode(self, index):
        """get Node from the Linked List using 0 indexing"""
        if index < 0:
            index += self._n
        if index < 0 or index >= self._n:
            raise IndexError("Index out of range")

        current_node = self.head
        current_index = 0

        while current_node is not None and current_index != index:
            current_node = current_node.next
            current_index += 1

        if current_node is not None:
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
        """Iterator for the SinglyLinkedList object"""
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


    def __repr__(self, verbose=False):
        """Representation of a SinglyLinkedList object"""
        if verbose:
            values = ["head"]
            values.extend(map(str, self.tolist()))
            values.append("None")
        else: values = map(str, self.tolist())
        return f"SinglyLinkedList({" -> ".join(values)})"


    def __len__(self):
        """Get the length of the Singly Linked List"""
        return self._n

    size = __len__
