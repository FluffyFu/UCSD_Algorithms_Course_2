from hash_substring import get_occurrences_naive, get_occurrences, compute_hash_of_substrings
import pudb


def test_compute_hash_of_substrings():
    text = 'aaaa'
    l = 2
    res = compute_hash_of_substrings(text, l)
    assert len(set(res)) == 1


def test_get_occurrences():
    # pudb.set_trace()
    text = 'abacaba'
    pattern = 'aba'

    assert get_occurrences(pattern, text) == [0, 4]

    pattern = 'Test'
    text = 'testTesttesT'
    assert get_occurrences(pattern, text) == [4]

    pattern = 'aaaaa'
    text = 'baaaaaaa'
    assert get_occurrences(pattern, text) == [1, 2, 3]


def test_get_occurrences_cases():
    with open('tests/06', 'r') as f:
        pattern = f.readline().strip()
        text = f.readline().strip()

    with open('tests/06.a', 'r') as f:
        truth = list(map(int, f.readline().split()))

    # pudb.set_trace()
    assert truth == get_occurrences(pattern, text)
