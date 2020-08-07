import glob
from process_packages import process_requests, Buffer, Request
import pudb


all_files = glob.glob('tests/*')

q_files = sorted([f for f in all_files if not 'a' in f])
a_files = sorted([f for f in all_files if 'a' in f])

counter = 1

for q, a in zip(q_files[11:12], a_files[11:12]):
    with open(q, 'r') as f:
        buffer_size, n_requests = map(int, f.readline().split())

        requests = []
        for line in f:
            # f does not contain the first line because the previous f.readline().
            arrived_at, time_to_process = map(int, line.split())
            requests.append(Request(arrived_at, time_to_process))

    with open(a, 'r') as f:
        start_time_truth = []

        for line in f:
            start_time_truth.append(int(line))

    net_buffer = Buffer(buffer_size)

    my_result = process_requests(requests, net_buffer)
    my_result = [r.started_at for r in my_result]

    assert my_result == start_time_truth, 'fail case {}\n my result {}\n truth {}'.format(
        counter, my_result, start_time_truth)

    counter += 1
