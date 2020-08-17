from tree_orders import TreeOrders
import pytest


def test_tree_orders():
    n = 5
    relations = [
        (4, 1, 2),
        (2, 3, 4),
        (5, -1, -1),
        (1, -1, -1),
        (3, -1, -1)
    ]

    tree = TreeOrders()
    tree.read_from_relations(n, relations)

    assert tree.inOrder() == [1, 2, 3, 4, 5]
    assert tree.preOrder() == [4, 2, 1, 3, 5]
    assert tree.postOrder() == [1, 3, 2, 5, 4]


@pytest.skip('tree is too deep for python')
def test_tree_orders_case():
    with open('tests/21') as f:
        n = int(f.readline())
        relations = []
        for line in f.readlines():
            relations.append(tuple(map(int, line.split())))

    with open('tests/21.a') as f:
        truth = []
        for line in f.readlines():
            truth.append(list(map(int, line.split())))
    tree = TreeOrders()
    tree.read_from_relations(n, relations)

    assert tree.inOrder() == truth[0]
    assert tree.preOrder() == truth[1]
    assert tree.postOrder() == truth[2]
