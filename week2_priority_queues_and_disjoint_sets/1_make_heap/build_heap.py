# python3

from typing import List, Tuple
from math import ceil, floor


def build_heap(data: List[int]) -> List[Tuple[int, int]]:
    """
    Build a heap from the given array in place and returns a sequence of
    swap operations. The heap is zero indexed, therefore, the relative relation
    between parent and child is as follows:

        i -> 2 * i + 1, and 2 * i + 2 (parent -> children)
        i -> floor((i - 1) / 2) (child -> parent)

    We heapfy the given array using a bottom-up approach. For a binary tree with n elements,
    there are ceiling(n/2) number of nodes. All the nodes are already heaps. We use sink down
    function from bottom until we reach to the top.
    """
    swaps: List[Tuple[int, int]] = []

    n = len(data)
    start = ceil(n/2) - 1
    for i in range(start, -1, -1):
        swaps = sink_down(i, data, swaps)

    return swaps


def sink_down(index: int, data: List[int], swaps: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Sink the element of the given index in the heap to keep the heap order.

    Returns:
        the swaps performed during the sink down operation.
    """
    while index * 2 + 1 < len(data):
        j = index * 2 + 1
        # the other child exist and is smaller than the current one.
        if (j+1 < len(data)) and data[j+1] < data[j]:
            j += 1
        # heap order already satisfied.
        if data[index] <= data[j]:
            return swaps
        else:
            swap(index, j, data)
            swaps.append((index, j))
            index = j
    return swaps


def swap(i: int, j: int, data: List[int]) -> None:
    """
    Swap the i and j element in the given list.
    """
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
