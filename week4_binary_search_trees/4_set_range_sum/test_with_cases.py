import sys
import threading
import pytest
import pudb
from bst import BST, Client
from binarytree import bst, Node
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def main():
    client = Client()
    answers = []
    with open('tests/83') as f:
        n = int(f.readline())
        for q in f.readlines():
            res = client.request_from_file(q)
            if res != None:
                # convert to str for easier comparison
                answers.append(str(res))

    with open('tests/83.a') as f:
        truth = []
        for a in f.readlines():
            truth.append(a.strip())

    assert answers == truth


if __name__ == '__main__':
    threading.Thread(target=main).start()
