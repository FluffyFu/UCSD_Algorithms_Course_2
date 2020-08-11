from merging_tables import Database
import pudb


def test_database():
    # pudb.set_trace()
    row_counts = [1, 1, 1, 1, 1]
    db = Database(row_counts)
    db.merge(2, 4)
    assert db.max_row_count == 2
    db.merge(1, 3)
    assert db.max_row_count == 2
    db.merge(0, 3)
    assert db.max_row_count == 3
    db.merge(4, 3)
    assert db.max_row_count == 5
    db.merge(4, 2)
    assert db.max_row_count == 5


def test_database_cases():
    with open('tests/116') as f:
        n_tables, n_ops = map(int, f.readline().split())
        row_counts = list(map(int, f.readline().split()))

        ops = []
        for line in f.readlines():
            ops.append(tuple(map(int, line.split())))

    with open('tests/116.a') as f:
        truth = []
        for line in f.readlines():
            truth.append(int(line))

    db = Database(row_counts)
    for op, max_truth in zip(ops, truth):
        db.merge(op[0]-1, op[1]-1)
        assert db.max_row_count == max_truth

