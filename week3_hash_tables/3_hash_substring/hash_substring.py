# python3

from typing import List


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences_naive(pattern, text):

    res = []
    for i in range(len(text)-len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            res.append(i)
    return res


def polynomial_hash(pattern: str, p=1000000007, x=263) -> int:
    """
    Compute the hash value of a string using polynomial hash.
    """
    res = 0
    for s in reversed(pattern):
        res = (res * x + ord(s)) % p
    return res


def compute_hash_of_substrings(text: str, l: int, p=1000000007, x=263) -> List[int]:
    """
    Compute the hash value of all the consecutive substrings in the text.

    Args:
        text: string used for searching.

        l: substring length.

    Returns:
        list of length len(text) - substring_len + 1
    """
    # calculate x**l mod p
    x_l = 1
    for _ in range(l):
        x_l = (x_l * x) % p

    hash_values = []
    n = len(text)

    # calculate the hash value of the last substring
    value = polynomial_hash(text[n-l:])
    hash_values.append(value)

    # calculate hash values of other substrings from right to left.
    for i in range(n-l-1, -1, -1):
        value = (x * value - ord(text[i+l]) * x_l + ord(text[i])) % p
        hash_values.append(value)

    return hash_values[::-1]


def get_occurrences(pattern: str, text: str) -> List[int]:
    """
    Implement Rabin-Karp's algorithm for search the given pattern in
    the text.

    Returns:
        the start index of the pattern in the text.
    """
    pattern_v = polynomial_hash(pattern)
    sub_vs = compute_hash_of_substrings(text, len(pattern))
    l = len(pattern)
    res: List[int] = []

    for i, v in enumerate(sub_vs):
        if v == pattern_v and pattern == text[i:i+l]:
            res.append(i)
    return res


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

