from build_heap import build_heap

with open('tests/04') as f:
    n = int(f.readline())
    data = list(map(int, f.readline().split()))

with open('tests/04.a') as f:
    n_swaps = int(f.readline())
    results = []
    for line in f.readlines():
        results.append(tuple(map(int, line.split())))


my_results = build_heap(data)
# my_results = [(b, a) for a, b in my_results]
assert my_results == results, 'my results len: {}, truth len: {}'.format(
    len(my_results), len(results))

print('my_results: ', my_results[:10])
print('truth: ', results[:10])
