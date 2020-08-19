from is_bst_hard import Solver, Solver2
import pudb
from binarytree import tree
from collections import deque


def test_solver():
    n = 3
    tree = [
        [2, 1, 2],
        [1, -1, -1],
        [3, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_bst() == True

    n = 3
    tree = [
        [1, 1, 2],
        [2, -1, -1],
        [3, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_bst() == False

    n = 3
    tree = [
        [2, 1, 2],
        [1, -1, -1],
        [2, -1, -1]
    ]

    solver = Solver(n, tree)
    assert solver.is_bst() == True

    n = 5
    tree = [
        [1, -1, 1],
        [2, -1, 2],
        [3, -1, 3],
        [4, -1, 4],
        [5, -1, -1]
    ]

    solver = Solver(n, tree)
    assert solver.is_bst() == True

    n = 7
    tree = [
        [4, 1, 2],
        [2, 3, 4],
        [6, 5, 6],
        [1, -1, -1],
        [3, -1, -1],
        [5, -1, -1],
        [7, -1, -1]
    ]

    solver = Solver(n, tree)
    assert solver.is_bst() == True

    n = 1
    tree = [
        [2147483647, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_bst() == True

    n = 7
    tree = [
        [4, 1, 2],
        [2, 3, 4],
        [6, 5, 6],
        [1, -1, -1],
        [3, -1, -1],
        [4, -1, -1],
        [7, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_bst() == True

    n = 2
    tree = [
        [-2147483648, 1, -1],
        [0, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_bst() == False

    # pudb.set_trace()
    n = 3
    tree = [
        [5, 1, -1],
        [1, -1, 2],
        [2, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_bst() == True


def test_solver2():
    n = 3
    tree = [
        [2, 1, 2],
        [1, -1, -1],
        [3, -1, -1]
    ]
    solver = Solver2(n, tree)
    assert solver.is_bst() == True

    n = 3
    tree = [
        [1, 1, 2],
        [2, -1, -1],
        [3, -1, -1]
    ]
    solver = Solver2(n, tree)
    assert solver.is_bst() == False

    n = 3
    tree = [
        [2, 1, 2],
        [1, -1, -1],
        [2, -1, -1]
    ]

    solver = Solver2(n, tree)
    assert solver.is_bst() == True

    n = 5
    tree = [
        [1, -1, 1],
        [2, -1, 2],
        [3, -1, 3],
        [4, -1, 4],
        [5, -1, -1]
    ]

    solver = Solver2(n, tree)
    assert solver.is_bst() == True

    n = 7
    tree = [
        [4, 1, 2],
        [2, 3, 4],
        [6, 5, 6],
        [1, -1, -1],
        [3, -1, -1],
        [5, -1, -1],
        [7, -1, -1]
    ]

    solver = Solver2(n, tree)
    assert solver.is_bst() == True

    n = 1
    tree = [
        [2147483647, -1, -1]
    ]
    solver = Solver2(n, tree)
    assert solver.is_bst() == True

    n = 7
    tree = [
        [4, 1, 2],
        [2, 3, 4],
        [6, 5, 6],
        [1, -1, -1],
        [3, -1, -1],
        [4, -1, -1],
        [7, -1, -1]
    ]
    solver = Solver2(n, tree)
    assert solver.is_bst() == True

    n = 2
    tree = [
        [-2147483648, 1, -1],
        [0, -1, -1]
    ]
    solver = Solver2(n, tree)
    assert solver.is_bst() == False

    n = 3
    tree = [
        [5, 1, -1],
        [1, -1, 2],
        [2, -1, -1]
    ]
    solver = Solver2(n, tree)
    assert solver.is_bst() == True


def build_map_key_to_index(root):
    vals = root.values
    vals = [v for v in vals if v != None]
    mapping = {v: i for i, v in enumerate(vals)}
    return mapping


def convert_tree_format(root):

    mapping = build_map_key_to_index(root)

    q = deque()
    q.append(root)
    res = []

    while len(q) > 0:
        node = q.popleft()
        val = node.val
        if node.left:
            left_index = mapping[node.left.val]
            q.append(node.left)
        else:
            left_index = -1

        if node.right:
            right_index = mapping[node.right.val]
            q.append(node.right)
        else:
            right_index = -1

        res.append([val, left_index, right_index])

    return res


def test_stress():

    for _ in range(100):
        my_tree = tree(height=2, is_perfect=False)
        n = my_tree.size
        tree_reformat = convert_tree_format(my_tree)

        solver = Solver(n, tree_reformat)
        solver2 = Solver2(n, tree_reformat)
        if solver.is_bst() != solver2.is_bst():
            print('n: ', n)
            print('tree_reformat: ', tree_reformat)
