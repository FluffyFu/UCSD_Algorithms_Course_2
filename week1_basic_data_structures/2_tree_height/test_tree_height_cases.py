from tree_height import build_tree, BFS, cal_tree_height, compute_height
import pudb
import glob

files = glob.glob('tests/*')
input_files = sorted([f for f in files if not 'a' in f])
result_files = sorted([f for f in files if 'a' in f])

print('total number of test cases: ', len(input_files))

counter = 1
for input_name, result_name in zip(input_files, result_files):
    with open(input_name) as f:
        n = int(f.readline())
        parents = [int(val) for val in f.readline().split()]

    with open(result_name) as f:
        truth = int(f.readline())

    assert compute_height(n, parents) == truth

    print('finished test ', counter)

    counter += 1
