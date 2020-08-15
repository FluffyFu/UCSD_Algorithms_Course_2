# python3

import sys
from collections import namedtuple
from typing import List

Answer = namedtuple('answer_type', 'i j len')


def solve_naive(s, t):
    """
    Naive algorithm to find the max length common substring in s and t.
    """
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
                    ans = Answer(i, j, l)
    return ans


def solve(s: str, t: str) -> Answer:
    """
    Find the maximum length substring between s and t with binary search and hashing.

    TIME COMPLEXITY: O(log(min(|s|, |t|)) * (|s| + |t|))

    The implementation follows the following steps:
        1. binary search substring length.

        2. For each length l, check if a common substring exist.
            - a naive would take O(m * n) time, where m and n
              are the number of substrings in s and t.

            - build a hash table whose keys are the hash values of substrings
              in s and check each substring's hash value of t against this table.
              This would only take O(max(m, n)) time. The same trick used in two sum.

            - To avoid collision, we use two hash functions to form the key.
    """
    p1 = int(10E9) + 7
    p2 = int(10E9) + 9
    x = 236

    hs_1 = compute_sub_hash(s, p1, x)
    hs_2 = compute_sub_hash(s, p2, x)
    ht_1 = compute_sub_hash(t, p1, x)
    ht_2 = compute_sub_hash(t, p2, x)

    right = min(len(s), len(t))
    left = 0

    res = Answer(0, 0, 0)

    while (left <= right):
        # binary search maximum length
        l = left + (right - left) // 2
        ans = check_substring_with_fixed_len(
            s, t, l, hs_1, ht_1, hs_2, ht_2, x, p1, p2)

        if ans.len > 0:
            res = ans
            left = l + 1
        else:
            right = l - 1

    return res


def check_substring_with_fixed_len(s: str, t: str, l: int, hs_1: List[int], ht_1: List[int],
                                   hs_2: List[int], ht_2: List[int], x: int, p1: int, p2: int) -> Answer:
    """
    Check if there exist a common substring in s and t with length l.
    """
    xl_1 = hash_power_x(x, p1, l)
    xl_2 = hash_power_x(x, p2, l)

    s_dict = {}  # key: tuple of two hash values, value: substring start index.

    for i in range(len(s) - l + 1):
        h1 = (hs_1[i+l] - xl_1 * hs_1[i]) % p1
        h2 = (hs_2[i+l] - xl_2 * hs_2[i]) % p2
        s_dict[(h1, h2)] = i

    for j in range(len(t) - l + 1):
        h1 = (ht_1[j+l] - xl_1 * ht_1[j]) % p1
        h2 = (ht_2[j+l] - xl_2 * ht_2[j]) % p2
        key = (h1, h2)

        if key in s_dict:
            i = s_dict[key]
            return Answer(i, j, l)

    return Answer(i, j, 0)


def compute_sub_hash(s: str, p: int, x: int) -> List[int]:
    """
    Compute the polynomial hash value of substring s[:i] where i = [0, len(s)].

    Args:
        s: str of interest.

        p: prime number used to do modulo.

        x: base of polynomial hashing.
    """
    val = 0
    res = [0]
    for c in s:
        val = (val * x + ord(c)) % p
        res.append(val)
    return res


def hash_power_x(x: int, p: int, m: int) -> int:
    """
    Compute x**m % p
    """
    res = 1
    for _ in range(m):
        res = (res * x) % p

    return res


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = solve(s, t)
        print(ans.i, ans.j, ans.len)
