from tree_height import build_tree, BFS, cal_tree_height, compute_height
import pudb
import glob


def test_build_tree():
    # pudb.set_trace()
    n = 5
    parents = [-1, 0, 4, 0, 3]
    root = build_tree(n, parents)
    # BFS(root)


def test_cal_tree_height():
    n = 5
    parents = [-1, 0, 4, 0, 3]
    root = build_tree(n, parents)
    assert cal_tree_height(root) == 4


def test_compute_height():
    files = glob.glob('tests/*')
    input_files = sorted([f for f in files if not 'a' in f])
    result_files = sorted([f for f in files if 'a' in f])

    counter = 1
    for input_name, result_name in zip(input_files, result_files):
        print('current test number: ', counter)
        with open(input_name) as f:
            n = int(f.readline())
            parents = [int(val) for val in f.readline().split()]

        with open(result_name) as f:
            truth = int(f.readline())

        assert compute_height(n, parents) == truth

        counter += 1
