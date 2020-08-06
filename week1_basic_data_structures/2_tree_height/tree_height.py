# python3

import sys
import threading
from queue import Queue
from typing import List


class Node:

    def __init__(self, key: int):
        self._key = key
        self._children: List[Node] = []

    def __repr__(self):
        return "Node(key={})".format(self._key)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value: int):
        self._key = value

    @property
    def children(self):
        return self._children

    def add_child(self, child: 'Node'):
        self._children.append(child)


def compute_height_naive(n: int, parents: list) -> int:
    """
    The original tree structure is stored in an array s.t. the value of
    the i-th element is its parent's index. If the element is root, its value
    is -1.

    This function calculates the maximum height of the tree with naive method:
    trace back from every node until the root and find the maximum travel distance.

    Args:
        n: number of nodes in the tree.

        parents: a list contains where each element is its ancestor's index.

    Returns:
        The max hight of the tree.
    """
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def compute_height(n: int, parents: list) -> int:
    """
    Compute the maximum height of tree by first reverse the pointer. In the original format,
    the pointer is pointing from the child to its parent (similar to UnionFind data structure).
    We first make them point from parent to children. Then we can use recursive call to compute
    its height.
    """
    root = build_tree(n, parents)
    return cal_tree_height(root)


def cal_tree_height(root: Node) -> int:
    """
    Given the root of a tree, calculate its height.
    """
    if len(root.children) == 0:
        return 1
    else:
        max_depth = 0
        for child in root.children:
            current_d = cal_tree_height(child)
            if current_d > max_depth:
                max_depth = current_d
        return 1 + max_depth


def build_tree(n: int, parents: list) -> Node:
    """
    Helper function to build a tree from the given array.
    """
    store: List[Node] = [Node(-1) for _ in range(n)]
    root_index = -1

    for child in range(n):
        parent = parents[child]

        if parent == -1:
            store[child].key = child
            root_index = child
        else:
            if store[parent].key != -1:
                # this parent has already been updated.
                parent_node = store[parent]
            else:
                # first visit this parent, update its key.
                parent_node = store[parent]
                parent_node.key = parent

            child_node = store[child]
            child_node.key = child
            parent_node.add_child(child_node)
            store[child] = child_node

    return store[root_index]


def BFS(root: Node) -> None:
    """
    Breadth-First search to traversal a tree and print out the node values.

    Helper function to print out the tree structure for debugging.

    Args:
        root: tree root.

    Returns:
        None
    """
    q: Queue = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node)
        for child in node.children:
            q.put(child)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
