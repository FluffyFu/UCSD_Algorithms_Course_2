# python3
import sys


class StackWithMax():
    """
    Implement a stack with the ability to return the current maximum in constant time.

    Use an auxiliary stack to stack max{a1}, max{a1, a2} ... max{a1, a2, .. an}. Each time we push
    a new item or pop an item, we update the auxiliary stack at the same time.
    """

    def __init__(self):
        self._stack = []
        self._max_stack = []

    def Push(self, a):
        self._stack.append(a)
        if len(self._max_stack) == 0:
            self._max_stack.append(a)
        else:
            self._max_stack.append(max(a, self._max_stack[-1]))

    def Pop(self):
        assert(len(self._stack))
        self._stack.pop()
        self._max_stack.pop()

    def Max(self):
        assert(len(self._stack))
        return self._max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
