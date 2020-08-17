from matching_with_mismatches import Solver
import pudb


def test_solver():
    # pudb.set_trace()
    k = 1
    text = 'ababab'
    pattern = 'baaa'
    solver = Solver(k, text, pattern)
    assert solver.solve() == [1]

    k = 1
    text = 'xabcabc'
    pattern = 'ccc'
    solver = Solver(k, text, pattern)
    assert solver.solve() == []

    k = 2
    text = 'xabcabc'
    pattern = 'ccc'
    solver = Solver(k, text, pattern)
    assert solver.solve() == [1, 2, 3, 4]

    k = 3
    text = 'aaa'
    pattern = 'xxx'
    solver = Solver(k, text, pattern)
    assert solver.solve() == [0]
