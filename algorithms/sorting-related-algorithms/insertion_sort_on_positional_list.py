def insertion_sort(positional_list):
    """
    We maintain a variable named `marker` that represents the rightmost position of
    the currently sorted portion of a list.

    During each pass, we consider the position just
    past the marker as the `pivot` and consider where the pivot's element belongs relative
    to the sorted portion

    we use another variable, named `walk`, to move leftward from
    the marker, as long as there remains a preceding element with value larger than the pivot's
    """

    if len(positional_list) <= 1:   # already sorted
        return positional_list

    marker = positional_list.first()   # start from the first element
    while marker != positional_list.last():
        # pivot is the next item to the marker
        pivot = positional_list.after(marker)
        value = pivot.getdata()
        if value > marker.getdata():   # pivot is already sorted
            marker = pivot    # move to the next node
        else:    # pivot is not sorted, we need to relocate the pivot into it's correct position
            walk = marker
            # find leftmost node greater than pivot's `value`
            while walk != positional_list.first() and positional_list.before(walk).getdata() > value:
                walk = positional_list.before(walk)

            # relocate pivot
            positional_list.add_before(walk, value)
            positional_list.delete(pivot)


# IMPLEMENTATION OF A POSITIONAL LIST
# ==== == == == == == == == == ==== == == == == == == == == ==== == == == == == == == == ==== == == == == == == == == ==


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


    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor._getdata()
            cursor = self.after(cursor)


    def __repr__(self):
        """Representation of a Postional List object"""
        sep = ' \u21cc '
        return f"PositionalList({sep.join(map(str, self))})"
