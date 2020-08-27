import pytest
import pudb
from bst import ColorNode, Color
from rbt import RBT
from bst import Client


@pytest.fixture
def my_tree():
    root = ColorNode(6, color=Color.BLACK)
    root.left = ColorNode(4, color=Color.RED)
    root.left.left = ColorNode(2, color=Color.BLACK)
    root.left.right = ColorNode(5, color=Color.BLACK)
    root.right = ColorNode(8, color=Color.BLACK)
    root.right.left = ColorNode(7, color=Color.RED)

    return root


@pytest.fixture
def my_tree_2():
    root = ColorNode(8)
    root.left = ColorNode(5)
    root.right = ColorNode(11)
    root.left.left = ColorNode(3)
    root.left.right = ColorNode(6)
    root.right.left = ColorNode(10)
    root.right.right = ColorNode(13)

    return root


def test_color_node():
    c_node = ColorNode(1, color=Color.RED)
    assert c_node.color == Color.RED
    c_node.color = Color.BLACK
    assert c_node.color == Color.BLACK
    assert c_node.val == 1
    assert c_node.left == None
    assert c_node.right == None


def test_rbt():
    rbt = RBT(None)
    rbt.add(1)
    assert rbt.root.val == 1
    rbt.add(2)
    assert rbt.root.val == 2
    rbt.add(3)
    assert rbt.root.val == 2
    assert rbt.root.left.color == Color.BLACK
    assert rbt.root.right.color == Color.BLACK


def test_rbt_del_min():
    rbt = RBT(None)
    rbt.add(1)
    assert rbt.find(1) == True
    rbt.add(2)
    assert rbt.find(2) == True
    assert rbt.find(3) == False

    # pudb.set_trace()
    rbt.del_min()
    assert rbt.find(1) == False
    assert rbt.find(2) == True


def test_rbt_del_max():
    rbt = RBT(None)

    rbt.add(1)
    rbt.add(3)

    rbt.del_max()
    assert rbt.find(3) == False
    assert rbt.find(1) == True

# TODO Fix this test


def test_rbt_delete():
    rbt = RBT(None)

    rbt.add(1)
    rbt.add(2)
    rbt.add(3)

    rbt.delete(2)
    assert rbt.find(2) == False
    assert rbt.find(1) == True
    assert rbt.find(3) == True

    rbt.add(2)
    rbt.delete(5)
    assert rbt.find(1) == True
    assert rbt.find(2) == True
    assert rbt.find(3) == False


def test_rbt_get_range(my_tree_2):
    rbt = RBT(my_tree_2)

    low = 1
    high = 6
    res = rbt.get_range(low, high)
    assert res == [3, 5, 6]

    low = 0
    high = 20
    res = rbt.get_range(low, high)
    assert res == [3,  5, 6, 8, 10, 11, 13]

    low = 20
    high = 0
    res = rbt.get_range(low, high)
    assert res == []

    low = 6.5
    high = 7
    res = rbt.get_range(low, high)
    assert res == []

    low = 8
    high = 8
    res = rbt.get_range(low, high)
    assert res == [8]


def test_client():
    client = Client(bst=RBT(None))
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
