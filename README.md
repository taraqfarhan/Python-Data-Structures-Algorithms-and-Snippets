# Python Data Structures, Algorithms & Snippets

A personal collection of classical algorithms and data structures implemented in Python — built for learning.

---

## Repository Structure

```
Python-Data-Structures-and-Algorithms
├── algorithms/
│   ├── array-related-algorithms/
│   ├── backtracking/
│   ├── bit-manipulation/
│   ├── dynamic-programming/
│   ├── graph-algorithms/
│   ├── greedy-algorithms/
│   ├── linked-list-related-algorithms/
│   ├── searching-algorithms/
│   ├── shortest-path-algorithms/
│   ├── sorting-algorithms/
│   ├── string-algorithms/
│   └── tree-algorithms/
├── data-structures/
│   ├── linear/
│   │   ├── array/
│   │   ├── linked-list/
│   │   ├── queue/
│   │   └── stack/
│   └── non-linear/
│       ├── graph/
│       ├── map (dictionary)/
│       └── set/
└── snippets/
```

---

## Getting Started

Just clone the repo and run any file directly:

```bash
git clone https://github.com/taraqfarhan/Python-Data-Structures-And-Algorithms.git


# to play with a file interactively, use the `-i` flag
❯ python3 -i data-structures/linear/linked-list/doubly_linked_list.py
>>> d = DoublyLinkedList("ABCDE")
>>> d
DoublyLinkedList(A ⇌ B ⇌ C ⇌ D ⇌ E)
>>> d.reverse()
>>> d
DoublyLinkedList(E ⇌ D ⇌ C ⇌ B ⇌ A)


❯ python3 -i data-structures/linear/stack/static_stack.py
>>> s = Stack.from_iterable([1, 2, 3, 4, 5], 10)
>>> s.size(), s._capacity
(5, 10)


❯ python3 -i data-structures/linear/linked-list/circular_singly_linked_list.py
>>> c = CircularLinkedList("ABCDEF")
>>> d = CircularLinkedList("GH")
>>> c.extend(d)
>>> len(c)
8
>>> c
CircularLinkedList(A -> B -> C -> D -> E -> F -> G -> H -> ...)
>>> for i in range(len(c)):
...     c[i, True]
...
Node(A -> B)
Node(B -> C)
Node(C -> D)
Node(D -> E)
Node(E -> F)
Node(F -> G)
Node(G -> H)
Node(H -> A)
```

**Requirements:** Python 3.9+ — no external dependencies for core implementations.

---

## Notes

- All implementations are written from scratch for learning purposes.
- Where the same algorithm appears under multiple categories (e.g., `kadane.py`, `dijkstra.py`, `coin_change.py`), each version emphasises the paradigm of its category — compare them to see how the same problem can be framed differently.
