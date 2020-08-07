from stack_with_max_naive import StackWithMax


def test_stack_with_max():
    s = StackWithMax()

    s.Push(1)
    assert s.Max() == 1
    s.Push(3)
    assert s.Max() == 3
    s.Pop()
    assert s.Max() == 1
