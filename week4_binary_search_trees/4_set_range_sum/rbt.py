"""
Implementation of Red-Black Tree
"""
from sys import stdin
import sys
import threading
from typing import Union, List, Any
from enum import Enum
from bst import Node, BST, Color, ColorNode, Client
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class RBT(BST):
    """
    Implementation of red-black tree. The tree obeys the following restrictions:
        1. the red edge is always leaning towards the left.
        2. a parent node can at most have one red child edge.
    """

    def __init__(self, root: ColorNode):
        self._root = root

    def _rotate_left(self, node: ColorNode) -> ColorNode:
        """
        The node's right child is red. Perform left-rotation to comply red-left-leaning rule.
        """
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _rotate_right(self, node: ColorNode) -> ColorNode:
        """
        The node's left child is red. Perform right-rotation to make the node's right child red.
        """
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = Color.RED
        return x

    def _flip_color(self, node: ColorNode) -> None:
        """
        Flip the color of the node and its children.
        """
        if node.color == Color.RED:
            node.color = Color.BLACK
        else:
            node.color = Color.RED

        if node.left.color == Color.RED:
            node.left.color = Color.BLACK
        else:
            node.left.color = Color.RED

        if node.right.color == Color.RED:
            node.right.color = Color.BLACK
        else:
            node.right.color = Color.RED

    def _is_red(self, node: ColorNode) -> bool:
        """
        Check is a node is red. If it's None, return False
        """
        if node == None:
            return False
        return node.color == Color.RED

    def add(self, val: int) -> None:
        """
        Add a new key to RBT.
        """
        self._root = self._add(self._root, val)
        self._root.color = Color.BLACK

    def _add(self, node: ColorNode, val: int) -> ColorNode:
        """
        Overwrite BST's _add method with ColorNode.
        """
        if node == None:
            # Always set the newly added color to RED, then use the
            # operations to maintain the restrictions. Think about how a
            # new node is added in a 2-3 tree helps.
            return ColorNode(val, color=Color.RED)
        if val < node.val:
            node.left = self._add(node._left, val)
        elif val > node.val:
            node.right = self._add(node._right, val)

        # maintain red-black rules. See Algorithms page 438 for details.
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_color(node)

        return node

    def _balance(self, node: ColorNode) -> ColorNode:
        """
        Maintain the invariant in the RBT.
        """
        if self._is_red(node.right):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_color(node)
        return node

    def _move_red_left(self, node: ColorNode) -> ColorNode:
        """
        Assume that node is red and both node.left and node.left.left are black.
        Make node.left or one of its children red.
        """
        self._flip_color(node)
        if self._is_red(node.right.left):
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
            self._flip_color(node)
        return node

    def _del_min(self, node: ColorNode) -> Union[ColorNode, None]:
        """
        Private method to delete the minimum key in the tree.
        """
        if node.left == None:
            return None
        if (not self._is_red(node.left)) and (not self._is_red(node.left.left)):
            node = self._move_red_left(node)
        node.left = self._del_min(node.left)
        return self._balance(node)

    def del_min(self) -> None:
        """
        Public method to delete the minimum key in the tree.
        """
        if (not self._is_red(self._root.left)) and (not self._is_red(self._root.right)):
            self._root.color = Color.RED
        self._root = self._del_min(self._root)
        if self._root:
            self._root.color = Color.BLACK

    def _move_red_right(self, node: ColorNode) -> ColorNode:
        """
        Assuming that node is red and both node.right and node.right.left are black,
        make node.right or one of its children red.
        """
        self._flip_color(node)
        if self._is_red(node.left.left):
            node = self._rotate_right(node)
            self._flip_color(node)
        return node

    def _del_max(self, node: ColorNode) -> None:
        if self._is_red(node.left):
            node = self._rotate_right(node)
        if node.right == None:
            return None
        if (not self._is_red(node.right)) and (not self._is_red(node.right.left)):
            node = self._move_red_right(node)
        node.right = self._del_max(node.right)
        return self._balance(node)

    def del_max(self) -> None:
        if (not self._is_red(self._root.left)) and (not self._is_red(self._root.right)):
            self._root.color = Color.RED
        self._root = self._del_max(self._root)
        if self._root:
            self._root.color = Color.BLACK

    def delete(self, val: int) -> None:
        """
        Public method to delete a node with the given value from the tree.
        """
        # make sure the element exist before deleting.
        # This simplifies _delete method for edge cases.
        if not self.find(val):
            return
        if (not self._is_red(self._root.left)) and (not self._is_red(self._root.right)):
            self._root.color = Color.RED
        self._root = self._delete(self._root, val)
        if self._root:
            self._root.color = Color.BLACK

    def _delete(self, node: ColorNode, val: int) -> Union[ColorNode, None]:
        """
        Private method to delete a node with the given value from the substree specified by node.
        """
        if val < node.val:
            if (not self._is_red(node.left)) and (not self._is_red(node.left.left)):
                node = self._move_red_left(node)
            node.left = self._delete(node.left, val)

        else:
            if self._is_red(node.left):
                node = self._rotate_right(node)
            if val == node.val and node.right == None:
                return None
            if (not self._is_red(node.right)) and (not self._is_red(node.right.left)):
                node = self._move_red_right(node)
            if val == node.val:
                x = self._min(node.right)
                node.val = x.val
                node.right = self._del_min(node.right)
            else:
                node.right = self._delete(node.right, val)

        return self._balance(node)


def main():
    n = int(stdin.readline())

    client = Client(bst=RBT(None))
    for _ in range(n):
        query = stdin.readline()
        client.request(query)


if __name__ == '__main__':
    threading.Thread(target=main).start()
