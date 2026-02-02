import collections
class BinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            
        def __repr__(self):
            return f"Node({self.data})"

    def __init__(self, rootval):
        self.root = self.Node(rootval)
        self._n = 1

    def preorder(self):
        return self._preorder(self.root)

    def inorder(self):
        return self._inorder(self.root)

    def postorder(self):
        return self._postorder(self.root)

    def levelorder(self):
        return self._levelorder(self.root)

    def insert(self, data):
        return self._insert(self.root, data)

    def iscomplete(self):
        """Check if the binary tree is complete. 
        A complete binary tree is a binary tree in which all the levels are completely filled 
        except possibly the last level, and the last level has all keys as left as possible."""
        if self.root is None:
            return True
        queue = collections.deque([self.root])
        end = False # flag to indicate if we have encountered a non-full node
        while queue:
            node = queue.popleft()
            if node.left:
                if end: # if we have already encountered a non-full node, then the tree cannot be complete
                    return False
                queue.append(node.left)
            else: # if we encounter a non-full node, we set the end flag to True
                end = True
            if node.right:
                if end: # if we have already encountered a non-full node, then the tree cannot be complete
                    return False
                queue.append(node.right)
            else: # if we encounter a non-full node, we set the end flag to True
                end = True
        return True
    
    
    def isfull(self):        
        """Check if the binary tree is full. A full binary tree is a binary tree in which every node other than the leaves has two children."""
        if self.root is None:
            return True
        queue = collections.deque([self.root])
        while queue:
            node = queue.popleft()
            if (node.left is None) != (node.right is None): # if a node has only one child, then the tree cannot be full
                return False
            if node.left: # if the node has a left child, it must also have a right child (since it's a full binary tree)
                queue.append(node.left)
            if node.right: # if the node has a right child, it must also have a left child (since it's a full binary tree)
                queue.append(node.right)
        return True
    
    
    def isperfect(self):
        """Check if the binary tree is perfect. A perfect binary tree is a binary tree in which all the internal nodes have two children and all the leaves are at the same level."""
        if self.root is None:
            return True
        queue = collections.deque([(self.root, 0)]) # we use a queue to perform a level-order traversal, and we keep track of the current level of each node
        leaf_level = None # variable to store the level of the first leaf node we encounter
        while queue:
            node, level = queue.popleft()
            if node.left is None and node.right is None: # if we encounter a leaf node
                if leaf_level is None: # if this is the first leaf node we encounter, we set the leaf_level variable to its level
                    leaf_level = level
                elif level != leaf_level: # if we encounter another leaf node at a different level, then the tree cannot be perfect
                    return False
            else: # if it's not a leaf node, it must have both left and right children (since it's a perfect binary tree)
                if node.left is None or node.right is None: # if it has only one child, then the tree cannot be perfect
                    return False
                queue.append((node.left, level + 1)) # add the left child to the queue with an incremented level
                queue.append((node.right, level + 1)) # add the right child to the queue with an incremented level
        return True
    
    
    def iscompletefull(self):
        """Check if the binary tree is complete and full. A complete and full binary tree is a binary tree that is both complete and full."""
        return self.iscomplete() and self.isfull()
    
    
    def height(self):
        """Calculate the height of the binary tree. The height of a binary tree is the number of edges on the longest path from the root to a leaf node."""
        if self.root is None:
            return -1 # the height of an empty tree is defined as -1
        queue = collections.deque([(self.root, 0)]) # we use a queue to perform a level-order traversal, and we keep track of the current height at each level
        max_height = 0
        while queue:
            node, height = queue.popleft()
            max_height = max(max_height, height) # update the maximum height encountered so far
            if node.left:
                queue.append((node.left, height + 1)) # if the node has a left child, we add it to the queue with an incremented height
            if node.right:
                queue.append((node.right, height + 1)) # if the node has a right child, we add it to the queue with an incremented height
        return max_height
    

    def _insert(self, root, data):
        """Insert a specific value in the Binary Tree"""
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left is None:
                node.left = self.Node(data)
                self._n += 1
                return node.left
            else:
                queue.append(node.left)
                
            if node.right is None:
                node.right = self.Node(data)
                self._n += 1
                return node.right
            else:
                queue.append(node.right)


    def _preorder(self, node):
        """Pre-order traversing. node.data -> left.data -> right.data"""
        if node is None:
            return
        print(node.data)
        self._preorder(node.left)
        self._preorder(node.right)


    def _inorder(self, node):
        """In-order traversing. left.data -> node.data -> right.data"""
        if node is None:
            return
        self._inorder(node.left)
        print(node.data)
        self._inorder(node.right)


    def _postorder(self, node):
        """Post-order traversing. left.data -> right.data -> node.data"""
        if node is None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.data)


    def _levelorder(self, root):
        """Breadth First Search in the Binary Tree"""
        if root is None:
            return
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            print(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
    def __len__(self):
        return self._n
    size = __len__

    def __repr__(self):
        return f"BinaryTree(root={self.root.data}, size={self._n})"