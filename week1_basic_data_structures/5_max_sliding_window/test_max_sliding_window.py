from max_sliding_window import QueueWithMax, max_sliding_window, max_sliding_window_2
import pudb


def test_queue_with_stack():

    q = QueueWithMax()
    q.enqueue(2)
    assert q.max() == 2
    q.enqueue(1)
    assert q.max() == 2
    q.dequeue()
    assert q.max() == 1


def test_max_sliding_window():
    sequence = [2, 7, 3, 1, 5, 2, 6, 2]
    m = 4
    assert max_sliding_window(sequence, m) == [7, 7, 5, 6, 6]


def test_max_sliding_window_2():
    # pudb.set_trace()
    sequence = [2, 7, 3, 1, 5, 2, 6, 2]
    m = 4
    assert max_sliding_window_2(sequence, m) == [7, 7, 5, 6, 6]

