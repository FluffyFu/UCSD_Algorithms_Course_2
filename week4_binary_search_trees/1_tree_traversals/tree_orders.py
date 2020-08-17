# python3

import sys
import threading
from typing import List, Tuple
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        """
        Read trees from stdin for online assessment.
        """
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def read_from_relations(self, n: int, relations: List[Tuple[int, int, int]]):
        """
        Read tree from the given input for unit tests.
        """
        self.n = n
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]

        for i, item in enumerate(relations):
            self.key[i] = item[0]
            self.left[i] = item[1]
            self.right[i] = item[2]

    def inOrder(self):
        self.result = []
        self._in_order(0)

        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._pre_order(0)

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._post_order(0)

        return self.result

    def _in_order(self, root: int) -> None:
        """
        Internal function to perform in-order traversal.
        """
        if root == -1:
            return
        self._in_order(self.left[root])
        self.result.append(self.key[root])
        self._in_order(self.right[root])

    def _pre_order(self, root: int) -> None:
        """
        Internal function to perform pre-order traversal.
        """
        if root == -1:
            return
        self.result.append(self.key[root])
        self._pre_order(self.left[root])
        self._pre_order(self.right[root])

    def _post_order(self, root: int) -> None:
        """
        Internal function to perform post-order traversal.
        """
        if root == -1:
            return
        self._post_order(self.left[root])
        self._post_order(self.right[root])
        self.result.append(self.key[root])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == '__main__':
    threading.Thread(target=main).start()
