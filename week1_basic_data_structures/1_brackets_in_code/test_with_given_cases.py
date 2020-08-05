import glob
from check_brackets import find_mismatch

all_files = glob.glob('tests/*')
input_files = sorted([f for f in all_files if not 'a' in f])
result_files = sorted([f for f in all_files if 'a' in f])

for q, a in zip(input_files, result_files):
    with open(q) as f:
        data = f.readline()

    with open(a) as f:
        result = f.readline().strip()
        if result == 'Success':
            result = 0
        else:
            result = int(result)

    my_result = find_mismatch(data)
    assert my_result == result, 'data: {}\n my result: {}\n truth: {}'.format(
        data, my_result, result)

