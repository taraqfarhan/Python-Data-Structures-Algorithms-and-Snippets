import collections

class BinarySearchTree:
    class Node:
        """A node in a binary search tree contains a data value and references to its left and right children."""
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
        
        def __repr__(self):
            return f"Node(data={self.data}, left={self.left}, right={self.right})"

    def __init__(self, rootval):
        """Initialize the binary search tree with a root value. 
        The root node is created with the given value, and the size of the tree is set to 1."""
        self.root = self.Node(rootval)
        self._n = 1

    def insert(self, data):
        """Insert a specific value in the Binary Search Tree.
        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        There must be no duplicate nodes."""
        return self._insert(self.root, data) # start inserting from the root node

    def contains(self, target):
        """Search for a target value in the Binary Search Tree.
        Returns True if the target value is found in the tree, and False otherwise."""
        return self._contains(self.root, target) # start searching from the root node

    def preorder(self):
        """Pre-order traversal: node.data -> left.data -> right.data"""
        return self._preorder(self.root) # start pre-order traversal from the root node

    def inorder(self):
        """In-order traversal: left.data -> node.data -> right.data"""
        return self._inorder(self.root) # start in-order traversal from the root node

    def postorder(self):
        """Post-order traversal: left.data -> right.data -> node.data"""
        return self._postorder(self.root) # start post-order traversal from the root node

    def levelorder(self): 
        """Level-order traversal (Breadth First Search): visit nodes level by level from left to right"""
        return self._levelorder(self.root) # start level-order traversal from the root node


    def _insert(self, node, data):
        """
        Insert a specific value in the Binary Search Tree
        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        There must be no duplicate nodes.
        
        Time complexity: O(h), where h is the height of the tree.
        In the worst case (when the tree is skewed), h can be equal to n,
        making the time complexity O(n).
        
        In the best case (when the tree is balanced), h is log(n),
        making the time complexity O(log n).
        """
        if data < node.data: # go to the left subtree (smaller values)
            if node.left is None: # if the left child is empty, insert the new node here
                node.left = self.Node(data) # create a new node and assign it to the left child of the current node
                self._n += 1
                return node.left # return the newly inserted node
            self._insert(node.left, data) # otherwise, continue searching in the left subtree
        elif data > node.data: # go to the right subtree (larger values)
            if node.right is None: # if the right child is empty, insert the new node here
                node.right = self.Node(data)  # create a new node and assign it to the right child of the current node
                self._n += 1
                return node.right # return the newly inserted node
            self._insert(node.right, data) # otherwise, continue searching in the right subtree


    def _contains(self, node, target):
        """Search for a target value in the Binary Search Tree"""
        if node is None: # if we reach a leaf node and haven't found the target, it means the target is not in the tree
            return False 
        if target == node.data: # if we find the target value, return True
            return True
        if target < node.data: # if the target value is smaller than the current node's value, search in the left subtree
            return self._contains(node.left, target)
        return self._contains(node.right, target) # if the target value is larger than the current node's value, search in the right subtree


    def _preorder(self, node):
        """Pre-order traversing. node.data -> left.data -> right.data"""
        if node is None: # if we reach a leaf node, we return to the previous level of the tree
            return
        # visit the current node first (pre-order), then recursively visit the left and right subtrees
        print(node.data)
        self._preorder(node.left)
        self._preorder(node.right)


    def _inorder(self, node):
        """In-order traversing. left.data -> node.data -> right.data"""
        if node is None: # if we reach a leaf node, we return to the previous level of the tree
            return
        # recursively visit the left subtree first (in-order), then visit the current node, and finally recursively visit the right subtree
        self._inorder(node.left)
        print(node.data)
        self._inorder(node.right)


    def _postorder(self, node):
        """Post-order traversing. left.data -> right.data -> node.data"""
        if node is None: # if we reach a leaf node, we return to the previous level of the tree
            return
        # recursively visit the left and right subtrees first (post-order), and then visit the current node
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.data)


    def _levelorder(self, root):
        """Breadth First Search traversal"""
        if root is None: # if the tree is empty, there are no nodes to traverse, so we simply
            return
        # Because we want to visit nodes level by level, 
        # and a queue allows us to keep track of the nodes we need to visit next in the correct order (first-in, first-out).
        queue = collections.deque([root]) # initialize a queue with the root node to start the level-order traversal
        while queue: # continue traversing until the queue is empty (i.e., we have visited all nodes in the tree)
            node = queue.popleft() # remove and return the leftmost node from the queue (the next node to visit in level-order)
            print(node.data) # visit the current node (print its data value)
            if node.left: # if the current node has a left child, add it to the queue to be visited later
                queue.append(node.left)
            if node.right: # if the current node has a right child, add it to the queue to be visited later
                queue.append(node.right)
                
                
    def __len__(self):
        return self._n
    size = __len__
    
    
    def __repr__(self):
        return f"BinarySearchTree(root={self.root.data}, size={self._n})"
    
    
    def __iter__(self):
        """In-order traversal iterator"""
        stack = []
        current = self.root
        while stack or current: # continue traversing until we have visited all nodes (i.e., the stack is empty and there are no more nodes to visit)
            # We go as far left as possible, pushing each node onto the stack as we go.
            while current:
                stack.append(current)
                current = current.left
            # Once we reach a leaf node (where current is None), we pop the last node from the stack, visit it (yield its data value), 
            # and then move to its right child to continue the traversal.    
            current = stack.pop()
            yield current.data
            current = current.right