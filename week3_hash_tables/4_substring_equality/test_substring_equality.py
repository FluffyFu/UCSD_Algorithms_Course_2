from substring_equality import Solver


def test_solver():
    s = 'trololo'
    solver = Solver(s)

    a, b, l = 0, 0, 7
    assert solver.ask(a, b, l) == True

    a, b, l = 2, 4, 3
    assert solver.ask(a, b, l) == True

    a, b, l = 3, 5, 1
    assert solver.ask(a, b, l) == True

    a, b, l = 1, 3, 2
    assert solver.ask(a, b, l) == False
