# python3

import sys
from typing import List, Tuple


class SolverNaivie:
    def __init__(self, s):
        self.s = s

    def ask(self, a, b, l):
        return s[a:a+l] == s[b:b+l]


class Solver:
    """
    Given a string s and a list of queries where two substring are specified.
    Check if the two substring are equal.

    In this application, we have the following constrains:

       1 < |s| < 5E5, 1 < q < 10E5

    A naive comparison in such scenario would result in O(sq) time complexity. Here we follow
    the following algorithms:

        1. Precompute H(s[0: i]) where i = [0, len(s)] and H() is polynomial hash. O(|s|)

        2. Precompute x**l mod m, where l = [0, len(s)]. O(|s|)

        3. H(s[i:i+l]) can be written as H([0:i+l]) - x**l * H([0:i]). O(|s|)

    The probability of collision is about l / m <= |s| / m. Here we choose m ~ 10E9, then
    the collision probability is ~ 10E-4. To avoid collision in real applications (if we
    do a naive comparison when collision happens, it is already O(|s|)), we use to hash functions
    and the collision probability drops to ~ 10E-9.
    """
    M1 = int(10E9) + 7  # first mode
    M2 = int(10E9) + 9  # second mode
    X = 237  # polynomial

    def __init__(self, s: str):
        self._s = s

        # hash values
        self._hash_vals_1 = self._precompute_substrings(self.M1)
        self._hash_vals_2 = self._precompute_substrings(self.M2)

        # polynomials of x
        self._xls_1 = self._precompute_xl(self.M1)
        self._xls_2 = self._precompute_xl(self.M2)

    def _precompute_substrings(self, p: int) -> List[int]:
        """
        Precompute the polynomial hash values of all the substring starting from the first
        letter.
        """
        hash_vals: List[int] = [0]
        for i in range(len(self._s)):
            val = (hash_vals[i] * self.X + ord(self._s[i])) % p
            hash_vals.append(val)

        return hash_vals

    def _precompute_xl(self, p: int) -> List[int]:
        """
        Compute the value of X**l mod p for l = [0, len(s)]
        """
        res = [1]
        val = 1
        for _ in range(len(self._s)):
            val = (val * self.X) % p
            res.append(val)
        return res

    def _hash_substring(self, a: int, l: int) -> Tuple[int, int]:
        """
        Compute the hash value of substing s[a:a+l], using the precomputed hash values.
        """
        xl_1 = self._xls_1[l]
        xl_2 = self._xls_2[l]

        hash_val_1 = (self._hash_vals_1[a+l] -
                      xl_1 * self._hash_vals_1[a]) % self.M1
        hash_val_2 = (self._hash_vals_2[a+l] -
                      xl_2 * self._hash_vals_2[a]) % self.M2

        return (hash_val_1, hash_val_2)

    def ask(self, a: int, b: int, l: int) -> bool:
        """
        Check if the two substring are the same.

        Args:
            a: start index of the first substring.

            b: start index of the second substring.

            l: substring length.
        """
        hash_val_first = self._hash_substring(a, l)
        hash_val_second = self._hash_substring(b, l)

        return hash_val_first == hash_val_second


if __name__ == '__main__':
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")
