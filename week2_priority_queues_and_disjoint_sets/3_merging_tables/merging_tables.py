# python3
from typing import List


class Database:
    """
    Union find (UF) data structure, except we need to keep track of the maximum row counts
    in each component.

    The key of this problem is that the problem only asks to return the value of current maximum row but
    not what table contains the maximum. In this case, we can pretend it's the parent who has the
    maximum number of rows.

    In each UF component, there two roots. One is the UF's root from the data structure perspective (P1).
    The other one the destination of all the symbolic links (P2). When merging, we use P1 to take the advantage
    of UF. When calculating the number of rows after merge, we are supposed to use the number of
    rows in P2. However, if we store P2's row number in P1 from the very beginning, WE DON'T NEED TO
    KEEP TRACK OF P2 ANYMORE.
    """

    def __init__(self, row_counts: List[int]):
        # maintain the max row count
        self._max_row_count = max(row_counts)
        # maintain union find tree height
        self._ranks = [1] * len(row_counts)
        # maintain union find tree structure.
        self._parents = list(range(len(row_counts)))
        # maintain the maximum row counts of each node.
        self._rows = list(row_counts)

    def merge(self, src: int, dst: int) -> None:
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            pass
        elif self._ranks[src_parent] > self._ranks[dst_parent]:
            self._parents[dst_parent] = src_parent

            # we don't need to keep track of self._rows[dst_parent]
            # anymore.
            self._rows[src_parent] += self._rows[dst_parent]

            # update max
            if self._rows[src_parent] > self._max_row_count:
                self._max_row_count = self._rows[src_parent]
        else:
            self._parents[src_parent] = dst_parent
            if self._ranks[src_parent] == self._ranks[dst_parent]:
                self._ranks[dst_parent] += 1
            self._rows[dst_parent] += self._rows[src_parent]

            # update max
            if self._rows[dst_parent] > self._max_row_count:
                self._max_row_count = self._rows[dst_parent]

    def get_parent(self, table: int) -> int:
        if self._parents[table] == table:
            return table
        # path compression
        self._parents[table] = self.get_parent(self._parents[table])
        return self._parents[table]

    @property
    def max_row_count(self):
        return self._max_row_count


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
