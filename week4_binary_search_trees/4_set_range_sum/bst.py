"""
Use a standard binary search tree to implement a symbol table that supports
the following operations:
    - add a key.
    - delete a key.
    - find a key.
    - sum all the elements in the tree within the given range.
"""

from sys import stdin
import sys
import threading
from enum import Enum
from typing import List, Any, Union
# from binarytree import Node
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    """
    Basic element in the binary tree.
    """

    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val = value

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


class Color(Enum):
    RED = True
    BLACK = False


class ColorNode(Node):
    """
    Node with color. The color is defined by the connected edge.
    """

    def __init__(self, val, left=None, right=None, color=Color.BLACK):
        super().__init__(val, left, right)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val: Color):
        self._color = val


class BST:

    def __init__(self, root: Union[Node, ColorNode]):
        self._root = root

    @property
    def root(self):
        return self._root

    def find(self, val: int) -> bool:
        """
        Public method to check if a val is in the BST.
        """
        return self._find(self._root, val)

    def _find(self, node: Union[Node, ColorNode], val: int) -> bool:
        """
        Internal function to find the given val the BST.
        """
        if node == None:
            return False
        elif val < node.val:
            return self._find(node.left, val)
        elif val > node.val:
            return self._find(node.right, val)
        return True

    def add(self, val: int) -> None:
        """
        Public method to add a val to BST.
        """
        self._root = self._add(self._root, val)

    def _add(self, node: Union[Node, ColorNode], val: int) -> Union[Node, ColorNode]:
        """
        Private method to add a new val to the BST specified by node.
        """
        if node == None:
            return Node(val)
        elif val > node.val:
            node.right = self._add(node.right, val)
        elif val < node.val:
            node.left = self._add(node.left, val)

        return node

    def del_min(self) -> None:
        """
        Public method to delete the minimum val in the tree.
        """
        self._root = self._del_min(self._root)

    def _del_min(self, node: Union[Node, ColorNode]) -> Union[Node, ColorNode]:
        """
        Private method to delete the minimum val in the BST.
        """
        if node == None:
            return node
        elif node.left == None:
            return node.right
        node.left = self._del_min(node.left)
        return node

    def del_max(self) -> None:
        """
        Public method to delete the maximum val in the tree.
        """
        self._root = self._del_max(self._root)

    def _del_max(self, node: Union[Node, ColorNode]) -> Union[Node, ColorNode]:
        """
        Private method to delete the maximum val in the tree.
        """
        if node == None:
            return node
        elif node.right == None:
            return node.left
        node.right = self._del_max(node.right)
        return node

    def min(self) -> Union[Node, ColorNode]:
        return self._min(self._root)

    def _min(self, node: Union[Node, ColorNode]) -> Union[Node, ColorNode]:
        if node == None or node.left == None:
            return node
        return self._min(node.left)

    def delete(self, val: int) -> None:
        """
        Public method to delete a val in the BST.
        """
        self._root = self._delete(self._root, val)

    def _delete(self, node: Union[Node, ColorNode], val: int) -> Union[Node, ColorNode]:
        """
        Private method to delete a val in the tree
        """
        if node == None:
            return node
        elif val > node.val:
            node.right = self._delete(node.right, val)
        elif val < node.val:
            node.left = self._delete(node.left, val)
        else:
            # found the val
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                # both left and right child are not empty. Substitute the delete val
                # with its successor (the smallest val that is greater than val)
                s = self._min(node.right)  # s.left == None is always true
                # attach the substree (without the successor) to the successor's right
                s.right = self._del_min(node.right)
                s.left = node.left
                return s
        return node

    def get_range(self, low: int, high: int) -> List[int]:
        """
        Return all the keys that is between low and high (inclusive).
        """
        res: List[int] = []
        self._get_range(self._root, low, high, res)

        return res

    def _get_range(self, node: Union[Node, ColorNode], low: int, high: int, q: List[int]) -> None:
        """
        Private method to get the values in the tree that are between low and high.
        """
        if node == None:
            return
        val = node.val
        if val < low:
            # key is less than the lower bound, search right substree.
            self._get_range(node.right, low, high, q)
        elif val > high:
            self._get_range(node.left, low, high, q)
        else:
            self._get_range(node.left, low, high, q)
            q.append(val)
            self._get_range(node.right, low, high, q)

    def range_sum(self, low: int, high: int) -> int:
        """
        Return the sum of all the keys between low and high (both inclusive)
        """
        return sum(self.get_range(low, high))


class Client:
    """
    Object used to handle the queries in this problem.
    """
    MODULO = 1000000001

    def __init__(self, bst=BST(None)):
        self._bst = bst
        self._last_sum_result = 0

    def request(self, query: str):
        q = query.split()
        if q[0] == '+':
            x = int(q[1])
            self._bst.add((x + self._last_sum_result) % self.MODULO)
        elif q[0] == '-':
            x = int(q[1])
            self._bst.delete((x + self._last_sum_result) % self.MODULO)
        elif q[0] == '?':
            x = int(q[1])
            if self._bst.find((x + self._last_sum_result) % self.MODULO):
                print('Found')
            else:
                print('Not found')
        else:
            low = (int(q[1]) + self._last_sum_result) % self.MODULO
            high = (int(q[2]) + self._last_sum_result) % self.MODULO
            res = self._bst.range_sum(low, high)
            self._last_sum_result = res
            print(res)

    def request_from_file(self, query: str) -> Any:
        q = query.split()
        if q[0] == '+':
            x = int(q[1])
            self._bst.add((x + self._last_sum_result) % self.MODULO)
        elif q[0] == '-':
            x = int(q[1])
            self._bst.delete((x + self._last_sum_result) % self.MODULO)
        elif q[0] == '?':
            x = int(q[1])
            if self._bst.find((x + self._last_sum_result) % self.MODULO):
                return 'Found'
            else:
                return 'Not found'
        else:
            low = (int(q[1]) + self._last_sum_result) % self.MODULO
            high = (int(q[2]) + self._last_sum_result) % self.MODULO
            res = self._bst.range_sum(low, high)
            self._last_sum_result = res
            return res


def main():
    n = int(stdin.readline())

    client = Client()
    for _ in range(n):
        query = stdin.readline()
        client.request(query)


if __name__ == '__main__':
    threading.Thread(target=main).start()
