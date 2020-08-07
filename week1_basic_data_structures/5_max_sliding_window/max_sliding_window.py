# python3
from typing import List
from collections import deque


class StackWithMax():
    """
    Implement a stack with the ability to return the current maximum in constant time.

    Use an auxiliary stack to stack max{a1}, max{a1, a2} ... max{a1, a2, .. an}. Each time we push
    a new item or pop an item, we update the auxiliary stack at the same time.
    """
    MIN = int(-1E8)

    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, a):
        self._stack.append(a)
        if len(self._max_stack) == 0:
            self._max_stack.append(a)
        else:
            self._max_stack.append(max(a, self._max_stack[-1]))

    def pop(self):
        assert(len(self._stack))
        self._max_stack.pop()
        return self._stack.pop()

    def max(self):
        if self.is_empty:
            return self.MIN
        return self._max_stack[-1]

    @property
    def is_empty(self):
        return len(self._stack) == 0


class QueueWithMax():

    """
    Implement a queue with two stacks with constant time maximum retrieving.
    """

    def __init__(self):
        self._s1 = StackWithMax()
        self._s2 = StackWithMax()

    def enqueue(self, a):
        self._s1.push(a)

    def dequeue(self):
        if self._s2.is_empty:
            while not self._s1.is_empty:
                v = self._s1.pop()
                self._s2.push(v)
        return self._s2.pop()

    def max(self):
        """
        Returns the maximum element in the current queue with constant time.
        """
        return max(self._s2.max(), self._s1.max())


def max_sliding_window(sequence: List[int], m: int) -> List[int]:
    """
    Given a list of n integers and an int m <= n, find the maximum value of each
    subset {ai, ai+1, ..., ai+m-1} where 1 <= i <= n-m +1

    In this implementation, two stacks with maximum (problem 4) are used to create a queue.
    For each enqueue operation, we push the item to stack 1 with constant time. For each dequeue operation,
    pop from stack 2 O(1). If stack 2 is empty, empty stack 1 and push the items to stack2 then pop from it.
    In this way, the enqueue is always O(1) and dequeue is amortized O(1).
    """

    maximums: List[int] = []
    q = QueueWithMax()
    n = len(sequence)

    for v in sequence[:m]:
        q.enqueue(v)

    maximums.append(q.max())

    for v in sequence[m:]:
        q.dequeue()
        q.enqueue(v)
        maximums.append(q.max())

    return maximums


def max_sliding_window_2(sequence: List[int], m: int) -> List[int]:
    """
    2nd implementation with a dequeue.

    1. Obviously, we need to keep track the current maximum. Note that whenever, we come
    across an element that's larger than the current maximum, WE DON'T NEED THE CURRENT
    MAXIMUM ANY MORE FOR THE FOLLOWING WINDOWS.

    2. However, if we come across an element that's
    smaller than or equal to the current maximum, we need to keep track of it. Because it may
    become the maximum in an upcoming window.

    3. Following 2, comparing with the current maximum is not enough. We need to keep track of
    largest, 2n largest, ... until k-th largest, if the sequence is in descending order.


    4. Since we need to check if the stored elements are still in the current window, we store
    the index instead of its value.


    So we maintain a dequeue dq with size m whose values are index of the given sequence. The dequeue is
    updated in the following way when the window is slide:

    - check if dq[0] is out of the current window. dequeue from left if it's true.

    - check if the current element is smaller than or equal to dq[-1].
        If it's true, enqueue from right. Otherwise, pop dq from right and keep comparing.
        The current element either finds some element larger and enqueued from right, or it
        becomes the largest.

    - dq[0] is the index of the largest element in the current window.

    TIME COMPLEXITY: O(n)
    Apparently, we need to scan the whole sequence which takes n step. For each step, the
    operations on the dequeue is amortized constant.

    SPACE COMPLEXITY O(m): this is better than the 2 StackWithMax method which actually using 4 stacks.
    """
    maximums: List[int] = []  # results

    # dq is actually maintained in descending order.
    dq: deque = deque(maxlen=m)
    n = len(sequence)

    for end in range(n):
        # add the current element
        v = sequence[end]
        while len(dq) > 0 and sequence[dq[-1]] < v:
            dq.pop()
        dq.append(end)

        # remove the current max if it is out of the current window.
        if dq[0] < end-m+1:
            dq.popleft()

        # for the first m element we only need to perform append once.
        if end >= m-1:
            maximums.append(sequence[dq[0]])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_2(input_sequence, window_size))

