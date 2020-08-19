#!/usr/bin/python3

import sys
import threading
from typing import List

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Solver:
    """
    Check if a binary tree is a binary search tree.

    Args:
        n (int): number of nodes.

        tree (list): tree structure.
    """

    def __init__(self, n: int, tree: List[List[int]]) -> None:
        self._n = n
        self._keys = [0 for _ in range(n)]
        self._left = [-1 for _ in range(n)]
        self._right = [-1 for _ in range(n)]

        for i, item in enumerate(tree):
            self._keys[i] = item[0]
            self._left[i] = item[1]
            self._right[i] = item[2]

    def is_binary_tree(self) -> bool:
        if self._n == 0:
            # empty tree is considered a BST.
            return True
        res: List[int] = []
        self._in_order_traversal(0, res)

        for i in range(self._n - 1):
            if res[i] > res[i+1]:
                return False
        return True

    def _in_order_traversal(self, root: int, res: List[int]) -> None:
        """
        Internal function to perform in-order traversal in the tree.
        """
        if root == -1:
            return
        self._in_order_traversal(self._left[root], res)
        res.append(self._keys[root])
        self._in_order_traversal(self._right[root], res)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    solver = Solver(nodes, tree)
    if solver.is_binary_tree():
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == '__main__':
    threading.Thread(target=main).start()
