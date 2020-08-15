from common_substring import solve, solve_naive, Answer
import pudb


def test_solve():
    s = 'cool'
    t = 'toolbox'
    assert solve(s, t) == Answer(1, 1, 3)

    s = 'aaa'
    t = 'bb'
    assert solve(s, t) == Answer(0, 0, 0)

    # pudb.set_trace()
    s = 'aabaa'
    t = 'babbaab'
    assert solve(s, t) == Answer(2, 3, 3)  # Answer(0, 4, 3) is also correct.

