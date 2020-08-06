import sys
import threading
from tree_height import build_tree, BFS, cal_tree_height, compute_height
import glob


files = glob.glob('tests/*')
input_files = sorted([f for f in files if not 'a' in f])
result_files = sorted([f for f in files if 'a' in f])

print('total number of test cases: ', len(input_files))


def main():
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


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
