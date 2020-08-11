from build_heap import sink_down, build_heap


def test_sink_down():
    data = [1, 2, 3, 4]
    index = 0
    swaps = []

    swaps = sink_down(index, data, swaps)
    assert swaps == []

    data = [2, 1, 3, 4]
    index = 0
    swaps = []

    swaps = sink_down(index, data, swaps)
    assert swaps == [(0, 1)]


def test_build_heap():
    data = [5, 4, 3, 2, 1]
    swaps = build_heap(data)
    assert swaps == [(4, 1), (1, 0), (3, 1)]

    data = [1, 2, 3, 4, 5]
    swaps = build_heap(data)
    assert swaps == []
