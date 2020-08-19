from is_bst import Solver
import pudb


def test_solver():
    n = 3
    tree = [
        [2, 1, 2],
        [1, -1, -1],
        [3, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_binary_tree() == True

    n = 3
    tree = [
        [1, 1, 2],
        [2, -1, -1],
        [3, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_binary_tree() == False

    n = 0
    tree = []
    solver = Solver(n, tree)
    assert solver.is_binary_tree() == True

    # pudb.set_trace()
    n = 5
    tree = [
        [1, -1, 1],
        [2, -1, 2],
        [3, -1, 3],
        [4, -1, 4],
        [5, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_binary_tree() == True

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
    assert solver.is_binary_tree() == True

    n = 4
    tree = [
        [4, 1, -1],
        [2, 2, 3],
        [1, -1, -1],
        [5, -1, -1]
    ]
    solver = Solver(n, tree)
    assert solver.is_binary_tree() == False
