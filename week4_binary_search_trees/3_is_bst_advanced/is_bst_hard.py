#!/usr/bin/python3

import sys
import threading
from typing import List

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Solver2:
    MIN = int(-10E16)
    MAX = int(10E16)

    def __init__(self, n: int, tree: List[List[int]]) -> None:
        self._n = n
        self._keys = [0 for _ in range(n)]
        self._left = [-1 for _ in range(n)]
        self._right = [-1 for _ in range(n)]
        self._max_vals = [self.MIN for _ in range(n)]  # the max of subtree-i
        self._min_vals = [self.MAX for _ in range(n)]  # the min of subtree-i

        for i, item in enumerate(tree):
            self._keys[i] = item[0]
            self._left[i] = item[1]
            self._right[i] = item[2]

    def is_bst(self) -> bool:
        if self._n == 0:
            return True
        return self._is_valid(0, self.MIN, self.MAX, False)

    def _is_valid_int(self, root: int, low: int, high: int) -> bool:
        """
        Only works for int keys.
        """
        if root == -1:
            return True
        key_val = self._keys[root]
        if key_val < low or key_val > high:
            return False
        return self._is_valid_int(self._left[root], low, key_val-1) and self._is_valid_int(
            self._right[root], key_val, high)

    def _is_valid(self, root: int, low: int, high: int, is_left: bool) -> bool:
        """
        Works for keys that support comparison.

        Args:
            root: root index.

            low: valid lower bound.

            high: valid upper bound.

            is_left: is the current node the left child of its parent. It does not matter
            for the root.
        """
        if root == -1:
            return True
        key_val = self._keys[root]
        if is_left:
            # current node is left child
            if key_val < low or key_val >= high:
                return False
        else:
            if key_val < low or key_val > high:
                return False
        return self._is_valid(self._left[root], low, key_val, True) and self._is_valid(
            self._right[root], key_val, high, False)


class Solver:
    """
    Check if the given binary tree satisfies the following requirements:
        1. The left child is smaller than the root.
        2. The right child is equal or greater than the root.
    """
    MIN = int(-10E16)
    MAX = int(10E16)

    def __init__(self, n: int, tree: List[List[int]]) -> None:
        self._n = n
        self._keys = [0 for _ in range(n)]
        self._left = [-1 for _ in range(n)]
        self._right = [-1 for _ in range(n)]
        self._max_vals = [self.MIN for _ in range(n)]  # the max of subtree-i
        self._min_vals = [self.MAX for _ in range(n)]  # the min of subtree-i

        for i, item in enumerate(tree):
            self._keys[i] = item[0]
            self._left[i] = item[1]
            self._right[i] = item[2]

    def is_bst(self) -> bool:
        if self._n == 0:
            return True
        return self._is_valid(0)

    def _is_valid(self, root: int) -> bool:
        """
        Internal function to check if the binary tree complies the requirements.
        """
        if root == -1:
            return True

        is_valid_left = self._is_valid(self._left[root])
        if not is_valid_left:
            return False
        is_valid_right = self._is_valid(self._right[root])
        if not is_valid_right:
            return False

        key_val = self._keys[root]
        left_max = self._max(self._left[root])
        if key_val <= left_max:
            return False
        right_min = self._min(self._right[root])
        if key_val > right_min:
            return False

        return True

    def _max(self, root: int) -> int:
        if self._max_vals[root] != self.MIN:
            return self._max_vals[root]

        if root == -1:
            return self.MIN
        key_val = self._keys[root]
        left_max = self._max(self._left[root])
        right_max = self._max(self._right[root])

        self._max_vals[root] = max([key_val, left_max, right_max])
        return self._max_vals[root]

    def _min(self, root: int) -> int:
        if self._min_vals[root] != self.MAX:
            return self._min_vals[root]

        if root == -1:
            return self.MAX
        key_val = self._keys[root]
        left_min = self._min(self._left[root])
        right_min = self._min(self._right[root])

        self._min_vals[root] = min([key_val, left_min, right_min])
        return self._min_vals[root]


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    solver = Solver2(nodes, tree)
    if solver.is_bst():
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == '__main__':
    threading.Thread(target=main).start()
