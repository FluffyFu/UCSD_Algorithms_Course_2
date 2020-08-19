from is_bst_hard import Solver, Solver2
import pudb


def test_solver():
    # pudb.set_trace()
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
