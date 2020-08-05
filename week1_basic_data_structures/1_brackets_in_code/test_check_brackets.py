from check_brackets import find_mismatch
import pudb


def test_find_mismatch():
    text = '[])'
    assert find_mismatch(text) == 3

    text = ']()'
    assert find_mismatch(text) == 1

    text = '{}([]}'
    assert find_mismatch(text) == 6

    text = '{}([]'
    assert find_mismatch(text) == 3

    text = '123()'
    assert find_mismatch(text) == 0
