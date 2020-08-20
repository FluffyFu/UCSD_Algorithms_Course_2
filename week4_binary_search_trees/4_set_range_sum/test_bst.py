import sys
import pytest
import pudb
from bst import BST, Client
from binarytree import bst, Node
sys.setrecursionlimit(10**7)  # max depth of recursion


@pytest.fixture
def my_tree():
    root = Node(8)
    root.left = Node(5)
    root.right = Node(11)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.right.left = Node(10)
    root.right.right = Node(13)

    return root


def test_bst(my_tree):

    bst = BST(my_tree)
    print(my_tree)

    # pudb.set_trace()
    assert bst.find(6) == True

    bst.add(6)
    assert bst.find(6) == True

    assert bst.find(3) == True
    bst.del_min()
    assert bst.find(3) == False

    assert bst.find(13) == True
    bst.del_max()
    assert bst.find(13) == False


def test_bst_delete(my_tree):
    bst = BST(my_tree)
    vals = [val for val in my_tree.values if val != None]

    for val in vals[:-1]:
        bst.delete(val)
        assert bst.root.is_bst == True


def test_bst_empty():
    bst = BST(None)

    bst.add(1)
    assert bst.find(1) == True

    bst.delete(1)
    assert bst.find(1) == False

    bst.delete(1)
    assert bst.find(1) == False


def test_bst_get_range(my_tree):
    print(my_tree)

    bst = BST(my_tree)
    low = 1
    high = 6
    res = bst.get_range(low, high)
    assert res == [3, 5, 6]

    low = 0
    high = 20
    res = bst.get_range(low, high)
    assert res == [3,  5, 6, 8, 10, 11, 13]

    low = 20
    high = 0
    res = bst.get_range(low, high)
    assert res == []

    low = 6.5
    high = 7
    res = bst.get_range(low, high)
    assert res == []

    low = 8
    high = 8
    res = bst.get_range(low, high)
    assert res == [8]


def test_client():
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

