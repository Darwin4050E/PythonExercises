"""Solution to binary_search_tree exercise.
"""

class TreeNode:
    """ Create a TreeNode object with initial data and optional left and right nodes.

    Attributes
    ----------
    data: str - number.
    left: TreeNode - left node.
    right: TreeNode - right node.
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    """Create a BinarySearchTree object with initial data.

    Attributes
    ----------
    root: TreeNode - binary search tree root.

    Methods
    -------
    insert(data, node): inserts data.
    data(): returns the binary search tree root.
    iterate_binary_tree(): travels the tree in this order: left, in, right.
    sorted_data(): returns a sorted list with all elements of the tree.
    """

    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
            self.root = self.insert(data, self.root)

    def insert(self, data, node):
        """Insert data"""
        if not node:
            return TreeNode(data)
        if int(data) <= int(node.data):
            node.left = self.insert(data, node.left)
        if int(data) > int(node.data):
            node.right = self.insert(data, node.right)
        return node

    def data(self):
        """Return the binary search tree root."""
        return self.root
    
    def iterate_binary_tree(self, node, list):
        """Travel the tree in this order: left, in, right."""
        if not node:
            return list
        if node.left:
            self.iterate_binary_tree(node.left, list)
        list.extend(node.data)
        if node.right:
            self.iterate_binary_tree(node.right, list)

    def sorted_data(self):
        """Return a sorted list with all elements of the tree."""
        result = []
        self.iterate_binary_tree(self.root, result)
        return result
    