"""
Use a standard binary search tree to implement a symbol table that supports
the following operations:
    - add a key.
    - delete a key.
    - find a key.
    - sum all the elements in the tree within the given range.
"""

from typing import List


class Node:
    """
    Basic element in the binary tree.
    """

    def __init__(self, key, left=None, right=None):
        self._key = key
        self._left = left
        self._right = right

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value


class BST:

    def __init__(self, root: Node):
        self._root = root

    def add(self, node: Node) -> None:
        pass

    def find(self, key: int) -> bool:
        """
        Public method to check if a key is in the BST.
        """
        return self._find(self._root, key)

    def _find(self, node: Node, key: int) -> bool:
        """
        Internal function to find the given key the BST.
        """
        if node == None:
            return False
        elif key < node.key:
            self._find(node.right, key)
        elif key > node.key:
            self._find(node.left, key)
        return True
