"""
A positional linked list that uses a doubly linked list with sentinels (header, trailer) under the hood.
We can insert and delete any node in any position from the list in constant time O(1)
if we know the reference of the node. To store that reference we have a Position object
for each node in the list.
"""

class PositionalList:
    """A sequential container whose elements can be accessed by Position."""

    class _Node:
        """Doubly-linked node."""
        def __init__(self, data, prev, next):
            self.data = data
            self.prev = prev   # previous node reference
            self.next = next  # next node reference

        def __repr__(self):
            """Representation of a Node object"""
            return f"Node({self.prev.data} <- {self.data} -> {self.next.data})"


    class Position:
        """
        An abstraction representing the location of a single element.
        Holds a direct reference to the underlying node.
        """
        def __init__(self, container, node):
            self._container = container   # used for validation
            self._node = node        # O(1) access to the node

        def _getdata(self):
            return self._node.data

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

        def __repr__(self):
            """Representation of a Position object"""
            return f"Position({self._container}, {self._node})"


    def __init__(self, positional_list=None):
        # Two sentinel nodes — they never hold real data but eliminate
        # all edge cases (empty list, insert at ends, etc.)
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._n = 0   # total nodes
        if positional_list is not None:
            for data in positional_list:
                self.append(data)


    def _getnode(self, p):
        """Return the node at Position p, or raise an error."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.next is None:          # convention: deprecated nodes have next=None
            raise ValueError('p is no longer valid')
        return p._node


    def _make_position(self, node):
        """Return Position for given node (or None for sentinel nodes)."""
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)


    def _insert_between(self, data, predecessor, successor):
        """Add element `data` between two existing nodes and return new Position."""
        node = self._Node(data, predecessor, successor)
        predecessor.next = node
        successor.prev = node
        self._n += 1
        return self._make_position(node)


    def _delete_node(self, node):
        """Delete a non-sentinel node and return its element."""
        value = node.data

        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor

        node.prev = node.next = node.data = None   # deprecate node

        self._n -= 1
        return value


    def __len__(self):
        return self._n
    size = __len__


    def isempty(self):
        return self._n == 0


    def first(self):
        """Return Position of the first element (or None if empty)."""
        return self._make_position(self._header.next)


    def last(self):
        """Return Position of the last element (or None if empty)."""
        return self._make_position(self._trailer.prev)


    def before(self, p):
        """Return Position just before p (or None if p is first)."""
        node = self._getnode(p)
        return self._make_position(node.prev)


    def after(self, p):
        """Return Position just after p (or None if p is last)."""
        node = self._getnode(p)
        return self._make_position(node.next)


    def add_first(self, e):
        """Insert element e at the front and return its new Position. O(1)."""
        return self._insert_between(e, self._header, self._header.next)
    appendleft = add_first


    def add_last(self, e):
        """Insert element e at the back and return its new Position. O(1)."""
        return self._insert_between(e, self._trailer.prev, self._trailer)
    append = add_last


    def add_before(self, p, e):
        """Insert element e before Position p and return its Position. O(1)."""
        node = self._getnode(p)
        return self._insert_between(e, node.prev, node)


    def add_after(self, p, e):
        """Insert element e after Position p and return its Position. O(1)."""
        node = self._getnode(p)
        return self._insert_between(e, node, node.next)


    def delete(self, p):
        """Remove and return the element at Position p. O(1)."""
        node = self._getnode(p)
        return self._delete_node(node)


    def pop(self):
        """Pop the last element"""
        if self.isempty():
            raise ValueError("Positional List is empty")
        return self.delete(self.last())


    def popleft(self):
        """Pop the first element"""
        if self.isempty():
            raise ValueError("Positional List is empty")
        return self.delete(self.first())


    def replace(self, p, e):
        """Replace element at Position p with e; return the old element. O(1)."""
        node = self._getnode(p)
        value  = node.data
        node.data = e
        return value


    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor._getdata()
            cursor = self.after(cursor)


    def __repr__(self):
        """Representation of a Postional List object"""
        sep = ' \u21cc '
        return f"PositionalList({sep.join(map(str, self))})"


    def tolist(self):
        return list(self)


    """if we want indexing, we can't access the items in O(1),
    rather the time complexity will be O(n)
    """

    def getnodebyindex(self, index):
        """get Node from the Linked List using 0 indexing"""
        if index < 0:
            index += self._n
        if index < 0 or index >= self._n:
            raise IndexError("Index out of range")

        if index <= self._n // 2:
            current_node = self._header.next
            current_index = 0

            while current_node.next is not None and current_index != index:
                current_node = current_node.next
                current_index += 1
        else:
            current_node = self._trailer.prev
            current_index = self._n - 1

            while current_node is not None and current_index != index:
                current_node = current_node.prev
                current_index -= 1

        return current_node


    def __getitem__(self, key, node=False):
        """get data from the Linked List using indexing and slicing"""
        # Supporting PositionalList[2]
        # And Supporting PositionalList[2, True]
        # We can achieve the same using PositionalList.__getitem__(2, True)
        if isinstance(key, (int, tuple)):
            if isinstance(key, tuple): key, node = key
            if key < 0:
                key += self._n    # handle negative index
            if key < 0 or key >= self._n:
                raise IndexError("Linked List index out of range")

            curr_node = self.getnodebyindex(key)   # get the node at that index
            if curr_node:
                if node: return curr_node    # if node exits and `node` argument is True, return that node
                return curr_node.data   # else return the data

        # Supporting PositionalList[2:3:2]
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return [self.getnodebyindex(k).data for k in range(start, stop, step)]
