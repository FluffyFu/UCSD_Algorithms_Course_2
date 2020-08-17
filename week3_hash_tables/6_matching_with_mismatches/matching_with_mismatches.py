# python3

import sys
from typing import List


class Solver:
    """
    Given a string text, and a pattern. Find all the substrings in text that match
    pattern with k-tolerance (at most k different letters).
    """
    M = int(10E9) + 7  # prime number for hashing.
    x = 236  # base for polynomial hashing.

    def __init__(self, k: int, text: str, pattern: str):
        self._k = k
        self._t = text
        self._p = pattern
        self._ht = self._compute_sub_hash(text)
        self._hp = self._compute_sub_hash(pattern)
        self._x_powers = self._compute_x_powers()

    def solve(self) -> List[int]:
        """
        Find matches start index.
        """
        res = []
        for i in range(len(self._t) - len(self._p) + 1):

            cur_k = self._k
            l = len(self._p)
            t_start = i
            p_start = 0
            while cur_k >= 0:
                next_mismatch = self._binary_search_mismatch(
                    t_start, p_start, l)
                if next_mismatch == i + len(self._p):
                    # no mismatch was found.
                    res.append(i)
                    break
                else:
                    cur_k -= 1
                    shift = next_mismatch - t_start + 1
                    t_start = t_start + shift
                    p_start = p_start + shift
                    l = l - shift
        return res

    def _compute_sub_hash(self, s: str) -> List[int]:
        """
        Helper function that calculates the hash value for all the substrings of s including
        the first letter.
        """
        res = [0]
        val = 0
        for c in s:
            val = (val * self.x + ord(c)) % self.M
            res.append(val)
        return res

    def _compute_x_powers(self) -> List[int]:
        """
        Helper function that compute x**l % m, where l = [0, len(p)]
        """
        res = [1]
        val = 1
        for _ in range(len(self._p)):
            val = (val * self.x) % self.M
            res.append(val)

        return res

    def _is_eqaul(self, i: int, j: int, l: int) -> bool:
        """
        Helper function to check if text[i: i+l] matches pattern[j: j+l].
        """
        hash_t = (self._ht[i+l] - self._x_powers[l] * self._ht[i]) % self.M
        hash_p = (self._hp[j+l] - self._x_powers[l] * self._hp[j]) % self.M

        return hash_t == hash_p

    def _binary_search_mismatch(self, i: int, j: int, l: int) -> int:
        """
        Use binary search to find the next mismatch index for text[i: i+l] and pattern[j: j+l]
        """
        left = i
        right = i + l - 1

        p_left = j

        while(left <= right):
            mid = left + (right - left) // 2
            sub_l = mid - left + 1

            if self._is_eqaul(left, p_left, sub_l):
                left = mid + 1
                p_left += sub_l
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        k, text, pattern = line.split()
        solver = Solver(int(k), text, pattern)
        ans = solver.solve()
        print(len(ans), *ans)
