import pytest
from bst import ColorNode, Color
from rbt import RBT


@pytest.fixture
def my_tree():
    root = ColorNode(6, color=Color.BLACK)
    root.left = ColorNode(4, color=Color.RED)
    root.left.left = ColorNode(2, color=Color.BLACK)
    root.left.right = ColorNode(5, color=Color.BLACK)
    root.right = ColorNode(8, color=Color.BLACK)
    root.right.left = ColorNode(7, color=Color.RED)

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
